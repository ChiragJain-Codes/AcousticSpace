from services.dataset_loader import load_dataset
from services.feature_extractor import extract_mfcc


def prepare_dataset():

    X = []
    Y = []

    real_files, fake_files = load_dataset()

    # Process Real Audio
    for file in real_files:
        mfcc = extract_mfcc(file)

        X.append(mfcc)
        Y.append(0)

    # Process Fake Audio
    for file in fake_files:
        mfcc = extract_mfcc(file)

        X.append(mfcc)
        Y.append(1)

    return X, Y