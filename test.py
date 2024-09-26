import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # 讀取 CSV 檔案
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    # 將資料寫入 JSON 檔案
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# 使用範例
csv_file_path = 'test.csv'
json_file_path = 'test.json'
csv_to_json(csv_file_path, json_file_path)