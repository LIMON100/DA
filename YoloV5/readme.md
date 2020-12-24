## TRAIN YOLOV5 on Custom Dataset


![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV5/images/03ccf5d6-a6cd-4352-820e-afc7772a95e1.jpg?raw=true)


Check which NVIDIA-GPU version you got. In colab there are several gpu version available. Most of the time it provide Tesla k-80.

    !nvidia-smi
    
    
    
Clone the YoloV5 repository which is written in pytorch by ultralytics. 

    !git clone https://github.com/ultralytics/yolov5

If you use in local machine then donot need to use '!' sign. Just simply clone the repository.



Go inside the repository and install the necessery tools for YoloV5.

    %cd yolov5
    !pip install -r requirements.txt
    
   
   
   
Now if you need to speed up your training than you can install nvidia-apex. It is a Pytorch extension with NVIDIA-maintained utilities to streamline mixed precision and distributed training.   

    !git clone https://github.com/NVIDIA/apex && cd apex && pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" . --user && cd .. && rm -rf apex
    
    
    
    
 Now Connect COlAB with your driver and install necessray packages. 
 
Now you need to configure two files. One is where your training data is and another is which yolov5 model you are going to use. There are 4 different types of yolov5 model is available. 5s, 5l, 5m, 5x. 


    !gdown --id "put your file address link in your drive" -O data/veh.yaml

for example, !gdown --id 1DVPEmt_RaFVfPZeNNW7IGHPZJSHaGBCL -O data/veh.yaml

    !gdown --id "file path" -O models/yolov5s.yaml
    
    

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






![](https://github.com/LIMON100/Dhaka-AI/blob/master/YoloV5/images/Shykat_02_018_jpg.rf.1dccfd91443605cf13d0f6150aaf3701.jpg?raw=true)



