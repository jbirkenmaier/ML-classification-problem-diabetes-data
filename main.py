import function_library as fl
import numpy as np

data = fl.read_data('diabetes_data_upload.csv')[0]
attributes = fl.read_data('diabetes_data_upload.csv')[1]

print(attributes)

num_of_attributes = len(attributes)
(training_data, test_data)= (fl.split_training_testing(data))

w = np.zeros(num_of_attributes)

print(len(training_data))
print(len(test_data))
print(len(data))
