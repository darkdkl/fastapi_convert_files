import os
import tempfile
import shutil
from fastapi import FastAPI, File
from validators import UploadDocImgFile
from converter import convert_doc_to_pdf

app = FastAPI()

@app.post('/')
async def load_file(file: UploadDocImgFile = File(...)):
    with tempfile.NamedTemporaryFile() as temp:
        shutil.copyfileobj(file.file,temp)
        convert_doc_to_pdf(temp.name,file.filename)
        os.renames(f"{temp.name.split('/')[-1]}.pdf",
                   f'{file.filename.split(".")[0]}.pdf')
    return {"ok": ''}

