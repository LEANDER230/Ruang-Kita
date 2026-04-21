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
    mood = st.select_slider("Sayang, hari ini perasaan kamu gimana?", options=["Sedih", "Biasa", "Jatuh Cinta"])
    
    st.write(f"Mood kamu hari ini: **{mood}**")

    if mood == "Sedih":
        st.write("Sini, Mas peluk jauh dulu buat Ara sayang. Dengerin lagu ini ya, biar Ara merasa aman:")
        st.video("https://youtu.be/Xct1EdyHMWw?list=RDXct1EdyHMWw") 
        
    elif mood == "Biasa":
        st.write("Apapun kegiatannya, semangat ya Sayang! Mas selalu ada di sini buat Ara.")
        st.video("https://youtu.be/T4cdfRohhcg?si=SJfApY0UgwCeb9Yd")
        
    elif mood == "Jatuh Cinta":
        st.balloons()
        st.write("Duh, senangnya liat Ara lagi bahagia! Mas jadi ikut senyum. Ini lagu khusus buat kamu, sesuai lagunya, bikin keinget saat kita ketemu di UKS")
        st.video("https://youtu.be/QJO3ROT-A4E?si=jSnmxDqbiBlBsY9e")

# --- RUANG MEMORI ---
elif page == "Ruang Memori":
    st.subheader("Galeri Kenangan Kita")
    st.write("Momen-momen indah kita, Sayang:")

    # Masukkan "Direct link" dari PostImages tadi di sini
    link_foto1 = C:\Users\user\Downloads\US\03.jpeg"
    link_foto2 = "C:\Users\user\Downloads\US\02.JPG"

    # Menampilkan fotonya
    st.image("C:\Users\user\Downloads\US\04.jpeg", caption="Momen pas kita lagi senang banget")
    st.info("Ingat gak waktu ini? Mas ingat banget betapa cantiknya Ara hari itu.")
    
    st.image("C:\Users\user\Downloads\US\01.JPG", caption="Satu lagi kenangan manis kita")

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
