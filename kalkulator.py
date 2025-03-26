import streamlit as st

def main():
    st.title("Kalkulator Sederhana")
    
    # Input angka pertama
    angka1 = st.text_input("Masukkan angka pertama:", "0")
    # Input angka kedua
    angka2 = st.text_input("Masukkan angka kedua:", "0")
    
    # Tombol untuk menghitung
    if st.button("Hitung"): 
        try:
            hasil = float(angka1) + float(angka2)
            st.success(f"Hasil penjumlahan: {hasil}")
        except ValueError:
            st.error("Masukkan angka yang valid!")
    
if __name__ == "__main__":
    main()
