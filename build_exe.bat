@echo off
setlocal

echo ============================================
echo   EXIName - creazione automatica del file .exe
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo ERRORE: Python non e' stato trovato nel PATH di sistema.
    echo Installa Python da https://www.python.org/downloads/
    echo IMPORTANTE: durante l'installazione spunta "Add python.exe to PATH".
    echo Poi rilancia questo file.
    echo.
    pause
    exit /b 1
)

echo [1/3] Pulisco eventuali build precedenti ...
if exist ".venv" rmdir /s /q ".venv"
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "EXIName.spec" del /q "EXIName.spec"

echo.
echo [2/3] Installo le dipendenze del programma e PyInstaller ...
python -m pip install --upgrade pip >nul
python -m pip install -r requirements.txt pyinstaller
if errorlevel 1 (
    echo.
    echo ERRORE durante l'installazione delle dipendenze. Controlla il messaggio sopra.
    pause
    exit /b 1
)

echo.
echo [3/3] Creo l'eseguibile con PyInstaller (puo' richiedere qualche minuto) ...
python -m PyInstaller --noconfirm --onedir --windowed --name EXIName ^
    --icon EXIName.ico ^
    --collect-data customtkinter ^
    --collect-all pillow_heif ^
    --collect-all tkinterdnd2 ^
    --collect-submodules hachoir ^
    --hidden-import PIL._tkinter_finder ^
    EXIName.py

if errorlevel 1 (
    echo.
    echo ERRORE durante la creazione dell'eseguibile. Controlla il messaggio sopra.
    pause
    exit /b 1
)

echo.
echo Fatto!
echo.
echo Trovi il programma nella cartella "dist\EXIName":
echo   - EXIName.exe
echo   - la cartella _internal
echo Copia sempre TUTTA la cartella "EXIName": l'exe senza _internal non si avvia.
echo.
pause
