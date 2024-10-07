# Scene Text Recognition

### Setup

- Install DepthAI [version 2.22.0.0, dated 9/29/2023] ([Documentation](https://docs.luxonis.com/projects/api/en/latest/install/#supported-platforms))
- Connect to OAK camera ([Documentation](https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/#device-setup))
- Install required packages from PyPI:
    
    ```bash
    pip install -r requirements.txt
    ```
    

### Usage

- Run the program using Python
    
    ```bash
    python3 main.py
    ```
    

### Output

The program outputs a [ImgDetections](https://docs.luxonis.com/projects/api/en/latest/components/messages/img_detections/#imgdetections) message. For visualization purposes, I have printed all detections and information about them to the console.

Expected output:

```bash
Label: Savantz
Confidence: 0.8230600357055664
Coordinates: (109.34834289550781, -205.5748748779297)
```

### Model Information

**EAST**

Trained on ICDAR 2013, ICDAR 2015
Downloaded from https://github.com/luxonis/depthai-model-zoo

[Source](https://github.com/argman/EAST)


**text-recognition-0012**

Trained on ICDAR 2013
Downloaded from https://github.com/openvinotoolkit/open_model_zoo

[Source](https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/intel/text-recognition-0012)