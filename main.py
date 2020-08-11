import io

from fastapi import FastAPI, UploadFile, File
import aiofile
app = FastAPI()


@app.post('/')
async def load_file(file: UploadFile = File(...)):
    # f = await file.read()
    # async with open(file.filename,'wb') as file:
    #     await file.write(f)
    # ff = await file.write(f)
    # print(ff)
    # print(type(file.filename))



    #проверить расширение файла..
    #ошибку выдать схемой response_model
    #предусмотреть обработку изображений (Pillow)
    #RКРНВЕРТАЦИЯ doc в pdf
    async with aiofile.open(file.filename, mode='wb+') as fn:
        fn.write(io.BytesIO(f))
        fn.flush()

    #

    # async with aiofiles.open('filename', mode='w') as f:
    #     contents = await f.read()
    # print(contents)
    # async with open('file.txt','w') as nf:
    #     with op
    #     nf.write()

    return {"ok": ''}

