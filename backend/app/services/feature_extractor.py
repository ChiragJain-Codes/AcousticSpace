import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def load_audio(file_path):
    """
    Load an audio file and return waveform and sample rate.
    """
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate


def generate_waveform(file_path):
    """
    Display waveform of an audio file.
    """
    audio, sample_rate = load_audio(file_path)

    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(audio, sr=sample_rate)

    plt.title("Audio Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()


def generate_spectrogram(file_path):
    """
    Display Mel Spectrogram of an audio file.
    """
    audio, sample_rate = load_audio(file_path)

    spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate
    )

    spectrogram_db = librosa.power_to_db(
        spectrogram,
        ref=np.max
    )

    plt.figure(figsize=(10, 4))

    librosa.display.specshow(
        spectrogram_db,
        sr=sample_rate,
        x_axis="time",
        y_axis="mel"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("Mel Spectrogram")

    plt.tight_layout()
    plt.show()