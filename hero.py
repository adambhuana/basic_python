import streamlit as st
import random

# Inisialisasi session_state jika belum ada
if "heroname" not in st.session_state:
    st.session_state.heroname = "Adam"
    st.session_state.heropower = 2
    st.session_state.anemyname = []
    st.session_state.anemypower = []
    st.session_state.randomlist = []
    st.session_state.jmlkalah = 0  # Jumlah musuh yang sudah dikalahkan
    st.session_state.randomanemy = -1
    st.session_state.game_started = False
    st.session_state.game_over = False
    st.session_state.level_2 = False  # Menandakan masuk ke level 2
    st.session_state.enemy_setup_done = False  # Menandakan musuh sudah diatur

st.title("🎮 Hero War - Green Academy")

# **1️⃣ Tahap 1: Pengaturan Musuh**
if not st.session_state.enemy_setup_done:
    st.subheader("⚔️ Pengaturan Musuh")

    # Pilih jumlah musuh
    jumlahanemy = st.number_input("Jumlah musuh:", min_value=1, step=1, key="jumlah_musuh")

    # Input nama dan kekuatan musuh
    anemyname = []
    anemypower = []
    for i in range(jumlahanemy):
        nama = st.text_input(f"Nama musuh {i+1}:", key=f"enemy_name_{i}")
        power = st.number_input(f"Kekuatan {nama if nama else 'musuh'}:", min_value=1, step=1, key=f"enemy_power_{i}")
        anemyname.append(nama)
        anemypower.append(power)

    # Tombol untuk menyimpan musuh
    if st.button("Mulai Permainan"):
        if all(anemyname) and all(anemypower):
            st.session_state.anemyname = anemyname
            st.session_state.anemypower = anemypower
            st.session_state.randomlist = list(range(jumlahanemy))
            st.session_state.enemy_setup_done = True
            st.rerun()
        else:
            st.warning("Harap isi semua nama dan kekuatan musuh!")

# **2️⃣ Tahap 2: Mulai Pertarungan**
if st.session_state.enemy_setup_done and not st.session_state.game_over:
    st.subheader(f"👤 Hero: {st.session_state.heroname} (Power: {st.session_state.heropower})")
    st.write(f"Musuh tersisa: {len(st.session_state.randomlist) - st.session_state.jmlkalah}")

    if st.session_state.jmlkalah < len(st.session_state.anemyname):
        # Pilih musuh secara acak
        if st.session_state.randomanemy == -1 or "tukar_musuh" in st.session_state:
            st.session_state.randomanemy = random.choice(st.session_state.randomlist)
            st.session_state.pop("tukar_musuh", None)

        enemy_name = st.session_state.anemyname[st.session_state.randomanemy]
        enemy_power = st.session_state.anemypower[st.session_state.randomanemy]

        st.subheader(f"⚔️ Musuh Muncul: {enemy_name} (Power: {enemy_power})")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🗡️ Serang!"):
                if st.session_state.heropower < enemy_power:
                    st.error("😢 Kamu kalah! Game Over.")
                    st.session_state.game_over = True
                else:
                    st.success(f"🎉 Kamu mengalahkan {enemy_name}!")
                    st.session_state.heropower += enemy_power
                    st.session_state.jmlkalah += 1

                    # Hapus musuh yang telah dikalahkan
                    st.session_state.randomlist.remove(st.session_state.randomanemy)

                    # Jika semua musuh dikalahkan, masuk ke level 2
                    if st.session_state.jmlkalah == len(st.session_state.anemyname):
                        st.balloons()
                        st.session_state.level_2 = True
                        st.rerun()
                    else:
                        st.session_state.randomanemy = -1  # Reset pilihan musuh
                        st.rerun()  # Perbarui UI untuk lanjut ke musuh berikutnya

        with col2:
            if st.button("🏃‍♂️ Tolak!"):
                st.session_state.tukar_musuh = True  # Set flag untuk mengganti musuh
                st.rerun()

# **3️⃣ Tahap 3: Level 2**
if st.session_state.level_2:
    st.success("🏆 Semua musuh dikalahkan! Masuk Level 2!")
    if st.button("Lanjut ke Level 2"):
        st.session_state.clear()  # Reset untuk level berikutnya
        st.rerun()

# **🔁 Restart Game**
if st.button("Restart Game"):
    st.session_state.clear()
    st.rerun()
