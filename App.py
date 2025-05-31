import streamlit as st

nama: str = "Budiono Siregar"                     
umur: int = 20                         
tinggi: float = 175.5                 
is_mahasiswa: bool = True
is_Raja_Iblis: bool = True

hobi: list[str] = ["makan", "main"]   
nilai: tuple[int, int, int] = (90, 85, 88) 

data: dict = {
    "nama": nama,
    "umur": umur,
    "tinggi": tinggi,
    "mahasiswa": is_mahasiswa,
    "hobi": hobi,
    "nilai": nilai
}

unik: set[int] = {1, 2, 3}

st.title("📄 Profil Budi")

st.markdown(f"""
- **Nama:** {data['nama']}
- **Umur:** {data['umur']} tahun
- **Tinggi:** {data['tinggi']} cm
- **Mahasiswa?** {'Ya' if data['mahasiswa'] else 'Tidak'}
- **Hobi:** {', '.join(data['hobi'])}
- **Nilai Ujian:** {data['nilai']}
- **Data Unik:** {unik}
""")
