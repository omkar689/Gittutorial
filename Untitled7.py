#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from imageai.Classification import ImageClassification
import os
execution_path = os.getcwd()
prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath( execution_path + "\resnet50_imagenet_tf.2.0.h5")
prediction.loadModel()


predictions, percentage_probabilities = prediction.classifyImage(r'C:\Users\TEJAS .S\OneDrive\Pictures\Saved Pictures\male.jpg', result_count=5)
for index in range(len(predictions)):
  print(predictions[index] , " : " , percentage_probabilities[index])

