$path1 = New-Item -Path "C:\Users\user\Desktop\$folder1" -ItemType Directory
$path2 = New-Item -Path "C:\Users\user\Desktop\$folder2" -ItemType Directory
$path3 = New-Item -Path "C:\Users\user\Desktop\$folder3" -ItemType Directory

$newfolders = ($path2+"\Task\"), ($path2+"\One\"), ($path2+"\Submit\")

Remove-Item -Path "C:\Users\user\Desktop\$folder1\*"
Remove-Item -Path "C:\Users\user\Desktop\$folder2\*"