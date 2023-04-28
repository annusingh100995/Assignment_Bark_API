from fastapi import FastAPI
from pydantic import BaseModel
import bark
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

# download and load all models
preload_models()


app = FastAPI()

class TextIn(BaseModel):
    text: str


#class PredictionOut(BaseModel):
#    language: str


@app.get("/")
def home():
    return {"health_check": "OK"}


"""@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}"""

@app.post("/predict")
def predict(text_prompt: TextIn):
    audio_array = generate_audio(text_prompt)
    #Audio(audio_array, rate=SAMPLE_RATE)
    return {"speech": audio_array}
