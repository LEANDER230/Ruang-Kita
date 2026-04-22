import streamlit as st
import time
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Untuk Ara Tersayang 💖", page_icon="💖", layout="wide")

# --- UI & CSS ROMANTIS (Pastel & Aesthetic) ---
st.markdown("""
<style>
    .stApp { background-color: #FFF9F9; } /* Putih Kemerah-merahan lembut */
    h1, h2, h3 { color: #FF7FA6 !important; font-family: 'Verdana', sans-serif; }
    
    /* Tombol Interaktif */
    div.stButton > button {
        background-color: #FFDEE9;
        border: 2px solid #FF7FA6;
        border-radius: 15px;
        transition: 0.3s;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #FF7FA6;
        color: white;
    }
    /* Kotak konten */
    .css-1r6slp0 { background-color: #FFFAFA; border-radius: 20px; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# Fungsi Setup AI
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- SIDEBAR (Satu saja agar tidak eror) ---
page = st.sidebar.radio("Pilih Menu:", ["Mood Kamu Hari Ini", "Ruang Memori", "Area Main (Dating Quiz)", "Sini Curhat Ara Sayang"])

# --- HEADER & VISUAL KUCING/PINGUIN ---
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2kwdnl6ZzZndm0xbWltbzF4M2h5Z3hwYWNtZGRoZ2pxNmh5N2Q4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xAFtqo0LiW3IIo/giphy.gif")
with col2:
    st.title("Halo Ara Tersayang! 💖")
    st.write("Dibuat khusus supaya Ara nggak kesepian pas Mas Levi lagi sibuk akademik.")
with col3:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzBuZTV4eW1sYnZ5d3k4d3J1cjVqNHJ4c3Z4Z3hwYWNtZGRoZ2pxNmh5N2Q4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpG3q1DkQ/giphy.gif")

# --- MOOD KAMU HARI INI ---
if page == "Mood Kamu Hari Ini":
    st.subheader("Mood Tracker 🌈")
    st.write("Klik emotikon yang paling menggambarkan perasaan Ara hari ini:")
    
    # DATABASE LENGKAP 10 MOOD
    data_mood = {
        "1. Sedih": {
            "emo": "😢", "pesan": "Sini Mas peluk jauh dulu... Jangan sedih lama-lama ya, Mas selalu ada buat dengerin Ara.",
            "lagu": ["https://youtu.be/QJO3ROT-A4E?si=e04SQFNZunkJ1Ejx"]
        },
        "2. Capek/Lelah": {
            "emo": "😫", "pesan": "Mas tahu Ara lagi berjuang keras. Istirahat ya? Mas bangga banget sama Ara yang hebat ini.",
            "lagu": ["https://youtu.be/T4cdfRohhcg?si=UReuklTRTXnXgFeOY"]
        },
        "3. Cemas/Gelisah": {
            "emo": "😰", "pesan": "Tarik napas dalam-dalam ya Sayang... Mas di sini, semuanya bakal baik-baik aja kok.",
            "lagu": ["https://youtu.be/Xct1EdyHMWw?si=pctatJhbgVTLsztH"]
        },
        "4. Galau": {
            "emo": "🙂", "pesan": "Lagi banyak pikiran ya? Cerita ke Mas yuk, jangan dipendem sendiri.",
            "lagu": ["https://youtu.be/Q04bUnPX8F8?si=OVVGqDXvP-ylv3Pq"]
        },
        "5. Biasa Aja": {
            "emo": "😐", "pesan": "Apapun kegiatannya, semangat ya Sayang! Mas yakin Ara bisa ngelewatin hari ini dengan KICAUUU.",
            "lagu": ["https://youtu.be/EaIrvHbYrLs?si=4XOY3LAJSQ9hViCP"]
        },
        "6. Butuh Motivasi": {
            "emo": "🔥", "pesan": "Ara itu hebat! Jangan lupa, Mas selalu dukung Ara dari sini. Gas pol!",
            "lagu": ["https://youtu.be/qvQwBd-uaJY"]
        },
        "7. Lagi Berbunga": {
            "emo": "🌸", "pesan": "Duh, senangnya liat Ara bahagia! Mas jadi ikut senyum liatnya.",
            "lagu": ["https://youtu.be/D-VytLhH-KE?si=LVR918kTKf1BOpg6"]
        },
        "8. Semangat Banget": {
            "emo": "🤩", "pesan": "Energi Ara nular ke Mas nih! Semangat terus ya Sayang!",
            "lagu": ["https://youtu.be/-LmRyAInlV8?si=fTKm1n2h1dc8MFuR"]
        },
        "9. Kangen Mas Levi": {
            "emo": "🥺", "pesan": "Sabar ya Sayang, btw lagu ini ngegambarin first impression mas ke kamu saat SMP. I miss you so much!",
            "lagu": ["https://youtu.be/wGdj-ic0cl8?si=dv7s-5IgoLcgf36K"]
        },
        "10. Makin Cinta Mas Levi": {
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
