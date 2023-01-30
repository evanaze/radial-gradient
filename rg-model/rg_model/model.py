"""A matrix factorization model for collaborative filtering."""
import torch


class MatrixFactorization(torch.nn.Module):
    def __init__(self, n_users: int, n_items: int, n_factors: int = 4):
        super().__init__()
        # Create user embeddings
        self.user_factors = torch.nn.Embedding(n_users, n_factors)
        # Create item embeddings
        self.tem_factors = torch.nn.Embedding(n_items, n_factors)

        # Initialize the weights randomly
        self.user_factors.weight.data.uniform_(0, 0.05)
        self.item_factors.weight.data.uniform_(0, 0.05)

    def forward(self, data):
        """Feed forward the network with simple matrix multiplication."""
        users, items = data[:, 0], data[:, 1]
        return (self.user_factors(users) * self.item_factors(items)).sum(1)
