from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = FastAPI()

class CaseText(BaseModel):
    text: str

texts = [
    "تم فصلي من جهة حكومية",
    "صدر قرار إداري غير مشروع",
    "لم يتم تنفيذ حكم نهائي",
    "أطالب بتنفيذ الحكم الصادر",
    "يوجد نزاع حول عقد مقاولة",
    "خلاف مع جهة حكومية حول عقد",
    "أطالب بتعويض عن ضرر",
    "تضررت بسبب قرار إداري"
]

labels = [
    "إلغاء قرار إداري",
    "إلغاء قرار إداري",
    "تنفيذ حكم إداري",
    "تنفيذ حكم إداري",
    "عقد إداري",
    "عقد إداري",
    "تعويض",
    "تعويض"
]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

model.fit(texts, labels)

@app.post("/predict")
def predict_case(data: CaseText):
    prediction = model.predict([data.text])
    return {"prediction": prediction[0]}
