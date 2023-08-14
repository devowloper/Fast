```python
from pydantic import BaseModel

class FileUpload(BaseModel):
    filename: str
    content_type: str
    file: bytes

class PrintEstimate(BaseModel):
    weight: float
    volume: float
    cost_price: float
    selling_price: float
    gross_profit_margin: float
```