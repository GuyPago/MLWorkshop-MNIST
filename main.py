from fastapi import FastAPI, status
import uvicorn
from controllers.MnistController import MnistController

app = FastAPI()
app.include_router(MnistController.router())

@app.get('/sanity')
def sainity_check():
    return status.HTTP_200_OK

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)