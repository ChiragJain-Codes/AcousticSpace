from services.feature_extractor import generate_waveform, generate_spectrogram

audio_path = "uploads/file_example_MP3_1MG.mp3"

generate_waveform(audio_path)

generate_spectrogram(audio_path)