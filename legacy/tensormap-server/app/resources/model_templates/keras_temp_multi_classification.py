import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


optimizertype = 'adam'
lossFunction = 'Cross-entropy loss'


np.random.seed(0)




optimizerType = 'adam'
lossFunction = 'Cross-entropy loss'

dataCsv = pd.read_csv()
_x = dataCsv[0]
_y = dataCsv[1]

x_train, y_train, x_test, y_test = train_test_split(_x, _y, random_state=42, shuffle=True, test_size=0.10)

network = tf.keras.models.Sequential(name='userModel')

network.compile(optimizer=optimizertype, loss=lossFunction)


mod_history = network.fit(x_train, y_train, epochs=100, verbose=1, batch_size=16)

(test_loss,) = network.evaluate(x_test, y_test)

predictions = network.predict(x_test, verbose=1)

argmax_pred_array = []
argmax_true_array = []

for i in range(len(prediction)):
    argmax_pred_array.append(np.argmax(prediction[i], 0))
    argmax_true_array.append(np.argmax(test_y[i], 0))

argmax_true_array = (np.array(argmax_true_array, dtype=np.int32)).tolist()
argmax_pred_array = (np.array(argmax_pred_array, dtype=np.int32)).tolist()

accuracy = accuracy_score(argmax_true_array, argmax_pred_array)
f1 = f1_score(argmax_true_array, argmax_pred_array, average='macro')
recall = recall_score(y_true=argmax_true_array, y_pred=argmax_pred_array, average='macro')
precision = precision_score(argmax_true_array, argmax_pred_array, average='macro')

print('Accuracy: ', accuracy)
print('F1: ', f1)
print('Recall: ', recall)
print('Precision: ', precision)

with open('results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(y_test, predictions))
