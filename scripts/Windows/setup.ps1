# This script is still in testing.
# Do not use this one.

Write-Host "Script created by Yi Ru.`n"
Write-Host "Start writing file...`n"

(Add-Content C:\Windows\System32\drivers\etc\hosts "`n") -and `
(Add-Content C:\Windows\System32\drivers\etc\hosts "140.232.230.73		ghostrider") -and `
(Write-Host "Done." -ForegroundColor green) -or `
(Write-Host "Permission denied. Please run again as administrator.`n" -ForegroundColor red)

Pause
