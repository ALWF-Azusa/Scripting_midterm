# modu.py

from typing import Dict
import json


# ----------------------------------
def triangle_zhonxin(a: tuple, b: tuple, c: tuple) -> tuple:
    # -> Function Annotations  簡稱 函式註解
    """
    Calculate the centroid of a triangle.

    Parameters:
    a (tuple): Coordinates of point a as a tuple (x1, y1).
    b (tuple): Coordinates of point b as a tuple (x2, y2).
    c (tuple): Coordinates of point c as a tuple (x3, y3).

    Returns:
    tuple: Coordinates of the centroid (x, y) as a tuple.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x = round((x1 + x2 + x3) / 3)
    y = round((y1 + y2 + y3) / 3)

    return x, y


# -------------------------


def read_json(file_name: str) -> Dict:
    """讀取 JSON 檔案並回傳內容為字典形式。"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def print_json(data: Dict) -> None:
    """將字典以格式化的 JSON 字串方式輸出到螢幕。"""
    print(json.dumps(data, ensure_ascii=False, indent=4))


def process_data(data: Dict, discount: float) -> None:
    """將菜單中每個品項的價格打折。"""
    for category in data['categories']:
        for item in category['items']:
            # 乘上折扣率，同時將價格四捨五入到整數
            item['price'] = round(item['price'] * discount)


def write_json(data: Dict, file_name: str) -> None:
    """將字典寫入成 JSON 檔案。"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
