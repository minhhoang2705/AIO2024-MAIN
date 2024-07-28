import numpy as np

def compute_prior_probablity(train_data):
  y_unique = ['no', 'yes']
  prior_probability = np.zeros(len(y_unique))
  for i in range(0,len(y_unique)):
    prior_probability[i]=len(np.where(train_data[:,4] == y_unique[i])[0])/len(train_data)
  return prior_probability

prior_probablity = compute_prior_probablity(train_data)
print("P(“Play Tennis” = No)", prior_probablity[0])
print("P(“Play Tennis” = Yes)", prior_probablity[1])
