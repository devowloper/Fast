```python
from fastapi import APIRouter, HTTPException
from ..models import PrintEstimate
from ..estimator import PrintEstimator

router = APIRouter()

@router.post("/estimate", response_model=PrintEstimate)
async def get_estimate(filament_type: str, infill_percentage: int, model_path: str):
    try:
        estimator = PrintEstimator(model_path)
        estimation = estimator.estimate(filament_type, infill_percentage)
        return estimation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```