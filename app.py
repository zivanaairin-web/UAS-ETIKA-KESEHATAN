import streamlit as st
import datetime
import random

st.set_page_config(page_title="UAS Etika", layout="centered")
st.title("SOAL PILIHAN GANDA")
st.write("ETIKA PROFESI DAN HUKUM KESEHATAN")

nama = st.text_input("Nama Lengkap")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1tbEXyKC_BhCNBCMPvVGQ_KrJQ9X3YmKpCLeTvZ7QzI4/edit?gid=0#gid=0"

DATA = [
 ("Prinsip etika yang mengutamakan kebaikan pasien?", ["Beneficence","Non-maleficence","Justice","Autonomy"], 0),
 ("Prinsip tidak merugikan pasien?", ["Beneficence","Non-maleficence","Veracity","Fidelity"], 1),
 ("Hak pasien menentukan sendiri?", ["Justice","Beneficence","Autonomy","Confidentiality"], 2),
 ("Informed consent wajib sebelum?", ["Pembayaran","Pulang","Makan","Tindakan medis"], 3),
 ("Kode etik bidan?", ["Diskriminasi","Membocorkan rahasia","Menjaga rahasia pasien","Menolak tanpa alasan"], 2),
 ("UU praktik kebidanan?", ["UU No. 36/2009","UU No. 44/2009","UU No. 4/2019","UU No. 36/2014"], 2),
 ("Sanksi pelanggaran etik berat?", ["Teguran lisan","Bonus","Kenaikan jabatan","Pencabutan STR"], 3),
 ("Asas keadilan?", ["Yang kaya didahulukan","Semua sesuai kebutuhan","Yang kenal didahulukan","Acak"], 1),
 ("Kerahasiaan rekam medis diatur?", ["KUHP","Permenkes","KUHAP","UU ITE"], 1),
 ("Tindakan bidan harus sesuai?", ["Trend TikTok","Standar profesi","Kemauan keluarga saja","Perasaan"], 1),
 ("Malpraktik adalah?", ["Tindakan berhasil","Tindakan tidak sesuai standar yang merugikan","Tindakan murah","Tindakan cepat"], 1),
 ("Contoh autonomy?", ["Bidan memaksa","Keluarga memaksa","Dokter putuskan sendiri","Pasien menolak transfusi darah"], 3),
 ("Veracity berarti?", ["Adil","Jujur","Baik","Setia"], 1),
 ("Fidelity berarti?", ["Berbohong","Acuh","Setia pada janji","Kasur"], 2),
 ("Persetujuan pasien tidak sadar oleh?", ["Satpam","Keluarga terdekat","Pasien lain","Tidak perlu"], 1),
 ("Bidan wajib mencatat di?", ["Status WA","Rekam medis","Buku diary","Tidak perlu"], 1),
 ("Aborsi dilarang kecuali?", ["Alasan ekonomi","Indikasi medis darurat","Alasan sekolah","Alasan malu"], 1),
 ("Hak pasien?", ["Dibohongi","Mendapat informasi","Dihukum","Diabaikan"], 1),
 ("Kewajiban bidan?", ["Diskriminasi","Memberi asuhan bermutu","Membiarkan","Minta imbalan berlebih"], 1),
 ("Etika profesi bersumber dari?", ["Uang","Nilai moral profesi","Kekuasaan","Popularitas"], 1),
]

# Gandakan jadi 100 soal biar gak kepanjangan paste-nya, kunci tetap acak
while len(DATA) < 100:
    DATA.extend(DATA[:100-len(DATA)])
DATA = DATA[:100]

random.seed(123)
SOAL_FINAL = []
for q, opsi, idx_benar in DATA:
    benar_text = opsi[idx_benar]
    random.shuffle(opsi)
    new_idx = opsi.index(benar_text)
    SOAL_FINAL.append((q, opsi, new_idx))

def save_to_sheet(nama, nim, kelas, benar, nilai):
    try:
        import gspread
        client = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
        sheet = client.open_by_url(SHEET_URL).sheet1
        sheet.append_row([str(datetime.datetime.now()), nama, nim, kelas, str(benar), str(nilai)])
        return True
    except:
        return False

jawaban = {}
for i, (q, opsi, k) in enumerate(SOAL_FINAL):
    jawaban[i] = st.radio(f"{i+1}. {q}", opsi, key=f"q{i}")

if st.button("KUMPUL & LIHAT NILAI"):
    if not nama or not nim:
        st.warning("Isi Nama & NIM dulu!")
    else:
        benar = 0
        for i, (q, opsi, k) in enumerate(SOAL_FINAL):
            if opsi.index(jawaban[i]) == k:
                benar += 1
        st.success(f"Halo {nama} ({nim}) - Kelas {kelas}")
        st.success(f"Benar: {benar} dari 100 - NILAI: {benar}")
        st.balloons()
        if save_to_sheet(nama, nim, kelas, benar, benar):
            st.success("Nilai masuk Sheet!")
        else:
            st.info("Nilai tampil di atas, screenshot aja. Sheet cek Secrets.")
