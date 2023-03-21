import uvicorn
from fastapi import FastAPI, Request
from fastapi import File, UploadFile

from src.components.predict import Prediction

app = FastAPI()
searched_images = []
predict_pipeline = Prediction()


@app.get("/", status_code=200)
@app.post("/")
async def index(request: Request):
    """
    Description : This Route loads the index.html
    """
    return JSONResponse(content={"message": "Welcome to Image Search"})


@app.post('/image')
async def upload_file(file: UploadFile = File(...)):
    """
    Description : This Route loads the predictions in a list which will be listed on webpage.
    """
    global searched_images, predict_pipeline
    try:
        if predict_pipeline:
            contents = file.file.read()
            searched_images = predict_pipeline.run_predictions(contents)
            return {"message": "Prediction Completed"}
        else:
            return {"message": "First Load Model in Production using reload_prod_model route"}
    except Exception as e:
        return {"message": f"There was an error uploading the file {e}"}


@app.post('/reload')
def reload():
    """
    Description : This Route resets the predictions in a list for reload.
    """
    global searched_images
    searched_images = []
    return


@app.get('/reload_prod_model')
def reload():
    """
    Description : This Route is Event Triggered or owner controlled to update
                  the model in prod with minimal downtime.
    """
    global predict_pipeline
    try:
        del predict_pipeline
        predict_pipeline = Prediction()
        return {"Response": "Successfully Reloaded"}
    except Exception as e:
        return {"Response": e}


@app.get('/gallery')
async def gallery(request: Request):
    """
    Description : This Route lists all the predicted images on the gallery.html listing depends on prediction.
    """
    global searched_images
    return JSONResponse(content={"length": len(searched_images), "searched_images": searched_images})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
