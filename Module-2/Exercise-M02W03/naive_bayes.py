from create_train_data import create_train_data
from compute_prior_probablity import compute_prior_probablity
import numpy as np

def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name  = compute_conditional_probability(train_data)

    return prior_probability,conditional_probability, list_x_name

data = create_train_data()
prior_probability,conditional_probability, list_x_name = train_naive_bayes(data)
