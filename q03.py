# q03.py
from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'


def main():
    # 讀取菜單
    menu = read_json(MENU_FILE)

    # 顯示原始菜單
    print("原始菜單:")
    print_json(menu)

    # 新增一個菜單項目
    new_item = {"name": "海鮮燉飯", "price": 239, "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"}
    menu['categories'][1]['items'].append(new_item)

    # 從使用者獲取折扣率
    discount = float(input("請輸入折扣率 (0.0 ~ 1.0): "))

    # 將折扣套用到菜單
    process_data(menu, discount)

    # 顯示更新後的菜單
    print("更新後的菜單:")
    print_json(menu)

    # 將更新後的菜單寫入輸出檔案
    write_json(menu, OUTPUT_FILE)


if __name__ == "__main__":
    main()
