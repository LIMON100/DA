## TRAIN YOLOV5 on Custom Dataset


![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV5/images/03ccf5d6-a6cd-4352-820e-afc7772a95e1.jpg?raw=true)


Check which NVIDIA-GPU version you got. In colab there are several gpu version available. Most of the time it provide Tesla k-80.

    !nvidia-smi
    
    
    
Clone the YoloV5 repository which is written in pytorch by ultralytics. 

    !git clone https://github.com/ultralytics/yolov5

If you use in local machine then donot need to use '!' sign. Just simply clone the repository.


### Install requirement packages for YoloV5

Go inside the repository and install the necessery tools for YoloV5.

    %cd yolov5
    !pip install -r requirements.txt
    
   
   
   
Now if you need to speed up your training than you can install nvidia-apex. It is a Pytorch extension with NVIDIA-maintained utilities to streamline mixed precision and distributed training.   

    !git clone https://github.com/NVIDIA/apex && cd apex && pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" . --user && cd .. && rm -rf apex
    
    
    
    
Now Connect COlAB with your driver and install necessray packages. 


### Setup files for training 

Now you need to configure two files. One is where your training data is and another is which yolov5 model you are going to use. There are 4 different types of yolov5 model is available. 5s, 5l, 5m, 5x. 


    !gdown --id "put your file address link in your drive" -O data/veh.yaml

for example, !gdown --id 1DVPEmt_RaFVfPZeNNW7IGHPZJSHaGBCL -O data/veh.yaml

    !gdown --id "file path" -O models/yolov5s.yaml
    
    

### Training

Google colab is free but there are some problems, one of them is you cannot training in idle. If you not working at the page of colab it will automatically stop working after 45 or less than 45 minutes. So there is a simple hack for this.

    function ClickConnect(){
    console.log("Working"); 
    document
      .querySelector('#top-toolbar > colab-connect-button')
      .shadowRoot.querySelector('#connect')
      .click() 
    }
    setInterval(ClickConnect,60000
    
This can wake-up colab till your one-day time out. One-day time out means colab let you work 12 hours in a day. So it will work 12 hours without any problem.



Notebook crashing is another major problem in colab. So before training any model just simply use this hack,

      %%capture




Training your model,

img 640 - resize the images to 640x640 pixels(You can resize it your own choice. But increse the size take so much time to run.)
batch 4 - 4 images per batch
epochs 30 - train for 30 epochs
data ./data/veh.yaml - path to dataset config
cfg ./models/yolov5s.yaml - model config
weights yolov5s.pt - use pre-trained weights from the YOLOv5s model
name yolov5s_clothing - name of our model
cache - cache dataset images for faster training

    %%capture
    !python train.py --img 640 --batch 16 --epochs 460 --data ./data/veh.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name yolov5s_veh --cache




### Show the loss graph

After training you can check how much good your model can or how decrese the loss is by ploting graph,

    from utils.general import plot_results         
    plot_results();



### Prediction


If you want to check the prediction of your model then save some images into yolov5->data->images folder and run below command. You can find the output inside yolov5->inference folder.

    #!python detect.py --weights weights/best.pt --img 640 --conf 0.50 --source ./data/images/


plot some images by calling a simple function.

    
    def load_image(img_path: Path, resize=True):
      img = cv2.cvtColor(cv2.imread(str(img_path)), cv2.COLOR_BGR2RGB)
      img = cv2.resize(img, (128, 256), interpolation = cv2.INTER_AREA)
      return img

    def show_grid(image_paths):
      images = [load_image(img) for img in image_paths]
      images = torch.as_tensor(images)
      images = images.permute(0, 3, 1, 2)
      grid_img = torchvision.utils.make_grid(images, nrow=11)
      plt.figure(figsize=(24, 12))
      plt.imshow(grid_img.permute(1, 2, 0))
      plt.axis('off');
      
     
     img_paths = list(Path("inference/output").glob("*.jpg"))[:22]
     show_grid(img_paths)
     
     


You can find everything inside training yolov5 with custom dataset notebook. I trained yolov5s only with different amount of dataset. But due to time-out problem in colab i could use another model like 5l,5l,5x. Training 4000 images in 5s almost take 10 hours it will take minimum 20 hours in 5l. So if your dataset is small then use any yolov5 model. 

![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV5/images/Shykat_02_018_jpg.rf.1dccfd91443605cf13d0f6150aaf3701.jpg?raw=true)



