if (Test-Path -Path ".\new_folder" -ItemType Directory) {
    New-Item -Path ".\if_folder" -ItemType Directory
    Write-Output "'new_folder' exists. 'if_folder' created."
} else {
    Write-Output "'new_folder' does not exist.'if_folder' not created."
}

if (Test-Path -Path ".\if_folder" -ItemType Directory) {
    New-Item -Path ".\hyperionDev" -ItemType Directory
    Write-Output "'if_folder' exists. 'hyperionDev' created."
} else {
    New-Item -Path ".new-projects" -ItemType Directory
    Write-Output "'if_folder' does not exist. 'new-projects' created."
}
