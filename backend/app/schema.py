from typing import List, Optional
from pydantic import BaseModel, Field


class ItemModel(BaseModel):
    id: Optional[int] = None
    ex_id: str = Field(..., description="客先キー")
    in_id: str = Field(..., description="丸糸キー")


class ItemCreateRequest(BaseModel):
    ex_id: str = Field(..., description="客先キー")
    in_id: str = Field(..., description="丸糸キー")


class ItemUpdateRequest(BaseModel):
    id: Optional[int] = Field(None, description="ID")
    ex_id: Optional[str] = Field(None, description="客先キー")
    in_id: Optional[str] = Field(None, description="丸糸キー")


class ItemResponse(BaseModel):
    data: List[ItemModel] = []
    errors: List[str] = []
