import numpy as np
import depthai
import east

# Create pipeline
pipeline = depthai.Pipeline()

# Define sources and outputs
colorCamera = pipeline.createColorCamera()
eastTextDetection = pipeline.createNeuralNetwork()

xoutEastTextDetection = pipeline.createXLinkOut()

# Properties
colorCamera.setPreviewSize(256, 256)
colorCamera.setInterleaved(False)

eastTextDetection.setBlobPath(east.blob_path)
xoutEastTextDetection.setStreamName("East Text Detection")

# Linking
colorCamera.preview.link(eastTextDetection.input)
eastTextDetection.out.link(xoutEastTextDetection.input)

# Connect to device and start pipeline
with depthai.Device(pipeline) as device:
    eastTextDetectionQueue = device.getOutputQueue(
        "East Text Detection", maxSize=1, blocking=False
    )

    while True:
        NNData = eastTextDetectionQueue.get()
        if NNData is not None:
            output = east.decode(NNData)
            print(output)
