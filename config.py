# Copyright © 2019 by Spectrico
# Licensed under the MIT License

#model_file = "model-weights-spectrico-mmr-mobilenet-224x224-908A6A8C.pb"   # path to the car make and model classifier
#model_file = "model-weights-spectrico-mmr-mobilenet-128x128-344FF72B.pb"  # path to the car make and model classifier
#model_file = "model-weights-spectrico-mmr-mobilenet-96x96-8BEE8BCC.pb"  # path to the car make and model classifier
model_file = "model-weights-spectrico-mmr-mobilenet-64x64-531A7126.pb"  # path to the car make and model classifier
label_file = "labels.txt"   # path to the text file, containing list with the supported makes and models
input_layer = "input_1"
output_layer = "softmax/Softmax"
#classifier_input_size = (224, 224) # input size of the classifier
#classifier_input_size = (128, 128)  # input size of the classifier
#classifier_input_size = (96, 96)  # input size of the classifier
classifier_input_size = (64, 64)  # input size of the classifier
