from textblob import TextBlob

# Leksikon kata Indonesia lokal (bebas error server & tanpa internet)
KAMUS_INDO = {
    # Kata Positif
    'bagus': 0.8, 'sangat bagus': 1.0, 'memuaskan': 0.8, 'cepat': 0.5, 
    'suka': 0.7, 'mantap': 0.9, 'keren': 0.8, 'rekomendasi': 0.7, 
    'pas': 0.4, 'nyaman': 0.7, 'murah': 0.4, 'ramah': 0.6, 'top': 0.8,
    
    # Kata Negatif
    'jelek': -0.8, 'buruk': -0.8, 'kecewa': -0.9, 'mengecewakan': -0.9, 
    'lambat': -0.6, 'lemot': -0.6, 'rusak': -0.8, 'cacat': -0.7, 
    'mahal': -0.4, 'parah': -0.7, 'lama': -0.5, 'rugi': -0.7, 'burik': -0.7
}

def analisis_sentimen(teks):
    teks_lower = teks.lower()
    
    # 1. Cek kata Bahasa Indonesia dari leksikon lokal
    skor_indo = 0.0
    ditemukan = False
    for kata, skor in KAMUS_INDO.items():
        if kata in teks_lower:
            skor_indo += skor
            ditemukan = True

    # 2. Jika Bahasa Inggris / tidak ada kata Indo di kamus, gunakan TextBlob
    if not ditemukan:
        analisis = TextBlob(teks)
        polaritas = analisis.sentiment.polarity
    else:
        # Batasi nilai antara -1.0 sampai 1.0
        polaritas = max(-1.0, min(1.0, skor_indo))

    # Penentuan Label Sentimen
    if polaritas > 0.05:
        label = "Positif"
    elif polaritas < -0.05:
        label = "Negatif"
    else:
        label = "Netral"

    return {
        "Teks": teks,
        "Polaritas": round(polaritas, 2),
        "Sentimen": label
    }

# --- PROGRAM INTERAKTIF ---
if __name__ == "__main__":
    print("=== ANALISIS SENTIMEN (INDO & INGGRIS) ===")
    print("Ketik 'keluar' untuk menghentikan program.\n")

    while True:
        input_ulasan = input("Masukkan ulasan: ")
        if input_ulasan.lower() == 'keluar':
            print("Selesai!")
            break
            
        if input_ulasan.strip():
            hasil = analisis_sentimen(input_ulasan)
            print(f"-> Polaritas : {hasil['Polaritas']}")
            print(f"-> Hasil     : {hasil['Sentimen']}\n")