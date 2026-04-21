import torchvision.transforms as transforms
from PIL import Image


class Inference:
    def preprocess_image(image: Image.Image):
        """
        Apply resizing and normalization transform
        """
        transforms()
        pass

    def process_and_predict(image: Image.Image):
        """
        Pipeline ->
        - Preprocess image
        - Extract features via CNN
        - Predict via selected model
        - Return final dictionary
        """
        pass
