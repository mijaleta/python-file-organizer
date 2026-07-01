# Python File Organizer

Automatically sorts files in a folder into subfolders based on file type.

## What It Does

Scans a folder and moves files into:

| Folder | Extensions |
|--------|------------|
| Images | .jpg, .jpeg, .png, .gif |
| Documents | .pdf, .docx, .txt |
| Videos | .mp4, .mkv, .mov |
| Music | .mp3, .wav |
| Archives | .zip, .rar |
| Others | anything else |

## Setup

1. Clone the repo
```bash
git clone https://github.com/mijaleta/python-file-organizer.git
cd python-file-organizer
```

2. Install dependencies
```bash
pip install python-dotenv
```

3. Create a `.env` file and set your folder path
```
FOLDER_PATH=import this one from the env file
```

## Usage

```bash
python file_organizer.py
```

## Project Structure

```
python-file-organizer/
├── file_organizer.py
├── .env              # your folder path (not committed)
├── .gitignore
└── README.md
```

## Notes

- Supports filenames in any language (UTF-8 encoded)
- Subfolders inside the target folder are skipped
- `.env` is excluded from git via `.gitignore`
