
#function for reading the data 
def read_data(name_of_file):
    data=[]
    with open('%s'%name_of_file) as datafile:
        attributes = datafile.readline().split() 
        for line in datafile:
            data.append(line.replace('\n', '').split(','))
        return data, attributes
    
'''    
now I want to slice the data into a "Training-set" and a "Testing-set"
The "Training-set" will be used for training the algorithm. The "Testing-set" will be used for testing and evaluating.
I will assign 75% of the dataset for training purposes and 25% for testing.
'''

def split_training_testing(data):
    num_of_examples = len(data)
    num_of_training_examples = 3 * num_of_examples//4
    num_of_test_examples = num_of_examples - num_of_training_examples
    
    training_data = data[:num_of_training_examples]
    test_data = data[num_of_training_examples:]

    return training_data, test_data

    
