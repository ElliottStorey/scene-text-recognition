import numpy as np
import blobconverter

blob_path = blobconverter.from_zoo(
    name="east_text_detection_256x256", zoo_type="depthai", shaves=6
)


def decode(NNData):
    print(
        {
            name: np.array(NNData.getLayerFp16(name))
            for name in [tensor.name for tensor in NNData.getRaw().tensors]
        }
    )
    scores = NNData.getLayerFp16("scores")
    geom1 = NNData.getLayerFp16("geom1")
    geom2 = NNData.getLayerFp16("geom2")
    print(scores, geom1, geom2)
    scores = np.reshape(scores, (1, 1, 64, 64))
    geom1 = np.reshape(geom1, (1, 4, 64, 64))
    geom2 = np.reshape(geom2, (1, 1, 64, 64))
    print(scores, geom1, geom2)
