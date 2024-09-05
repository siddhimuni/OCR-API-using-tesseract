import pytesseract
import asyncio

img_path= "test.png"
async def read_image(img_path, lang="eng"):
    try:
        text=pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(1)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)