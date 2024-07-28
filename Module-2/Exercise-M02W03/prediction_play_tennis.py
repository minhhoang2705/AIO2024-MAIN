from create_train_data import create_train_data
from naive_bayes import train_naive_bayes

def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):

    x1=get_index_from_value(X[0],list_x_name[0])
    x2=get_index_from_value(X[1],list_x_name[1])
    x3=get_index_from_value(X[2],list_x_name[2])
    x4=get_index_from_value(X[3],list_x_name[3])

    p0=prior_probability[0] \
    *conditional_probability[0][0,x1] \
    *conditional_probability[1][0,x2] \
    *conditional_probability[2][0,x3] \
    *conditional_probability[3][0,x4]

    p1=prior_probability[1]\
    *conditional_probability[0][1,x1]\
    *conditional_probability[1][1,x2]\
    *conditional_probability[2][1,x3]\
    *conditional_probability[3][1,x4]

    if p0>p1:
        y_pred=0
    else:
        y_pred=1

    return y_pred

if __name__ == "__main__":
  X = ['Sunny','Cool', 'High', 'Strong']
  data = create_train_data()
  prior_probability,conditional_probability, list_x_name = train_naive_bayes(data)
  pred =  prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)
  
  if(pred):
    print("Ad should go!")
  else:
    print("Ad should not go!")
