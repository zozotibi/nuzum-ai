from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="نُظُم API")

# CORS (مهم لربط Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CaseText(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "نُظُم API يعمل بنجاح"}

@app.post("/predict")
def predict_case(data: CaseText):
    text = data.text

    if "حكم" in text and "تنفيذ" in text:
        result = "تنفيذ حكم إداري"
    elif "قرار" in text or "فصل" in text:
        result = "إلغاء قرار إداري"
    elif "عقد" in text or "مقاولة" in text:
        result = "عقد إداري"
    elif "تعويض" in text or "ضرر" in text:
        result = "تعويض"
    else:
        result = "غير محدد"

    return {"prediction": result}
