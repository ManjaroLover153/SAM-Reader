import winreg
import ctypes
import os
import sys
import re

def is_admin():
    """Check if the script is running with admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def read_user_rids():
    """Read user RIDs from SAM registry hive."""
    print("=== Local User RIDs ===")
    rids = []
    path = r"SAM\SAM\Domains\Account\Users"
    try:
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as reg:
            with winreg.OpenKey(reg, path) as key:
                i = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        if subkey_name != "Names":
                            rids.append(subkey_name)
                            print(f"RID: {subkey_name}")
                        i += 1
                    except OSError:
                        break
    except PermissionError:
        print("[!] Access denied. Run as Administrator.")
    return rids

def list_usernames():
    """List local account usernames."""
    print("\n=== Local Usernames ===")
    usernames = []
    path = r"SAM\SAM\Domains\Account\Users\Names"
    try:
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as reg:
            with winreg.OpenKey(reg, path) as key:
                i = 0
                while True:
                    try:
                        username = winreg.EnumKey(key, i)
                        usernames.append(username)
                        print(f"- {username}")
                        i += 1
                    except OSError:
                        break
    except PermissionError:
        print("[!] Access denied. Run as Administrator.")
    return usernames

def extract_strings_from_binary(data):
    """Attempt to extract readable ASCII/UTF-16LE strings from binary."""
    ascii_strings = re.findall(rb'[ -~]{4,}', data)
    utf16_strings = re.findall(rb'(?:[\x20-\x7E]\x00){4,}', data)

    decoded = []

    for s in ascii_strings:
        try:
            decoded.append(s.decode('ascii'))
        except:
            pass

    for s in utf16_strings:
        try:
            decoded.append(s.decode('utf-16le'))
        except:
            pass

    return decoded

def read_security_questions(rids):
    """Attempt to read security question data from F binary value."""
    print("\n=== Attempting to Read Security Questions ===")
    base = r"SAM\SAM\Domains\Account\Users"
    try:
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as reg:
            for rid in rids:
                path = f"{base}\\{rid}"
                try:
                    with winreg.OpenKey(reg, path) as key:
                        data, _ = winreg.QueryValueEx(key, "F")
                        strings = extract_strings_from_binary(data)
                        print(f"\n[RID: {rid}] Possible strings found:")
                        for s in strings:
                            if "?" in s.lower() or "your" in s.lower():
                                print(f"  > {s}")
                except FileNotFoundError:
                    continue
    except PermissionError:
        print("[!] Access denied reading security questions.")

def main():
    print("================================")
    print(" Windows SAM Viewer + Security Questions")
    print("================================")

    if not is_admin():
        print("[!] You must run this script as Administrator.")
        os.system("pause")
        sys.exit(1)

    rids = read_user_rids()
    list_usernames()
    read_security_questions(rids)

    print("\n[*] Done.")
    os.system("pause")

if __name__ == "__main__":
    main()
