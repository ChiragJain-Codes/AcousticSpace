from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parents[3]

# Dataset Folders
REAL_DIR = BASE_DIR / "dataset" / "real"
FAKE_DIR = BASE_DIR / "dataset" / "fake"


def load_dataset():
    real_files = []
    fake_files = []

    # Real Audio Files
    for file in REAL_DIR.iterdir():
        if file.suffix.lower() in [".wav", ".mp3", ".flac"]:
            real_files.append(str(file))

    # Fake Audio Files
    for file in FAKE_DIR.iterdir():
        if file.suffix.lower() in [".wav", ".mp3", ".flac"]:
            fake_files.append(str(file))

    return real_files, fake_files