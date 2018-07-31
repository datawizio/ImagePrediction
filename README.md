# From picture to prediction.

This folder contains an example of transfer-learning the Inception v3 model for classification images utilizing TensorFlow and deploying it on Android.

[How it looks](https://youtu.be/Cp-GVpLy7OM)

# Files:
- android - Android app.  
- Inception-v3-model - here we train Inception v3 model.

# Usege
Firstly, you need data for training your model. In our case we use [telegram bot](https://github.com/winioleh/video_collector) for collecting videos and associate it to some food product.
If you have enough data you can start trainig your model, for more information look at [Inception-v3-model](https://github.com/winioleh/From-Image-To-Prediction/tree/master/Inception-v3-model) 
When your model is trained you can start deploying it on your Android device, for more information look at [android](https://github.com/winioleh/From-Image-To-Prediction/tree/master/android)
