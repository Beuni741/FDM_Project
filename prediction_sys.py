import numpy as np
import pickle

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (1,0,53,1,1,1976,2,4,2,3,2,2,2,2,3,4,4,5,5,2)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('Customer is Satisfied')
else:
  print('Customer is Dissatisfied')
  