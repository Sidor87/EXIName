# EXIName

🇮🇹 **Italiano** · 🇬🇧 [English](#english)

EXIName è un'applicazione per Windows che rinomina automaticamente foto e video
usando la data e l'ora di scatto salvate nei metadati EXIF, con il formato
`AAAA-MM-GG hh.mm.ss`. Così i file si ordinano in modo cronologico in qualsiasi
cartella, indipendentemente dal dispositivo che li ha creati.

### Funzionalità
- Rinomina in base alla data di scatto EXIF
- Selezione di più cartelle, con opzione per includere le sottocartelle
- Drag & drop di cartelle e file
- Formati supportati: JPG, PNG, TIFF, DNG, NEF, MP4, MOV
- Scheda **Rinomina WhatsApp**: converte i nomi dei file WhatsApp
  (es. `IMG-20260825-WA0002` → `2026-08-25-WA0002`)
- Anteprima prima/dopo in tabella, prima di applicare le modifiche
- Interfaccia semplice e moderna (customtkinter)

### Requisiti
- Windows
- Python 3 (solo per eseguire dal sorgente)

### Avvio dal sorgente
```bash
pip install -r requirements.txt
python EXIName.py
```

### Creazione dell'eseguibile
Esegui `build_exe.bat`: lo script controlla che Python sia installato, pulisce
le build precedenti, installa le dipendenze e PyInstaller e crea il programma
nella cartella `dist\EXIName`.

> ⚠️ Distribuisci sempre **l'intera cartella** `EXIName`: `EXIName.exe` non si
> avvia senza la cartella `_internal` che si trova accanto.

### Dipendenze
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) – interfaccia grafica
- [Pillow](https://python-pillow.org/) – lettura EXIF delle immagini
- [pillow-heif](https://github.com/bigcat88/pillow_heif) – supporto HEIC
- [hachoir](https://github.com/vstinner/hachoir) – metadati dei video
- [tkinterdnd2](https://github.com/Eliav2/tkinterdnd2) – drag & drop

---

<a name="english"></a>
## 🇬🇧 English

EXIName is a Windows application that automatically renames photos and videos
using the capture date and time stored in their EXIF metadata, in the format
`YYYY-MM-DD hh.mm.ss`. Your files sort chronologically in any folder, no matter
which device created them.

### Features
- Rename by EXIF capture date
- Select multiple folders, with an option to include subfolders
- Drag & drop folders and files
- Supported formats: JPG, PNG, TIFF, DNG, NEF, MP4, MOV
- **WhatsApp Rename** tab: converts WhatsApp file names
  (e.g. `IMG-20260825-WA0002` → `2026-08-25-WA0002`)
- Before/after preview table before applying changes
- Clean, modern interface (customtkinter)

### Requirements
- Windows
- Python 3 (only to run from source)

### Run from source
```bash
pip install -r requirements.txt
python EXIName.py
```

### Build the executable
Run `build_exe.bat`: the script checks that Python is installed, cleans previous
builds, installs the dependencies and PyInstaller, and creates the program in
the `dist\EXIName` folder.

> ⚠️ Always distribute the **whole** `EXIName` folder: `EXIName.exe` won't start
> without the `_internal` folder next to it.

### Dependencies
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) – GUI
- [Pillow](https://python-pillow.org/) – image EXIF reading
- [pillow-heif](https://github.com/bigcat88/pillow_heif) – HEIC support
- [hachoir](https://github.com/vstinner/hachoir) – video metadata
- [tkinterdnd2](https://github.com/Eliav2/tkinterdnd2) – drag & drop
