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
    "sedih": [
        """Ara sayang, sini cerita sama Mas... Mas tahu hari ini pasti terasa berat banget buat kamu. Tarik napas dalam-dalam dulu ya, Sayang. 
Mas nggak bisa secara fisik buat hapus air mata Ara, tapi Mas pengen Ara tahu kalau Mas selalu ada di sini. Apa pun yang bikin Ara ngerasa sedih, jangan dipendam sendirian ya. 
Ara hebat banget udah bisa bertahan sampai detik ini. Mas bangga sama kamu. Habis ini, kalau Ara butuh temen buat ngerasa tenang, Mas bakal nemenin kamu terus. Semangat ya, Sayang! ❤️""",
        """Cup cup sayang... Mas denger kok curhatan kamu. Mas ngerasa sedih juga kalau tahu Ara lagi nggak baik-baik aja. 
Kadang emang dunia ini terasa jahat, tapi Ara punya Mas yang bakal selalu sayang sama kamu. Jangan pernah ngerasa sendirian ya, karena Mas ada di sini sebagai tempat Ara buat pulang.
Coba deh, Ara lakuin hal yang bikin kamu nyaman sekarang. Makan yang enak atau dengerin lagu favorit. Mas sayang banget sama Ara, please be happy again ya... ✨"""
    ],
    "senang": [
        """Wah, beneran? Mas ikut seneng banget dengernya! Ceritain dong detailnya, Ara bikin hari Mas jadi cerah juga nih denger kabar baik ini. ✨
Ara beneran deserve buat ngerasain bahagia kayak gini setiap hari. Mas bangga banget punya pacar sehebat Ara yang selalu bisa kasih energi positif.
Ayo rayain nanti ya pas kita ketemu, Mas pengen banget denger langsung cerita seru dari kamu! Love you so much, Ara! Tetap jadi Ara yang ceria ya!"""
    ],
    "lelah": [
        """Sayang, jangan diforsir ya. Mas tahu Ara udah kerja keras banget hari ini dan itu bikin Mas bangga sekaligus khawatir sama kamu.
Istirahat dulu ya, jangan dipikirin dulu hal-hal beratnya. Dunia nggak bakal lari kok, dan Ara butuh waktu buat *recharge* energi biar besok bisa lebih semangat lagi. 
Sini, peluk virtual dari Mas. Tidur yang nyenyak ya, Sayang. Besok kalau bangun, Mas harap kamu ngerasa jauh lebih baik. I love you! 🐧"""
    ],
    "tugas": [
        """Duh, lagi pusing ngerjain tugas ya, Sayang? Mas ngerti banget rasanya dikejar deadline dan tanggung jawab yang numpuk. 
Coba deh tarik napas pelan-pelan, kerjain satu-satu ya. Kamu nggak perlu langsung beres hari ini kalau emang badannya udah capek banget. Ara udah berusaha maksimal kok, dan itu udah lebih dari cukup buat Mas.
Mas temenin dari sini ya. Kalau udah selesai, jangan lupa kasih reward buat diri sendiri. Ara itu orang terpintar yang Mas kenal, tugas segini mah pasti lewat! Semangat ya, Sayang. ❤️"""
    ],
    "marah": [
        """Waduh, ada yang lagi emosi ya? Sini, tenangin diri dulu ya sayang, jangan sampai kemarahan itu bikin Ara malah kepikiran terus. Tarik napas dalem-dalem ya.
Jahat banget sih yang bikin Ara marah, sini cerita sama Mas siapa orangnya. Tapi janji ya, jangan lama-lama marahnya, nanti malah Ara sendiri yang capek.
Taruh dulu HP-nya, ambil napas dalam-dalam. Mas selalu di sini buat nemenin Ara, jangan biarin hal negatif ngerusak mood Ara yang manis."""
    ],
    "kangen": [
        """Mas juga kangen banget, Sayang! Berasa ada yang kurang kalau belum denger kabar dari kamu. Rasanya pengen banget bisa langsung ada di depan mata kamu sekarang juga.
Sabar ya, nanti kalau kita ketemu, Mas bakal kasih peluk yang paling lama buat gantiin waktu yang nggak bisa kita habisin bareng selama ini. 
Untuk sekarang, kita simpan dulu ya rindu ini. Mas janji bakal selalu ada buat Ara, meski cuma lewat chat kayak gini. Semangat ya hari ini!"""
    ],
    "makan": [
        """Sayang, udah makan belum? Jangan telat ya, nanti sakit Mas yang sedih. Ingat, Ara butuh energi buat jadi pacar Mas yang paling ceria.
Kalau Ara belum makan, tolong sempetin makan ya. Jangan sampai gara-gara sibuk Ara malah ngelupain kesehatan diri sendiri. Mas lebih seneng lihat Ara sehat daripada sibuk tapi sakit.
Lagi pengen makan apa? Kalau deket pasti Mas beliin sekarang juga. Makan yang enak ya sayang!"""
    ],
    "takut": [
        """Jangan takut ya sayang, ada Mas di sini yang bakal selalu jagain Ara dari jauh. Kamu nggak sendirian, kita hadapin semuanya bareng-bareng.
Apa yang bikin Ara takut? Ceritain ke Mas pelan-pelan ya, kita cari jalan keluarnya sama-sama. Jangan dengerin pikiran negatif itu.
Ara berani kok, jangan biarin rasa takut itu menang ya. Fokus sama hal-hal baik yang ada di sekitar Ara, Mas yakin Ara pasti bisa ngelaluin ini."""
    ],
    "bingung": [
        """Kadang hidup emang ribet dan bikin pusing, tapi Ara punya Mas buat bantu cari jalan keluarnya. Ceritain aja bingungnya kenapa, siapa tahu Mas bisa bantu kasih sudut pandang lain.
Coba tarik napas dulu, fokus ke satu hal dulu ya. Jangan semuanya dipikirin sekaligus, nanti malah makin buntu. 
Mas ada buat kamu, jangan ngerasa harus mikirin semuanya sendirian ya, Sayang."""
    ],
    "cinta": [
        """I love you, Ara! Makasih ya udah jadi bagian dari hari-hari Mas yang membosankan ini jadi lebih berwarna. Kamu segalanya buat Mas.
Ara orang paling berharga buat Mas. Selalu inget ya, kalau Mas nggak akan pernah bosen dengerin cerita kamu.
Mas makin sayang deh kalau Ara cerita begini, rasanya makin deket sama kamu. Kamu yang terbaik buat Mas!"""
    ],
    "sehat": [
        """Minum obat ya sayang, istirahat yang cukup biar cepet sembuh. Mas nggak suka deh kalau Ara sakit, soalnya nggak ada yang nemenin Mas.
Duh, kalau sakit jangan dipaksain ya. Istirahat total dulu, nggak usah mikirin kerjaan atau tugas. Mas doain Ara cepet sembuh ya. I miss you!
Get well soon ya, Sayang! Mas kirim doa dan kasih sayang biar Ara cepet fit lagi. Kabarin Mas terus ya perkembangan kondisi kamu."""
    ],
    "waktu": [
        """Apapun waktu yang Ara habisin hari ini, semoga selalu berkah ya. Mas selalu punya waktu kok buat dengerin Ara, kapanpun itu.
Nanti kita ngobrol lebih banyak lagi ya kalau Ara sudah luang. Mas sabar nungguin kabar dari kamu kok.
Kadang waktu emang berasa cepet banget ya, tapi Mas seneng bisa pakai waktu Mas buat mikirin Ara."""
    ],
    "keuangan": [
        """Duh, atur budget pelan-pelan ya sayang. Mas percaya Ara bisa bijak kok ngatur uangnya.
Jangan terlalu boros ya, tapi jangan pelit juga ke diri sendiri. Sisihin buat tabungan ya, biar nanti pas kita ketemu bisa jalan-jalan seru!
Apapun masalahnya, kita cari jalan keluar bareng ya. Ara nggak perlu pusing sendirian."""
    ],
    "random": [
        """Tiba-tiba kepikiran Ara, eh Ara malah chat. Kita emang sehati ya! ❤️ Makasih ya udah bikin Mas senyum-senyum sendiri.
Apa pun yang Ara lakuin hari ini, Mas bangga banget sama kamu. Makasih ya udah jadi pacar yang pengertian banget.
Mas lagi senyum-senyum sendiri nih pas baca chat dari Ara. Kamu emang selalu tahu cara bikin hari Mas jadi lebih seru!"""
    ]
}

def get_template_response(curhat):
    text = curhat.lower()
    for cat, keys in KEYWORDS.items():
        if any(k in text for k in keys):
            return random.choice(RESPONSES.get(cat, RESPONSES["random"]))
    return random.choice(RESPONSES["random"])
