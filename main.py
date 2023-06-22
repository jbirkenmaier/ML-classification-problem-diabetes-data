import function_library as fl


data = fl.read_data('diabetes_data_upload.csv')[0]

fl.split_training_testing(data)
