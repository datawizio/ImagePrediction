# Inception v3 transfer-learning

This folder contains an example of transfer-learning the Inception v3 model for classification images utilizing TensorFlow.

[what is transfer-learning](https://becominghuman.ai/transfer-learning-retraining-inception-v3-for-custom-image-classification-2820f653c557)

# Dependencies:
- Python 3.6
- Tensorflow 1.7 (TOCO will not work with 1.8 so be sure that you install Tensorflow 1.70

## What you need to start training your model?
Firstly, you should specify where is your dataset, to do this you just need edit retrain.py on 1152 row.
```python
parser.add_argument(
      '--image_dir',
      type=str,
      default='<PATH-TO-YOUR-DATASET>',
      help='Path to folders of labeled images.'
  )
```
Also you can tune some parameters such as number of training steps, learning rate. Aditionaly you can specify what part of your dataset you want use for validation and testing.For more information look at retrain.py.
```python
parser.add_argument(
      '--how_many_training_steps',
      type=int,
      default=30000,
      help='How many training steps to run before ending.'
  )
  parser.add_argument(
      '--learning_rate',
      type=float,
      default=0.0001,
      help='How large a learning rate to use when training.'
  )
  parser.add_argument(
      '--testing_percentage',
      type=int,
      default=2,
      help='What percentage of images to use as a test set.'
  )
  parser.add_argument(
      '--validation_percentage',
      type=int,
      default=2,
      help='What percentage of images to use as a validation set.'
  )
```
### After you have specified all the necessary parameters, you can start training your model by running it retrain.py from the command prompt:
```bash
:~$ python retrain.py
```
### When your model is being trained you will have two files in tmp/, it is output_labels.txt(contains class names) and output_graph.pb(it is your model). Now you are ready to use it.
## Making predictions with make_predections.py.
### Specify path to data, which you want to classify.
```python
data_root = 'dataset/'
src= data_root + 'test/new_imgs/'

```
### Specify path to your model(*.pb file) and path to file which contains the class names(output_labels.txt).
```python
labels = 'tmp/output_labels.txt'
graph = 'tmp/output_graph.pb'

```

### Specify names of input and output layers.(If you didnt edit stracture of network you dont need this step)
```python
input_layer = 'Mul:0'
output_layer ='final_result:0'

```

### If you done these step you can make predictions by running make_predictions.py from the command prompt:
```bash
:~$ python make_predections.py
```