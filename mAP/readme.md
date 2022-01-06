# Calculate mAP for custom model

## For YOLO
       
   Convert the annotated text file to yolo format
           
    python convert_to_yolo.py

## For Pascal-VOC
1. Annot your custom validation dataset
2. Convert the xml file into csv file

       python xml_to_csv.py
    
4. Test the custom validation dataset and create extra column name CONFIDENCE


## Change the appropiate COLUMN name into xml_to_csv.py file and then run it.


## For MAIXPY
