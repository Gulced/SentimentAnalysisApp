import pandas as pd

# CSV'yi oku
df = pd.read_csv("sentiment_data.csv")

# Hatalı Label'ları filtrele (sadece 0 veya 1 kalsın)
df = df[df["Label"].isin([0, 1])]

# Eksik veya boş Text'leri temizle
df = df.dropna(subset=["Text"])

# Yeni temiz dosya olarak kaydet
df.to_csv("clean_sentiment_data.csv", index=False)
print("Temiz CSV oluşturuldu: clean_sentiment_data.csv")


