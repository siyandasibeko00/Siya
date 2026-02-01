$newFolder = "C:\Users\Folder\new_folder"
$ifFolder = "C:\Users\Folder\if_folder"

if (Test-Path -Path $newFolder -PathType) {
    Write-Putput "The folder 'new_folder' already exists. Creating 'if_folder'."

    New-Item -Path $ifFolder -ItemType Directory
    Write-Output "Folder 'if_folder' created."
} else {
    Write-Output "The folder 'new_folder' does not exist. 'if_folder' not created."
}

if (Test-Path -Path ".$ifFolder") {
    New-Item -Path ".\hyperionDev" -ItemType Directory
    Write-Output "if_folder found. Create hyperionDev."
} else {
    New-Item -Path ".$newFolder" -ItemType Directory
    Write-Output "if_folder not found. Create new-projects."
}
