import pickle

with open("crawling_data.pickle", "wb") as f:
    pickle.dump(cst_dict, f)