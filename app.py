from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# إنشاء التطبيق
app = FastAPI()

# تفعيل CORS (للسماح لـ Netlify بالاتصال)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يسمح لأي واجهة Frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل النموذج
model = joblib.load("model.pkl")

# شكل البيانات القادمة من الواجهة
class CaseText(BaseModel):
    text: str

# نقطة التنبؤ
@app.post("/predict")
def predict_case(data: CaseText):
    prediction = model.predict([data.text])
    return {
        "prediction": prediction[0]
    }

