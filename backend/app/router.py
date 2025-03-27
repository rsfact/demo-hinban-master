from fastapi import APIRouter
from typing import Optional
from schema import ItemModel, ItemCreateRequest, ItemUpdateRequest, ItemResponse
import service

router = APIRouter(prefix="/api/items", tags=["items"])

# すべての品番を取得
@router.get("/", response_model=ItemResponse)
async def get_part_numbers(
    id: Optional[int] = None,
    ex_id: Optional[str] = None,
    in_id: Optional[str] = None
):
    # 検索条件を構築
    item_filter = {
        "id": id,
        "ex_id": ex_id,
        "in_id": in_id
    }

    # 条件に一致する品番を検索
    items = service.search_items(item_filter)

    # レスポンスを構築
    return ItemResponse(data=items)

# IDで品番を取得
@router.get("/{item_id}", response_model=ItemResponse)
async def get_part_number(item_id: int):
    item = service.get_item_by_id(item_id)
    if not item:
        return ItemResponse(errors=["品番が見つかりません"])
    return ItemResponse(data=[item])

# 新しい品番を作成
@router.post("/", response_model=ItemResponse)
async def create_part_number(item: ItemCreateRequest):
    try:
        # CreateItemModelからItemModelに変換
        new_item = ItemModel(ex_id=item.ex_id, in_id=item.in_id)
        created_item = service.create_item(new_item)
        return ItemResponse(data=[created_item])
    except Exception as e:
        return ItemResponse(errors=[f"品番作成エラー: {str(e)}"])

# 品番を更新
@router.put("/{item_id}", response_model=ItemResponse)
async def update_part_number(item_id: int, item: ItemUpdateRequest = None):
    # 既存のアイテムを取得
    existing_item = service.get_item_by_id(item_id)
    if not existing_item:
        return ItemResponse(errors=["更新する品番が見つかりません"])

    # リクエストボディがない場合は空のオブジェクトを作成
    if item is None:
        item = ItemUpdateRequest()

    # 既存の値を使用して、更新するフィールドのみを変更
    update_data = {
        "id": item_id,
        "ex_id": item.ex_id if item.ex_id is not None else existing_item.ex_id,
        "in_id": item.in_id if item.in_id is not None else existing_item.in_id
    }

    # 更新用のItemModelを作成
    update_item = ItemModel(**update_data)

    # 更新を実行
    updated_item = service.update_item(item_id, update_item)
    return ItemResponse(data=[updated_item])

# 品番を削除
@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_part_number(item_id: int):
    success = service.delete_item(item_id)
    if not success:
        return ItemResponse(errors=["削除する品番が見つかりません"])

    # 削除成功の場合は空のデータを返す
    return ItemResponse(data=[ItemModel(id=item_id, ex_id="", in_id="")])
