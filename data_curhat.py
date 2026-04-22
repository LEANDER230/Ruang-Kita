import random

# Daftar kata kunci yang luas untuk mendeteksi curhatan Ara
KEYWORDS = {
    "sedih": ["sedih", "nangis", "galau", "kecewa", "sakit hati", "menangis", "pedih", "sendirian", "nyesek", "hancur", "terluka", "suram", "down", "tangis"],
    "senang": ["senang", "happy", "seneng", "bahagia", "seru", "bangga", "asik", "keren", "berhasil", "menang", "sukses", "gembira", "tawa", "ketawa", "lucu"],
    "lelah": ["lelah", "capek", "penat", "ngantuk", "bosan", "jenuh", "kurang tidur", "pusing", "berat", "letih", "ngos-ngosan", "lemes", "mengantuk"],
    "tugas": ["tugas", "deadline", "ujian", "revisi", "pr", "kuliah", "sekolah", "presentasi", "laporan", "skripsi", "bab", "dosen", "sidang", "makalah", "praktikum", "abstrak"],
    "marah": ["marah", "emosi", "kesal", "sebal", "dendam", "jengkel", "berantem", "adu", "ngamuk", "badmood", "bete"],
    "kangen": ["kangen", "rindu", "pengen ketemu", "kangen banget", "kangen ya", "kangen kamu", "kangen mas"],
    "makan": ["lapar", "makan", "laper", "belum makan", "pengen makan", "jajan", "lapar sekali", "haus", "lapar"],
    "takut": ["takut", "cemas", "khawatir", "panik", "deg-degan", "ngeri", "takut banget", "was-was", "gugup"],
    "bingung": ["bingung", "pusing", "gak tahu", "apa ya", "buntu", "bingung banget", "gak ngerti", "mikir"],
    "cinta": ["cinta", "sayang", "rindu", "suka", "pacar", "hubungan", "kita", "kamu", "romantis", "doi"],
    "sehat": ["sakit", "demam", "flu", "pusing", "obat", "dokter", "nggak enak badan", "kurang sehat", "batuk", "pilek"],
    "waktu": ["hari ini", "tadi", "besok", "nanti", "malam", "pagi", "sibuk", "tunggu", "jam"],
    "keuangan": ["duit", "uang", "hemat", "boros", "nabung", "harga", "mahal", "murah", "bayar"]
}

# Template balasan (Setiap kategori punya 5 variasi dasar, silakan tambah sendiri hingga 100 per kategori)
RESPONSES = {
    "sedih": ["Ara sayang, jangan sedih ya... Sini Mas peluk virtual. ❤️", "Cup cup sayang... tumpahin aja ya nangisnya.", "Mas sedih kalau lihat Ara sedih. Semangat ya!", "Apapun yang bikin Ara sedih, nanti pasti berlalu kok.", "Mas selalu ada di sini buat dengerin Ara, jangan dipendam sendiri."],
    "senang": ["Wah, beneran? Mas ikut seneng banget dengernya!", "Alhamdulillah! Ara emang paling hebat. Ayo rayain!", "Seneng banget dengernya! Ara deserve bahagia selalu.", "Mood Mas langsung naik denger kabar baik dari Ara.", "Yes! Itu baru pacar Mas! Bangga banget!"],
    "lelah": ["Sayang, jangan diforsir ya. Istirahat dulu, Mas sayang Ara! 🐧", "Mas ngerti capeknya Ara. Tarik napas, minum air ya.", "Duh, pacar Mas capek ya? Sini, istirahat dulu.", "Rehat sejenak ya, Sayang. Kesehatan Ara nomor satu.", "Udah cukup ya buat hari ini. Mas mau Ara tidur nyenyak."],
    "tugas": ["Semangat ngerjain tugasnya! Mas percaya Ara bisa.", "Dikit lagi selesai kok! Jangan lupa makan ya.", "Tugas emang kadang jahat, tapi Ara jauh lebih hebat!", "Fokus ya! Mas tahu Ara orangnya detail dan teliti.", "Jangan begadang terus ya sayang! Kesehatan tetap nomor satu."],
    "marah": ["Waduh, ada yang lagi emosi ya? Sini, tenangin diri dulu.", "Jahat banget sih yang bikin Ara marah, sini cerita sama Mas.", "Taruh dulu HP-nya, ambil napas dalam-dalam. Mas di sini buat Ara."],
    "kangen": ["Mas juga kangen banget! Cepet ketemu yuk.", "Duh, nunggu ketemu Ara tuh berasa lama banget.", "Kangennya disimpan dulu ya, nanti kalau ketemu Mas kasih banyak peluk."],
    "makan": ["Udah makan belum? Jangan telat ya, nanti sakit Mas sedih.", "Makan yang enak ya sayang! Butuh energi buat jadi pacar Mas.", "Lagi pengen makan apa? Kalau deket pasti Mas beliin."],
    "takut": ["Jangan takut ya, ada Mas di sini yang jagain Ara.", "Apa yang bikin Ara takut? Ceritain ke Mas, kita hadapin bareng.", "Ara berani kok, jangan dengerin pikiran negatifnya ya."],
    "bingung": ["Kadang hidup emang ribet, tapi Ara punya Mas buat bantu cari jalan.", "Bingung kenapa sayang? Ceritain pelan-pelan ya.", "Coba tarik napas, fokus satu-satu dulu ya."],
    "cinta": ["I love you, Ara! Makasih ya udah jadi bagian dari hari Mas.", "Ara orang paling berharga buat Mas. Selalu.", "Mas makin sayang deh kalau Ara cerita begini.", "Apapun situasinya, Ara tetap yang terbaik buat Mas.", "Mas selalu nunggu chat dari Ara, makasih ya udah nyapa."],
    "sehat": ["Minum obat ya sayang, istirahat yang cukup biar cepet sembuh.", "Duh, kalau sakit jangan dipaksain ya. Istirahat total dulu.", "Mas doain Ara cepet sembuh ya. I miss you, get well soon!"],
    "waktu": ["Apapun waktu yang Ara habisin, semoga selalu berkah ya.", "Mas selalu punya waktu kok buat dengerin Ara.", "Nanti kita ngobrol lebih banyak lagi ya kalau sudah luang."],
    "keuangan": ["Duh, atur budget pelan-pelan ya sayang. Mas percaya Ara bijak.", "Jangan terlalu boros ya, tapi jangan pelit juga ke diri sendiri."],
    "random": ["Tiba-tiba kepikiran Ara, eh Ara malah chat. Kita emang sehati ya! ❤️", "Apa pun yang Ara lakuin hari ini, Mas bangga banget.", "Mas lagi senyum-senyum sendiri nih pas baca chat dari Ara."]
}

def get_template_response(curhat):
    text = curhat.lower()
    for cat, keys in KEYWORDS.items():
        if any(k in text for k in keys):
            return random.choice(RESPONSES.get(cat, RESPONSES["random"]))
    return random.choice(RESPONSES["random"])
