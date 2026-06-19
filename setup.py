#This Python script prepares the environment for the app
#This script does the following checks:-
#   * Checks if KDE Connect is installed
#   * Checks whether scrcpy is downloaded
#   * Checks if v4l2 library is available

def checkKDEConnect():
    import shutil
    if shutil.which("kdeconnect-cli"):
        print("[OK] KDE Connect is installed")
    else:
        print("[*] KDE Connect not available")

def checkscrcpy():
    from pathlib import Path
    if Path("scrcpy").exists:
        print("[OK] Scrcpy is installed")
    else:
        print("[*] Scrcpy not available")

def checkVideo4Linux():
    import shutil
    if shutil.which("v4l2loopback"):
        print("[OK] V4L2 is installed")
    else:
        print("[*] V4L2 not available")

if __name__ == "__main__":
    checkKDEConnect()
    checkscrcpy()
    checkVideo4Linux()
