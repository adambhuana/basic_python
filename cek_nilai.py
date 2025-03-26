import streamlit as st

def main():
    st.title("Konversi Nilai Ujian ke Huruf")
    
    # Input nilai ujian
    nilaiujian = st.number_input("Masukkan Nilai angka dari 0-100:", min_value=0, max_value=100, step=1)
    
    # Tombol untuk mengevaluasi nilai
    if st.button("Konversi"): 
        if nilaiujian >= 80 and nilaiujian <= 100:
            st.success("Huruf: A")
        elif nilaiujian >= 70:
            st.success("Huruf: B")
        elif nilaiujian < 0:
            st.error("Maaf nilai tidak boleh lebih rendah dari NOL")
        else:
            st.warning("Gagal")
    
if __name__ == "__main__":
    main()
