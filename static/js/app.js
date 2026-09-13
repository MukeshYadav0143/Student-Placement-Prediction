/* ==========================================================================
   CampusPulse AI - Student Placement Predictor & Career Platform
   Interactive Particle Background, Dynamic Charts, Confetti & Simulation
   ========================================================================== */

let radarChartInstance = null;
let deptChartInstance = null;
let backlogChartInstance = null;
let batchDataCache = [];
let baselineProbability = 82.5;

// ==========================================================================
// 1. Interactive Constellation Canvas Particle Background
// ==========================================================================
(function initParticleCanvas() {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', function() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particleCount = Math.min(65, Math.floor(width / 22));
  const particles = [];

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.45,
      vy: (Math.random() - 0.5) * 0.45,
      radius: Math.random() * 1.8 + 1,
      alpha: Math.random() * 0.5 + 0.2
    });
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;
      if (p.y < 0) p.y = height;
      if (p.y > height) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(99, 102, 241, ' + p.alpha + ')';
      ctx.fill();

      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const dx = p.x - p2.x;
        const dy = p.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 110) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = 'rgba(99, 102, 241, ' + (0.12 * (1 - dist / 110)) + ')';
          ctx.lineWidth = 0.75;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(animate);
  }
  animate();
})();

// ==========================================================================
// 2. Navigation Tabs
// ==========================================================================
document.querySelectorAll('.nav-tab').forEach(function(tabBtn) {
  tabBtn.addEventListener('click', function() {
    document.querySelectorAll('.nav-tab').forEach(function(b) { b.classList.remove('active'); });
    document.querySelectorAll('.tab-content').forEach(function(c) { c.classList.remove('active'); });

    tabBtn.classList.add('active');
    const targetId = tabBtn.getAttribute('data-tab');
    const targetTab = document.getElementById(targetId);
    if (targetTab) {
      targetTab.classList.add('active');
      if (targetId === 'analytics-tab') {
        fetchAnalytics();
      }
      if (targetId === 'whatif-tab') {
        runWhatIf();
      }
    }
  });
});

// ==========================================================================
// 3. Slider Sync Utility
// ==========================================================================
function updateSliderVal(name, displayVal, decimals) {
  const el = document.getElementById('val_' + name);
  if (el) {
    if (decimals !== undefined && decimals !== null && !isNaN(displayVal)) {
      el.textContent = parseFloat(displayVal).toFixed(decimals);
    } else {
      el.textContent = displayVal;
    }
  }
}

// ==========================================================================
// 4. Quick Presets Loader
// ==========================================================================
async function loadPreset(profileType) {
  try {
    const res = await fetch('/api/sample/' + encodeURIComponent(profileType));
    const data = await res.json();
    if (data.error) {
      alert(data.error);
      return;
    }

    document.getElementById('age').value = data.age;
    document.getElementById('gender').value = data.gender;
    document.getElementById('department').value = data.department;

    document.getElementById('cgpa').value = data.cgpa;
    updateSliderVal('cgpa', data.cgpa, 2);

    document.getElementById('attendance').value = data.attendance;
    updateSliderVal('attendance', data.attendance + '%');

    document.getElementById('tenth').value = data.tenth;
    updateSliderVal('tenth', data.tenth + '%');

    document.getElementById('twelfth').value = data.twelfth;
    updateSliderVal('twelfth', data.twelfth + '%');

    document.getElementById('backlogs').value = data.backlogs;
    document.getElementById('projects').value = data.projects;
    document.getElementById('internship').value = data.internship;

    document.getElementById('aptitude').value = data.aptitude;
    updateSliderVal('aptitude', data.aptitude);

    document.getElementById('communication').value = data.communication;
    updateSliderVal('communication', data.communication);

    runPrediction();
  } catch (err) {
    console.error('Error loading preset:', err);
  }
}

