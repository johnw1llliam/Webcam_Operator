import subprocess
import sys

running = True

while running:
    print("====Input the operation number====")
    print("1. Turn Off WebCam")
    print("2. Turn On WebCam")
    print("0. Exit")
    user_input = int(input("Your input: "))
    if user_input == 1:
        comm_disable = subprocess.Popen(["powershell.exe", r"file_path\WebcamDisabler_github.ps1"], stdout=sys.stdout)
        comm_disable.communicate()
    elif user_input == 2:
        comm_enable = subprocess.Popen(["powershell.exe", r"file_path\WebcamEnabler_github.ps1"], stdout=sys.stdout)
        comm_enable.communicate()
    elif user_input == 0:
        print("Bye")
        running = False
    else:
        print("Input correct number!")