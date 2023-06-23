import function_library as fl
import numpy as np

(data, attributes, class_data) = fl.read_data('diabetes_data_upload.csv')

print(class_data)

num_of_attributes = len(attributes)
(training_data, test_data)= (fl.split_training_testing(data))

w = np.zeros(num_of_attributes)
