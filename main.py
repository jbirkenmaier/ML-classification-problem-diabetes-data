import function_library as fl
import numpy as np

(data, data_without_class, attributes, class_data) = fl.read_data('diabetes_data_upload.csv')

num_of_attributes = len(attributes)
(x_train, y_train, x_test, y_test)= (fl.split_training_testing(data))

w = np.zeros(num_of_attributes)
b = 1

results = fl.gradient_descent(w, b, x_train, y_train, lamb=10e4, alpha=pow(10,-5), steps=10000)
