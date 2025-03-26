import streamlit as st

# Inisialisasi session state jika belum ada
if "slotpistol" not in st.session_state:
    st.session_state.slotpistol = 8
    st.session_state.peluru = 5
    st.session_state.amunisi = [st.session_state.peluru] * st.session_state.slotpistol
    st.session_state.maksimumtembak = 0
    st.session_state.poweranemy = 50
    st.session_state.namaanemy = "Hulk"

st.title("Simulasi Penembakan Pistol")

# Tampilkan status musuh dan amunisi
st.write(f"Enemy: {st.session_state.namaanemy} ({st.session_state.poweranemy})")
st.write(f"Amunisi: {st.session_state.amunisi}")

# Jika musuh masih hidup, tombol bisa ditekan
if st.session_state.poweranemy > 0:
    if st.button("Shoot"):
        if st.session_state.maksimumtembak < st.session_state.slotpistol:
            # Kurangi peluru dari amunisi
            st.session_state.amunisi[st.session_state.maksimumtembak] = 0
            st.session_state.maksimumtembak += 1

            # Kurangi power musuh
            st.session_state.poweranemy -= st.session_state.peluru
            if st.session_state.poweranemy < 0:
                st.session_state.poweranemy = 0  # Hindari nilai negatif

            # Reload jika semua peluru habis
            if st.session_state.maksimumtembak == st.session_state.slotpistol:
                st.warning("Reloading...")
                st.session_state.amunisi = [st.session_state.peluru] * st.session_state.slotpistol
                st.session_state.maksimumtembak = 0

        # Update status musuh dan amunisi
        st.write(f"Enemy sekarang: {st.session_state.namaanemy} ({st.session_state.poweranemy})")
        st.write(f"Amunisi: {st.session_state.amunisi}")

# Jika musuh sudah kalah
if st.session_state.poweranemy == 0:
    st.success("Enemy defeated!")
