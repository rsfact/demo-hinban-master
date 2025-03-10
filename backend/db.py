import json
import os
from typing import Dict, List, Optional
from schema import ItemModel

# JSONファイルのパス
DB_FILE = os.path.join(os.path.dirname(__file__), "db.json")

# データベースからすべてのアイテムを取得
def get_all_items() -> List[ItemModel]:
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    return [ItemModel(**item) for item in data["items"]]

# 条件に一致するアイテムを検索
def search_items(item_filter: Dict) -> List[ItemModel]:
    items = get_all_items()
    filtered_items = []

    for item in items:
        match = True
        for key, value in item_filter.items():
            if value is not None and getattr(item, key) != value:
                match = False
                break
        if match:
            filtered_items.append(item)

    return filtered_items

# IDでアイテムを取得
def get_item_by_id(item_id: int) -> Optional[ItemModel]:
    items = get_all_items()
    for item in items:
        if item.id == item_id:
            return item
    return None

# 新しいアイテムを作成
def create_item(item: ItemModel) -> ItemModel:
    with open(DB_FILE, "r") as f:
        data = json.load(f)

    # 自動インクリメントID
    new_id = data["last_id"] + 1
    data["last_id"] = new_id

    # 新しいアイテムを作成
    new_item = item.dict()
    new_item["id"] = new_id
    data["items"].append(new_item)

    # JSONファイルに保存
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return ItemModel(**new_item)

# アイテムを更新
def update_item(item_id: int, item: ItemModel) -> Optional[ItemModel]:
    with open(DB_FILE, "r") as f:
        data = json.load(f)

    # アイテムを検索して更新
    for i, existing_item in enumerate(data["items"]):
        if existing_item["id"] == item_id:
            # IDは変更しない
            updated_item = item.dict(exclude_unset=True)
            updated_item["id"] = item_id
            data["items"][i] = updated_item

            # JSONファイルに保存
            with open(DB_FILE, "w") as f:
                json.dump(data, f, indent=2)

            return ItemModel(**updated_item)

    return None

# アイテムを削除
def delete_item(item_id: int) -> bool:
    with open(DB_FILE, "r") as f:
        data = json.load(f)

    # 削除前のアイテム数
    initial_count = len(data["items"])

    # アイテムを削除
    data["items"] = [item for item in data["items"] if item["id"] != item_id]

    # 削除後のアイテム数が変わっていれば成功
    if len(data["items"]) < initial_count:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=2)
        return True

    return False
