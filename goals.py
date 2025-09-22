import requests
import re
import os

# Trgoals domain kontrol
base = "https://trgoals"
domain = ""

for i in range(1393, 2101):
    test_domain = f"{base}{i}.xyz"
    try:
        response = requests.head(test_domain, timeout=3)
        if response.status_code == 200:
            domain = test_domain
            print(f"Çalışır domain bulundu: {domain}")
            break
    except:
        continue

if not domain:
    print("Çalışır bir domain bulunamadı.")
    exit()

# Kanallar ve isimleri
channel_ids = {
    "yayinzirve": "beIN Sports 1 ☪️",
    "yayininat": "beIN Sports 1 ⭐",
    "yayin1": "beIN Sports 1 ♾️",
    "yayinb2": "beIN Sports 2",
    "yayinb3": "beIN Sports 3",
    "yayinb4": "beIN Sports 4",
    "yayinb5": "beIN Sports 5",
    "yayinbm1": "beIN Sports 1 Max",
    "yayinbm2": "beIN Sports 2 Max",
    "yayinss": "Saran Sports 1",
    "yayinss2": "Saran Sports 2",
    "yayint1": "Tivibu Sports 1",
    "yayint2": "Tivibu Sports 2",
    "yayint3": "Tivibu Sports 3",
    "yayint4": "Tivibu Sports 4",
    "yayinsmarts": "Smart Sports",
    "yayinsms2": "Smart Sports 2",
    "yayintrtspor": "TRT Spor",
    "yayintrtspor2": "TRT Spor 2",
    "yayinas": "A Spor",
    "yayinatv": "ATV",
    "yayintv8": "TV8",
    "yayintv85": "TV8.5",
    "yayinnbatv": "NBA TV",
    "yayinex1": "Tâbii 1",
    "yayinex2": "Tâbii 2",
    "yayinex3": "Tâbii 3",
    "yayinex4": "Tâbii 4",
    "yayinex5": "Tâbii 5",
    "yayinex6": "Tâbii 6",
    "yayinex7": "Tâbii 7",
    "yayinex8": "Tâbii 8"
}

# M3U başlığı
m3u_master = "#EXTM3U\n"

# Her kanal için URL çek ve master dosyaya ekle
for channel_id, channel_name in channel_ids.items():
    channel_url = f"{domain}/channel.html?id={channel_id}"
    try:
        r = requests.get(channel_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        match = re.search(r'const baseurl = "(.*?)"', r.text)
        if match:
            baseurl = match.group(1)
            full_url = f"http://proxylendim101010.mywire.org/proxy.php?url={baseurl}{channel_id}"

            # Kanalı M3U'ya ekle
            m3u_master += f'#EXTINF:-1,{channel_name}\n{full_url}\n'

            print(f"✅ {channel_name} eklendi.")
        else:
            print(f"❌ {channel_name} için baseurl bulunamadı.")
    except Exception as e:
        print(f"⚠️ {channel_name} işlenirken hata: {e}")

# Tek dosyaya yaz
with open("goals.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_master)

print("✅ goals.m3u başarıyla oluşturuldu!")
