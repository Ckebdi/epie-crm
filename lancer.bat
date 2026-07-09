@echo off
echo ============================================
echo    CRM RH - Epie Formation
echo ============================================
echo.
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR : Python n'est pas installe.
    echo Telecharge-le sur https://www.python.org/downloads/
    pause
    exit /b
)
echo Installation des dependances...
pip install flask openpyxl --quiet
echo.
echo Demarrage du serveur CRM...
echo.
echo  Ouvre ton navigateur : http://localhost:5000
echo  Reseau local : http://[IP_DU_SERVEUR]:5000
echo.
echo  (Ctrl+C pour arreter)
echo.
python app.py
pause
