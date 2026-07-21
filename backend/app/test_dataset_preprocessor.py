from services.dataset_preprocessor import prepare_dataset

X, Y = prepare_dataset()

print("Total Samples:", len(X))
print("Labels:", Y)