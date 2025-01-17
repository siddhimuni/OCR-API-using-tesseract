
from fastapi import FastAPI, UploadFile, File
import tesse
import utils
from typing import List
import time
import asyncio

app=FastAPI()
@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response={}
    s=time.time()
    for img in Images:
        print("Image uploaded: ", img.filename)
        temp_file=utils._sve_file_to_server(img, path="./", save_as=img.filename)
        text = await tesse.read_image(temp_file)
        response[img.filename]=text
    response['Time taken'] = round( (time.time() - s),2)

    return response