import uvicorn
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

from imagedetecter import detect_lable, detect_object, detect_text

app = FastAPI()


class DetectItem(BaseModel):
    uri: str
    isLabelDetect: bool = False
    isTextlDetect: bool = False


@app.post("/api/detectImage/")
async def create_item(item: DetectItem):
    detected_lable = detect_lable(item.uri)
    detected_text = detect_text(item.uri)
    detected_object = detect_object(item.uri)
    return {
        "lable":detected_lable,
        "object" : detected_object,
        "text": detected_text
    }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
