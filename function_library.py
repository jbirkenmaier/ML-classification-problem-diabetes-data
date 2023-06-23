
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
    
    return data, attributes, class_data
    
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

#function for gradient descent
def gradient_descent():
    
    pass

#function for model
def model():
    pass
