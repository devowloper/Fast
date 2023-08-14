```python
import os
from fastapi import UploadFile

async def save_upload_file(upload_file: UploadFile, destination: str) -> None:
    try:
        with open(destination, "wb") as buffer:
            while content := await upload_file.read(1024):  # async read
                buffer.write(content)
    finally:
        await upload_file.close()

def remove_file(file_path: str) -> None:
    if os.path.isfile(file_path):
        os.remove(file_path)
```