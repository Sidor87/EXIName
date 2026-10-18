#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build di EXIName in versione portable (cartella + zip).

Da lanciare tramite build_exe.bat (usa il Python di sistema).
Risultato:
    dist\\EXIName\\EXIName.exe  (+ cartella _internal)
    release\\EXIName_v<versione>_portable.zip   (con LEGGIMI.txt e LICENSE)
"""

import os
import re
import sys
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "EXIName.py"
ICON = ROOT / "EXIName.ico"
LICENSE = ROOT / "LICENSE"                 # copiata nello zip se presente
GITHUB_ICON = ROOT / "github.png"          # facoltativa
BUILD = ROOT / "build"
DIST = ROOT / "dist"
RELEASE = ROOT / "release"
APP = "EXIName"
AUTHOR = "Sidor87"

README = """EXIName {v} - versione portable
================================

Per avviare il programma apri:  EXIName.exe

Non serve installare nulla. La cartella "_internal" contiene i file
necessari al funzionamento: non spostarla, non rinominarla e non
cancellarla. Puoi spostare l'intera cartella EXIName dove vuoi
(anche su una chiavetta USB).

EXIName e' gratuito per uso personale e non commerciale; e' vietata
la vendita. Dettagli nel file LICENSE (PolyForm Noncommercial 1.0.0).

Aggiornamenti: https://github.com/Sidor87/EXIName
"""


def fail(msg):
    print(f"\n[ERRORE] {msg}")
    sys.exit(1)


def read_version() -> str:
    text = SCRIPT.read_text(encoding="utf-8")
    m = re.search(r'^APP_VERSION\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not m:
        fail("APP_VERSION non trovata in EXIName.py")
    return m.group(1)


def write_version_file(version: str) -> Path:
    """Dati mostrati in Proprieta' > Dettagli dell'exe."""
    nums = [int(x) for x in re.findall(r"\d+", version)][:4]
    nums += [0] * (4 - len(nums))
    t = tuple(nums)
    content = f"""VSVersionInfo(
  ffi=FixedFileInfo(filevers={t}, prodvers={t}, mask=0x3f, flags=0x0,
                    OS=0x40004, fileType=0x1, subtype=0x0, date=(0, 0)),
  kids=[
    StringFileInfo([StringTable('041004B0', [
      StringStruct('CompanyName', '{AUTHOR}'),
      StringStruct('FileDescription', 'EXIName - Rinomina intelligente per data di scatto'),
      StringStruct('FileVersion', '{version}'),
      StringStruct('InternalName', '{APP}'),
      StringStruct('LegalCopyright', '(c) {AUTHOR}'),
      StringStruct('OriginalFilename', '{APP}.exe'),
      StringStruct('ProductName', '{APP}'),
      StringStruct('ProductVersion', '{version}')])]),
    VarFileInfo([VarStruct('Translation', [1040, 1200])])
  ]
)
"""
    BUILD.mkdir(exist_ok=True)
    path = BUILD / "version_info.txt"
    path.write_text(content, encoding="utf-8")
    return path


def run_pyinstaller(version_file: Path):
    import PyInstaller.__main__

    args = [
        str(SCRIPT),
        "--name", APP,
        "--onedir",                     # cartella: EXIName.exe + _internal
        "--windowed",                   # niente finestra nera della console
        "--noconfirm",
        "--clean",
        "--noupx",                      # UPX aumenta i falsi allarmi degli antivirus
        "--icon", str(ICON),
        "--version-file", str(version_file),
        "--distpath", str(DIST),
        "--workpath", str(BUILD / "pyinstaller"),
        "--specpath", str(BUILD),
        # librerie con file extra o moduli caricati dinamicamente
        "--collect-data", "customtkinter",      # temi .json
        "--collect-all", "tkinterdnd2",         # librerie native del drag & drop
        "--collect-submodules", "hachoir",      # lettori delle date dei video
        "--collect-all", "pillow_heif",         # supporto .heic
        "--hidden-import", "PIL._tkinter_finder",  # immagini Pillow dentro tkinter
        # moduli inutili che gonfierebbero la build
        "--exclude-module", "numpy",
        "--exclude-module", "matplotlib",
        "--exclude-module", "pandas",
        "--exclude-module", "scipy",
        "--exclude-module", "IPython",
    ]
    if GITHUB_ICON.exists():
        args += ["--add-data", f"{GITHUB_ICON}{os.pathsep}."]
    PyInstaller.__main__.run(args)


def make_zip(version: str) -> Path:
    app_dir = DIST / APP
    (app_dir / "LEGGIMI.txt").write_text(README.format(v=version), encoding="utf-8")
    if LICENSE.exists():
        shutil.copy2(LICENSE, app_dir / "LICENSE.txt")
    RELEASE.mkdir(exist_ok=True)
    zip_path = RELEASE / f"{APP}_v{version}_portable.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted(app_dir.rglob("*")):
            if f.is_file():
                z.write(f, Path(APP) / f.relative_to(app_dir))
    return zip_path


def main():
    for f in (SCRIPT, ICON):
        if not f.exists():
            fail(f"manca il file {f.name} nella cartella {ROOT}")
    version = read_version()
    print(f"== Build di {APP} {version} ==")

    if (DIST / APP).exists():
        shutil.rmtree(DIST / APP)
    run_pyinstaller(write_version_file(version))

    exe = DIST / APP / (APP + (".exe" if os.name == "nt" else ""))
    if not exe.exists():
        fail("l'eseguibile non e' stato creato: controlla i messaggi sopra.")
    zip_path = make_zip(version)
    size = zip_path.stat().st_size / 1024 / 1024
    print("\n== Fatto ==")
    print(f"  Programma : {exe}")
    print(f"  Zip       : {zip_path}  ({size:.1f} MB)")


if __name__ == "__main__":
    main()
