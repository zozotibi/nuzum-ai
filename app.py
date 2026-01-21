from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# تفعيل CORS (ضروري لربط Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل النموذج
model = joblib.load("model.pkl")

class CaseText(BaseModel):
    text: str

@app.post("/predict")
def predict_case(data: CaseText):
    prediction = model.predict([data.text])
    return {
        "prediction": prediction[0]
    }
