import pickle

Data_1 = "train_samples/pkl/pkl_data_1.pkl"

f=open(Data_1, "rb")
file = pickle.load(f)
print(file['time_series'][0]['process_state'])