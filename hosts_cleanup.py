import os
import shutil
import sys
import ctypes

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BACKUP_PATH = HOSTS_PATH + ".backup"

TARGET_LINES = {
    "# force disable ghub updates:",
    "127.0.0.1 updates.ghub.logitechg.com",
    "127.0.0.1 util.logitech.io",
}

# ---------------- ADMIN CHECK ---------------- #

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relaunch_as_admin():
    params = " ".join(f'"{arg}"' for arg in sys.argv)
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1
    )
    sys.exit(0)

# ---------------- CORE LOGIC ---------------- #

def backup_hosts():
    if not os.path.exists(BACKUP_PATH):
        shutil.copy2(HOSTS_PATH, BACKUP_PATH)
        print(f"[✔] Backup created → {BACKUP_PATH}")
    else:
        print("[i] Backup already exists")

def restore_hosts():
    if not os.path.exists(BACKUP_PATH):
        print("[✖] No backup found — nothing to restore")
        return

    shutil.copy2(BACKUP_PATH, HOSTS_PATH)
    print("[✔] Hosts file restored successfully")

def clean_hosts():
    if not os.path.exists(HOSTS_PATH):
        print("[✖] Hosts file not found")
        return

    with open(HOSTS_PATH, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    new_lines = []
    removed = 0

    for line in lines:
        if line.strip() in TARGET_LINES:
            removed += 1
        else:
            new_lines.append(line)

    if removed == 0:
        print("[i] No matching entries found — nothing removed")
        return

    # Write safely (never empty-write)
    with open(HOSTS_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(new_lines)

    print(f"[✔] Removed {removed} blocked GHub entrie(s)")

# ---------------- MENU ---------------- #

def menu():
    while True:
        print("\n=== Hosts File Utility ===")
        print("1) Remove Logitech GHub blocks")
        print("2) Restore hosts file from backup")
        print("3) Exit")

        choice = input("\nSelect an option (1/2/3): ").strip()

        if choice == "1":
            backup_hosts()
            clean_hosts()
        elif choice == "2":
            restore_hosts()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("[✖] Invalid option")

# ---------------- ENTRY ---------------- #

if __name__ == "__main__":
    if not is_admin():
        print("[!] Admin required — requesting elevation...")
        relaunch_as_admin()

    try:
        menu()
    except Exception as e:
        print("\n[CRITICAL ERROR]")
        print(e)
        input("\nPress Enter to exit...")
