import streamlit as st
import random

st.set_page_config(page_title="UAS ETIKA PROFESI", layout="centered")
st.title("UAS ETIKA PROFESI & HUKUM KESEHATAN")
st.write("100 Soal - Jawaban Teracak - Isi Nama, NIM, Kelas")

nama = st.text_input("Nama Lengkap")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

# KUNCI DISEMBUNYIIN JADI ANGKA 17=A 18=B 19=C 20=D - mahasiswa gak bisa liat
# Format: [soal, [pilihan], kunci_angka]
DATA = [
["Prinsip mengutamakan kebaikan pasien adalah?", ["Beneficence","Non-maleficence","Justice","Autonomy"], 17],
["Prinsip tidak merugikan pasien?", ["Beneficence","Non-maleficence","Veracity","Fidelity"], 18],
["Hak pasien menentukan sendiri disebut?", ["Justice","Beneficence","Autonomy","Confidentiality"], 19],
["Informed consent wajib sebelum?", ["Pembayaran","Pulang","Makan","Tindakan medis"], 20],
["Bidan wajib menjaga?", ["Gosip","Rahasia pasien","Uang pasien","HP pasien"], 18],
["UU praktik kebidanan no?", ["UU 36/2009","UU 44/2009","UU 4/2019","UU 36/2014"], 19],
["Sanksi etik terberat?", ["Teguran lisan","Bonus","Naik jabatan","Pencabutan STR"], 20],
["Asas keadilan berarti?", ["Yang kaya dulu","Semua sesuai kebutuhan","Yang kenal dulu","Acak"], 18],
["Rekam medis diatur oleh?", ["KUHP","Permenkes","KUHAP","UU ITE"], 18],
["Tindakan bidan harus sesuai?", ["TikTok","Standar profesi","Kemauan keluarga","Perasaan"], 18],
["Malpraktik adalah?", ["Tindakan berhasil","Tindakan tidak sesuai standar yang merugikan","Tindakan murah","Tindakan cepat"], 18],
["Contoh autonomy?", ["Bidan memaksa","Keluarga memaksa","Dokter putuskan sendiri","Pasien menolak transfusi"], 20],
["Veracity berarti?", ["Adil","Jujur","Baik","Setia"], 18],
["Fidelity berarti?", ["Berbohong","Acuh","Setia pada janji","Tidur"], 19],
["Pasien tidak sadar, persetujuan oleh?", ["Satpam","Keluarga terdekat","Pasien lain","Tidak perlu"], 18],
["Bidan wajib mencatat di?", ["Status WA","Rekam medis","Buku diary","Tidak perlu"], 18],
["Aborsi dilarang kecuali?", ["Alasan ekonomi","Indikasi medis darurat","Alasan sekolah","Alasan malu"], 18],
["Hak pasien untuk?", ["Dibohongi","Mendapat informasi","Dihukum","Diabaikan"], 18],
["Kewajiban bidan?", ["Diskriminasi","Memberi asuhan bermutu","Membiarkan","Minta imbalan berlebih"], 18],
["Etika profesi bersumber dari?", ["Uang","Nilai moral profesi","Kekuasaan","Popularitas"], 18],
]

# Gandakan jadi 100 soal dengan acak beda
while len(DATA) < 100:
    DATA = DATA + DATA[:100-len(DATA)]
DATA = DATA[:100]

# Acak urutan soal & jawaban - beda tiap mahasiswa
if "soal_acak" not in st.session_state:
    temp = []
    for q, opts, k in DATA:
        benar_text = opts[k-17]
        opts2 = opts[:]
        random.shuffle(opts2)
        temp.append([q, opts2, opts2.index(benar_text)])
    random.shuffle(temp)
    st.session_state.soal_acak = temp

jawaban = []
for i, (q, opts, kunci) in enumerate(st.session_state.soal_acak):
    st.markdown(f"**{i+1}. {q}**")
    pil = st.radio(f"Pilih {i+1}", opts, key=f"q{i}", index=None)
    jawaban.append(pil)

if st.button("KUMPUL & LIHAT NILAI", type="primary"):
    if not nama or not nim:
        st.warning("Isi Nama & NIM dulu")
    else:
        benar = 0
        for i, (q, opts, kunci) in enumerate(st.session_state.soal_acak):
            if jawaban[i] == opts[kunci]:
                benar += 1
        st.success(f"{nama} ({nim}) - Kelas {kelas}")
        st.success(f"BENAR {benar} dari 100 - NILAI: {benar}")
        st.info("Screenshot nilai ini & kirim ke dosen")
