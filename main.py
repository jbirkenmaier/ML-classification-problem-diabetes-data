import function_library as fl
import numpy as np

(data, data_without_class, attributes, class_data) = fl.read_data('diabetes_data_upload.csv')

num_of_attributes = len(attributes)
(x_train, y_train, x_test, y_test)= (fl.split_training_testing(data))

w = np.zeros(num_of_attributes)
b = 1

results = fl.gradient_descent(w, b, x_train, y_train, lamb=10e4, alpha=pow(10,-5), steps=10000)

#print(results[0])
#print(x_test)

'''
Now that we obtained the values for our model (results[0] is w and results[1] is b) we need to
hold the model to test.
Therefore we need to use the test datasets we created in the beginning.
'''

prediction = [fl.sig(fl.model_function(element, results[0], results[1])) for element in x_test]

y_hat = []

for i in range(len(prediction)):
    if prediction[i] >= 0.72611:
        y_hat.append(1)
    else:
        y_hat.append(0)
        
true,false = [0,0]

print(y_hat)

for i in range(len(y_test)):
    if y_hat[i] == y_test[i]:
        true +=1
    else:
        false +=1
        
print(true/len(y_test))

'''
I reach an accuracy of abobut 55% with this algorithm, which is not great but it is a first start.
I still have to solve some issues. The most pressing to me is why my boundary is at around 0.72 and not
around 0.5 as I expected.
Also, is there a better way to find the exact boundary, without hard-coding it in like I did?
'''
