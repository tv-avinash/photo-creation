from cog import BasePredictor, Input
import numpy as np
from PIL import Image

class Predictor(BasePredictor):
    def predict(self, text: str = Input(default="hello")):
        # Create an image with text
        img = Image.new("RGB", (512, 512), color=(255, 100, 150))
        return img
