# Calculate mAP for custom model

## Different type of bounding box format

The bounding box has the following (x, y) coordinates of its corners: top-left is (x_min, y_min), top-right is (x_max, y_min), bottom-left is (x_min, y_max), bottom-right is (x_max, y_max). As you see, coordinates of the bounding box's corners are calculated with respect to the top-left corner of the image.

There are multiple formats of bounding boxes annotations. Each format uses its specific representation of bouning boxes coordinates. Albumentations supports four formats:  


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
