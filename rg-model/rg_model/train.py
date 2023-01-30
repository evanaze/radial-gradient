"""Training script."""
from torch.utils.data import DataLoader
from rg_model.dataset import LikesDataset


dataset = LikesDataset("../rg-data/like_data.csv")
train_dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
