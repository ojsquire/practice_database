import numpy as np
from faker import Faker

N_WORDS = 10

# Create some random words
Faker.seed(0)
fake = Faker()
tracks = [fake.word() for _ in range(N_WORDS)]

# Sample probabilities from an exponential distribution
exponential_probs = np.random.exponential(scale=1.0, size=N_WORDS)
total_exponential_probs = sum(exponential_probs)
exponential_probs_norm = exponential_probs / total_exponential_probs

# Choose words `size` times according to the exponential distribution
names = np.random.choice(a=tracks, size=(100), p=list(exponential_probs_norm))

# Print selection
print(sorted(names))