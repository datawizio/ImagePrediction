# From picture to prediction.

This folder contains an example of transfer-learning the Inception v3 model for classification images utilizing TensorFlow and deploying it on Adroid.

[how it looks](https://becominghuman.ai/transfer-learning-retraining-inception-v3-for-custom-image-classification-2820f653c557)

#Files
-android - Android app
-Inception-v3-model - here we train Inception v3 model and can make predictions

#Usege
Firstly, you need get data for training your model. In our case we use telegram bot for collecting videos and associate it to some food product.
If you have enough data you can start trainin you model, for more information look at [Inception-v3-model](https://github.com/winioleh/From-Image-To-Prediction/tree/master/Inception-v3-model) 
When your model is trained you can start deploying it on your Android device, for more information look at [android](https://github.com/winioleh/From-Image-To-Prediction/tree/master/android)