// ==========================================================================
// 5. Single Student Prediction Execution
// ==========================================================================
async function runPrediction() {
  const loading = document.getElementById('loadingSpinner');
  const resultContent = document.getElementById('resultContent');

  if (loading) loading.style.display = 'flex';
  if (resultContent) resultContent.style.opacity = '0.35';

  const payload = {
    age: document.getElementById('age').value,
    gender: document.getElementById('gender').value,
    department: document.getElementById('department').value,
    cgpa: document.getElementById('cgpa').value,
    attendance: document.getElementById('attendance').value,
    tenth: document.getElementById('tenth').value,
    twelfth: document.getElementById('twelfth').value,
    backlogs: document.getElementById('backlogs').value,
    projects: document.getElementById('projects').value,
    internship: document.getElementById('internship').value,
    aptitude: document.getElementById('aptitude').value,
    communication: document.getElementById('communication').value
  };

  try {
    const response = await fetch('/api/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    if (loading) loading.style.display = 'none';
    if (resultContent) resultContent.style.opacity = '1';

    if (data.error) {
      alert('Prediction Error: ' + data.error);
      return;
    }

    baselineProbability = data.probability;
    updateResultUI(data);
  } catch (err) {
    if (loading) loading.style.display = 'none';
    if (resultContent) resultContent.style.opacity = '1';
    alert('Server connection error: ' + err.message);
  }
}

function updateResultUI(data) {
  const prob = data.probability;
  const isPlaced = data.prediction === 1;

  // 1. Update Gauge & Status Pill
  const gaugeFill = document.getElementById('gaugeFill');
  const gaugePct = document.getElementById('gaugePct');
  const statusPill = document.getElementById('statusPill');

  const circumference = 264;
  const offset = circumference - (prob / 100) * circumference;
  if (gaugeFill) {
    gaugeFill.style.strokeDashoffset = offset;
    if (prob >= 75) {
      gaugeFill.style.stroke = '#10b981';
    } else if (prob >= 50) {
      gaugeFill.style.stroke = '#06b6d4';
    } else if (prob >= 35) {
      gaugeFill.style.stroke = '#f59e0b';
    } else {
      gaugeFill.style.stroke = '#f43f5e';
    }
  }

  if (gaugePct) {
    animateCounter(gaugePct, prob, '%');
  }

  if (statusPill) {
    if (isPlaced) {
      statusPill.className = 'status-pill status-placed';
      statusPill.innerHTML = '<i class="fa-solid fa-circle-check"></i> PLACED';
      triggerConfetti();
    } else {
      statusPill.className = 'status-pill status-notplaced';
      statusPill.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> NOT PLACED';
    }
  }

  // 2. Update Package and Tier
  const packageValue = document.getElementById('packageValue');
  const tierBadge = document.getElementById('tierBadge');

  if (packageValue) {
    if (isPlaced) {
      packageValue.textContent = data.insights.package_lpa + ' LPA';
    } else {
      packageValue.textContent = '0.00 LPA';
    }
  }

  if (tierBadge) {
    if (isPlaced) {
      tierBadge.textContent = data.insights.tier;
      tierBadge.className = 'tier-badge ' + data.insights.tier_badge;
    } else {
      tierBadge.textContent = 'Placement Support Needed';
      tierBadge.className = 'tier-badge';
    }
  }

  // 3. Update Radar Chart
  if (data.insights && data.insights.radar) {
    renderRadarChart(data.insights.radar);
  }

  // 4. Update Diagnostic Lists
  renderList('strengthsList', data.insights.strengths, 'No prominent strengths identified.');
  renderList('weaknessesList', data.insights.weaknesses, 'No major red flags detected!');
  renderList('roadmapList', data.insights.recommendations, 'Maintain current trajectory and practice interview communication.');
}

function renderList(elementId, items, emptyText) {
  const el = document.getElementById(elementId);
  if (!el) return;
  if (!items || items.length === 0) {
    el.innerHTML = '<li>' + emptyText + '</li>';
    return;
  }
  el.innerHTML = items.map(function(item) { return '<li>' + item + '</li>'; }).join('');
}

function animateCounter(el, target, suffix) {
  if (!suffix) suffix = '';
  const duration = 1000;
  const startTime = performance.now();

  function update(time) {
    const elapsed = time - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const val = (progress * target).toFixed(1);
    el.textContent = val + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

function triggerConfetti() {
  if (typeof confetti === 'function') {
    confetti({
      particleCount: 85,
      spread: 60,
      origin: { y: 0.7 },
      colors: ['#6366f1', '#10b981', '#38bdf8', '#fbbf24']
    });
  }
}

// ==========================================================================
// 6. 6-Factor Radar Chart
// ==========================================================================
function renderRadarChart(radarData) {
  const ctx = document.getElementById('radarChart');
  if (!ctx || typeof Chart === 'undefined') return;

  const labels = Object.keys(radarData);
  const scores = Object.values(radarData);

  if (radarChartInstance) {
    radarChartInstance.destroy();
  }

  radarChartInstance = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Candidate Readiness Score',
        data: scores,
        backgroundColor: 'rgba(99, 102, 241, 0.25)',
        borderColor: '#6366f1',
        pointBackgroundColor: '#38bdf8',
        pointBorderColor: '#fff',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
          grid: { color: 'rgba(255, 255, 255, 0.08)' },
          pointLabels: {
            color: '#94a3b8',
            font: { family: 'Inter', size: 11, weight: '500' }
          },
          ticks: {
            backdropColor: 'transparent',
            color: 'rgba(255, 255, 255, 0.4)',
            stepSize: 25,
            font: { size: 9 }
          },
          suggestedMin: 0,
          suggestedMax: 100
        }
      },
      plugins: { legend: { display: false } }
    }
  });
}

