import streamlit as st
import time
import google.generativeai as genai

# Memanggil kunci dari Secrets yang baru kamu simpan
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Pengaturan Halaman
st.set_page_config(page_title="Untuk Ara Tersayang 💖", page_icon="💖")

st.title("Halo Ara Tersayang! 💖")
st.write("Meskipun aku lagi sibuk akademik, web ini dibuat khusus biar kamu merasa tetap ditemani.")

# Sidebar Navigasi
page = st.sidebar.radio("Pilih Menu:", ["Beranda & Mood", "Ruang Memori", "Area Main (Dating Quiz)", "Sini Curhat Ara Sayang"])

# --- BERANDA & MOOD ---
if page == "Beranda & Mood":
    st.subheader("Mood Tracker 🌈")
    st.write("Ceritakan perasaanmu hari ini, biar Mas bisa kasih 'obat' penenang atau penyemangat!")
    
    mood = st.select_slider("Ara lagi ngerasa apa hari ini?", options=["Sedih", "Capek/Lelah", "Biasa", "Lagi Berbunga", "Jatuh Cinta"])
    
    # Daftar referensi lagu (bisa ditambah sesuka hati!)
    playlist = {
        "Sedih": ["https://youtu.be/Xct1EdyHMWw", "https://youtu.be/k2q_qTm08_s"],
        "Capek/Lelah": ["https://youtu.be/T4cdfRohhcg", "https://youtu.be/L8eRzOp09jA"],
        "Biasa": ["https://youtu.be/dQw4w9WgXcQ", "https://youtu.be/e-ORhEE9VVg"],
        "Lagi Berbunga": ["https://youtu.be/QJO3ROT-A4E", "https://youtu.be/n4RjJKxsamQ"],
        "Jatuh Cinta": ["https://youtu.be/QJO3ROT-A4E", "https://youtu.be/C0DPdy98e4c"]
    }

    st.write(f"Mood kamu hari ini: **{mood}**")
    
    # Area Support System
    if mood == "Sedih":
        st.error("Ya ampun, Ara sayang... Sini Mas peluk jauh dulu. Jangan sedih lama-lama ya? Mas selalu ada buat dengerin Ara.")
        pilihan_lagu = st.selectbox("Mau dengerin lagu apa buat nenangin hati?", playlist["Sedih"])
        st.video(pilihan_lagu)
        
    elif mood == "Capek/Lelah":
        st.warning("Mas tahu Ara lagi berjuang keras. Istirahat ya? Inget, Mas bangga banget sama Ara yang hebat ini. Tarik napas dulu...")
        pilihan_lagu = st.selectbox("Lagu buat nemenin istirahat:", playlist["Capek/Lelah"])
        st.video(pilihan_lagu)
        
    elif mood == "Biasa":
        st.info("Apapun kegiatannya, semangat ya Sayang! Mas yakin Ara bisa ngelewatin hari ini dengan keren.")
        pilihan_lagu = st.selectbox("Lagu penyemangat:", playlist["Biasa"])
        st.video(pilihan_lagu)
        
    elif mood == "Lagi Berbunga" or mood == "Jatuh Cinta":
        st.balloons()
        st.success("Duh, senangnya liat Ara bahagia! Mas jadi ikut senyum. Mas makin sayang deh!")
        pilihan_lagu = st.selectbox("Lagu buat ngerayain kebahagiaan Ara:", playlist[mood])
        st.video(pilihan_lagu)

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
    
    # Inisialisasi status kuis
    if 'soal_ke' not in st.session_state:
        st.session_state.soal_ke = 1
        st.session_state.skor = 0

    soal_list = [
        {"id": 1, "tanya": "Di mana tempat pertama kali kita bertemu?", "pilihan": ["Perpustakaan", "Kantin", "UKS", "Lapangan Olahraga"], "jawab": "UKS"},
        {"id": 2, "tanya": "Waktu di UKS, kita itu kelas berapa SMP?", "pilihan": ["1", "2", "3", "Sudah SMA"], "jawab": "3"},
        {"id": 3, "tanya": "Apa yang aku tumpahin pas pertama ketemu?", "pilihan": ["Es Jeruk", "Teh", "Air Putih", "Kopi"], "jawab": "Teh"},
        {"id": 4, "tanya": "Berapa tahun kita sempat lost contact dari SMP sampai SMA?", "pilihan": ["1", "2", "3", "4"], "jawab": "3"},
        {"id": 5, "tanya": "Kapan aku menghubungi kamu lagi?", "pilihan": ["Awal kuliah", "Saat SMA", "Pas liburan", "Belum pernah"], "jawab": "Saat SMA"},
        {"id": 6, "tanya": "Berapa tahun kita LDR?", "pilihan": ["1", "2", "3", "5"], "jawab": "2"},
        {"id": 7, "tanya": "Siapa nama kucingku?", "pilihan": ["Badrul", "Badroel", "Kiko", "Moli"], "jawab": "Badrul"},
        {"id": 8, "tanya": "Warna apa yang paling aku suka?", "pilihan": ["Merah", "Biru", "Hitam", "Putih"], "jawab": "Biru"},
        {"id": 9, "tanya": "Total berapa saudara yang aku punya?", "pilihan": ["5", "6", "7", "8"], "jawab": "7"},
        {"id": 10, "tanya": "Siapa nama kakak tengahku?", "pilihan": ["Kak Sheila", "Kak Nur", "Kak Hilda"], "jawab": "Kak Nur"}
    ]

    if st.session_state.soal_ke <= 10:
        soal = soal_list[st.session_state.soal_ke - 1]
        st.write(f"### Pertanyaan {soal['id']} dari 10")
        jawaban = st.radio(soal['tanya'], soal['pilihan'], key=f"q{soal['id']}")
        
        if st.button("Lanjut Swipe >>"):
            if jawaban == soal['jawab']:
                st.session_state.skor += 1
                st.balloons() # Balon terbang setiap jawaban benar
                st.toast("Jawaban Benar! Kamu keren banget! 🐧✨", icon="✅")
            else:
                st.toast("Salah sedikit, tapi Mas tetap sayang kok! ❤️", icon="❌") # Efek silang
            
            # Beri jeda sedikit agar efek terlihat sebelum pindah soal
            import time
            time.sleep(1) 
            
            st.session_state.soal_ke += 1
            st.rerun()
    else:
        # Hasil Akhir
        st.write("## Kuis Selesai! 🎉")
        st.write(f"Skor akhir kamu: {st.session_state.skor}/10")
        
        # Efek Pinguin jika skor sempurna
        if st.session_state.skor == 10:
            st.snow()
            st.markdown(
                """<style>.stSnowflake::after {content: '🐧' !important; font-size: 3rem;}</style>""",
                unsafe_allow_html=True
            )
            st.success("Sempurna! Kamu emang paling kenal Mas! ❤️🐧")
        
        if st.button("Main Lagi?"):
            st.session_state.soal_ke = 1
            st.session_state.skor = 0
            st.rerun()

