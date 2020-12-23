
![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/1%20(1).png?raw=true)

## What is YOLO

"You Only Look Once" (YOLO) is a popular algorithm because it achieves high accuracy while also being able to run in real-time. This algorithm "only looks once" at the image in the sense that it requires only one forward propagation pass through the network to make predictions. After non-max suppression, it then outputs recognized objects together with the bounding boxes.

In comparison to recognition algorithms, a detection algorithm does not only predict class labels but detects locations of objects as well. So, It not only classifies the image into a category, but it can also detect multiple Objects within an Image. This Algorithm applies a single Neural network to the Full Image. It means that this network divides the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities.


## YoloV3

YOLO V3 is an improvement over previous YOLO detection networks. Compared to prior versions, it features multi-scale detection, stronger feature extractor network, and some changes in the loss function. As a result, this network can now detect many more targets from big to small. And, of course, just like other single-shot detectors, YOLO V3 also runs quite fast and makes real-time inference possible on GPU devices.


## Architecture

The feature extractor YOLO V3 uses is called Darknet-53. YOLOV3 makes use of only convolutional layers. As its name suggests, it contains 53 convolutional layers, each followed by a batch normalization layer and Leaky ReLU activation. No form of pooling is used, and a convolutional layer with stride 2 is used to downsample the feature maps. This helps in preventing the loss of low-level features often attributed to pooling. Below is architecture of darknet-53,

  ![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/da.PNG?raw=true)
  
 


## How it works


Now suppoese the input is a batch of images, and each image has the shape (m, 608, 608, 3)
The output is a list of bounding boxes along with the recognized classes. Each bounding box is represented by 6 numbers  (𝑝𝑐,𝑏𝑥,𝑏𝑦,𝑏ℎ,𝑏𝑤,𝑐)  as explained above. If you expand  𝑐(class-label)  into an 80-dimensional vector, each bounding box is then represented by 85 numbers.


Anchor boxes are chosen by exploring the training data to choose reasonable height/width ratios that represent the different classes. Suppose we choose, 5 anchor boxes were chosen (to cover the 80 classes). 
The dimension for anchor boxes is the second to last dimension in the encoding:  (𝑚, 𝑛𝐻, 𝑛𝑊, 𝑎𝑛𝑐ℎ𝑜𝑟𝑠, 𝑐𝑙𝑎𝑠𝑠𝑒𝑠).
The YOLO architecture is: IMAGE (m, 608, 608, 3) -> DEEP CNN -> ENCODING (m, 19, 19, 5, 85). See the below image

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/e1.PNG?raw=true)


If the center/midpoint of an object falls into a grid cell, that grid cell is responsible for detecting that object. Since we are using 5 anchor boxes, each of the 19 x19 cells thus encodes information about 5 boxes. Anchor boxes are defined only by their width and height.

For simplicity, we will flatten the last two last dimensions of the shape (19, 19, 5, 85) encoding. So the output of the Deep CNN is (19, 19, 425).

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/e2.PNG?raw=true)


Now, for each box (of each cell) we will compute the following element-wise product and extract a probability that the box contains a certain class.
The class score is  𝑠𝑐𝑜𝑟𝑒𝑐,𝑖=𝑝𝑐×𝑐𝑖 : the probability that there is an object  𝑝𝑐  times the probability that the object is a certain class  𝑐𝑖 .

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/e3.PNG?raw=true)


After applying anchor boxes the visualization will look like this,

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/tm.PNG?raw=true)



## Non-MAX Suppression

First, we filter boxes based on their objectness score. Generally, boxes having scores below a threshold (for example below 0.5) are ignored. Next, Non-maximum Suppression (NMS) intends to cure the problem of multiple detections of the same image

The model gives a total of 19x19x5x85 numbers, with each box described by 85 numbers. It is convenient to rearrange the (19,19,5,85) (or (19,19,425)) dimensional tensor into the following variables:

#### box_confidence: 
tensor of shape  (19×19,5,1)  containing  𝑝𝑐  (confidence probability that there's some object) for each of the 5 boxes predicted in each of the 19x19 cells.
#### boxes: 
tensor of shape  (19×19,5,4)  containing the midpoint and dimensions  (𝑏𝑥,𝑏𝑦,𝑏ℎ,𝑏𝑤)  for each of the 5 boxes in each cell.
#### box_class_probs: 
tensor of shape  (19×19,5,80)  containing the "class probabilities"  (𝑐1,𝑐2,...𝑐80)  for each of the 80 classes for each of the 5 boxes per cell.

Even after filtering by thresholding over the class scores, we still end up a lot of overlapping boxes. A second filter for selecting the right boxes is called NMS. NMS uses the very important function called “Intersection over Union”, or IoU. 


![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/nms.PNG?raw=true)



#### Intersection Over Union (IOU)

To find the intersection of the two boxes  (𝑥𝑖1,𝑦𝑖1,𝑥𝑖2,𝑦𝑖2) :

  The top left corner of the intersection  (𝑥𝑖1,𝑦𝑖1)  is found by comparing the top left corners  (𝑥1,𝑦1)  of the two boxes and finding a vertex that has an x-coordinate that is closer to the right, and y-coordinate that is closer to the bottom.
  
  The bottom right corner of the intersection  (𝑥𝑖2,𝑦𝑖2)  is found by comparing the bottom right corners  (𝑥2,𝑦2)  of the two boxes and finding a vertex whose x-coordinate is closer to the left, and the y-coordinate that is closer to the top.
  
  The two boxes may have no intersection. You can detect this if the intersection coordinates you calculate end up being the top right and/or bottom left corners of an intersection box. Another way to think of this is if you calculate the height  (𝑦2−𝑦1)  or width  (𝑥2−𝑥1)  and find that at least one of these lengths is negative, then there is no intersection (intersection area is zero).
  
  The two boxes may intersect at the edges or vertices, in which case the intersection area is still zero. This happens when either the height or width (or both) of the calculated intersection is zero.


The important rule to apply NMS:
1. Select the box that has the highest score.

2. Compute its overlap with all other boxes, and remove boxes that overlap it more than iou_threshold.

3. Go back to step 1 and iterate until there are no more boxes with a lower score than the currently selected box.


After apply Non-max-suppression

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/AANM.PNG?raw=true)


## SUMMARY :

1. Input image (height, width, 3)

2. The input image goes through a CNN, resulting in a (19,19,5,85) dimensional output.

3. After flattening the last two dimensions, the output is a volume of shape (19, 19, 425):

   - Each cell in a 19x19 grid over the input image gives 425 numbers.
          
   - 425 = 5 x 85 because each cell contains predictions for 5 boxes, corresponding to 5 anchor boxes, as seen in lecture.
          
   - 85 = 5 + 80 where 5 is because  (𝑝𝑐,𝑏𝑥,𝑏𝑦,𝑏ℎ,𝑏𝑤)  has 5 numbers, and 80 is the number of classes we'd like to detect
          
          
4. You then select only few boxes based on:

   - Score-thresholding: throw away boxes that have detected a class with a score less than the threshold
          
   - Non-max suppression: Compute the Intersection over Union and avoid selecting overlapping boxes



## Training with Custom Dataset


![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV3/images/1%20(2).png?raw=true)
