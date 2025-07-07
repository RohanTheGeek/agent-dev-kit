import psutil
import time
import socket
import json
import os
import shutil

SERVER_IP = "192.168.86.81"
SERVER_PORT = 9999

def clean_temp_dirs():
    cleaned_paths = ['/tmp', '/var/tmp', os.path.expanduser('~/.cache')]
    deleted_files = 0

    # Targeted cleanup for /var/tmp/junkfile
    junkfile = '/var/tmp/junkfile'
    if os.path.exists(junkfile):
        try:
            os.remove(junkfile)
            deleted_files += 1
        except Exception as e:
            print("Failed to delete junkfile:", e)

    # General temp/cache cleanup
    for path in cleaned_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                        deleted_files += 1
                    except:
                        pass
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                    except:
                        pass
    return deleted_files

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk_before = psutil.disk_usage('/').percent
    action = None

    if disk_before > 80:
        deleted = clean_temp_dirs()
        time.sleep(2)  # Let OS release space
        disk_after = psutil.disk_usage('/').percent
        action = f"Auto-cleaned {deleted} temp/cache files"
    else:
        disk_after = disk_before

    return {
        "cpu_percent": cpu,
        "memory_percent": mem,
        "disk_percent": disk_after,       # For ML model
        "disk_before": disk_before,       # For display
        "disk_after": disk_after,         # For display
        "action_taken": action or "None", # For display
        "boot_time": time.ctime(psutil.boot_time())
    }

# Main loop
while True:
    data = json.dumps(get_system_metrics())
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(data.encode('utf-8'))
        s.close()
    except Exception as e:
        print("Error:", e)
    time.sleep(5)