// ==========================================================================
// 7. Real-Time What-If Career Simulator
// ==========================================================================
let whatIfTimeout = null;

function runWhatIf() {
  const cgpaEl = document.getElementById('sim_cgpa');
  const projEl = document.getElementById('sim_projects');
  const backEl = document.getElementById('sim_backlogs');
  const aptEl = document.getElementById('sim_aptitude');
  const internEl = document.getElementById('sim_internship');

  if (!cgpaEl) return;

  document.getElementById('sim_cgpa_val').textContent = cgpaEl.value;
  document.getElementById('sim_projects_val').textContent = projEl.value;
  document.getElementById('sim_backlogs_val').textContent = backEl.value;
  document.getElementById('sim_aptitude_val').textContent = aptEl.value;

  clearTimeout(whatIfTimeout);
  whatIfTimeout = setTimeout(async function() {
    const payload = {
      cgpa: cgpaEl.value,
      projects: projEl.value,
      backlogs: backEl.value,
      aptitude: aptEl.value,
      internship: internEl.value,
      age: 22,
      gender: 'Male',
      department: 'CSE',
      attendance: 85,
      tenth: 80,
      twelfth: 80,
      communication: 75
    };

    try {
      const res = await fetch('/api/what-if', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (data.probability !== undefined) {
        document.getElementById('simProbDisplay').textContent = data.probability + '%';
        const simStatus = document.getElementById('simStatusDisplay');
        if (data.prediction === 1) {
          simStatus.textContent = 'Predicted: PLACED ??';
          simStatus.style.color = '#34d399';
        } else {
          simStatus.textContent = 'Predicted: NOT PLACED ??';
          simStatus.style.color = '#fb7185';
        }

        const delta = (data.probability - baselineProbability).toFixed(1);
        const deltaEl = document.getElementById('simDeltaDisplay');
        if (delta >= 0) {
          deltaEl.innerHTML = '<i class="fa-solid fa-arrow-trend-up"></i> +' + delta + '% vs baseline profile';
          deltaEl.style.color = '#34d399';
          deltaEl.style.background = 'rgba(16, 185, 129, 0.1)';
        } else {
          deltaEl.innerHTML = '<i class="fa-solid fa-arrow-trend-down"></i> ' + delta + '% vs baseline profile';
          deltaEl.style.color = '#fb7185';
          deltaEl.style.background = 'rgba(244, 63, 94, 0.1)';
        }
      }
    } catch (e) {
      console.error('What-If simulation failed:', e);
    }
  }, 150);
}

// ==========================================================================
// 8. Cohort Analytics & Historical Charts
// ==========================================================================
async function fetchAnalytics() {
  try {
    const res = await fetch('/api/analytics');
    const data = await res.json();
    if (data.error) return;

    document.getElementById('kpiTotal').textContent = data.total_students.toLocaleString();
    document.getElementById('kpiPlaced').textContent = data.placed_students.toLocaleString();
    document.getElementById('kpiRate').textContent = data.placement_rate + '%';
    document.getElementById('kpiAvgPkg').textContent = data.avg_package_lpa + ' LPA';

    renderDeptChart(data.department_rates);
    renderBacklogChart(data.backlog_rates);
  } catch (err) {
    console.error('Failed to load analytics:', err);
  }
}

function renderDeptChart(deptData) {
  const ctx = document.getElementById('deptChart');
  if (!ctx || typeof Chart === 'undefined') return;

  if (deptChartInstance) deptChartInstance.destroy();

  deptChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: Object.keys(deptData),
      datasets: [{
        label: 'Placement Rate (%)',
        data: Object.values(deptData),
        backgroundColor: 'rgba(99, 102, 241, 0.7)',
        borderRadius: 8,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#94a3b8' } },
        y: { grid: { color: 'rgba(255, 255, 255, 0.06)' }, ticks: { color: '#94a3b8' }, max: 100 }
      }
    }
  });
}

