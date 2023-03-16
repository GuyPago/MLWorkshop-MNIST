from fastapi import APIRouter, status, UploadFile
from fastapi_router_controller import Controller
from fastapi.security import HTTPBasic
from DI import mnist_service

from services.MnistService import MnistService

router = APIRouter(prefix='/mnist', tags=['Phonebooks'])
controller = Controller(router)
security = HTTPBasic()

@controller.resource()
class MnistController():
    mnist_service: MnistService = mnist_service

    @controller.route.post('/predict', status_code=status.HTTP_200_OK)
    async def add_contact(self, file: UploadFile) -> int:
        image = await file.read()
        return self.mnist_service.predict(image)