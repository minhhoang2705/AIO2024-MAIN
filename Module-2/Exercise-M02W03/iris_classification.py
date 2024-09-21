from sklearn import datasets
import numpy as np
import math 


def create_train_data_iris():
  data = np.loadtxt("iris.data.txt", delimiter=",", dtype=str)
  return data

def compute_prior_probablity_iris(train_data):
  y_unique = np.unique(train_data[:,4])
  prior_probability = np.zeros(len(y_unique))
  for i in range(0,len(y_unique)):
    prior_probability[i]=len(np.where(train_data[:,4] == y_unique[i])[0])/len(train_data)
  return prior_probability

def compute_conditional_probability_iris(train_data):
  y_unique = np.unique(train_data[:,4]) # 0 for Setosa, 1 for Versicolour, 2 for Virginica
  x_feature = 4
  conditional_probability = []
  list_x_name = []
  for i in range(0,train_data.shape[1]-1):
    x_conditional_probability = np.zeros((len(y_unique), 2))
    for j in range(0,len(y_unique)):
        mean = np.mean((train_data[:,i][np.where(train_data[:,4] == y_unique[j])]).astype(float))
        sigma =  np.std((train_data[:,i][np.where(train_data[:,4] == y_unique[j])]).astype(float))
        sigma = sigma * sigma
        x_conditional_probability[j]= [mean, sigma]

    conditional_probability.append(x_conditional_probability)
  return conditional_probability

def gauss(x, mean, sigma):
  result = (1.0 / (np.sqrt(2*math.pi*sigma))) \
  * (np.exp(-(float(x) - mean) ** 2 / (2 * sigma)))
  return result

def train_gaussian_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity_iris(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability  = compute_conditional_probability_iris(train_data)

    return prior_probability,conditional_probability

def prediction_iris(X,  prior_probability, conditional_probability):

    p0=prior_probability[0] \
    *gauss(X[0], conditional_probability[0][0][0],conditional_probability[0][0][1])  \
    *gauss(X[1], conditional_probability[1][0][0],conditional_probability[1][0][1])  \
    *gauss(X[2], conditional_probability[2][0][0],conditional_probability[2][0][1])  \
    *gauss(X[3], conditional_probability[3][0][0],conditional_probability[3][0][1])

    p1=prior_probability[1] \
    *gauss(X[0], conditional_probability[0][1][0],conditional_probability[0][1][1])  \
    *gauss(X[1], conditional_probability[1][1][0],conditional_probability[1][1][1])  \
    *gauss(X[2], conditional_probability[2][1][0],conditional_probability[2][1][1])  \
    *gauss(X[3], conditional_probability[3][1][0],conditional_probability[3][1][1])

    p2=prior_probability[2] \
    *gauss(X[0], conditional_probability[0][2][0],conditional_probability[0][2][1])  \
    *gauss(X[1], conditional_probability[1][2][0],conditional_probability[1][2][1])  \
    *gauss(X[2], conditional_probability[2][2][0],conditional_probability[2][2][1])  \
    *gauss(X[3], conditional_probability[3][2][0],conditional_probability[3][2][1])

    # print(p0, p1)

    list_p = [p0, p1, p2]

    return list_p.index(np.max(list_p))

if __name__ == "__main__":
  X = [5.0,2.0,3.5,1.0]
  train_data = create_train_data_iris()
  y_unique = np.unique(train_data[:,4])
  prior_probability, conditional_probability = train_gaussian_naive_bayes(train_data)
  pred = y_unique[prediction_iris(X, prior_probability, conditional_probability)]
  assert pred == "Iris-versicolor"
  
