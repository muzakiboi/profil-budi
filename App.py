import streamlit as st

# 🎓 Biodata si Budi — versi kekinian
nama: str = "Budi"                     # 🧍‍♂️ Nama lengkap (string)
umur: int = 20                         # 🎂 Umur (integer)
tinggi: float = 175.5                  # 📏 Tinggi badan dalam cm (float)
is_mahasiswa: bool = True             # 🎓 Status mahasiswa (boolean)

# 🎯 Hobi dan Nilai-nilai
hobi: list[str] = ["makan", "main"]    # 🎮 List of hobbies
nilai: tuple[int, int, int] = (90, 85, 88)  # 📝 Nilai ujian (tuple)

# 🗂️ Data lengkap dalam dictionary
data: dict = {
    "nama": nama,
    "umur": umur,
    "tinggi": tinggi,
    "mahasiswa": is_mahasiswa,
    "hobi": hobi,
    "nilai": nilai
}

# 🔐 Set — data unik
unik: set[int] = {1, 2, 3}             # ✨ Kumpulan angka unik

# 🧠 Tampilan Streamlit
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
