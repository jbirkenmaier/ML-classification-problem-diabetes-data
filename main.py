import function_library as fl


data = fl.read_data('diabetes_data_upload.csv')[0]
(training_data, test_data)= (fl.split_training_testing(data))

print(len(training_data))
print(len(test_data))
print(len(data))
