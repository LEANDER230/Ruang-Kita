with tab5:
    st.subheader("🐧 Anak Kita Puyo")

    # 1. INISIALISASI
    defaults = {
        'health': 100, 'xp': 0, 'level': 1, 'lapar': 0, 'bosan': 0, 
        'kotor': 0, 'pintar': 0, 'sakit': False, 'dead': False,
        'puyo_image': "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3d3RzNXM1NGsydWQxd2w0cTdra3B6ZDNyaWZpdW5wYnV3ZjByMGthNiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/c0pgbXEP80iyOAZcCK/giphy.gif"
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
        "Lari": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MDBoY3l4eXJ5bzA4c29mZ3lxczZndGZ0MHkwZng1dGpwNXdiejZ2aiZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/84gHS1mDKOLsQpIMcN/giphy.gif",
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
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NjlxYndmZmV0cTAwMHM5bXZ1bmU3bHJzZjZ6OGp1azh1dHVkc3dpOCZlcD12MV9zdGlja2Vyc19yZWxhdGVkJmN0PXM/TKKCwabNYbaJe8mG2B/giphy.gif")
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
