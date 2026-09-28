import streamlit as st
from textblob import TextBlob

# Kamus lokal dari kode yang ada
KAMUS_INDO = {
    'bagus': 0.8, 'sangat bagus': 1.0, 'memuaskan': 0.8, 'cepat': 0.5,
    'suka': 0.7, 'mantap': 0.9, 'keren': 0.8, 'rekomendasi': 0.7,
    'pas': 0.4, 'nyaman': 0.7, 'murah': 0.4, 'ramah': 0.6, 'top': 0.8,
    'jelek': -0.8, 'buruk': -0.8, 'kecewa': -0.9, 'mengecewakan': -0.9,
    'lambat': -0.6, 'lemot': -0.6, 'rusak': -0.8, 'cacat': -0.7,
    'mahal': -0.4, 'parah': -0.7, 'lama': -0.5, 'rugi': -0.7, 'burik': -0.7
}

def analisis_sentimen(teks):
    teks_lower = teks.lower()
    skor_indo = 0.0
    ditemukan = False

    for kata, skor in KAMUS_INDO.items():
        if kata in teks_lower:
            skor_indo += skor
            ditemukan = True

    if not ditemukan:
        analisis = TextBlob(teks)
        polaritas = analisis.sentiment.polarity
    else:
        polaritas = max(-1.0, min(1.0, skor_indo))

    if polaritas > 0.05:
        label = "Positif"
    elif polaritas < -0.05:
        label = "Negatif"
    else:
        label = "Netral"

    return round(polaritas, 2), label

# Tampilan Aplikasi
st.title("Aplikasi Analisis Sentimen")
input_teks = st.text_area("Masukkan teks ulasan:")

if st.button("Analisis"):
    if input_teks.strip():
        polaritas, sentimen = analisis_sentimen(input_teks)
        st.write(f"**Polaritas:** {polaritas}")
        st.write(f"**Hasil Sentimen:** {sentimen}")
    else:
        st.warning("Masukkan teks ulasan terlebih dahulu!")