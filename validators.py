from fastapi import UploadFile
from typing import Any,Type
from starlette.datastructures import UploadFile as StarletteUploadFile

class UploadDocImgFile(UploadFile):

    def validate(cls: Type["UploadFile"], v: Any) -> Any:
        if not isinstance(v, StarletteUploadFile):
            raise ValueError(f"Expected UploadFile, received: {type(v)}")
        extension=v.filename.split('.')[-1]
        allow_extensions = ['pdf','doc','docx']
        if extension and extension not in allow_extensions:
            raise ValueError(f'This file not allowed,only {allow_extensions}')
        return v