# --- SINI CURHAT ARA SAYANG ---
if page == "Beranda & Mood":
    st.subheader("Beranda")
    # ... isi kodingan beranda ...

elif page == "Ruang Memori":
    st.subheader("Ruang Memori")
    # ... isi kodingan memori ...

elif page == "Area Main (Dating Quiz)":
    st.subheader("Dating Quiz")
    # ... isi kodingan kuis ...

elif page == "Sini Curhat Ara Sayang":
    st.subheader("Ruang Akademik & Curhat 💬")
    st.write("Ceritakan apa saja yang Ara rasain hari ini.")
    
    curhat = st.text_area("Tulis curhatan atau keluh kesah Ara di sini:")
    
    if st.button("Kirim Cerita"):
        if curhat:
            with st.chat_message("user"):
                st.write(curhat)
            
            with st.status("Mas lagi baca curhatan Ara... 💭", expanded=True) as status:
                try:
                    # Pastikan variabel prompt berada di sini, di dalam blok try
                    # Kita pakai model yang pasti ada di daftar kamu
                    model = genai.GenerativeModel('gemini-flash-latest')
                    prompt = (
                        "Kamu adalah pacar AI untuk Ara. Gaya bicaramu harus: "
                        "1. Tidak formal sama sekali (gunakan 'Mas', 'Ara', 'Sayang', 'Wkwkwk'). "
                        "2. Sangat akrab, kocak, aneh, dan random. "
                        "3. Kalau Ara cerita aneh-aneh, responlah dengan antusias. "
                        "4. Selipkan alasan kenapa Mas agak lambat balasnya: 'Sorry ya Sayang, Mas lagi sibuk banget nih buat masa depan kita berdua'. "
                        "5. Tetap romantis di akhir jawaban, bikin Ara merasa selalu ada yang nemenin. "
                        f"Ara sedang curhat: {curhat}. "
                        "Berikan jawaban yang seru, bikin dia ketawa, tapi tetap bikin dia merasa disayang."
                    )
                    
                    response = model.generate_content(prompt)
                    status.update(label="Mas sudah selesai baca & ngetik! ✨", state="complete")
                    
                    with st.chat_message("assistant", avatar="❤️"):
                        st.write(response.text)
                
                except Exception as e:
                    status.update(label="Aduh, Mas ada kendala...", state="error")
                    if "429" in str(e):
                        st.warning("Sayang, Mas lagi kecapean nih kuotanya habis buat hari ini. Kita lanjut ngobrol nanti ya? Mas sayang Ara banget kok! 🥺")
                    else:
                        st.error(f"Error detail: {e}")
        else:
            st.warning("Jangan lupa tulis curhatannya dulu ya, Sayang. Mas nungguin nih... 🌸")
