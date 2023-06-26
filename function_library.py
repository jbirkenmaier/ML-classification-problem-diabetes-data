import numpy as np

#function for reading the data 
def read_data(name_of_file):
    data=[]
    class_data=[]
    with open('%s'%name_of_file) as datafile:
        attributes = datafile.readline().replace('\n', '').split(',')[:-1]
        for line in datafile:
            data.append(line.replace('\n', '').split(','))
            class_data.append(data[-1][-1])
    class_data = [int(element.replace('Positive', '1').replace('Negative', '0')) for element in class_data]
    data_without_class = [element[:-1] for element in data]
    return data, data_without_class, attributes, class_data
    
'''    
now I want to slice the data into a "Training-set" and a "Testing-set"
The "Training-set" will be used for training the algorithm. The "Testing-set" will be used for testing and evaluating.
I will assign 75% of the dataset for training purposes and 25% for testing.
'''

#function for splitting the data into "training-" and "testing-" data
def split_training_testing(data):
    num_of_examples = len(data)
    num_of_training_examples = 3 * num_of_examples//4
    num_of_test_examples = num_of_examples - num_of_training_examples
    
    training_data = data[:num_of_training_examples]
    test_data = data[num_of_training_examples:]
    
    return training_data, test_data

'''
As the provided data is mostly binary, with exception of the patient age, feature scaling might not be necessary.
I will see if that is true later in the progress of the project. For now I will leave out feature scaling.
'''

def model_function(x,w,b):
    return np.dot(x,w)+b

def sig(value):
    return 1/(1+np.exp(-value))

def loss(w,b,x,y):
    z = model_function(x,w,b)
    d = sig(z)
    if y == 1:
        return -np.log(d)
    if y == 0:
        return -np.log(1-f)

def cost(x,w,b,y):
    m=len(x)
    J=0
    for i in range(m):
        J+=loss(w,b,x[i],y[i])
    return J/m

def derivative_of_cost(w,b,x,y,lamb):
    m = len(x)
    n = len(w)

    dJ_dw = np.zeros(n)
    dJ_db = 0
    l=0
    x=np.array(x)
    x_list = x
    loss_list = np.array([loss(w,b,x,y) for (x,y) in zip(x,y)])
    dJ_dw = np.dot(loss_list, x_list) + lamb /m*w
    dJ_db = np.sum(loss_list)

    return dJ_dw/m, dJ/db/m

#function for gradient descent
def gradient_descent():
    
    pass

#function for model
def model():
    pass
