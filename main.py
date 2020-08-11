import io
import shutil

from fastapi import FastAPI, UploadFile, File

from validators import UploadDocImgFile

app = FastAPI()





@app.post('/')
async def load_file(file: UploadDocImgFile = File(...)):
    with open(file.filename,"wb") as f:
        shutil.copyfileobj(file.file, f)





    #проверить расширение файла..
    #ошибку выдать схемой response_model
    #предусмотреть обработку изображений (Pillow)
    #RКРНВЕРТАЦИЯ doc в pdf


    return {"ok": ''}

