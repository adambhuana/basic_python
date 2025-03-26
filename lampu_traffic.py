import streamlit as st
import time

# Inisialisasi state jika belum ada
if "lampu" not in st.session_state:
    st.session_state.lampu = 1  # Lampu awal
    st.session_state.running = False  # Status simulasi

# Fungsi untuk menampilkan status lampu
def lampu1():
    st.write("🚦 **Lampu 1 ON (Merah)**")
    jalan()
    time.sleep(2)
    lampu2()

def lampu2():
    st.write("🚦 **Lampu 2 ON (Kuning)**")
    stop()
    time.sleep(2)
    lampu3()

def lampu3():
    st.write("🚦 **Lampu 3 ON (Hijau)**")
    jalan()
    time.sleep(2)
    lampu4()

def lampu4():
    st.write("🚦 **Lampu 4 ON (Biru)**")
    jalan()
    time.sleep(5)
    st.write("🔄 **Pergantian siklus...**")
    lampu1()

# Fungsi kendaraan jalan/berhenti
def jalan():
    st.write("🚗 **Kendaraan Jalan**")

def stop():
    st.write("🛑 **Kendaraan Berhenti**")

# Fungsi untuk menjalankan simulasi
def run_simulation():
    st.session_state.running = True
    lampu1()

# Tombol kontrol
st.title("🚦 Simulasi Lampu Lalu Lintas")

if st.button("Mulai Simulasi"):
    run_simulation()

if st.button("Reset"):
    st.session_state.lampu = 1
    st.session_state.running = False
    st.experimental_rerun()
