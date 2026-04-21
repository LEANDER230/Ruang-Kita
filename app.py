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
        {"url": "https://i.imgur.com/BIl7U24.jpeg", "caption": "Akhirnya Almet ku dipakai kamuuuu!!!"},
        {"url": "https://i.imgur.com/K5aKkhY.jpeg","caption": "KARCIS PARKIR SAMA KAMU KAN BY???!!!"},
        {"url": "https://i.imgur.com/UPVe97I.jpeg", "caption": "Infokan Blok M, maniesss!"},
        {"url": "https://i.imgur.com/9L0eCBA.jpeg", "caption": "Eh ada cogan Unair nih!!!"},
        {"url": "https://i.imgur.com/i7lzkUr.jpeg", "caption": "Hai kakak cantik UAI!!!"},
        {"url": "https://i.imgur.com/DhfbMSS.jpeg", "caption": "LUCUU AMAT PACAR GUAAAA"},
        {"url": "https://i.imgur.com/L1F74YZ.jpeg", "caption": "ALOOO DUNIAAAA"},
        {"url": "https://i.imgur.com/fj4Lf8c.jpeg", "caption": "BAIK BAIK YA DUNIA SAMA KAMIII"},
        {"url": "https://i.imgur.com/NbtWNbM.jpeg", "caption": "RESMI MENAMATKAN PHOTOBOOTH DI KBM WKWKWK"},
        {"url": "https://i.imgur.com/MTdk9zT.jpeg", "caption": "Lucu banget bentuk mata kitaaa"},
        {"url": "https://i.imgur.com/SHksTlD.jpeg", "caption": "Ara sayangggg kok senyum mu manis bangetttt"},
        {"url": "https://i.imgur.com/ezNgaLe.jpeg", "caption": "Ngedateee nih ceritanya hihihi"},
        {"url": "https://i.imgur.com/7VSIsW6.jpeg", "caption": "Uhuk UHuk UHuk salting liatnyaaa"},
        {"url": "https://i.imgur.com/rf3wShK.jpeg", "caption": "Kaget yaa minum ku cepettt"},
        {"url": "https://i.imgur.com/3KN3ujI.jpeg", "caption": "LUCUU NIATNYA MAU BELI SEPATU MALAH KEJEBAK DUDUK DI KBC WKWKWK"},
        {"url": "https://i.imgur.com/nqWgqUd.jpeg", "caption": "Anak-Anak kita lucuuu bangetttt"},
        {"url": "https://i.imgur.com/9I9GlB4.jpeg", "caption": "Manisnya anak-anak semanis senyum Ibu dan Ayahnya yaa"},
        {"url": "https://i.imgur.com/ZBd6Y9o.jpeg", "caption": "Nanti kita foto bareng Puyoo, Petantang-Petenteng, dan Mola yaaa"},
        {"url": "https://i.imgur.com/czZYo93.jpeg", "caption": "Cieee berangkat bawa air, pulang sama anak Unair"},
        {"url": "https://i.imgur.com/5Cn0CV9.jpeg", "caption": "Ayooo buat cerita seru lainnya lagiii"},
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
    st.subheader("Dating Quiz: Seberapa kenal kita? 🐧❤️")
    st.write("Coba tes ingatan kamu tentang perjalanan cerita kita dan keluargaku, Sayang!")
    st.markdown("---")

    # Daftar soal-soal (Sama seperti sebelumnya, total 10 soal)
    # ... (kode soal q1-q10 sama seperti sebelumnya) ...
    
    # 1. Soal Pertemuan
    q1 = st.radio("Di mana tempat pertama kali kita bertemu?", ["Perpustakaan", "Kantin", "UKS", "Lapangan Olahraga"])
    
    # 2. Soal Kelas
    q2 = st.text_input("Waktu kita ketemu di UKS, kita itu kelas berapa SMP sih?")

    # 3. Soal Teh
    q3 = st.radio("Apa yang aku tumpahin pas pertama ketemu kamu?", ["Es Jeruk", "Teh", "Air Putih", "Kopi"])

    # 4. Soal Lost Contact
    q4 = st.text_input("Berapa tahun kita sempat lost contact dari SMP sampai SMA?")

    # 5. Soal Menghubungi Kembali
    q5 = st.radio("Kapan aku menghubungi kamu lagi setelah sekian lama?", ["Saat awal kuliah", "Saat SMA", "Pas liburan", "Enggak pernah"])

    # 6. Soal LDR
    q6 = st.text_input("Berapa tahun kita menjalani LDR (Long Distance Relationship)?")

    # 7. Soal Nama Kucing
    q7 = st.text_input("Siapa nama kucing kesayanganku?")

    # 8. Soal Warna Favorit
    q8 = st.text_input("Warna apa sih yang paling aku suka?")

    # 9. Soal Total Saudara
    q9 = st.text_input("Total berapa saudara yang aku punya?")
    
    # 10. Soal Nama Kakak Tengah
    q10 = st.radio("Siapa nama kakak tengah aku?", ["Kak Sheila", "Kak Nur", "Kak Hilda"])

    if st.button("Cek Semua Jawaban"):
        score = 0
        
        # Logika Penilaian (Total 10 soal)
        if q1 == "UKS": score += 1
        if q2.strip() == "3": score += 1
        if q3 == "Teh": score += 1
        if q4.strip() == "3": score += 1
        if q5 == "Saat SMA": score += 1
        if q6.strip() == "2": score += 1
        if q7.lower().strip() == "Badroel": score += 1
        if q8.lower().strip() == "Biru": score += 1
        if q9.strip() == "7": score += 1
        if q10 == "Kak Nur": score += 1

        # TAMPILAN HASIL & EFEK PINGUIN
        st.markdown("---")
        
        if score == 10:
            # === TRIK EFEK PINGUIN ===
            # Kita pakai st.snow() tapi kita ubah gambarnya jadi emoji pinguin
            st.snow() 
            st.balloons() # Tambahin balon juga biar rame!
            
            # CSS untuk mengubah partikel salju menjadi pinguin
            st.markdown(
                """
                <style>
                .stSnowflake {
                    font-size: 3rem !important;
                }
                .stSnowflake::after {
                    content: '🐧' !important; 
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            
            st.success("Waaa! Kamu benar-benar pasangan yang paling perhatian! Skor 10/10 buat kamu! ❤️")
            st.write("Tuh, lihat! Puyooo ikut ngerayain kemenangan kamu, Ara! 🐧✨")
            
        elif score >= 7:
            st.info(f"Skor kamu {score}/10. Wah, kamu benar-benar ingat banyak hal penting tentang hidupku.")
        else:
            st.error(f"Skor kamu {score}/10. Tidak apa-apa, yang penting kita terus bikin memori bareng ya! 😉")

# --- ACADEMIC BUDDY & CURHAT ---
elif page == "Academic Buddy & Curhat":
    st.subheader("Ruang Akademik & Curhat")
    st.write("Status Aku: Lagi fokus ngerjain tugas akademik biar cepet kelar dan bisa main sama Ara!")
    
    pesan = st.text_area("Tulis pesan buat aku di sini, nanti aku baca pas istirahat ya:")
    if st.button("Kirim Pesan"):
        st.success("Pesan Ara sudah masuk ke hatiku! Aku pasti baca nanti.")
    
    st.write("---")
    st.write("Ara, makasih ya sudah sabar nungguin aku. Semangat juga buat harimu!")
