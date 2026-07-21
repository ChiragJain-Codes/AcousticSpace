from pathlib import Path
import shutil

# -----------------------------
# Project Root
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# -----------------------------
# Source Dataset
# -----------------------------
TRAIN_AUDIO_DIR = Path(r"D:\Games\LA\LA\ASVspoof2019_LA_train\flac")

PROTOCOL_FILE = Path(
    r"D:\Games\LA\LA\ASVspoof2019_LA_cm_protocols\ASVspoof2019.LA.cm.train.trn.txt"
)

# -----------------------------
# Destination
# -----------------------------
REAL_DIR = PROJECT_ROOT / "dataset" / "real"
FAKE_DIR = PROJECT_ROOT / "dataset" / "fake"

REAL_DIR.mkdir(parents=True, exist_ok=True)
FAKE_DIR.mkdir(parents=True, exist_ok=True)

real_count = 0
fake_count = 0

with open(PROTOCOL_FILE, "r") as file:
    for line in file:

        parts = line.strip().split()

        audio_name = parts[1] + ".flac"
        label = parts[-1]

        source = TRAIN_AUDIO_DIR / audio_name

        if not source.exists():
            continue

        if label == "bonafide":
            shutil.copy(source, REAL_DIR / audio_name)
            real_count += 1
        else:
            shutil.copy(source, FAKE_DIR / audio_name)
            fake_count += 1

print("=" * 40)
print(f"Real Files : {real_count}")
print(f"Fake Files : {fake_count}")
print("=" * 40)
print("Dataset Organized Successfully ✅")