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
    st.subheader("Galeri Kenangan Kita 📸")
    st.write("Setiap detik bersamamu adalah cerita yang ingin aku simpan selamanya, Ara.")
    st.markdown("---")

    # Daftar link foto (Pastikan semua link berakhiran .jpeg atau .jpg)
    # Mas bisa tambahkan link foto lainnya di dalam daftar ini
    galeri_foto = [
        {"url": "https://i.imgur.com/u0exoFO.jpeg", "caption": "Momen saat kita tertawa bersama"},
        {"url": "https://i.imgur.com/H8G4NgH.jpeg", "caption": "Kenangan yang tak akan pernah aku lupa"},
        {"url": "https://i.imgur.com/5HGCbWb.jpeg", "caption": "Ciee akhirnya bisa pegangan setelah 2 tahun"},
        {"url": "https://i.imgur.com/00gTVP7.jpeg", "caption": "Akhirnya kita foto bareng yaa setelah bertahun-tahun"},
        {"url": "https://i.imgur.com/Wbx5TPG.jpeg", "caption": "Yang dulu masih unyu-unyu SMP, eh udah Kuliah ajaa"},
        {"url": "https://i.imgur.com/UWeOE59.jpeg", "caption": "Eh apaa nihhh wkwwk, Muach Muach Muachhh!!!"},
        # Tambahkan foto ketiga, keempat, dst di bawah sini dengan format yang sama
    ]

    # Kita buat tampilan 2 kolom agar rapi (seperti bingkai)
    cols = st.columns(2)
    
    for i, item in enumerate(galeri_foto):
        with cols[i % 2]:
            # Menampilkan gambar dengan ukuran yang sama
            st.image(item["url"], caption=item["caption"], use_column_width=True)
            st.write("") # Memberi jarak antar foto

    st.markdown("---")
    st.subheader("Pesan untuk Ara")
    st.write("""
    Ara sayang,
    
    Melihat foto-foto ini mengingatkanku betapa beruntungnya aku memilikimu. 
    Terima kasih sudah menjadi bagian terindah dalam hari-hariku. 
    Meskipun aku sedang sibuk dengan akademik, ingatlah bahwa hatiku selalu ada di sampingmu.
    
    Aku mencintaimu hari ini, besok, dan seterusnya. ❤️
    """)
    
    st.success("Mari buat lebih banyak kenangan indah lagi di masa depan!")

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
