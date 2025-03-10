from typing import Dict, List, Optional
from schema import ItemModel
import db

# すべてのアイテムを取得
def get_all_items() -> List[ItemModel]:
    return db.get_all_items()

# 条件に一致するアイテムを検索
def search_items(item_filter: Dict) -> List[ItemModel]:
    # 空のフィルターの場合は全件取得
    if all(value is None for value in item_filter.values()):
        return get_all_items()
    return db.search_items(item_filter)

# IDでアイテムを取得
def get_item_by_id(item_id: int) -> Optional[ItemModel]:
    return db.get_item_by_id(item_id)

# 新しいアイテムを作成
def create_item(item: ItemModel) -> ItemModel:
    # IDは自動生成されるので無視
    return db.create_item(item)

# アイテムを更新
def update_item(item_id: int, item: ItemModel) -> Optional[ItemModel]:
    # 存在確認
    existing_item = get_item_by_id(item_id)
    if not existing_item:
        return None

    return db.update_item(item_id, item)

# アイテムを削除
def delete_item(item_id: int) -> bool:
    # 存在確認
    existing_item = get_item_by_id(item_id)
    if not existing_item:
        return False

    return db.delete_item(item_id)
