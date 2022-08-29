
Learning type 
Talking about the learning type, we mainly find the implementation of stochastic and batch learning scenarios. Both of them help train our neural networks. Let’s discuss a general introduction of both of these learning methods.

Stochastic gradient descent:  this type of learning sometimes can also be referred to as online gradient descent or online learning and we normally estimate the error gradient in it where a single sample from the training data is selected and after calculation of the error we update the weights of the model we also call weights as a parameter. More details about this training can be found here.

Batch learning: We also call this learning batch learning. In this type of learning, we train the models in a batch manner and push the model into production at regular intervals based on the performance of the model with batch data or new data. More details about this type of training can be found here. 

Both of these learning methods have different convergence rates. We can differentiate between these learning using the following points:

Stochastic gradient descent is considered to be faster than batch learning.
The accuracy of a model trained with SGD learning is better than batch learning.
SGD is more convenient in tracking the changes in weights and signals.
Batch learning has better conditions of convergence.
Most of the acceleration mechanism works with batch learning.
Convergence rates are simpler in batch learning.
It is suggested to prefer SGD learning over batch learning because it makes our neural network converge faster with the large datasets.

Input normalization 
This method is also one of the most helpful methods to make neural networks converge faster. In many of the learning processes, we experience faster training when the training data sum to zero. We can normalize the input data by subtracting the mean value from each input variable. We can also call this process centring.  Normalization also affects the speed of convergence for example convergence of a neural network can be faster if the average input variable values are near zero. 

In the processes of modelling, we can also observe the effect of centring when the input data is transferred to the hidden layer from the prior layers. One more thing which is noticeable here is that normalization mostly works properly with batch training. So if batch training is applied in the neural networks we can make it converge faster using the input normalization and the whole process can be called batch normalization. 

In input normalization, we also find the usage of principal component analysis for decorrelating the data. Decorrelating is the process of removing linear dependencies between the variables and here it should only work with input variables to remove the linear dependencies between input variables. 


Activation function 
Information about different activation functions can be found here. In this section, we are going to compare these activation functions in terms of making neural network convergence faster. 

One of the very basic things about the sigmoid function is that it makes the neural network capable of dealing better with nonlinear input and it is the most common form of the activation function. In the list of sigmoid functions, we see that hyperbolic tangent sigmoid makes neural networks converge faster than the standard logistic sigmoid function. If not using these standard functions we can use ReLU activation to converge faster.


Learning rate 
Learning rate is also one of the major factors that work for the speed of convergence of the neural network. We can also consider the learning rate as the update in the weights of parameters of neural networks. Convergence and accuracy of the model can be considered inversely proportional. It means if the learning rate is higher there can be a faster convergence but less optimal accuracy while with a small learning rate we can expect that the accuracy will be higher but the convergence will be slower. 

By looking at the above situation we can say that we need to fix the learning rate in a dynamic nature so that when the parameter vector oscillates, the learning rate should be slower and when it is steady then the learning rate should be higher.

One more method to adjust the optimal learning rate is to use an adaptive learning rate. This kind of learning rate can also be considered as applying different learning rates at each parameter of the neural network. The adaptive learning rate has proven the faster convergence of neural networks by making the convergence of weights at the same speed.

Choosing Target Values
This tip highlights a more careful consideration of the choice of target variables.

In the case of binary classification problems, target variables may be in the set {0, 1} for the limits of the logistic activation function or in the set {-1, 1} for the hyperbolic tangent function when using the cross-entropy or hinge loss functions respectively, even in modern neural networks.

The authors suggest that using values at the extremes of the activation function may make learning the problem more challenging.

Common wisdom might seem to suggest that the target values be set at the value of the sigmoid’s asymptotes. However, this has several drawbacks.

They suggest that achieving values at the point of saturation of the activation function (edges) may require larger and larger weights, which could make the model unstable.

One approach to addressing this is to use target values away from the edge of the output function.

Choose target values at the point of the maximum second derivative on the sigmoid so as to avoid saturating the output units.

I recall that in the 1990s, it was common advice to use target values in the set of {0.1 and 0.9} with the logistic function instead of {0 and 1}.


Tip #6: Initializing the Weights
This tip highlights the importance of the choice of weight initialization scheme and how it is tightly related to the choice of activation function.

In the context of the sigmoid activation function, they suggest that the initial weights for the network should be chosen to activate the function in the linear region (e.g. the line part not the curve part of the S-shape).

The starting values of the weights can have a significant effect on the training process. Weights should be chosen randomly but in such a way that the sigmoid is primarily activated in its linear region.

This advice may also apply to the weight activation for the ReLU where the linear part of the function is positive.

This highlights the important impact that initial weights have on learning, where large weights saturate the activation function, resulting in unstable learning, and small weights result in very small gradients and, in turn, slow learning. Ideally, we seek model weights that are over the linear (non-curvy) part of the activation function.

… weights that range over the sigmoid’s linear region have the advantage that (1) the gradients are large enough that learning can proceed and (2) the network will learn the linear part of the mapping before the more difficult nonlinear part.

The authors suggest a random weight initialization scheme that uses the number of nodes in the previous layer, the so-called fan-in. This is interesting as it is a precursor of what became known as the Xavier weight initialization scheme.

Radial Basis Functions vs Sigmoid Units
This final tip is perhaps less relevant today, and I recommend trying radial basis functions (RBF) instead of sigmoid activation functions in some cases.

The authors suggest that training RBF units can be faster than training units using a sigmoid activation.

Unlike sigmoidal units which can cover the entire space, a single RBF unit covers only a small local region of the input space. This can be an advantage because learning can be faster.
