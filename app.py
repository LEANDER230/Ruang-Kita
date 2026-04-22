import time
import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Untuk Ara Tersayang 💖", layout="centered")

# 2. CSS CUSTOM
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
    html, body, [class*="css"], .stMarkdown, .stText, div, p { 
        font-family: 'Fredoka One', cursive !important; 
        color: #1B4332 !important; 
    }
    .stApp { background-color: #D8F3DC !important; }
    div[data-baseweb="tab-list"] { background-color: #B7E4C7; border-radius: 20px; padding: 10px; }
    div[data-baseweb="tab"] { color: #1B4332 !important; font-weight: bold; }
    div.stButton > button { background-color: #2D6A4F !important; color: #D8F3DC !important; border-radius: 25px !important; border: none; transition: 0.3s; }
    div.stButton > button:hover { transform: scale(1.1); background-color: #081C15 !important; }
</style>
""", unsafe_allow_html=True)

# 3. KONFIGURASI API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 4. JUDUL
st.title("Halo Ara Tersayang! 💖")

# 5. MENU TABS
tab1, tab2, tab3, tab4 = st.tabs(["🌈 Mood", "📸 Memori", "🐧 Kuis", "💬 Curhat"])

with tab1:
    st.subheader("Mood Tracker 🌈")
    st.write("Klik emotikon yang paling menggambarkan perasaan Ara hari ini:")
    
    # DATABASE LENGKAP 10 MOOD
    data_mood = {
        "Sedih": {
            "emo": "😢", "pesan": "Sini Mas peluk jauh dulu... Jangan sedih lama-lama ya, Mas selalu ada buat dengerin Ara.",
            "lagu": ["https://youtu.be/QJO3ROT-A4E?si=e04SQFNZunkJ1Ejx"]
        },
        "Capek/Lelah": {
            "emo": "😫", "pesan": "Mas tahu Ara lagi berjuang keras. Istirahat ya? Mas bangga banget sama Ara yang hebat ini.",
            "lagu": ["https://youtu.be/T4cdfRohhcg?si=UReuklTRTXnXgFeOY"]
        },
        "Cemas/Gelisah": {
            "emo": "😰", "pesan": "Tarik napas dalam-dalam ya Sayang... Mas di sini, semuanya bakal baik-baik aja kok.",
            "lagu": ["https://youtu.be/Xct1EdyHMWw?si=pctatJhbgVTLsztH"]
        },
        "Galau": {
            "emo": "🙂", "pesan": "Lagi banyak pikiran ya? Cerita ke Mas yuk, jangan dipendem sendiri.",
            "lagu": ["https://youtu.be/Q04bUnPX8F8?si=OVVGqDXvP-ylv3Pq"]
        },
        "Biasa Aja": {
            "emo": "😐", "pesan": "Apapun kegiatannya, semangat ya Sayang! Mas yakin Ara bisa ngelewatin hari ini dengan KICAUUU.",
            "lagu": ["https://youtu.be/EaIrvHbYrLs?si=4XOY3LAJSQ9hViCP"]
        },
        "Butuh Motivasi": {
            "emo": "🔥", "pesan": "Ara itu hebat! Jangan lupa, Mas selalu dukung Ara dari sini. Gas pol!",
            "lagu": ["https://youtu.be/qvQwBd-uaJY"]
        },
        "Lagi Berbunga": {
            "emo": "🌸", "pesan": "Duh, senangnya liat Ara bahagia! Mas jadi ikut senyum liatnya.",
            "lagu": ["https://youtu.be/D-VytLhH-KE?si=LVR918kTKf1BOpg6"]
        },
        "Semangat Banget": {
            "emo": "🤩", "pesan": "Energi Ara nular ke Mas nih! Semangat terus ya Sayang!",
            "lagu": ["https://youtu.be/-LmRyAInlV8?si=fTKm1n2h1dc8MFuR"]
        },
        "Kangen Mas Levi": {
            "emo": "🥺", "pesan": "Sabar ya Sayang, btw lagu ini ngegambarin first impression mas ke kamu saat SMP. I miss you so much!",
            "lagu": ["https://youtu.be/wGdj-ic0cl8?si=dv7s-5IgoLcgf36K"]
        },
        "Makin Cinta Mas Levi": {
            "emo": "😍", "pesan": "Aduh, Mas jadi melting... Mas juga makin cinta sama Ara! Terima kasih sudah jadi pacar terbaik.",
            "lagu": ["https://www.youtube.com/watch?v=dElRVQFqj-k&list=RDdElRVQFqj-k&start_radio=1&pp=ygUJTUFSUlkgWU9VoAcB"]
        }
    }

    # LOGIKA TOMBOL
    if 'selected_mood' not in st.session_state:
        st.session_state.selected_mood = None

    cols = st.columns(5)
    idx = 0
    for mood_name, info in data_mood.items():
        if cols[idx % 5].button(info["emo"], help=mood_name):
            st.session_state.selected_mood = mood_name
        idx += 1

    if st.session_state.selected_mood:
        m = st.session_state.selected_mood
        st.write("---")
        st.subheader(f"Mood Ara hari ini: **{m}**")
        st.info(data_mood[m]["pesan"])
        st.video(data_mood[m]["lagu"][0])

    if st.button("Sapa Mas Levi 🐱"):
        st.toast("Meong! Mas Levi selalu sayang Ara! 🐾", icon="🐱")

with tab2:
    st.subheader("Galeri Kenangan Kita 📸")
    st.write("Setiap detik bersamamu adalah cerita favorit Mas.")
    st.success("Mari buat lebih banyak kenangan indah lagi!")

with tab3:
    st.subheader("Dating Quiz 🐧❤️")
    if 'skor' not in st.session_state: st.session_state.skor = 0
    st.write(f"Skor kamu: {st.session_state.skor}")
    if st.button("Main Lagi"):
        st.session_state.skor = 0
        st.rerun()

with tab4:
    st.subheader("Ruang Curhat")
    curhat = st.text_area("Tulis ceritamu di sini:")
    if st.button("Kirim ke Mas"):
        if curhat:
            st.balloons()
            model = genai.GenerativeModel('gemini-flash-latest')
            response = model.generate_content(f"Ara curhat: {curhat}. Beri respon romantis dan lucu sebagai pacar.")
            st.write(response.text)
        else:
            st.warning("Jangan lupa tulis curhatannya dulu ya, Sayang.")
