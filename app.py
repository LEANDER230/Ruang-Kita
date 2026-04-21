import streamlit as st
import time

# Pengaturan Halaman
st.set_page_config(page_title="Untuk Ara Tersayang 💖", page_icon="💖")

st.title("Halo Ara Tersayang! 💖")
st.write("Meskipun aku lagi sibuk akademik, web ini dibuat khusus biar kamu merasa tetap ditemani.")

# Sidebar Navigasi
page = st.sidebar.radio("Pilih Menu:", ["Beranda & Mood", "Ruang Memori", "Area Main (Dating Quiz)", "Academic Buddy & Curhat"])

# --- BERANDA & MOOD ---
if page == "Beranda & Mood":
    st.subheader("Mood Tracker")
    mood = st.select_slider("Gimana perasaan Ara hari ini?", options=["Sedih", "Biasa", "Senang", "Berbunga-bunga"])
    
    if mood == "Sedih":
        st.write("Sini peluk jauh dulu untuk Ara! 🫂. Dengerin lagu ini ya, biar lebih tenang:")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Ganti dengan link lagu favorit kalian
    elif mood == "Berbunga-bunga":
        st.balloons()
        st.success("Senang banget dengarnya! Senyum Ara itu semangatku.")

# --- RUANG MEMORI ---
elif page == "Ruang Memori":
    st.subheader("Galeri Kenangan Kita")
    st.write("Klik untuk melihat momen berharga kita:")
    
    # Contoh slider/carousel sederhana
    if st.button("Lihat Foto Kenangan"):
        st.image("https://via.placeholder.com/600x400", caption="Momen di suatu tempat spesial") # Ganti URL foto kamu
        st.info("Ingat gak waktu kita di sini? Aku ingat betapa cantiknya Ara hari itu.")

# --- AREA MAIN ---
elif page == "Area Main (Dating Quiz)":
    st.subheader("Dating Quiz: Seberapa kenal kita?")
    answer = st.text_input("Di mana tempat pertama kali kita makan bareng?")
    if st.button("Cek Jawaban"):
        if answer.lower() == "restoran x": # Ganti dengan jawaban yang benar
            st.success("Bener banget! Kamu ingat hal sekecil itu, makasih ya Ara.")
        else:
            st.error("Hampir! Coba ingat-ingat lagi waktu itu kamu pakai baju warna apa...")

# --- ACADEMIC BUDDY & CURHAT ---
elif page == "Academic Buddy & Curhat":
    st.subheader("Ruang Akademik & Curhat")
    st.write("Status Aku: Lagi fokus ngerjain tugas akademik biar cepet kelar dan bisa main sama Ara!")
    
    pesan = st.text_area("Tulis pesan buat aku di sini, nanti aku baca pas istirahat ya:")
    if st.button("Kirim Pesan"):
        st.success("Pesan Ara sudah masuk ke hatiku! Aku pasti baca nanti.")
    
    st.write("---")
    st.write("Ara, makasih ya sudah sabar nungguin aku. Semangat juga buat harimu!")
