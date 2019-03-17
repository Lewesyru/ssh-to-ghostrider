@echo off

cls
echo Script created by Yi Ru.

echo.
echo Start writing file...
echo.

(echo. >> C:\Windows\System32\drivers\etc\hosts &&^
echo 140.232.230.73		ghostrider>> C:\Windows\System32\drivers\etc\hosts &&^
echo Done.) ||^
echo Please run again as administrator.

echo. & pause
