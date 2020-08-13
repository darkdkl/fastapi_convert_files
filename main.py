import io
import shutil
from fastapi import FastAPI, File
from validators import UploadDocImgFile
from converter import convert_doc_to_pdf

app = FastAPI()





@app.post('/')
async def load_file(file: UploadDocImgFile = File(...)):
    #TODO реализовать используя temfile
    with open(file.filename,"wb") as f:
        shutil.copyfileobj(file.file, f)

    print(convert_doc_to_pdf(file.filename))








    #проверить расширение файла..
    #ошибку выдать схемой response_model
    #предусмотреть обработку изображений (Pillow)
    #RКРНВЕРТАЦИЯ doc в pdf


    return {"ok": ''}

