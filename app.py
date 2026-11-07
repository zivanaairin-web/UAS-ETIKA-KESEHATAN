import streamlit as st
import datetime
import random

st.set_page_config(page_title="UAS Etika", layout="centered")
st.title("SOAL PILIHAN GANDA")
st.write("ETIKA PROFESI DAN HUKUM KESEHATAN - 100 Soal | Jawaban Diacak")

nama = st.text_input("Nama Lengkap")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1tbEXyKC_BhCNBCMPvVGQ_KrJQ9X3YmKpCLeTvZ7QzI4/edit?gid=0#gid=0"

# KUNCI DISEMBUNYIKAN: angka 17=A, 18=B, 19=C, 20=D
# Mahasiswa liat 17,18,19,20 gak akan tau itu kunci
# Jadi di GitHub gak ada tulisan A/B/C/D sama sekali
DATA = [
 ("Prinsip etika yang mengutamakan kebaikan pasien?", ["Beneficence","Non-maleficence","Justice","Autonomy"], 17),
 ("Prinsip tidak merugikan pasien?", ["Beneficence","Non-maleficence","Veracity","Fidelity"], 18),
 ("Hak pasien menentukan sendiri?", ["Justice","Beneficence","Autonomy","Confidentiality"], 19),
 ("Informed consent wajib sebelum?", ["Pembayaran","Pulang","Makan","Tindakan medis"], 20),
 ("Kode etik bidan?", ["Diskriminasi","Membocorkan rahasia","Menjaga rahasia pasien","Menolak tanpa alasan"], 19),
 ("UU praktik kebidanan?", ["UU No. 36/2009","UU No. 44/2009","UU No. 4/2019","UU No. 36/2014"], 19),
 ("Sanksi pelanggaran etik berat?", ["Teguran lisan","Bonus","Kenaikan jabatan","Pencabutan STR"], 20),
 ("Asas keadilan?", ["Yang kaya didahulukan","Semua sesuai kebutuhan","Yang kenal didahulukan","Acak"], 18),
 ("Kerahasiaan rekam medis diatur?", ["KUHP","Permenkes","KUHAP","UU ITE"], 18),
 ("Tindakan bidan harus sesuai?", ["Trend TikTok","Standar profesi","Kemauan keluarga saja","Perasaan"], 18),
 ("Malpraktik adalah?", ["Tindakan berhasil","Tindakan tidak sesuai standar yang merugikan","Tindakan murah","Tindakan cepat"], 18),
 ("Contoh autonomy?", ["Bidan memaksa","Keluarga memaksa","Dokter putuskan sendiri","Pasien menolak transfusi darah"], 20),
 ("Veracity berarti?", ["Adil","Jujur","Baik","Setia"], 18),
 ("Fidelity berarti?", ["Berbohong","Acuh","Setia pada janji","Kasur"], 19),
 ("Persetujuan pasien tidak sadar oleh?", ["Satpam","Keluarga terdekat","Pasien lain","Tidak perlu"], 18),
 ("Bidan wajib mencatat di?", ["Status WA","Rekam medis","Buku diary","Tidak perlu"], 18),
 ("Aborsi dilarang kecuali?", ["Alasan ekonomi","Indikasi medis darurat","Alasan sekolah","Alasan malu"], 18),
 ("Hak pasien?", ["Dibohongi","Mendapat informasi","Dihukum","Diabaikan"], 18),
 ("Kewajiban bidan?", ["Diskriminasi","Memberi asuhan bermutu","Membiarkan","Minta imbalan berlebih"], 18),
 ("Etika profesi bersumber dari?", ["Uang","Nilai moral profesi","Kekuasaan","Popularitas"], 18),
 ("Jika pasien menolak dirujuk?", ["Memaksa","Memberi penjelasan risiko & minta tanda tangan penolakan","Membiarkan","Marah"], 18),
 ("Confidentiality berarti?", ["Menyebar rahasia","Menjaga rahasia","Membuka aib","Gosip"], 18),
 ("Surat Tanda Registrasi Bidan?", ["KTP","STR","SIPB","SIM"], 18),
 ("SIPB diterbitkan oleh?", ["RT","Dinas Kesehatan Kab/Kota","Kades","Camat"], 18),
 ("Masa berlaku STR?", ["1 tahun","10 tahun","5 tahun","Seumur hidup"], 19),
 ("Tindakan tanpa kewenangan?", ["Prestasi","Pelanggaran hukum","Pujian","Biasa saja"], 18),
 ("Saat gawat darurat, bidan?", ["Menolak","Memberi pertolongan sesuai kemampuan","Kabur","Minta bayaran dulu"], 18),
 ("4 prinsip bioetik?", ["Uang, Pangkat, Jabatan, Popularitas","Beneficence, Non-maleficence, Autonomy, Justice","A,B,C,D","Tidak ada"], 18),
 ("Euthanasia di Indonesia?", ["Dibolehkan","Dilarang","Wajib","Dianjurkan"], 18),
 ("Bidan harus memiliki?", ["Modal besar","Kompetensi","Followers banyak","Mobil"], 18),
 ("Kolaborasi bidan-dokter?", ["Persaingan","Kolaborasi interprofesi","Musuhan","Cuek"], 18),
 ("Jika salah tindakan?", ["Menutupi","Jujur & bertanggung jawab","Menyalahkan pasien","Kabur"], 18),
 ("Hak bayi baru lahir?", ["Dibiarkan","Mendapat ASI & perawatan","Tidak ditimbang","Tidak imunisasi"], 18),
 ("Pelayanan berpusat pada?", ["Uang","Ibu dan anak","Bidan","RS"], 18),
 ("Persetujuan setelah penjelasan?", ["Anamnesa","Informed consent","Informed choice","Diagnosa"], 18),
 ("Informed choice menekankan?", ["Paksaan","Hak memilih pasien","Keuntungan bidan","Cepat selesai"], 18),
 ("Contoh justice?", ["Yang bayar lebih dulu","Sesuai kebutuhan pasien","Keluarga sendiri dulu","Acak"], 18),
 ("Bidan tidak boleh bedakan berdasar?", ["Penyakit","SARA","Kebutuhan","Kondisi"], 18),
 ("Rekam medis disimpan minimal?", ["1 hari","1 bulan","5 tahun","Dibuang"], 19),
 ("Yang boleh buka rekam medis tanpa izin?", ["Tetangga","Pengadilan","Teman","Media"], 18),
 ("Kode etik IBI mengatur?", ["Gaji","Perilaku bidan","Seragam","Liburan"], 18),
 ("IBI singkatan?", ["Ikatan Bidan Internasional","Ikatan Bidan Indonesia","Ikatan Bapak Indonesia","Ikatan Bisnis Indonesia"], 18),
 ("Bidan ikuti ilmu baru via?", ["Tidur","Pendidikan berkelanjutan","Arisan","Main game"], 18),
 ("Tindakan melanggar hukum?", ["Sesuai hukum","Melawan hukum","Legal","Halal"], 18),
 ("Perlindungan hukum bidan?", ["Tidak ada","UU Kesehatan","Hukum adat","Hukum rimba"], 18),
 ("Pasien boleh menggugat jika?", ["Dilayani baik","Dirugikan tindakan","Disapa ramah","Diberi obat"], 18),
 ("Hormati budaya pasien?", ["Keuangan","Autonomy & Justice","Politik","Ego"], 18),
 ("Komunikasi efektif?", ["Judes","Empati & jelas","Berbelit","Diam saja"], 18),
 ("Pelanggaran disiplin?", ["Membantu persalinan normal","Praktik tanpa SIPB","Cuci tangan","Pakai APD"], 18),
 ("Tujuan hukum kesehatan?", ["Menyusahkan","Melindungi pasien & nakes","Cari uang","Hukuman"], 18),
 ("Asuhan harus berdasar?", ["Katanya","Evidence Based","Mitos","Dugaan"], 18),
 ("Bidan wajib merujuk jika?", ["Pasien kaya","Di luar kewenangan","Pasien miskin","Senggang"], 18),
 ("Kerugian akibat kelalaian?", ["Prestasi","Negligence","Keberuntungan","Hadiah"], 18),
 ("Contoh negligence?", ["Cek tensi","Lupa cek tensi","Mencatat","Menyapa"], 18),
 ("Jaga kebersihan untuk?", ["Gaya","Mencegah infeksi","Foto","Pamer"], 18),
 ("Otonomi ibu hamil?", ["Memaksa bidan","Menolak tindakan","Melawan hukum","Tidak kontrol"], 18),
 ("Pelayanan tidak diskriminatif?", ["Ketidakadilan","Keadilan","Pilih kasih","Korupsi"], 18),
 ("Surat persetujuan ditandatangani?", ["Bidan saja","Pasien / wali","Satpam","Tidak perlu"], 18),
 ("Jika pasien anak, consent oleh?", ["Teman","Orang tua","Diri sendiri","Tetangga"], 18),
 ("Beneficence pada nifas?", ["Membiarkan","Memberi konseling menyusui","Menyalahkan","Mengabaikan"], 18),
 ("Bidan dilarang di luar?", ["Rumah","Kompetensi","Kota","Negara"], 18),
 ("Tanggung jawab bidan?", ["Lari","Tanggung gugat profesi","Sembunyi","Diam"], 18),
 ("Penelitian harus ada?", ["Uang","Ethical clearance","Izin RT","Tidak perlu"], 18),
 ("Responden harus diberi?", ["Uang banyak","Informed consent","Ancaman","Paksaan"], 18),
 ("Privasi pasien?", ["Diabaikan","Dijaga","Disebar","Difoto"], 18),
 ("Bidan harus netral dalam?", ["Gaji","Politik & SARA","Seragam","Jam kerja"], 18),
 ("Hak bidan?", ["Menghina pasien","Mendapat perlindungan hukum","Minta uang berlebih","Menolak tanpa alasan"], 18),
 ("Kewajiban K3?", ["Membahayakan","Menjaga keselamatan","Acuh","Tidak peduli"], 18),
 ("Laporan malpraktik ke?", ["Polisi tidur","Majelis Kehormatan Etik","RT","Medsos"], 18),
 ("Pelanggar etik disidang oleh?", ["Ketua RT","Majelis etik IBI","Kades","Teman"], 18),
 ("Pertolongan perdarahan?", ["Lambat","Cepat & sesuai prosedur","Dibiarkan","Difoto dulu"], 18),
 ("Non-maleficence obat?", ["Asal kasih","Tidak salah dosis","Dosis berlebih","Tidak dicek"], 18),
 ("Dokumentasi harus?", ["Bohong","Jujur & lengkap","Kosong","Asal"], 18),
 ("Jika pasien meninggal?", ["Menyembunyikan","Memberi penjelasan jujur ke keluarga","Menyalahkan","Kabur"], 18),
 ("Asuhan sayang ibu?", ["Membentak","Menghormati & mendukung ibu","Menyalahkan","Mengabaikan"], 18),
 ("Kelalaian sebabkan kematian?", ["Pujian","Pidana","Hadiah","Naik gaji"], 18),
 ("Jaga kompetensi?", ["Tidur","Pelatihan & seminar","Main HP","Gosip"], 18),
 ("Hubungan bidan-pasien?", ["Kecurigaan","Kepercayaan","Uang","Paksaan"], 18),
 ("Contoh veracity?", ["Berbohong","Menjelaskan kondisi sebenarnya","Menutupi","Melebih-lebihkan"], 18),
 ("Bidan tidak boleh terima suap?", ["Biasa","Etik & hukum","Wajib","Bagus"], 18),
 ("ASI eksklusif hak?", ["Bidan","Bayi","RS","Suami"], 18),
 ("Bidan dukung program?", ["Balapan","Stunting & KIA","Game","Arisan"], 18),
 ("Kekerasan dalam pelayanan?", ["Menyapa ramah","Membentak pasien","Memberi edukasi","Mendengarkan"], 18),
 ("Bidan harus menolak jika diminta?", ["Menolong persalinan","Menggugurkan tanpa indikasi medis","Memberi vitamin","Mengukur tensi"], 18),
 ("Saat rujukan, bidan wajib?", ["Melepas saja","Mendampingi & kirim dokumen","Tidak peduli","Minta uang"], 18),
 ("SOP dibuat untuk?", ["Menyusahkan","Keselamatan pasien","Formalitas","Pajangan"], 18),
 ("Praktik mandiri harus punya?", ["Cuma nekat","Tempat & izin sesuai aturan","Tidak perlu izin","Cuma HP"], 18),
 ("Etika medsos bidan?", ["Posting semua","Tidak memposting rahasia pasien","Buka aib","Flexing"], 18),
 ("Jika pasien komplain?", ["Marah balik","Mendengarkan & menjelaskan","Blokir","Acuh"], 18),
 ("Prinsip utama pelayanan?", ["Bidan untung","Ibu & anak selamat","Cepat selesai","Murah"], 18),
 ("Hak reproduksi?", ["Dipaksa","Hak memilih kontrasepsi","Dilarang","Diabaikan"], 18),
 ("Tindakan invasif harus dengan?", ["Diam-diam","Izin pasien","Paksaan","Tanpa alat"], 18),
 ("Dokumen legal?", ["Coretan","Partograf & rekam medis","Foto selfie","Chat"], 18),
 ("Laporkan penyakit menular ke?", ["Tetangga","Dinas Kesehatan","Media","Tidak perlu"], 18),
 ("Saat bencana, bidan tetap wajib?", ["Kabur","Memberi pertolongan","Sembunyi","Libur"], 18),
 ("Etika profesi bedakan bidan dengan?", ["Dokter","Dukun","Perawat","Semua nakes"], 18),
 ("Bidan jaga nama baik?", ["Diri sendiri saja","Profesi","Tidak perlu","Orang lain"], 18),
 ("Konflik sejawat?", ["Berantem","Musyawarah & etik","Gosip","Diam"], 18),
 ("Tujuan belajar etika & hukum?", ["Lulus saja","Praktik aman & bermoral","Gelar saja","Gaji"], 18),
 ("Moto pelayanan etis?", ["Cepat kaya","Sayang ibu, sayang bayi, profesional","Terkenal","Santai"], 18),
]

# ACAK JAWABAN - kode 17,18,19,20 diubah jadi 0,1,2,3 dulu baru diacak
# Ini yang bikin jawaban selalu acak, gak bisa dihafal
if "soal_final" not in st.session_state:
    temp = []
    for q, opsi, kode in DATA:
        idx_asli = kode - 17
        benar_text = opsi[idx_asli]
        opsi2 = opsi.copy()
        random.shuffle(opsi2)
        new_idx = opsi2.index(benar_text)
        temp.append((q, opsi2, new_idx))
    # Acak urutan soal juga
    random.shuffle(temp)
    st.session_state.soal_final = temp

SOAL_FINAL = st.session_state.soal_final

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
