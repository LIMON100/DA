
## Onnx

The Open Neural Network Exchange (ONNX) is an open-source ecosystem that aims to standardize and optimize artificial intelligence models across a variety of platforms.

ONNX Runtime is a cross-platform inference and training machine-learning accelerator. 


### Training model
If you only save the model weights, you will not be able to convert it to ONNX, because the model architecture is required and really important to convert your model to ONNX. With the model architecture, ONNX is able to trace the different layers of your model and convert it to a graph (also called an intermediate representation). Model weights are the weights of the different layers which are used to compute the output of the model. So, they are equally important to successfully convert your model.


### Input names and output names
You will need to define the input names and the output names of your model. These metadata are used to describe the inputs and outputs of your model.


### Input sample
ONNX will trace the different layers of the model in order to create a graph of theses layers.

While tracing the layers, ONNX will also need an input sample to understand how the model is working and what operators are used to compute the outputs.

The selected sample will be the input of the first layer of the model and is also used to define the input shape of the model.
