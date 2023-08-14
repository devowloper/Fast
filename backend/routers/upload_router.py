```python
from fastapi import APIRouter, UploadFile, File
from ..utils.file_utils import save_upload_file
from ..models import FileUpload

router = APIRouter()

@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_upload = FileUpload(file=file)
    file_path = await save_upload_file(file_upload)
    return {"filepath": file_path}
```