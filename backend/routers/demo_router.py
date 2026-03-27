from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from backend.services.demo_service import DemoService


router = APIRouter(prefix="/demo", tags=["demo"])



@router.get(path="")
async def get_data(data_id:str, service = Depends(DemoService)):
    message = f"This is a query parameter {data_id}"
    return {"message": message}
