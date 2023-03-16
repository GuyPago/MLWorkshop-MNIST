from pydantic import BaseModel
from torchvision import transforms
from models.MnistModel import MnistModel
from PIL import Image
import io

class MnistService(BaseModel):
    model: MnistModel
    _transform  = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((28,28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)),
    ])

    def predict(self, image):
        image = self.preprocess(image)

        return self.model.predict(image)
    
    def preprocess(self, image):
        preprocessed_image = Image.open(io.BytesIO(image))
        preprocessed_image = self._transform(preprocessed_image)
        
        return preprocessed_image