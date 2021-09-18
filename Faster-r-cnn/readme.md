# FASTER-R-CNN

## How to train Faster-r-cnn model in custom dataset

#### Annotation the images to xml format with any annotation tool.


#### Convert xml file to csv

    python xml_to_csv.py
    
    

#### Convert csv file to tfrecord

    python generate_tfrecord.py
