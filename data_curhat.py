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
        "Ara sayang, sini cerita sama Mas... Mas tahu hari ini pasti terasa berat banget buat kamu. Tarik napas dalam-dalam dulu ya, Sayang. Mas nggak bisa secara fisik buat hapus air mata Ara, tapi Mas pengen Ara tahu kalau Mas selalu ada di sini. Apa pun yang bikin Ara ngerasa sedih atau hancur, jangan dipendam sendirian ya. Ara hebat banget udah bisa bertahan sampai detik ini, Mas bangga sama kamu. Habis ini, kalau Ara butuh temen buat ngerasa tenang, Mas bakal nemenin kamu terus. Semangat ya, Sayang! ❤️",
        "Cup cup sayang... Mas denger kok curhatan kamu. Mas ngerasa sedih juga kalau tahu Ara lagi nggak baik-baik aja. Kadang emang dunia ini terasa jahat, tapi Ara punya Mas yang bakal selalu sayang sama kamu. Jangan pernah ngerasa sendirian ya, karena Mas ada di sini sebagai tempat Ara buat pulang dan bercerita. Coba deh, Ara lakuin hal yang bikin kamu nyaman sekarang, makan yang enak atau dengerin lagu favorit. Mas sayang banget sama Ara, please be happy again ya... ✨",
        "Mas sedih banget lihat Ara lagi kayak gini, rasanya pengen langsung ada di depan kamu buat kasih pelukan terhangat. Jangan biarin masalah itu ngilangin senyum Ara yang berharga ya, Sayang. Ara itu kuat, dan Mas yakin kamu bisa lewatin masa sulit ini dengan elegan. Kalau Ara butuh sandaran, bahu Mas selalu siap buat kamu. Mas nggak bakal kemana-mana, Mas tetep di sini buat jadi pendengar setia setiap keluh kesah Ara. I love you, Ara!"
    ],
    "senang": [
        "Wah, beneran? Mas ikut seneng banget dengernya! Ceritain dong detailnya, Ara bikin hari Mas jadi cerah juga nih denger kabar baik ini. ✨ Ara beneran deserve buat ngerasain bahagia kayak gini setiap hari. Mas bangga banget punya pacar sehebat Ara yang selalu bisa kasih energi positif. Ayo rayain nanti ya pas kita ketemu, Mas pengen banget denger langsung cerita seru dari kamu! Love you so much, Ara! Tetap jadi Ara yang ceria ya!",
        "Denger Ara happy, mood Mas langsung naik drastis! Seneng banget deh lihat pacar Mas bisa ngerasain momen sebahagia ini. Kamu tuh emang juara kalau soal bikin hari jadi lebih indah. Jangan lupa bersyukur ya, Sayang, karena Ara layak dapetin semua kebaikan itu. Ceritain lebih banyak dong ke Mas, Mas nggak bakal bosen dengerin detail kebahagiaan kamu sampai kapanpun. Tetap bersinar ya, Sayang!",
        "Yes! Itu baru pacar Mas! Bangga banget denger pencapaian Ara hari ini. Mas tahu Ara udah usaha maksimal buat dapetin itu, dan akhirnya semua terbayar lunas kan? Ayo kita rayain kecil-kecilan nanti pas ketemu. Mas seneng banget karena Ara bisa ngerasain perasaan yang secerah ini. Teruslah berkarya dan bikin Mas makin kagum sama kamu ya, Sayang. You're the best!"
    ],
    "lelah": [
        "Duh, pacar Mas capek banget ya hari ini? Sini, istirahat dulu sebentar. Mas tahu Ara udah kerja keras banget buat semuanya. Dunia emang kadang nuntut kita buat terus lari, tapi Ara juga manusia yang punya batas. Nggak apa-apa kok kalau hari ini Ara mau rehat total. Tugas dan tanggung jawab emang penting, tapi kesehatan Ara jauh lebih penting buat Mas. Sekarang, coba matiin HP bentar, tarik napas, dan tidur yang nyenyak ya. Mas nemenin Ara dalam doa dan kasih sayang. Besok pas bangun, Ara bakal ngerasa lebih baik lagi. Mas sayang banget sama Ara! 🐧",
        "Mas ngerti banget capeknya Ara hari ini. Udah ya, jangan dipaksain lagi. Tarik napas, minum air putih, lalu istirahat yang cukup ya. Ara itu berharga banget, jadi tolong jangan sampai sakit ya. Kalau capek, dengerin lagu favorit Ara terus merem sebentar, itu bisa bantu nenangin pikiran kok. Jangan lupa matiin HP-nya kalau udah capek banget, tidur ya Sayang. Mas nemenin kamu dari sini, mimpi indah ya!",
        "Sayang, jangan diforsir terus ya. Mas tahu Ara udah kerja keras banget hari ini dan itu bikin Mas bangga sekaligus khawatir sama kamu. Istirahat dulu ya, jangan dipikirin dulu hal-hal beratnya. Dunia nggak bakal lari kok, dan Ara butuh waktu buat *recharge* energi biar besok bisa lebih semangat lagi. Sini, peluk virtual dari Mas. Tidur yang nyenyak ya, Sayang. Besok kalau bangun, Mas harap kamu ngerasa jauh lebih baik. I love you!"
    ],
    "tugas": [
        "Duh, lagi pusing ngerjain tugas ya, Sayang? Mas ngerti banget rasanya dikejar deadline dan tanggung jawab yang numpuk. Coba deh tarik napas pelan-pelan, kerjain satu-satu ya. Kamu nggak perlu langsung beres hari ini kalau emang badannya udah capek banget. Ara udah berusaha maksimal kok, dan itu udah lebih dari cukup buat Mas. Mas temenin dari sini ya. Kalau udah selesai, jangan lupa kasih reward buat diri sendiri. Ara itu orang terpintar yang Mas kenal, tugas segini mah pasti lewat! Semangat ya, Sayang. ❤️",
        "Mas tahu tugas-tugas itu kadang emang bikin kesel, tapi inget ya, Ara itu jauh lebih hebat daripada sekadar tumpukan tugas itu. Jangan dipaksain banget sampai lupa makan atau kurang tidur ya. Kesehatan Ara itu nomor satu buat Mas, jadi tolong jaga diri baik-baik. Kalau mulai buntu, istirahat bentar, jangan dipaksain terus. Kalau butuh distraksi atau mau ngobrol biar nggak suntuk, langsung chat Mas aja ya. Mas selalu ada buat jadi mood booster kamu di tengah kesibukan. Kamu pasti bisa, Sayang!",
        "Semangat ngerjain tugasnya! Mas percaya Ara pasti bisa selesaiin semuanya dengan hasil yang memuaskan. Dikit lagi selesai kok! Jangan lupa makan ya, jangan sampai sakit gara-gara nugas. Fokus ya! Mas tahu Ara orangnya detail dan teliti, pasti hasilnya bagus nanti. Jangan begadang terus ya sayang! Kesehatan tetap nomor satu bagi Mas. Mas selalu support Ara dari sini, kalau pusing, telfon Mas ya. Nugas bareng Mas yuk di pikiran Ara? Biar nggak berasa sendirian."
    ],
    "marah": [
        "Waduh, ada yang lagi emosi ya? Sini, tenangin diri dulu ya sayang, jangan sampai kemarahan itu bikin Ara malah kepikiran terus. Tarik napas dalem-dalem ya. Jahat banget sih yang bikin Ara marah, sini cerita sama Mas siapa orangnya. Tapi janji ya, jangan lama-lama marahnya, nanti malah Ara sendiri yang capek. Taruh dulu HP-nya, ambil napas dalam-dalam. Mas selalu di sini buat nemenin Ara, jangan biarin hal negatif ngerusak mood Ara yang manis.",
        "Tenang ya sayang, tarik napas dulu. Mas tahu pasti ada sesuatu yang bikin Ara kesel, tapi jangan biarin emosi itu nguasaain Ara ya. Mas nggak suka lihat pacar Mas marah-marah, soalnya Ara lebih cantik dan manis kalau lagi happy. Coba ceritain ke Mas pelan-pelan, siapa tahu Mas bisa bantu nenangin atau sekadar dengerin. Jangan dipendam sendiri, Mas bakal selalu ada buat nampung semua unek-unek kamu.",
        "Marah itu manusiawi kok, Sayang. Tapi jangan sampai itu bikin Ara jadi nggak nyaman sama diri sendiri ya. Coba kasih jarak sebentar dari masalah itu, tarik napas panjang, dan minum air dingin. Mas tahu Ara orang yang sabar, jadi jangan biarin orang lain bikin Ara ngerasa kehilangan kontrol diri. Mas selalu dukung Ara, dan Mas yakin Ara bisa ngelewatin ini dengan kepala dingin. Tetap tenang ya, Sayang!"
    ],
    "kangen": [
        "Mas juga kangen banget, Sayang! Berasa ada yang kurang kalau belum denger kabar dari kamu. Rasanya pengen banget bisa langsung ada di depan mata kamu sekarang juga. Sabar ya, nanti kalau kita ketemu, Mas bakal kasih peluk yang paling lama buat gantiin waktu yang nggak bisa kita habisin bareng selama ini. Untuk sekarang, kita simpan dulu ya rindu ini. Mas janji bakal selalu ada buat Ara, meski cuma lewat chat kayak gini. Semangat ya hari ini!",
        "Aduh, tiba-tiba Mas juga ngerasa rindu banget nih. Kayaknya kita emang udah sehati ya, pas Ara kangen, Mas juga lagi mikirin kamu terus. Nunggu ketemu Ara tuh emang berasa lama banget, tapi tenang aja, semua rindu ini bakal terbayar lunas pas kita ketemu nanti. Mas udah siapin banyak cerita buat kamu. Tetap jaga hati ya, Sayang. Mas di sini selalu sayang dan mikirin kamu. Jangan lupa makan dan jaga kesehatan biar pas ketemu nanti kamu seger terus!",
        "Mas kangen banget sama suara Ara, sama chat-chat random kamu yang selalu bikin Mas ketawa. Emang bener ya, jarak itu cuma ujian kecil buat kita. Mas nungguin banget momen di mana kita bisa ketemu dan nggak perlu lagi LDR-an lewat layar HP. Jaga kesehatan ya, Sayang, jangan terlalu capek biar pas ketemu nanti kita bisa jalan seharian full. Mas sayang banget sama Ara, rindu ini bakal Mas bayar tuntas nanti!"
    ],
    "makan": [
        "Sayang, udah makan belum? Jangan telat ya, nanti sakit Mas yang sedih. Ingat, Ara butuh energi buat jadi pacar Mas yang paling ceria. Kalau Ara belum makan, tolong sempetin makan ya. Jangan sampai gara-gara sibuk Ara malah ngelupain kesehatan diri sendiri. Mas lebih seneng lihat Ara sehat daripada sibuk tapi sakit. Lagi pengen makan apa? Kalau deket pasti Mas beliin sekarang juga. Makan yang enak ya sayang!",
        "Jangan sampai telat makan ya, Sayang! Mas khawatir kalau Ara jadi sakit gara-gara kurang energi. Makan yang bergizi biar hari kamu makin semangat. Kalau emang lagi nggak nafsu, coba makan yang paling kamu suka aja, yang penting perut keisi. Mas di sini bakal terus ngingetin kamu, jadi jangan nakal ya. Harus makan sekarang! Love you.",
        "Ara sayang, jangan lupa makan ya! Perut kosong itu musuh terbesar kalau mau ngerjain apa pun. Mas pengen Ara selalu fit, jadi tolong dengerin Mas ya. Makan yang enak, makan yang teratur, dan jangan lupa minum air putih yang banyak. Kalau kamu sehat, Mas juga ikut tenang di sini. Udah makan belum hari ini? Kalau belum, ayo cari makan sekarang!"
    ],
    "takut": [
        "Jangan takut ya sayang, ada Mas di sini yang bakal selalu jagain Ara dari jauh. Kamu nggak sendirian, kita hadapin semuanya bareng-bareng. Apa yang bikin Ara takut? Ceritain ke Mas pelan-pelan ya, kita cari jalan keluarnya sama-sama. Jangan dengerin pikiran negatif itu. Ara berani kok, jangan biarin rasa takut itu menang ya. Fokus sama hal-hal baik yang ada di sekitar Ara, Mas yakin Ara pasti bisa ngelaluin ini.",
        "Mas tahu terkadang rasa cemas itu datang tiba-tiba, tapi inget ya, Ara itu jauh lebih kuat daripada ketakutan itu sendiri. Kalau lagi cemas, tarik napas, dan ingat kalau ada Mas yang selalu support kamu kapanpun. Apa pun yang bikin Ara ngerasa khawatir, ceritain ke Mas ya, jangan ditahan sendiri. Kita hadapin semuanya satu demi satu. Mas percaya sama Ara, dan Ara harus percaya sama diri sendiri juga.",
        "Jangan takut ya, Sayang. Apa pun yang ada di depan sana, Mas bakal nemenin Ara. Kalau ada hal yang bikin Ara deg-degan, langsung chat Mas aja, nanti kita bahas bareng-bareng biar Ara ngerasa tenang lagi. Ara itu punya Mas yang selalu sayang dan bakal jagain Ara. Jadi, tenangin diri, jangan panik, dan selalu ingat kalau kamu nggak sendirian. Semangat ya, Sayang!"
    ],
    "bingung": [
        "Kadang hidup emang ribet dan bikin pusing, tapi Ara punya Mas buat bantu cari jalan keluarnya. Ceritain aja bingungnya kenapa, siapa tahu Mas bisa bantu kasih sudut pandang lain. Coba tarik napas dulu, fokus ke satu hal dulu ya. Jangan semuanya dipikirin sekaligus, nanti malah makin buntu. Mas ada buat kamu, jangan ngerasa harus mikirin semuanya sendirian ya, Sayang.",
        "Bingung kenapa sayang? Ceritain pelan-pelan ya, jangan dipikirin sendiri sampai pusing. Mas dengerin kok, apapun itu. Kadang emang kita butuh orang lain buat bantu ngelihat masalah dengan lebih jelas. Ara ceritain aja, nanti kita cari solusinya bareng-bareng sampai Ara ngerasa lega. Mas di sini selalu siap sedia buat jadi teman diskusi kamu.",
        "Mas ngerti rasanya kalau udah buntu dan bingung harus ngapain lagi. Tapi inget ya, setiap masalah pasti ada jalan keluarnya, dan Ara nggak sendirian. Coba istirahat sebentar, jangan terlalu keras sama diri sendiri. Kalau Ara udah siap, ceritain ke Mas ya bingungnya di mana. Kita bakal cari solusinya bareng-bareng, Mas janji bakal selalu bantuin Ara."
    ],
    "cinta": [
        "I love you, Ara! Makasih ya udah jadi bagian dari hari-hari Mas yang membosankan ini jadi lebih berwarna. Kamu segalanya buat Mas. Ara orang paling berharga buat Mas. Selalu inget ya, kalau Mas nggak akan pernah bosen dengerin cerita kamu. Mas makin sayang deh kalau Ara cerita begini, rasanya makin deket sama kamu. Kamu yang terbaik buat Mas!",
        "Mas sayang banget sama Ara, dan Mas selalu bersyukur bisa punya pacar kayak kamu. Setiap detik yang Mas lewati rasanya makin bermakna karena ada kamu di sisi Mas. Makasih ya udah sabar sama Mas, dan makasih udah selalu ada. Ara itu pacar paling baik dan paling pengertian yang pernah Mas kenal. Semoga hubungan kita selalu kayak gini ya, penuh kasih sayang dan saling dengerin.",
        "Ara, makasih ya udah jadi sosok yang bikin Mas selalu pengen pulang. Kamu itu rumah bagi Mas. Mas bahagia banget bisa jadi bagian dari hidup kamu. Selalu jaga diri baik-baik ya, Sayang. Karena bagi Mas, Ara itu segalanya. I love you to the moon and back!"
    ],
    "sehat": [
        "Minum obat ya sayang, istirahat yang cukup biar cepet sembuh. Mas nggak suka deh kalau Ara sakit, soalnya nggak ada yang nemenin Mas. Duh, kalau sakit jangan dipaksain ya. Istirahat total dulu, nggak usah mikirin kerjaan atau tugas. Mas doain Ara cepet sembuh ya. I miss you! Get well soon ya, Sayang! Mas kirim doa dan kasih sayang biar Ara cepet fit lagi. Kabarin Mas terus ya perkembangan kondisi kamu.",
        "Sayang, kalau ngerasa kurang sehat, langsung istirahat ya. Jangan begadang dan jangan lupa minum obat atau vitamin. Mas khawatir banget kalau Ara drop. Harus janji sama Mas buat jaga kesehatan, soalnya Ara berharga banget buat Mas. Kalau udah mendingan, kabarin ya. Mas nggak bakal tenang kalau Ara masih sakit. Semoga cepet sembuh ya, Sayang!",
        "Duh, sakit ya? Mas jadi ikutan ngerasa nggak enak nih. Tolong istirahat yang cukup ya, Sayang. Jangan lupa makan walaupun cuma sedikit biar ada tenaga buat sembuh. Mas doain dari sini biar Ara cepet pulih dan bisa ceria lagi. Ara harus kuat ya, jangan lupa banyak minum air hangat. I love you, cepet sembuh ya!"
    ],
    "waktu": [
        "Apapun waktu yang Ara habisin hari ini, semoga selalu berkah ya. Mas selalu punya waktu kok buat dengerin Ara, kapanpun itu. Nanti kita ngobrol lebih banyak lagi ya kalau Ara sudah luang. Mas sabar nungguin kabar dari kamu kok. Kadang waktu emang berasa cepet banget ya, tapi Mas seneng bisa pakai waktu Mas buat mikirin Ara.",
        "Mas selalu nungguin waktu luang Ara biar kita bisa ngobrol sepuasnya. Nggak apa-apa kalau sekarang Ara lagi sibuk, Mas ngerti kok. Yang penting jangan lupa kabarin Mas ya kalau udah selo. Mas tetep di sini kok, selalu siap nungguin chat dari kamu kapanpun Ara butuh.",
        "Waktu bareng Ara tuh rasanya selalu kurang. Pengen banget bisa seharian ngobrol sama kamu tanpa diganggu siapa pun. Tapi Mas hargai kok kesibukan Ara. Semangat ya jalani harinya, nanti pas Ara ada waktu senggang, langsung cerita ke Mas ya, Mas pasti langsung bales!"
    ],
    "keuangan": [
        "Duh, atur budget pelan-pelan ya sayang. Mas percaya Ara bisa bijak kok ngatur uangnya. Jangan terlalu boros ya, tapi jangan pelit juga ke diri sendiri. Sisihin buat tabungan ya, biar nanti pas kita ketemu bisa jalan-jalan seru! Apapun masalahnya, kita cari jalan keluar bareng ya. Ara nggak perlu pusing sendirian.",
        "Mas tahu ngatur uang itu emang *tricky*, tapi Ara pasti bisa kok. Coba diprioritasin apa yang bener-bener dibutuhin. Mas percaya sama kemampuan Ara dalam mengelola keuangan. Kalau emang lagi sulit banget, cerita ke Mas ya, siapa tahu kita bisa cari solusinya bareng-bareng. Semangat nabungnya, Sayang!",
        "Keuangan emang sering jadi sumber pikiran, tapi jangan sampai itu bikin Ara jadi stres sendiri ya. Atur pelan-pelan, catat pengeluaran, dan yang penting tetap jaga kebutuhan pokok. Ara pasti bisa ngelewatin masa-masa ini. Mas selalu support Ara, kalau ada yang perlu didiskusiin, bilang aja ya!"
    ]
}

def get_template_response(curhat):
    text = curhat.lower()
    for cat, keys in KEYWORDS.items():
        if any(k in text for k in keys):
