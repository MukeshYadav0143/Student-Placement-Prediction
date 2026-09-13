import os
import sys
import time
import webbrowser
import threading

def open_browser():
    time.sleep(2.0)
    url = "http://127.0.0.1:5000"
    print(f"\n=======================================================")
    print(f"   CAMPUSPULSE AI - PLACEMENT PREDICTION PLATFORM      ")
    print(f"=======================================================")
    print(f" [OK] Server running at: {url}")
    print(f" [OK] Launching user interface in browser...")
    print(f" Press CTRL+C in this terminal to stop the server.")
    print(f"=======================================================\n")
    webbrowser.open(url)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "random_forest_placement_model.pkl")

    if not os.path.exists(model_path):
        print("[!] Trained model not found. Training model now...")
        from src.train_model import train
        train()

    threading.Thread(target=open_browser, daemon=True).start()

    from app import app
    app.run(host="127.0.0.1", port=5000, debug=False)
