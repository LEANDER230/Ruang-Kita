import time
import streamlit as st
import data_curhat
import random
import google.generativeai as genai
import time
SAPAAN_MAS_LEVI = [
    "Meong! Mas Levi selalu sayang Ara! 🐾",
    "Meong! Mas Levi kangen Ara banget! 🐾",
    "Meong! Mas Levi cinta Ara selamanya! 🐾",
    "Meong! Ara adalah pacar terbaik Mas Levi! 💖"
]

GIF_MAS_LEVI = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzM5YmNrYmxhZ3djMHV3ZGN3eTByejlhb2duaXM4emZtaHNmaTNqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aKSTkz8Wph5WHrBJgy/giphy.gif"

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Untuk Ara Tersayang 💖", layout="centered")

# 2. CSS CUSTOM
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
    
    /* Font dan Warna Teks Utama */
    html, body, [class*="css"], .stMarkdown, .stText, div, p { 
        font-family: 'Fredoka One', cursive !important; 
        color: #023E8A !important; /* Biru gelap yang lembut, bukan hitam */
    }
    
    /* Background Utama (Biru Sangat Muda/Pastel) */
    .stApp { background-color: #E0F7FA !important; }
    
    /* Tab List */
    div[data-baseweb="tab-list"] { 
        background-color: #89C2D9 !important; 
        border-radius: 20px; 
        padding: 10px; 
    }
    div[data-baseweb="tab"] { color: #023E8A !important; }
    
    /* Tombol */
    div.stButton > button { 
        background-color: #89C2D9 !important; 
        color: #023E8A !important; 
        border-radius: 25px !important;
        border: 2px solid #023E8A !important;
    }
    div.stButton > button:hover { background-color: #A3D5EA !important; }
    
    /* Selectbox (Dropdown) */
    div[data-baseweb="select"] > div {
        background-color: #89C2D9 !important;
        border: 2px solid #023E8A !important;
        color: #023E8A !important;
        border-radius: 25px !important;
    }
    div[data-baseweb="select"] svg { fill: #023E8A !important; }
    div[role="listbox"] { background-color: #89C2D9 !important; }
    div[role="option"] { color: #023E8A !important; }

    /* Kotak Chat/Respon */
    div[data-testid="stChatMessage"] {
        background-color: #BDE0FE !important; /* Biru muda cerah */
        border-radius: 15px !important;
        padding: 15px !important;
        border: 2px solid #89C2D9 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. KONFIGURASI API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 4. JUDUL
st.title("Halo Ara Tersayang! 💖")

if st.button("Sapa Mas Levi 🐱"):
    # 1. Pilih kalimat & Toast
    kalimat = random.choice(SAPAAN_MAS_LEVI)
    st.toast(kalimat, icon="🐱")
    
    # 2. Buat container untuk SEMUANYA (GIF + Audio)
    placeholder_konten = st.empty()
    
    # 3. Masukkan gambar dan audio ke dalam container tersebut
    with placeholder_konten.container():
        st.image(GIF_MAS_LEVI, width=200)
        st.audio("suara_levi.mp3", format="audio/mp3", autoplay=True)
    
    # 4. Tunggu 5 detik, lalu hapus SEMUANYA
    time.sleep(5)
    placeholder_konten.empty()
    
# 5. MENU TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌈 Mood", "📸 Memori", "🐧 Kuis", "💬 Curhat", "Puyo 🐧"])

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

with tab2:
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

with tab3:
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

with tab4:
    st.subheader("Ruang Akademik & Curhat 💬")
    st.write("Ceritakan apa saja yang Ara rasain hari ini.")
    
    curhat = st.text_area("Tulis curhatan atau keluh kesah Ara di sini:")
    
    # Fungsi Rotasi API Key agar tidak kena limit
    def get_model():
        if 'key_index' not in st.session_state:
            st.session_state.key_index = 1
        
        # Coba sampai 10 key yang sudah kamu setting
        for _ in range(3):
            try:
                key_name = f"GOOGLE_API_KEY_{st.session_state.key_index}"
                genai.configure(api_key=st.secrets[key_name])
                return genai.GenerativeModel('gemini-1.5-flash')
            except:
                st.session_state.key_index = (st.session_state.key_index % 3) + 1
        return None

    if st.button("Kirim Cerita"):
        if curhat:
            with st.chat_message("user"):
                st.write(curhat)
            
            # --- LOGIKA TAMBAHAN ---
            jawaban_template = data_curhat.get_template_response(curhat)
            
            if jawaban_template:
                with st.chat_message("assistant", avatar="❤️"):
                    st.write(jawaban_template)
            else:
                # --- KODE ASLI KAMU MULAI DARI SINI ---
                with st.status("Mas lagi baca curhatan Ara... 💭", expanded=True) as status:
                    try:
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
                # --- KODE ASLI KAMU SELESAI ---
        else:
            st.warning("Jangan lupa tulis curhatannya dulu ya, Sayang. Mas nungguin nih... 🌸")

with tab5:
    st.subheader("🐧 Tamagotchi Puyo: Survival Mission")

    # 1. INISIALISASI
    defaults = {
        'health': 100, 'xp': 0, 'level': 1, 'lapar': 0, 'bosan': 0, 
        'kotor': 0, 'pintar': 0, 'sakit': False, 'dead': False,
        'puyo_image': "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eGIwdzdpNHB4MjZhamxrbmNjMjdnbDlzbXkzaGo3d3pldnBwems0YiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/llbukyWUS3u7OLRMkh/giphy.gif"
    }
    for key, value in defaults.items():
        if key not in st.session_state: st.session_state[key] = value

    gif_map = {
        "Makan": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmsyeGZkcWx6bHYyYnYwNTFjY2E0M25qN3p0N3M4dGdyMnBvMTJrcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/nJ0gVNNt7jo0ZhRh0l/giphy.gif",
        "Main": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3anFwNmljYnczYzlsYWp5N29wMDg0eXY1dm8ydjdnb2MyOTQ3aThrMSZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/4aLv4k0EB4aRy1RL1n/giphy.gif",
        "Bobo": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NWYzcmdleTV3dTA5MWV3NjExbnV0eWltcDMycHp1MHgxbjAxNXFoMCZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/5TSmLaEK7arBLptvGP/giphy.gif",
        "Mandi": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmRjZmRsbnc2YXg1MW9xN2M3d3NvcGdlN2Q5dDlyNWhmdWdxcXpncCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/uRcYNX7PaFuApTrYHs/giphy.gif",
        "Obat": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2VtdTczMXhsZXFkdXoyMnN0Y2FwMjMxOTJuMTFoY2hlaHoxY3UyeSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/EPNsCa5wJVLPWnCBf3/giphy.gif",
        "Belajar": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cjBmaTV0ZDl4eGN3eXp6N3pudmYxN203cjRkem01MzY0a2Vvam84NiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/8XMQXxCYanFL5QTHPG/giphy.gif",
        "Nyanyi": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Mm1zZnpmdmoydmJlMm1qZDgwNnN0ajJvYmM2eHpuYTh2Ymk1YWI0ZCZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/3ZJmUGKn3m5aK0LkfG/giphy.gif",
        "Lari": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MDBoY3l4eXJ5bzA4c29mZ3lxczZndGZ0MHkwZng1dGpwNXdiejZ2aiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/84gHL1mDKOLsQpIMcN/giphy.gif",
        "Gambar": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NmV2a29tZTBxY2I4MTd5eGtmbmlqaXQxMzA0NW5saDhoZTQ0aWxlciZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/qWCcogWJEkHQWH6xiC/giphy.gif",
        "Peluk": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dmkzcGt6ZGN1Z2k3bXNxODFpeGdhaHhtbHN0bnJjbTdhajc4Znk3MiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/MU26oatNJOBNCMOmDQ/giphy.gif"
    }

    # 2. FUNGSI LOGIKA
    def update_puyo(nama, h_c, xp_c, l_c, b_c, k_c, p_c, msg):
        if st.session_state.dead: return
        if st.session_state.sakit and nama != "Obat":
            st.toast("Puyo lemas! Kasih Obat dulu.", icon="🤒")
            return
        
        st.session_state.health = max(0, min(100, st.session_state.health + h_c))
        st.session_state.xp += xp_c
        st.session_state.lapar = max(0, min(100, st.session_state.lapar + l_c))
        st.session_state.bosan = max(0, min(100, st.session_state.bosan + b_c))
        st.session_state.kotor = max(0, min(100, st.session_state.kotor + k_c))
        st.session_state.pintar += p_c
        
        if st.session_state.health <= 0: st.session_state.dead = True
        if nama == "Obat": st.session_state.sakit = False
        if not st.session_state.sakit and random.random() < 0.05: st.session_state.sakit = True
        if st.session_state.xp >= 100 * st.session_state.level:
            st.session_state.level += 1
            st.balloons()
            
        st.session_state.puyo_image = gif_map.get(nama, st.session_state.puyo_image)
        st.info(f"{msg}")

    # 3. TAMPILAN
    if st.session_state.dead:
        st.error("💀 PUYO TELAH TIADA...")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZ4cDN4cDB4dDdzZzR4c3Z4Znp4eDdzZzR4c3Z4Znp4eDdzZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKRn6V9n45F7JLi/giphy.gif")
        if st.button("🔄 Hidupkan Kembali"):
            for key in defaults: st.session_state[key] = defaults[key]
            st.rerun()
    else:
        st.image(st.session_state.puyo_image, width=150)
        if st.session_state.lapar > 60: st.warning("⚠️ Puyo lapar! MAKAN!")
        if st.session_state.kotor > 50: st.error("💩 Puyo kotor! MANDI!")
        if st.session_state.sakit: st.error("🤒 Puyo SAKIT! OBAT!")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Lvl", st.session_state.level)
        c2.metric("XP", st.session_state.xp)
        c3.metric("Health", f"{st.session_state.health}%")
        c4.metric("Pintar", st.session_state.pintar)
        st.progress(st.session_state.health / 100)

        # 4. 10 TOMBOL
        data = [
            ("Makan", 5, 5, -30, 0, 0, 0, "Kenyang!"), ("Main", -2, 10, 5, -40, 0, 0, "Seru!"),
            ("Bobo", 10, 2, 5, 0, 0, 0, "Bobo.."), ("Mandi", 5, 0, 0, 0, -50, 0, "Wangi!"),
            ("Obat", 20, -5, 0, 0, 0, 0, "Sehat!"), ("Belajar", -5, 15, 5, 5, 0, 20, "Pintar!"),
            ("Nyanyi", 2, 8, 0, -20, 0, 0, "Merdu!"), ("Lari", -8, 12, 10, -50, 10, 0, "Sporty!"),
            ("Gambar", 1, 6, 0, -10, 0, 10, "Kreatif!"), ("Peluk", 3, 4, 0, 0, 0, 0, "Sayang!")
        ]
        for i in range(0, 10, 5):
            cols = st.columns(5)
            for j in range(5):
                if cols[j].button(data[i+j][0]):
                    update_puyo(*data[i+j])
                    st.rerun()

        # 5. MISI DINAMIS
        st.write("---")
        st.subheader("🎯 Misi Puyo")
        if st.session_state.pintar < 30: st.write("📖 **Belajar** biar Puyo makin pintar (Target 30).")
        if st.session_state.bosan > 40: st.write("🎶 **Nyanyi** atau **Main** agar tidak stress.")
        if st.session_state.kotor > 30: st.write("🧼 **Mandi** supaya Puyo bersih.")
        if st.session_state.health < 60: st.write("🏃 **Lari** & **Bobo** biar fit kembali.")
        if st.session_state.pintar >= 30 and st.session_state.bosan <= 20: st.success("🎉 Misi hari ini selesai!")
