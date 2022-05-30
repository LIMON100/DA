# Calculate mAP for custom model

## mAP(Mean Average Precision)

### Intersection Over Union (IOU)

Intersection Over Union (IOU) is a measure based on Jaccard Index that evaluates the overlap between two bounding boxes. It requires a ground truth bounding box and a predicted bounding box. By applying the IOU we can tell if detection is valid (True Positive) or not (False Positive).

IOU is given by the overlapping area between the predicted bounding box and the ground truth bounding box divided by the area of union between them:  

 

The image below illustrates the IOU between a ground truth bounding box (in green) and a detected bounding box (in red).


### Precision & recall

Precision measures how accurate are your predictions. i.e. the percentage of your predictions are correct.

Recall measures how well you find all the positives. For example, we can find 80% of the possible positive cases in our top K predictions.

True Positive, False Positive, False Negative, and True Negative

Some basic concepts used by the metrics:

    True Positive (TP): A correct detection. Detection with IOU ≥ threshold

    False Positive (FP): A wrong detection. Detection with IOU < threshold

    False Negative (FN): A ground truth not detected

    True Negative (TN): Does not apply. It would represent a corrected misdetection. In the object detection task, there are many possible bounding boxes that should not be detected within an image. Thus, TN would be all possible bounding boxes that were correctly not detected (so many possible boxes within an image). That's why it is not used by the metrics.
    
    
### Average Precision

Another way to compare the performance of object detectors is to calculate the area under the curve (AUC) of the Precision x Recall curve. As AP curves are often zigzag curves going up and down, comparing different curves (different detectors) in the same plot usually is not an easy task - because the curves tend to cross each other much frequently. That's why Average Precision (AP), a numerical metric, can also help us compare different detectors. In practice AP is the precision averaged across all recall values between 0 and 1..


There are 7 images with 15 ground-truth objects represented by the green bounding boxes and 24 detected objects represented by the red bounding boxes. Each detected object has a confidence level and is identified by a letter (A,B,...,Y).

The following table shows the bounding boxes with their corresponding confidences. The last column identifies the detections as TP or FP. In this example, a TP is considered if IOU 30%, otherwise it is a FP. By looking at the images above we can roughly tell if the detections are TP or FP.


In some images, there is more than one detection overlapping a ground truth (Images 2, 3, 4, 5, 6, and 7). For those cases, the first detection is considered TP while the others are FP. This rule is applied by the PASCAL VOC 2012 metric: "e.g. 5 detections (TP) of a single object is counted as 1 correct detection and 4 false detections”.

The Precision x Recall curve is plotted by calculating the precision and recall values of the accumulated TP or FP detections. For this, first, we need to order the detections by their confidences, then we calculate the precision and recall for each accumulated detection as shown in the table below (Note that for recall computation, the denominator term ("Acc TP + Acc FN" or "All ground truths") is constant at 15 since GT boxes are constant irrespective of detections).


Example computation for the 2nd row (Image 7): Precision = TP/(TP+FP) = 1/2 = 0.5 and Recall = TP/(TP+FN) = 1/15 = 0.066


Plotting the precision and recall values we have the following Precision x Recall curve:

The general definition for the Average Precision (AP) is finding the area under the precision-recall curve above.

After calculating the AP(Average Precision) of every object then sum them up and divided them by the number of class

## Different type of bounding box format

The bounding box has the following (x, y) coordinates of its corners: top-left is (x_min, y_min), top-right is (x_max, y_min), bottom-left is (x_min, y_max), bottom-right is (x_max, y_max). As you see, coordinates of the bounding box's corners are calculated with respect to the top-left corner of the image.

There are multiple formats of bounding boxes annotations. Each format uses its specific representation of bouning boxes coordinates. Albumentations supports four formats:  


## Pascal VOC Bounding box :(x-top left, y-top left, x-bottom right, y-bottom right)

Pascal VOC provides standardized image data sets for object detection

Difference between COCO and Pacal VOC data formats will quickly help understand the two data formats

       1. Pascal VOC is an XML file, unlike COCO which has a JSON file.

       2. In Pascal VOC we create a file for each of the image in the dataset. In COCO we have one file each, for entire dataset for training, testing and validation.

       3. The bounding Box in Pascal VOC and COCO data formats are different

Pascal_voc is a format used by the Pascal VOC dataset. Coordinates of a bounding box are encoded with four values in pixels: [x_min, y_min, x_max, y_max]. x_min and y_min are coordinates of the top-left corner of the bounding box. x_max and y_max are coordinates of bottom-right corner of the bounding box


## Albumentations

Like pascal_voc albumentations also uses four values [x_min, y_min, x_max, y_max] to represent a bounding box. But unlike pascal_voc, albumentations uses normalized values. To normalize values, we divide coordinates in pixels for the x- and y-axis by the width and the height of the image.

    Let the coordinates of the bounding box are x1= 359, y1= 20, x2= 582, y2= 224 

    Height =638 width=850, then:

    59 / 850, 20 / 638, 582 / 850,224 / 638] which are [0.422352, 0.031347, 0.684705, 0.351097].

Albumentations uses this format internally to work with bounding boxes and augment them.

## COCO

## COCO Bounding box: (x-top left, y-top left, width, height)

Coco is a format used by the Common Objects in Context COCO dataset.

In coco, a bounding box is defined by four values in pixels [x_min, y_min, width, height]. They are coordinates of the top-left corner along with the width and height of the bounding box.


## YOLO

In yolo, a bounding box is represented by four values [x_center, y_center, w, h]. x_center and y_center are the normalized coordinates of the center of the bounding box. To make coordinates normalized, we take pixel values of x and y, which marks the center of the bounding box on the x- and y-axis. Then we divide the value of x by the width of the image and value of y by the height of the image. w and h represent the width and the height of the bounding box. They are normalized as well.


## For YOLO
       
   1. Add classes list in a text file
   2. Insert all annotated text file in a folder
   3. Insert images into one folder
   4. Convert the annotated text file to yolo format
           
    python convert_to_yolo.py
    
   5. Run below file to calculate mAP
     
    python calculate_map.py

## For Pascal-VOC
1. Annot your custom validation dataset
2. Convert the xml file into csv file

       python xml_to_csv.py
    
4. Test the custom validation dataset and create extra column name CONFIDENCE


## Change the appropiate COLUMN name into xml_to_csv.py file and then run it.

## For MAIXPY

https://github.com/LIMON100/Deploy-ML/tree/master/Maixduino/Calculate_mAP



## Bounding boxes outside of the image
