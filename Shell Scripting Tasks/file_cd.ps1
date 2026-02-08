New-Item -Path "Shell", "Scripting", "Task" -ItemType Directory

cd Shell

New-Item -Path "HyperionDev", "Powershell", "New Folder" -ItemType Directory

cd ..

Remove-Item -Path "Scripting", "Task"