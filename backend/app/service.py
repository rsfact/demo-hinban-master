from typing import Dict, List, Optional
from schema import ItemModel
from db.database import get_db
from db.models import Item

# すべてのアイテムを取得
def get_all_items() -> List[ItemModel]:
    db = next(get_db())
    items = db.query(Item).all()
    return [ItemModel(id=item.id, ex_id=item.ex_id, in_id=item.in_id) for item in items]

# 条件に一致するアイテムを検索
def search_items(item_filter: Dict) -> List[ItemModel]:
    db = next(get_db())
    query = db.query(Item)

    # フィルター条件を適用
    if item_filter.get("id") is not None:
        query = query.filter(Item.id == item_filter["id"])
    if item_filter.get("ex_id") is not None:
        query = query.filter(Item.ex_id == item_filter["ex_id"])
    if item_filter.get("in_id") is not None:
        query = query.filter(Item.in_id == item_filter["in_id"])

    items = query.all()
    return [ItemModel(id=item.id, ex_id=item.ex_id, in_id=item.in_id) for item in items]

# IDでアイテムを取得
def get_item_by_id(item_id: int) -> Optional[ItemModel]:
    db = next(get_db())
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        return ItemModel(id=item.id, ex_id=item.ex_id, in_id=item.in_id)
    return None

# 新しいアイテムを作成
def create_item(item: ItemModel) -> ItemModel:
    db = next(get_db())
    db_item = Item(ex_id=item.ex_id, in_id=item.in_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return ItemModel(id=db_item.id, ex_id=db_item.ex_id, in_id=db_item.in_id)

# アイテムを更新
def update_item(item_id: int, item: ItemModel) -> Optional[ItemModel]:
    db = next(get_db())
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return None

    # 更新（オプショナルフィールドの場合は更新しない）
    if item.ex_id is not None:
        db_item.ex_id = item.ex_id
    if item.in_id is not None:
        db_item.in_id = item.in_id

    db.commit()
    db.refresh(db_item)

    return ItemModel(id=db_item.id, ex_id=db_item.ex_id, in_id=db_item.in_id)

# アイテムを削除
def delete_item(item_id: int) -> bool:
    db = next(get_db())
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True