function renderBacklogChart(backlogData) {
  const ctx = document.getElementById('backlogChart');
  if (!ctx || typeof Chart === 'undefined') return;

  if (backlogChartInstance) backlogChartInstance.destroy();

  const labels = Object.keys(backlogData).map(function(b) { return b + ' Backlogs'; });
  const values = Object.values(backlogData);

  backlogChartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Placement Rate (%)',
        data: values,
        borderColor: '#f43f5e',
        backgroundColor: 'rgba(244, 63, 94, 0.15)',
        fill: true,
        tension: 0.35,
        pointBackgroundColor: '#f43f5e',
        pointRadius: 5
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#94a3b8' } },
        y: { grid: { color: 'rgba(255, 255, 255, 0.06)' }, ticks: { color: '#94a3b8' }, max: 100 }
      }
    }
  });
}

// ==========================================================================
// 9. Batch Prediction & CSV Export
// ==========================================================================
function openBatchFileInput() {
  const el = document.getElementById('batchFileInput');
  if (el) el.click();
}

async function handleFileUpload(file) {
  if (!file) return;
  const formData = new FormData();
  formData.append('file', file);

  const dropZone = document.getElementById('dropZone');
  dropZone.innerHTML = '<div class="spinner-ring"></div><p style="margin-top:10px">Processing Cohort Records...</p>';

  try {
    const res = await fetch('/api/batch-predict', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();

    dropZone.innerHTML = 
      '<i class="fa-solid fa-cloud-arrow-up upload-icon"></i>' +
      '<h3>Upload Student Cohort CSV</h3>' +
      '<p>Processed <strong>' + data.total_records + '</strong> candidates successfully!</p>' +
      '<input type="file" id="batchFileInput" accept=".csv" style="display: none;" onchange="handleFileUpload(this.files[0])" />' +
      '<button class="btn-primary" style="margin-top: 15px; width: auto; padding: 10px 24px;" onclick="openBatchFileInput()">' +
      'Upload Another CSV</button>';

    if (data.data) {
      batchDataCache = data.data;
      document.getElementById('batchResults').style.display = 'block';
      document.getElementById('batchSummaryText').textContent = 
        'Evaluated ' + data.total_records + ' students | ' + data.placed_count + ' Placed (' + ((data.placed_count/data.total_records)*100).toFixed(1) + '%)';

      const tbody = document.getElementById('batchTableBody');
      tbody.innerHTML = data.data.slice(0, 50).map(function(row) {
        return '<tr>' +
          '<td>#' + row.Student_ID + '</td>' +
          '<td>' + row.Department + '</td>' +
          '<td>' + row.CGPA + '</td>' +
          '<td><span class="status-pill ' + (row.Prediction === 'Placed' ? 'status-placed' : 'status-notplaced') + '">' + row.Prediction + '</span></td>' +
          '<td>' + row.Probability_Pct + '%</td>' +
        '</tr>';
      }).join('');
    }
  } catch (err) {
    alert('Failed to evaluate cohort batch: ' + err.message);
  }
}

function downloadSampleCSV() {
  const rows = [
    'Student_ID,Age,Gender,Department,CGPA,Attendance,10th_Percentage,12th_Percentage,Backlogs,Internship,Projects,Communication_Score,Aptitude_Score',
    '2001,22,Male,CSE,8.45,88.5,82.0,85.0,0,1,3,82,85',
    '2002,23,Female,ECE,7.10,75.0,78.0,72.0,1,0,2,65,68',
    '2003,22,Male,IT,9.20,95.0,91.0,89.5,0,1,4,90,92',
    '2004,24,Male,ME,5.80,60.0,62.0,59.0,3,0,1,52,50',
    '2005,22,Female,CSE,7.80,82.0,79.0,81.0,0,1,3,76,78'
  ];
  const csvContent = 'data:text/csv;charset=utf-8,' + encodeURIComponent(rows.join('\n'));
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', 'sample_placement_cohort.csv');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

function exportBatchResults() {
  if (!batchDataCache || batchDataCache.length === 0) {
    alert('No batch evaluation data available to export.');
    return;
  }
  const rows = ['Student_ID,Department,CGPA,Prediction,Probability_Pct'];
  batchDataCache.forEach(function(r) {
    rows.push(r.Student_ID + ',' + r.Department + ',' + r.CGPA + ',' + r.Prediction + ',' + r.Probability_Pct);
  });
  const csv = rows.join('\n');
  const encodedUri = encodeURI('data:text/csv;charset=utf-8,' + csv);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', 'evaluated_placement_results.csv');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Initial Auto-run on Page Load
window.addEventListener('DOMContentLoaded', function() {
  runPrediction();
});
