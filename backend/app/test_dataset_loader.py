from services.dataset_loader import load_dataset

real_files, fake_files = load_dataset()

print("Real Files:")
print(real_files)

print("\nFake Files:")
print(fake_files)