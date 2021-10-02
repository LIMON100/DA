# FASTER-R-CNN

## How to train Faster-r-cnn model in custom dataset

#### Annotation the images to xml format with any annotation tool.


#### Write down the classes names and save it with .pbtxt format


#### Convert xml file to csv

    python xml_to_csv.py
   
   

#### Convert csv file to tfrecord

convert train file

    python generate_tfrecords.py --path_to_images "path your train images folder" --path_to_annot "path train csv file" --path_to_label_map "path to labelmap.pbtxt file" --path_to_save_tfrecords "save path"
    
    
convert validation file

    
    python generate_tfrecords.py --path_to_images "path your validation images folder" --path_to_annot "path validation csv file" --path_to_label_map "path to labelmap.pbtxt file" --path_to_save_tfrecords "save path"



#### Download config file according to your desire and change this line


change config file:

    num_classes: classes number

    batch_size: 64(better but if you don't have powerful gpu than change whatever you want)

    num_steps: 25000(2000 per class is better. You can set more)

    fine_tune_checkpoint : set path where you save trained model expample(your_checkpoint_path/ckpt-0)

    label_map_path: change path in train+eval

    input_path: change tfrecord path for both train+eval



### Training

go to models->research folder,

    !PIPELINE_CONFIG_PATH='path the configuration file'

    !MODEL_DIR="path to the save training file"
    
   
   
run
    
    python object_detection/model_main_tf2.py --pipeline_config_path=${PIPELINE_CONFIG_PATH} --model_dir=${MODEL_DIR} --alsologtostderr
    


### Evaluation


    PIPELINE_CONFIG_PATH={path to pipeline config file}
    
    MODEL_DIR={path to model directory}
    
    CHECKPOINT_DIR=${MODEL_DIR}
    
    MODEL_DIR={path to model directory}
    
    python object_detection/model_main_tf2.py --pipeline_config_path=${PIPELINE_CONFIG_PATH} --model_dir=${MODEL_DIR} --checkpoint_dir=${CHECKPOINT_DIR} --alsologtostderr
    
    
    
    
### Kick-off


If the training interrupted due to some accident such as power interruption or sudden computer shutdown while you are training your custom object detection project using the tensor-flow object detection API using any of the sample pre-trained models such as ssd_mobilenet_v2, faster_rcnn_inception_v2 etc. Follow this steps to resume training from where your last model saved your weights or model.ckpt.


In the folder ./object_detection/models/research/object_detection/samples/configs/ssd_mobilenet_v2_coco.config or whatever your pre-trained model is when you open your config file there is a section called fine_tune_checkpoint this is where the training process saves and loads its status during its training progress. change the directory location for the fine_tune_checkpoint section. Once you change that, whatever interrupted your training process to resume it just use the same command for training. It start executing from the last saved checkpoint and iteration number.






### Make model for production:


PIPELINE_CONFIG_PATH = 'set path of your configuration file'
