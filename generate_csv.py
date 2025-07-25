import os
import csv

def load_data_from_folder(folder_path, label):
    data = []
    for filename in sorted(os.listdir(folder_path))[:100]:  # İlk 100 dosya
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            text = file.read().replace('\n', ' ').strip()
            data.append((label, text))
    return data

pos_path = os.path.expanduser("~/Downloads/aclImdb/train/pos")
neg_path = os.path.expanduser("~/Downloads/aclImdb/train/neg")

data = load_data_from_folder(pos_path, 1) + load_data_from_folder(neg_path, 0)

with open("sentiment_data.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Label", "Text"])
    writer.writerows(data)

print("✅ CSV dosyası oluşturuldu: sentiment_data.csv")

