# Python ANPR

This project is buit on top of an existing python implementation that uses computer vision to identify and read the registration plates of UK vehicles.

## Requirements
To run the application at this stage you will need a sample mp4 file as well as a pre-trained pytorch model to enable the image classification. I have provided these resources below:

[Sample Videos](https://drive.google.com/file/d/1R0Jj5p0jVRsgRHNVBXNePtWZjF5ayQRw/view?usp=sharing)

[pytorch pretrained model](https://drive.google.com/file/d/1NdK73iUH9Bn3-5KGRorGCPDRFRxkRxc3/view?usp=sharing)

## Installation
After installing the requirements, ensure there exists a samples directory containing sample.mp4. Also ensure that there exists a directory named models containing the pretrained model. Then from the project root:

```
docker image build -t python-anpr-0.0.1 .
```

And then run a container:

```
docker run -it python-anpr-0.0.1  
```

## Goal
I aim to containerize the python implementation and expose it on a web server, allowing it to receive video streams or images for processing. It should then return the vehicle registrations and some miscellaneous data such as MOT/tax status.

## Current status
Currently, the project can successfully identify and read registration plates from an mp4 file with high confidence. The area of the video that is scanned can also be altered to optimise the execution speed.

The project can be ran without creating a docker image and line 72 of main.py can be uncommented to see a live demonstration of the scanner running.


![image](https://github.com/callumjfortune/python-anpr/assets/114265390/610e40c7-f972-4776-989f-059f1bc48cfe)
