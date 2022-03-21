# Calculate mAP for custom model

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
