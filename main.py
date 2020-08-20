import os
import tempfile
import shutil
import time

from fastapi import FastAPI, File,BackgroundTasks
from validators import UploadDocImgFile
from converter import convert_doc_to_pdf
from fastapi.responses import FileResponse

app = FastAPI()


@app.post('/')
async def load_file(file: UploadDocImgFile = File(...)):
    with tempfile.NamedTemporaryFile() as temp:
        shutil.copyfileobj(file.file,temp)
        convert_doc_to_pdf(temp.name,file.filename)
        new_file= f'{file.filename.split(".")[0]}.pdf'
        os.renames(f"{temp.name.split('/')[-1]}.pdf",new_file )
    return {'file': new_file}


def remove_file(file:str):
    print('до')
    time.sleep(2)
    os.remove(os.path.abspath(file))
    print("после")


@app.get('/file/')
async def get_file(file: str,background_tasks: BackgroundTasks):
    if os.path.exists(file):
        background_tasks.add_task(remove_file,file)
        return FileResponse(os.path.abspath(file))

#именование файлов
