# Subtitle Translator (.vtt and .srt) to Another Language

![Subtitles Translator to Another Language](https://mikethewolf83.github.io/assets/img/subtr.jpg)

This script translates `.vtt` or `.srt` subtitle files from a source language to a target language, preserving all timestamp formatting. It uses the `deep-translator` library to translate line by line.

---

## 🧰 Requirements

- Python 3.7 or higher
- Internet connection (required to access Google Translate)
- A `.vtt` or `.srt` subtitle file you want to translate

---

## 🧪 Create a Virtual Environment (Optional but Recommended)

### On **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

### On **Linux/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install deep-translator
```

---

## ▶️ How to Use the Script

Run the script from the terminal with the following arguments:

```bash
python subtr.py --format vtt --in original_file.vtt --out translated_file.vtt --lang-in en --lang-out es
```

### Available Parameters:

- `--format`: File format (`vtt` or `srt`)
- `--in`: Input subtitle file path
- `--out`: Output (translated) file path
- `--lang-in`: Source language (default: `en`)
- `--lang-out`: Target language (default: `es`)

### Examples:

**Translate a `.vtt` file from English to Spanish:**
```bash
python subtr.py --format vtt --in input.vtt --out output.vtt
```

**Translate a `.srt` file from English to French:**
```bash
python subtr.py --format srt --in input.srt --out output.srt --lang-out fr
```

---

## 📝 Notes

- The script only translates text lines. It does not modify timestamps or sequence numbers.
- It's recommended to back up your original file before overwriting.
