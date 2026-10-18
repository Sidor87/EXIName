<img width="596" height="400" alt="EXIName" src="https://github.com/user-attachments/assets/ccfdd5f9-ee2e-45f4-91ed-4bb2c0354e54" />

# EXIName

🇮🇹 **Italiano** · 🇬🇧 [English](#english)

**EXIName** è un programma gratuito per Windows che rinomina in blocco foto e video usando
la **data e l'ora reali dello scatto**, lette dai metadati del file. Il nome predefinito è:

```
2025-12-24 18.05.32.jpg
```

Così i file si mettono in ordine cronologico da soli, in qualsiasi cartella, anche se
arrivano da telefoni, fotocamere o app diverse.

Versione attuale: **0.3.0** · Interfaccia in italiano e inglese

---

## Indice
- [Scarica e avvia](#scarica-e-avvia)
- [Come si usa](#come-si-usa)
- [Rinomina per data](#rinomina-per-data)
- [Rinomina WhatsApp](#rinomina-whatsapp)
- [Foto scattate nello stesso secondo](#foto-scattate-nello-stesso-secondo)
- [Escludere dei file dalla rinomina](#escludere-dei-file-dalla-rinomina)
- [Colori della tabella](#colori-della-tabella)
- [Formati supportati](#formati-supportati)
- [Sicurezza dei file](#sicurezza-dei-file)
- [Impostazioni salvate](#impostazioni-salvate)
- [Avvio dal sorgente e creazione dell'eseguibile](#avvio-dal-sorgente-e-creazione-delleseguibile)
- [Novità](#novità)
- [Licenza](#licenza)

---

## Scarica e avvia

1. Vai nella pagina [**Releases**](https://github.com/Sidor87/EXIName/releases/latest)
   e scarica `EXIName_v<versione>_portable.zip`.
2. Estrai lo zip dove vuoi (anche su una chiavetta USB).
3. Apri `EXIName.exe`.

Non serve installare nulla.

> ⚠️ Tieni sempre insieme `EXIName.exe` e la cartella `_internal` che si trova accanto:
> senza quella cartella il programma non parte. Se vuoi spostarlo, sposta l'intera cartella `EXIName`.

> ℹ️ Alla prima apertura Windows SmartScreen può mostrare l'avviso «App non riconosciuta»,
> perché il programma non è firmato digitalmente. Clicca **Ulteriori informazioni → Esegui comunque**.

---

## Come si usa

1. **Aggiungi le cartelle**: premi **＋ Aggiungi cartella** oppure trascina cartelle o
   singoli file dentro la finestra. Puoi aggiungerne quante vuoi; ognuna appare come
   un'etichetta con la ✕ per toglierla (passando il mouse vedi il percorso completo).
2. **Sottocartelle**: lascia spuntato **Includi sottocartelle** se vuoi leggere anche le
   cartelle contenute (accanto vedi quante sono). La scelta viene ricordata.
3. Premi **▶ Avvia**. Il programma legge le cartelle e poi la data di scatto di ogni file.
   Puoi usare **Pausa** e **Stop** (con Stop tieni i risultati letti fino a quel momento).
   La barra di stato mostra percentuale, tempo trascorso e tempo rimanente.
4. **Controlla la tabella**: per ogni file vedi il nome attuale e quello proposto.
5. Togli con **Canc** i file che non vuoi rinominare (vedi [sotto](#escludere-dei-file-dalla-rinomina)).
6. Premi **Rinomina** e conferma.

Aggiungere o togliere cartelle non avvia nulla: la lettura parte solo con **Avvia**.

---

## Rinomina per data

Per ogni foto o video EXIName cerca la data di scatto:

| Tipo di file | Da dove legge la data |
|---|---|
| Immagini (JPG, HEIC, PNG, …) | EXIF `DateTimeOriginal` / `DateTimeDigitized` |
| RAW basati su TIFF (DNG, NEF, TIFF) | EXIF letto direttamente, senza aprire l'immagine RAW |
| Video (MP4, MOV, …) | metadati del contenitore (data di creazione) |

Se la data di scatto **manca** (o è una data "segnaposto" precedente al 1970), viene usata la
**data di ultima modifica** del file. Per questo la tabella ha due colonne:

- **Rinomina EXIF**: file con una data di scatto vera;
- **Rinomina modifica**: file senza data di scatto, rinominati con la data di modifica.

### Correggere una data a mano
Fai **doppio click** sulla data proposta, scrivi quella giusta nel formato
`aaaa-mm-gg hh.mm.ss` e conferma. La riga diventa arancione.

Doppio click sul **nome del file** invece apre il file con il programma predefinito.

### Formato del nome
Sopra la tabella ci sono tre menu per scegliere il formato:

| Menu | Opzioni |
|---|---|
| **Data** | `aaaa-mm-gg` (predefinito), `gg-mm-aaaa`, `mm-gg-aaaa`, `aaaa_mm_gg`, `gg_mm_aaaa`, `aaaammgg`, `gg.mm.aaaa` |
| **Ora** | `hh.mm.ss` (predefinito), `hh-mm-ss`, `hhmmss`, `hh.mm`, `hh-mm`, senza orario |
| **Separatore** tra data e ora | spazio (predefinito), `_`, `-` |

A destra vedi un esempio del risultato. Ogni cambio di formato va confermato e viene
**ricordato** per le volte successive. Il pulsante **Predefinito** riporta al formato
`aaaa-mm-gg hh.mm.ss`.

---

## Rinomina WhatsApp

La seconda scheda sistema i file con il nome tipico di WhatsApp
(`IMG-`, `VID-`, `AUD-`, `PTT-`, `STK-`, `DOC-`):

```
IMG-20260825-WA0002.jpg  →  2026-08-25-WA0002.jpg
```

La data è presa dal nome stesso, quindi funziona anche quando WhatsApp ha cancellato i
metadati. Tre opzioni, con esempio dal vivo:

- **Togli prefisso** (`IMG-`, `VID-`, …)
- **Data con trattini** (`20260825` → `2026-08-25`)
- **Togli contatore** (`-WA0002`) – se due file finiscono con lo stesso nome ricevono `_1`, `_2`

Il pulsante **Rinomina** agisce sulla scheda aperta in quel momento.

---

## Foto scattate nello stesso secondo

Raffiche e foto multiple possono avere lo stesso identico orario. Invece di aggiungere
`_1`, `_2`, EXIName **sposta l'orario di un secondo alla volta**:

```
IMG_4001.jpg  (18.05.32)  →  2025-12-24 18.05.32.jpg
IMG_4002.jpg  (18.05.32)  →  2025-12-24 18.05.33.jpg   (+1 secondo)
IMG_4003.jpg  (18.05.32)  →  2025-12-24 18.05.34.jpg   (+2 secondi)
```

Le regole, cartella per cartella:

1. un file che ha **già** il nome giusto lo tiene;
2. un file rinominato in passato con un orario spostato lo tiene: **rileggere la stessa
   cartella non rimescola nulla**;
3. chi ha l'orario esatto libero lo prende (se una foto è stata scattata davvero alle
   18.05.33, tiene 18.05.33 e il doppione passa a 18.05.34);
4. gli altri prendono il primo secondo libero.

Sono considerati occupati anche i file presenti nella cartella che non vengono rinominati.
File con estensione diversa (es. `.jpg` e `.mov`) possono avere lo stesso orario.
I vecchi nomi del tipo `2025-12-24 18.05.32_1.jpg` vengono convertiti nel nuovo sistema.

Se scegli un formato **senza secondi** (es. `hh.mm` o senza orario) non è possibile spostare
di un secondo: in quel caso si usano `_1`, `_2`, …

Le righe con l'orario spostato sono **blu** nella tabella.

---

## Escludere dei file dalla rinomina

Non vuoi rinominare tutto quello che c'è nella cartella? Nella tabella:

| Comando | Azione |
|---|---|
| Click / Ctrl+click / Maiusc+click | seleziona una o più righe |
| **Canc** | toglie le righe selezionate dalla rinomina |
| **Ctrl+A** | seleziona tutte le righe |
| **Tasto destro** | menu con *Escludi dalla rinomina*, *Seleziona tutto*, *Apri il file* |
| **Ripristina esclusi (n)** (in basso) | rimette in elenco i file esclusi |

I file esclusi **non vengono toccati** e il loro nome resta occupato, quindi nessun altro
file può prenderlo. Una nuova lettura con **Avvia** riparte da zero (nessun file escluso).

Puoi anche ordinare la tabella cliccando sull'intestazione di una colonna (un secondo
click inverte l'ordine).

---

## Colori della tabella

| Colore | Significato |
|---|---|
| 🟢 Verde | il file ha già il nome giusto, non viene toccato |
| 🔵 Blu | orario spostato di qualche secondo (stesso orario di un altro file) |
| 🟠 Arancione | data corretta a mano |
| 🔴 Rosso | conflitto: il nome è già usato, il file viene saltato |

In basso trovi il riepilogo: quante immagini e video, quanti da rinominare e quanti in conflitto.

---

## Formati supportati

| Tipo | Estensioni |
|---|---|
| Immagini | `.jpg` `.jpeg` `.png` `.bmp` `.gif` `.heic` `.heif` `.webp` |
| RAW / TIFF | `.dng` `.nef` `.tif` `.tiff` |
| Video | `.mp4` `.mov` `.avi` `.mkv` `.m4v` `.3gp` `.wmv` `.flv` `.mts` `.m2ts` `.webm` |

Le cartelle e i file nascosti (che iniziano con `.`) vengono ignorati.

---

## Sicurezza dei file

- EXIName **cambia solo il nome** dei file: contenuto, metadati e date restano intatti.
- Non sposta né cancella nulla.
- La rinomina avviene in due passaggi (prima un nome temporaneo, poi quello finale), così
  due file possono scambiarsi il nome senza sovrascriversi.
- Se un file non può essere rinominato (ad esempio è aperto in un altro programma), riprende
  il suo nome originale e alla fine vedi l'elenco degli errori.
- Prima di rinominare compare sempre un riepilogo da confermare.

---

## Impostazioni salvate

Lingua, formato del nome e spunta delle sottocartelle sono salvati in:

```
%APPDATA%\EXIName\settings.json
```

Per tornare alle impostazioni iniziali basta cancellare quel file.

In alto a destra trovi:
- **Aggiornamenti**: apre questa pagina; diventa arancione quando esce una nuova versione;
- **Info**: versione, autore e crediti;
- **Aiuto**: una guida rapida;
- **IT / EN**: cambia lingua.

---

## Avvio dal sorgente e creazione dell'eseguibile

Serve solo se vuoi modificare il programma. Requisiti: Windows e Python 3.10 o successivo.

### Avvio dal sorgente
```bash
pip install -r requirements.txt
python EXIName.py
```
In alternativa fai doppio click su `avvia_controllo.bat`.

### Creazione della versione portable
Fai doppio click su `build_exe.bat`. Lo script:
1. controlla che Python sia installato;
2. installa o aggiorna le librerie e PyInstaller;
3. crea il programma in `dist\EXIName\` (`EXIName.exe` + `_internal`);
4. crea lo zip `release\EXIName_v<versione>_portable.zip` con `LEGGIMI.txt` e `LICENSE.txt`.

Il file `EXIName.ico` deve trovarsi nella stessa cartella di `build_exe.py`.
Se accanto c'è anche un `github.png`, viene usato come icona del link aggiornamenti.

### File del repository
| File | A cosa serve |
|---|---|
| `EXIName.py` | il programma (file unico, immagini incorporate) |
| `build_exe.bat` / `build_exe.py` | creazione della versione portable e dello zip |
| `avvia_controllo.bat` | avvio rapido dal sorgente |
| `requirements.txt` | librerie Python necessarie |
| `EXIName.ico` | icona del programma |
| `LICENSE` | licenza |

### Librerie usate
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) – interfaccia grafica
- [Pillow](https://python-pillow.org/) – lettura EXIF delle immagini
- [pillow-heif](https://github.com/bigcat88/pillow_heif) – supporto HEIC/HEIF
- [hachoir](https://github.com/vstinner/hachoir) – date dei video
- [tkinterdnd2](https://github.com/Eliav2/tkinterdnd2) – trascinamento di cartelle e file

`pillow-heif` e `tkinterdnd2` sono facoltative: senza la prima i `.heic` vengono rinominati
con la data di modifica, senza la seconda si aggiungono le cartelle solo con il pulsante.

---

## Novità

### 0.3.0
- Spunta **Includi sottocartelle** (ricordata) al posto della domanda a ogni Avvio
- Tasto **Canc** per escludere file dalla rinomina, Ctrl+A, menu del tasto destro, *Ripristina esclusi*
- Stesso orario: **+1 secondo** invece di `_1`, `_2`; i file già sistemati non vengono più toccati
- Grafica più compatta e netta, molto più spazio per l'elenco dei file
- Logo Daedalus Code nella finestra Info

### 0.2.1
- Formato del nome personalizzabile (ordine della data, orario, separatore)

### 0.2.0
- Pulsanti Avvia / Pausa / Stop con percentuale, tempo trascorso e rimanente
- Italiano / inglese, controllo aggiornamenti, Info e Aiuto
- Scheda Rinomina WhatsApp, drag & drop, supporto DNG / NEF / TIFF / HEIC / video

---

## Licenza

EXIName è **gratuito per uso personale e non commerciale**.
È vietata la vendita o qualsiasi uso a scopo di lucro.
Dettagli nel file [LICENSE](LICENSE) (PolyForm Noncommercial 1.0.0).

Sviluppato da **Sidor87** · Daedalus Code

---
---

<a name="english"></a>
# 🇬🇧 English

**EXIName** is a free Windows program that batch-renames photos and videos using the
**real capture date and time** read from the file's metadata. The default name is:

```
2025-12-24 18.05.32.jpg
```

Your files sort chronologically on their own, in any folder, even when they come from
different phones, cameras or apps.

Current version: **0.3.0** · Interface in Italian and English

## Download and run

1. Open the [**Releases**](https://github.com/Sidor87/EXIName/releases/latest) page and
   download `EXIName_v<version>_portable.zip`.
2. Extract it anywhere (a USB stick works too).
3. Open `EXIName.exe`. Nothing to install.

> ⚠️ Always keep `EXIName.exe` together with the `_internal` folder next to it.
> To move the program, move the whole `EXIName` folder.

> ℹ️ Windows SmartScreen may say «Unrecognized app» the first time, because the program is
> not digitally signed. Click **More info → Run anyway**.

## How to use it

1. **Add folders** with **＋ Add folder** or drag folders/files onto the window. Each one
   shows as a tag with a ✕ to remove it (hover to see the full path).
2. Keep **Include subfolders** ticked to scan subfolders too (the count is shown next to it).
   The choice is remembered.
3. Press **▶ Start**. You can **Pause** or **Stop** (Stop keeps the partial results).
   The status bar shows percentage, elapsed and remaining time.
4. **Check the table**: current name and proposed name for each file.
5. Remove with **Del** the files you don't want to rename.
6. Press **Rename** and confirm.

## Rename by date

| File type | Where the date comes from |
|---|---|
| Images (JPG, HEIC, PNG, …) | EXIF `DateTimeOriginal` / `DateTimeDigitized` |
| TIFF-based RAW (DNG, NEF, TIFF) | EXIF read directly, without decoding the RAW image |
| Videos (MP4, MOV, …) | container metadata (creation date) |

If the capture date is **missing** (or is a placeholder before 1970), the file's **last
modified date** is used. That's why the table has two columns: **EXIF rename** and
**Modified-date rename**.

- **Double-click a proposed date** to correct it by hand (`yyyy-mm-dd hh.mm.ss`); the row turns orange.
- **Double-click a file name** to open the file.

### Name format
Three menus above the table:

| Menu | Options |
|---|---|
| **Date** | `yyyy-mm-dd` (default), `dd-mm-yyyy`, `mm-dd-yyyy`, `yyyy_mm_dd`, `dd_mm_yyyy`, `yyyymmdd`, `dd.mm.yyyy` |
| **Time** | `hh.mm.ss` (default), `hh-mm-ss`, `hhmmss`, `hh.mm`, `hh-mm`, no time |
| **Separator** | space (default), `_`, `-` |

Every change must be confirmed and is remembered. **Default** restores `yyyy-mm-dd hh.mm.ss`.

## Rename WhatsApp

```
IMG-20260825-WA0002.jpg  →  2026-08-25-WA0002.jpg
```

Works for `IMG-`, `VID-`, `AUD-`, `PTT-`, `STK-`, `DOC-`. The date is taken from the name
itself, so it works even when WhatsApp stripped the metadata. Options: **Remove prefix**,
**Dashed date**, **Remove counter** (duplicates get `_1`, `_2`).
**Rename** applies to the tab that is currently open.

## Photos taken in the same second

Instead of `_1`, `_2`, EXIName **shifts the time by one second at a time**:

```
IMG_4001.jpg  (18.05.32)  →  2025-12-24 18.05.32.jpg
IMG_4002.jpg  (18.05.32)  →  2025-12-24 18.05.33.jpg   (+1 second)
IMG_4003.jpg  (18.05.32)  →  2025-12-24 18.05.34.jpg   (+2 seconds)
```

Rules, folder by folder:

1. files that already have the right name keep it;
2. files renamed earlier with a shifted time keep it, so **scanning the same folder
   again changes nothing**;
3. files whose exact time is free take it (a photo really taken at 18.05.33 keeps it
   and the duplicate moves to 18.05.34);
4. the others take the first free second.

Files in the folder that are not being renamed count as taken. Different extensions
(`.jpg` and `.mov`) may share the same time. Old names like `..._1.jpg` are converted.
With a format **without seconds** the program falls back to `_1`, `_2`, …
Shifted rows are shown in **blue**.

## Excluding files

| Command | Action |
|---|---|
| Click / Ctrl+click / Shift+click | select rows |
| **Del** | exclude the selected rows from renaming |
| **Ctrl+A** | select all |
| **Right-click** | *Exclude from renaming*, *Select all*, *Open the file* |
| **Restore excluded (n)** | put them back |

Excluded files are not touched and their names stay reserved. A new **Start** begins from
scratch. Click a column header to sort (click again to reverse).

## Table colors

| Color | Meaning |
|---|---|
| 🟢 Green | already has the right name |
| 🔵 Blue | time shifted by a few seconds |
| 🟠 Orange | date edited by hand |
| 🔴 Red | conflict, the file is skipped |

## Supported formats

| Type | Extensions |
|---|---|
| Images | `.jpg` `.jpeg` `.png` `.bmp` `.gif` `.heic` `.heif` `.webp` |
| RAW / TIFF | `.dng` `.nef` `.tif` `.tiff` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` `.m4v` `.3gp` `.wmv` `.flv` `.mts` `.m2ts` `.webm` |

Hidden folders and files (starting with `.`) are ignored.

## File safety

- Only file **names** change: content, metadata and dates are untouched. Nothing is moved or deleted.
- Renaming is done in two steps (temporary name, then final name), so files can swap names safely.
- If a file can't be renamed (e.g. it's open elsewhere) it gets its original name back and
  you see the list of errors at the end.
- A summary always asks for confirmation before renaming.

## Saved settings

Language, name format and the subfolders option are saved in
`%APPDATA%\EXIName\settings.json`. Delete it to reset.
Top right: **Updates** (turns orange when a new version is out), **About**, **Help**, **IT / EN**.

## Run from source / build

Requires Windows and Python 3.10 or newer.

```bash
pip install -r requirements.txt
python EXIName.py
```

Or double-click `avvia_controllo.bat`. To build the portable version run `build_exe.bat`:
it installs the libraries and PyInstaller, creates `dist\EXIName\` and the zip
`release\EXIName_v<version>_portable.zip` (with `LEGGIMI.txt` and `LICENSE.txt`).
`EXIName.ico` must be next to `build_exe.py`.

Libraries: [customtkinter](https://github.com/TomSchimansky/CustomTkinter),
[Pillow](https://python-pillow.org/), [pillow-heif](https://github.com/bigcat88/pillow_heif)
(optional), [hachoir](https://github.com/vstinner/hachoir),
[tkinterdnd2](https://github.com/Eliav2/tkinterdnd2) (optional).

## License

EXIName is **free for personal and non-commercial use**. Selling it or any for-profit use
is not allowed. See [LICENSE](LICENSE) (PolyForm Noncommercial 1.0.0).

Developed by **Sidor87** · Daedalus Code
