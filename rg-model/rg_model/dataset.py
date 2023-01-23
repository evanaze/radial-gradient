"""A module for loading the dataset."""
import pandas as pd
from torch.utils.data.dataset import Dataset


class LikesDataset(Dataset):
    def __init__(self, filepath: str):
        self.df = pd.read_csv(filepath)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx: int):
        return self.df.iloc[idx]
