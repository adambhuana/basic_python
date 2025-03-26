import streamlit as st
import random

# Inisialisasi session state untuk skor dan ronde
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.scoresaya = 0
    st.session_state.scorekomp = 0
    st.session_state.result = ""
    st.session_state.komp_choice = ""
    st.session_state.user_choice = ""

# Peta gambar
image_dict = {
    "batu": "🪨",
    "kertas": "📄",
    "gunting": "✂️"
}

# Fungsi untuk memainkan game
def play(choice):
    if st.session_state.round > 3:
        return  # Jika sudah 3 ronde, hentikan permainan
    
    komputer = random.choice(['gunting', 'batu', 'kertas'])
    st.session_state.komp_choice = komputer
    st.session_state.user_choice = choice

    # Menentukan hasil
    if choice == komputer:
        st.session_state.result = "🔄 Seri!"
    elif (choice == "gunting" and komputer == "kertas") or \
         (choice == "batu" and komputer == "gunting") or \
         (choice == "kertas" and komputer == "batu"):
        st.session_state.result = "🎉 Kamu Menang!"
        st.session_state.scoresaya += 1
    else:
        st.session_state.result = "💀 Kamu Kalah!"
        st.session_state.scorekomp += 1

    # Naikkan ronde
    st.session_state.round += 1

# Reset permainan
def reset_game():
    st.session_state.round = 1
    st.session_state.scoresaya = 0
    st.session_state.scorekomp = 0
    st.session_state.result = ""
    st.session_state.komp_choice = ""
    st.session_state.user_choice = ""

# UI Streamlit
st.title("✊ ✋ ✌️ Game Batu-Gunting-Kertas")
st.write(f"**Ronde: {st.session_state.round} / 3**")

# Pilihan User
st.subheader("Pilih: ")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Batu"):
        play("batu")
with col2:
    if st.button("📄 Kertas"):
        play("kertas")
with col3:
    if st.button("✂️ Gunting"):
        play("gunting")

# Menampilkan hasil
if st.session_state.komp_choice:
    st.subheader("Hasil Ronde:")
    st.write(f"👤 Kamu: {image_dict[st.session_state.user_choice]}")
    st.write(f"🖥️ Komputer: {image_dict[st.session_state.komp_choice]}")
    st.subheader(st.session_state.result)

# Menampilkan skor
st.write(f"📊 **Skor Kamu:** {st.session_state.scoresaya}")
st.write(f"🤖 **Skor Komputer:** {st.session_state.scorekomp}")

# Menentukan pemenang setelah 3 ronde
if st.session_state.round > 3:
    if st.session_state.scoresaya > st.session_state.scorekomp:
        st.success("🏆 **Selamat! Kamu menang pertandingan!**")
    elif st.session_state.scoresaya < st.session_state.scorekomp:
        st.error("😢 **Sayang sekali, kamu kalah pertandingan.**")
    else:
        st.warning("🔄 **Hasil akhir: Seri!**")

    if st.button("🔄 Reset Permainan"):
        reset_game()
