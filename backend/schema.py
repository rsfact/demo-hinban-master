from typing import List, Optional
from pydantic import BaseModel, Field

# 品番データモデル（レスポンス用）
class ItemModel(BaseModel):
    id: Optional[int] = None
    ex_id: str = Field(..., description="社外品番")
    in_id: str = Field(..., description="社内品番")

# 品番作成リクエスト用モデル（idなし）
class CreateItemModel(BaseModel):
    ex_id: str = Field(..., description="社外品番")
    in_id: str = Field(..., description="社内品番")

# 品番更新リクエスト用モデル（idなし）
class UpdateItemModel(BaseModel):
    ex_id: str = Field(..., description="社外品番")
    in_id: str = Field(..., description="社内品番")

# 単一アイテムのレスポンス
class ItemResponse(BaseModel):
    data: Optional[ItemModel] = None
    errors: List[str] = []

# 複数アイテムのレスポンス
class ItemListResponse(BaseModel):
    data: List[ItemModel] = []
    errors: List[str] = []
