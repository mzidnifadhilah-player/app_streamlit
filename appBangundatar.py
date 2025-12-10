import streamlit as st

#  halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu= st.sidebar.selectbox('pilih aplikasi',['luas persegi','luas segitiga','luas lingkaran'])

if menu=='luas persegi':
    st.write('ini halaman untuk menghitung luas persegi :balloon::smile:')
    st.markdown(':red[luas persegi panjang]')
    st.image('data:image/png;base64,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')
    def luaspersegi(a):
        return a*a
    sisi=st.number_input('silahkan masukkan sisi', min_value=0,)
    if st.button('hitung'):
        luas= sisi*sisi
        st.write(f'luas persegi adalah {luas}')
 
elif menu=='luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    
