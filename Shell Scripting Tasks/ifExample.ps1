if (Test-Path -Path "C:\Users\User\Hyperion\ShellScripting\new_folder" -ItemType Directory) {
    New-Item -Path "C:\Users\User\Hyperion\ShellScripting\if_folder" -ItemType Directory
    Write-Output "'new_folder' exists. 'if_folder' created."
} else {
    Write-Output "'new_folder' does not exist.'if_folder' not created."
}

if (Test-Path -Path "C:\Users\User\Hyperion\ShellScripting\if_folder" -ItemType Directory) {
    New-Item -Path "C:\Users\User\Hyperion\ShellScripting\hyperionDev" -ItemType Directory
    Write-Output "'if_folder' exists. 'hyperionDev' created."
} else {
    New-Item -Path "C:\Users\User\Hyperion\ShellScripting\new-projects" -ItemType Directory
    Write-Output "'if_folder' does not exist. 'new-projects' created."
}
