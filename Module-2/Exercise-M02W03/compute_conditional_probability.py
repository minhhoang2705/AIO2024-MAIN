import numpy as np

def compute_conditional_probability(train_data):
  y_unique = ['no', 'yes']
  conditional_probability = []
  list_x_name = []
  for i in range(0,train_data.shape[1]-1):
    x_unique = np.unique(train_data[:,i])
    print("x_unique", x_unique)

    list_x_name.append(x_unique)

    x_conditional_probability = np.zeros((len(y_unique),len(x_unique)))
    for j in range(0,len(y_unique)):
      for k in range(0,len(x_unique)):
        x_conditional_probability[j,k]= len(np.where((train_data[:,i] == x_unique[k]) & (train_data[:,4] == y_unique[j]))[0])/len(np.where(train_data[:,4] == y_unique[j])[0])

    conditional_probability.append(x_conditional_probability)
  return conditional_probability, list_x_name
