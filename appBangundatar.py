import streamlit as st
import math

#  halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu= st.sidebar.selectbox('pilih aplikasi',['luas persegi','luas segitiga','luas lingkaran', 'luas persegipanjang'])

if menu=='luas persegi':
    st.write('ini halaman untuk menghitung luas persegi :balloon::smile:')
    st.markdown(':red[luas persegi]')
    st.image('data:image/png;base64,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')
    def luaspersegi(a):
        return a*a
    sisi=st.number_input('silahkan masukkan sisi', min_value=0,)
    if st.button('hitung'):
        luas= sisi*sisi
        st.write(f'luas persegi adalah {luas}')
 
elif menu=='luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    st.markdown(':blue[luas segitiga]')
    st.image('data:image/png;base64,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')
    alas=st.number_input('silahkan masukkan alas',min_value=0,)
    tinggi=st.number_input('silahkan masukkan tinggi',min_value=0,) 
    if st.button('hitung luas'):
        luas= 1/2*alas*tinggi
        st.success(f'luas segitiga adalah {luas}')
        
elif menu =='luas lingkaran':
    st.write(':red[ini halaman untuk menghitung luas lingkaran]:smile:')
    st.markdown('luas lingkaran')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6HyUDjw1UrN-AHA3geVL_Ee_2olFVU7C8rQ&s')
    jari2 = st.number_input('silahkan masukkan jari-jari',min_value=0)
    
    if st.button('hitung luas'):
        luas= math.pi *(jari2**2)
        st.success(f'luas lingkaran adalah {luas}')
        
elif menu == 'luas persegipanjang':
    st.write(':red[ini halaman untuk menghitung luas persegi panjang]:smile:')
    st.markdown('luas persegipanjang')
    st.image('https://images.bisnis.com/posts/2023/02/25/1631651/2._ini_rumus_luas_persegi_panjang_dan_contoh_soalnya_(dok._nuraini).jpg')
    panjang= st.number_input('silahkan masukkan panjang',min_value=0)
    lebar= st.number_input('silahkan masukkan lebar',min_value=0)
    
    if st.button('hitung luas'):
        luas= panjang*lebar
        st.success(f'luas persegi panjang adalah {luas}')
    