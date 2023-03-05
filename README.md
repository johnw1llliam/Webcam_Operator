# WebcamOperator

## Description
This program will help you to enable and disable webcam on your Laptop/PC without having to buy webcam cover and potentially break your screen (due to the pressure that you apply during opening and closing the cover to your screen).

With the help of python and Windows Powershell, we can disable our webcam easily without having to type the script in the powershell everytime we want to turn on/off our camera.

## Installation
### 1. Set Execution Policy in Powershell to Unrestricted </br>
1.1. Press windows search button </br>
1.2. Type 'Windows Power Shell' </br>
1.3. Launch Windows Powershell as Administrator </br>
1.4. Type: Set-ExecutionPolicy Unrestricted -Scope CurrentUser </br>
1.5. press 'y' and enter </br>

### 2. Finding out your camera device name
2.1. Press windows search button </br>
2.2. type 'Device Manager' and enter </br>
2.3. Click cameras and you will find your camera device name </br>
2.4. Remember it or write it, you will need it </br>

### 3. Moving up the .ps1 files
3.1. Copy the .ps1 files </br>
3.2. Move them to any directory that you want </br>
3.3. Remember the directory or write it, you will need it </br>

### 4. Changing data in the .ps1 files
4.1. Edit the .ps1 files (you can use notepad or notepad++) </br>
4.2. Change the "camera_name" in both .ps1 files to your device camera name in step 2, example: "HP Wide Vision Camera HD" </br>
4.3. Save the changes </br>

### 5. Changing data in the python file
5.1. Change the comm_enable and comm_disable variable file path to the directory in step 3, </br>
     ex:  comm_disable = subprocess.Popen(["powershell.exe", r"C:\PS1\WebcamDisabler.ps1"], stdout=sys.stdout) </br>
          comm_enable = subprocess.Popen(["powershell.exe", r"file_path\WebcamEnabler.ps1"], stdout=sys.stdout) </br>
5.2. Save the file and run it! </br>

Note: You can convert the python file to exe, just google it. This will make your life easier
