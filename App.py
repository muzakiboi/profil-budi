import streamlit as st

# 🔐 Data
nama = "Budi"
umur = 20
tinggi = 175.5
is_mahasiswa = True
hobi = ["makan", "main"]
nilai = (90, 85, 88)
data = {
    "nama": nama,
    "umur": umur,
    "tinggi": tinggi,
    "mahasiswa": is_mahasiswa,
    "hobi": hobi,
    "nilai": nilai
}
unik = {1, 2, 3}

# 🎨 UI Tampilan
st.title("📄 Profil Budi")

st.markdown(f"""
- **Nama:** {data["nama"]}
- **Umur:** {data["umur"]} tahun
- **Tinggi:** {data["tinggi"]} cm
- **Mahasiswa?** {"Ya" if data["mahasiswa"] else "Tidak"}
- **Hobi:** {", ".join(data["hobi"])}
- **Nilai Ujian:** {data["nilai"]}
- **Data Unik:** {unik}
""")