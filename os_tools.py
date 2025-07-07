# os_tools.py
import os
import psutil
import platform
import socket
import shutil
import zipfile
import time
import pyperclip
from datetime import datetime
from PIL import ImageGrab
import requests

# Restrict file operations to base directory
BASE_DIR = os.getcwd()

def _safe_path(path):
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(BASE_DIR):
        raise ValueError("Access outside base directory is not allowed.")
    return abs_path

def log_action(action, result):
    with open("agent.log", "a") as log:
        log.write(f"[{datetime.now()}] ACTION: {action}\nRESULT: {result}\n\n")

# ─── SYSTEM INFO ───────────────────────────────────────────────────────

def get_cpu_usage():
    result = f"CPU usage is {psutil.cpu_percent(interval=1)}%"
    log_action("get_cpu_usage", result)
    return result

def get_memory_usage():
    mem = psutil.virtual_memory()
    result = f"Memory usage: {mem.percent}% of {round(mem.total / (1024**3), 2)} GB"
    log_action("get_memory_usage", result)
    return result

def get_disk_usage():
    usage = psutil.disk_usage(BASE_DIR)
    result = f"Disk usage: {usage.percent}% ({round(usage.used/(1024**3), 2)} GB used / {round(usage.total/(1024**3), 2)} GB total)"
    log_action("get_disk_usage", result)
    return result

def get_uptime():
    uptime = time.time() - psutil.boot_time()
    minutes = int(uptime // 60)
    result = f"System uptime: {minutes} minutes"
    log_action("get_uptime", result)
    return result

def get_os_info():
    info = platform.uname()
    result = f"OS: {info.system} {info.release}, Version: {info.version}"
    log_action("get_os_info", result)
    return result

# ─── FILE & DIRECTORY OPS ──────────────────────────────────────────────

def list_files(path="."):
    try:
        path = _safe_path(path)
        result = "\n".join(os.listdir(path))
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"list_files({path})", result)
    return result

def create_file(filename, content=""):
    try:
        filename = _safe_path(filename)
        with open(filename, "w") as f:
            f.write(content)
        result = f"File '{filename}' created."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"create_file({filename})", result)
    return result

def read_file(filename):
    try:
        filename = _safe_path(filename)
        with open(filename, "r") as f:
            result = f.read()
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"read_file({filename})", result)
    return result

def delete_file(filename):
    try:
        filename = _safe_path(filename)
        os.remove(filename)
        result = f"File '{filename}' deleted."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"delete_file({filename})", result)
    return result

def rename_file(old_name, new_name):
    try:
        old_name = _safe_path(old_name)
        new_name = _safe_path(new_name)
        os.rename(old_name, new_name)
        result = f"Renamed '{old_name}' to '{new_name}'."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"rename_file({old_name}, {new_name})", result)
    return result

def move_file(src, dst):
    try:
        src = _safe_path(src)
        dst = _safe_path(dst)
        shutil.move(src, dst)
        result = f"Moved '{src}' to '{dst}'."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"move_file({src}, {dst})", result)
    return result

def copy_file(src, dst):
    try:
        src = _safe_path(src)
        dst = _safe_path(dst)
        shutil.copy(src, dst)
        result = f"Copied '{src}' to '{dst}'."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"copy_file({src}, {dst})", result)
    return result

def zip_folder(folder_path):
    try:
        folder_path = _safe_path(folder_path)
        zip_name = f"{folder_path}.zip"
        shutil.make_archive(folder_path, 'zip', folder_path)
        result = f"Folder '{folder_path}' zipped as '{zip_name}'."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"zip_folder({folder_path})", result)
    return result

def create_directory(dirname):
    try:
        dirname = _safe_path(dirname)
        os.makedirs(dirname, exist_ok=True)
        result = f"Directory '{dirname}' created."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"create_directory({dirname})", result)
    return result

def delete_directory(dirname):
    try:
        dirname = _safe_path(dirname)
        shutil.rmtree(dirname)
        result = f"Directory '{dirname}' deleted."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"delete_directory({dirname})", result)
    return result

# ─── NETWORK OPS ───────────────────────────────────────────────────────

def check_connectivity():
    try:
        requests.get("https://www.google.com", timeout=3)
        result = "Internet connection: ✅ Available"
    except:
        result = "Internet connection: ❌ Unavailable"
    log_action("check_connectivity", result)
    return result

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        result = f"IP Address: {ip}"
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action("get_ip_address", result)
    return result

# ─── CLIPBOARD + SCREENSHOT ────────────────────────────────────────────

def get_clipboard():
    try:
        result = pyperclip.paste()
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action("get_clipboard", result)
    return result

def set_clipboard(text):
    try:
        pyperclip.copy(text)
        result = "Text copied to clipboard."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action(f"set_clipboard({text})", result)
    return result

def take_screenshot():
    try:
        image = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        image.save(filename)
        result = f"Screenshot saved as '{filename}'."
    except Exception as e:
        result = f"[ERROR] {e}"
    log_action("take_screenshot", result)
    return result
