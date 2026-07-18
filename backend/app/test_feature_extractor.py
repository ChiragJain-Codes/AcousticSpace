from services.feature_extractor import extract_mfcc

audio_path = "uploads/file_example_MP3_1MG.mp3"

mfcc = extract_mfcc(audio_path)

print("MFCC Shape:", mfcc.shape)
print(mfcc)