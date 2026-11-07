import streamlit as st
import datetime
import random

st.set_page_config(page_title="UAS Etika Profesi & Hukum Kesehatan", layout="centered")
st.title("SOAL PILIHAN GANDA")
st.write("**ETIKA PROFESI DAN HUKUM KESEHATAN - Pelayanan Kebidanan**")

nama = st.text_input("Nama Lengkap")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1tbEXyKC_BhCNBCMPvVGQ_KrJQ9X3YmKpCLeTvZ7QzI4/edit?gid=0#gid=0"

# SOAL SAJA, TANPA KUNCI - JADI MAHASISWA BUKA GITHUB GAK LIAT JAWABAN
SOAL = [
    ("1. Prinsip etika yang mengutamakan kebaikan pasien?", ["Beneficence", "Non-maleficence", "Justice", "Autonomy"]),
    ("2. Prinsip tidak merugikan pasien?", ["Beneficence", "Non-maleficence", "Veracity", "Fidelity"]),
    ("3. Hak pasien menentukan sendiri?", ["Justice", "Beneficence", "Autonomy", "Confidentiality"]),
    ("4. Informed consent wajib sebelum?", ["Pembayaran", "Pulang", "Makan", "Tindakan medis"]),
    ("5. Kode etik bidan?", ["Diskriminasi", "Membocorkan rahasia", "Menjaga rahasia pasien", "Menolak tanpa alasan"]),
    ("6. UU praktik kebidanan?", ["UU No. 36/2009", "UU No. 44/2009", "UU No. 4/2019", "UU No. 36/2014"]),
    ("7. Sanksi pelanggaran etik berat?", ["Teguran lisan", "Bonus", "Kenaikan jabatan", "Pencabutan STR"]),
    ("8. Asas keadilan?", ["Yang kaya didahulukan", "Semua sesuai kebutuhan", "Yang kenal didahulukan", "Acak"]),
    ("9. Kerahasiaan rekam medis diatur?", ["KUHP", "Permenkes", "KUHAP", "UU ITE"]),
    ("10. Tindakan bidan harus sesuai?", ["Trend TikTok", "Standar profesi", "Kemauan keluarga saja", "Perasaan"]),
    ("11. Malpraktik adalah?", ["Tindakan berhasil", "Tindakan tidak sesuai standar yang merugikan", "Tindakan murah", "Tindakan cepat"]),
    ("12. Contoh autonomy?", ["Bidan memaksa", "Keluarga memaksa", "Dokter putuskan sendiri", "Pasien menolak transfusi darah"]),
    ("13. Veracity berarti?", ["Adil", "Jujur", "Baik", "Setia"]),
    ("14. Fidelity berarti?", ["Berbohong", "Acuh", "Setia pada janji", "Kasur"]),
    ("15. Persetujuan pasien tidak sadar oleh?", ["Satpam", "Keluarga terdekat", "Pasien lain", "Tidak perlu"]),
    ("16. Bidan wajib mencatat di?", ["Status WA", "Rekam medis", "Buku diary", "Tidak perlu"]),
    ("17. Aborsi dilarang kecuali?", ["Alasan ekonomi", "Indikasi medis darurat", "Alasan sekolah", "Alasan malu"]),
    ("18. Hak pasien?", ["Dibohongi", "Mendapat informasi", "Dihukum", "Diabaikan"]),
    ("19. Kewajiban bidan?", ["Diskriminasi", "Memberi asuhan bermutu", "Membiarkan", "Minta imbalan berlebih"]),
    ("20. Etika profesi bersumber dari?", ["Uang", "Nilai moral profesi", "Kekuasaan", "Popularitas"]),
    ("21. Jika pasien menolak dirujuk?", ["Memaksa", "Memberi penjelasan risiko & minta tanda tangan penolakan", "Membiarkan", "Marah"]),
    ("22. Confidentiality berarti?", ["Menyebar rahasia", "Menjaga rahasia", "Membuka aib", "Gosip"]),
    ("23. Surat Tanda Registrasi Bidan?", ["KTP", "STR", "SIPB", "SIM"]),
    ("24. SIPB diterbitkan oleh?", ["RT", "Dinas Kesehatan Kab/Kota", "Kades", "Camat"]),
    ("25. Masa berlaku STR?", ["1 tahun", "10 tahun", "5 tahun", "Seumur hidup"]),
    ("26. Tindakan tanpa kewenangan?", ["Prestasi", "Pelanggaran hukum", "Pujian", "Biasa saja"]),
    ("27. Saat gawat darurat, bidan?", ["Menolak", "Memberi pertolongan sesuai kemampuan", "Kabur", "Minta bayaran dulu"]),
    ("28. 4 prinsip bioetik?", ["Uang, Pangkat, Jabatan, Popularitas", "Beneficence, Non-maleficence, Autonomy, Justice", "A,B,C,D", "Tidak ada"]),
    ("29. Euthanasia di Indonesia?", ["Dibolehkan", "Dilarang", "Wajib", "Dianjurkan"]),
    ("30. Bidan harus memiliki?", ["Modal besar", "Kompetensi", "Followers banyak", "Mobil"]),
    ("31. Kolaborasi bidan-dokter?", ["Persaingan", "Kolaborasi interprofesi", "Musuhan", "Cuek"]),
    ("32. Jika salah tindakan?", ["Menutupi", "Jujur & bertanggung jawab", "Menyalahkan pasien", "Kabur"]),
    ("33. Hak bayi baru lahir?", ["Dibiarkan", "Mendapat ASI & perawatan", "Tidak ditimbang", "Tidak imunisasi"]),
    ("34. Pelayanan berpusat pada?", ["Uang", "Ibu dan anak", "Bidan", "RS"]),
    ("35. Persetujuan setelah penjelasan?", ["Anamnesa", "Informed consent", "Informed choice", "Diagnosa"]),
    ("36. Informed choice menekankan?", ["Paksaan", "Hak memilih pasien", "Keuntungan bidan", "Cepat selesai"]),
    ("37. Contoh justice?", ["Yang bayar lebih dulu", "Sesuai kebutuhan pasien", "Keluarga sendiri dulu", "Acak"]),
    ("38. Bidan tidak boleh bedakan berdasar?", ["Penyakit", "SARA", "Kebutuhan", "Kondisi"]),
    ("39. Rekam medis disimpan minimal?", ["1 hari", "1 bulan", "5 tahun", "Dibuang"]),
    ("40. Yang boleh buka rekam medis tanpa izin?", ["Tetangga", "Pengadilan", "Teman", "Media"]),
    ("41. Kode etik IBI mengatur?", ["Gaji", "Perilaku bidan", "Seragam", "Liburan"]),
    ("42. IBI singkatan?", ["Ikatan Bidan Internasional", "Ikatan Bidan Indonesia", "Ikatan Bapak Indonesia", "Ikatan Bisnis Indonesia"]),
    ("43. Bidan ikuti ilmu baru via?", ["Tidur", "Pendidikan berkelanjutan", "Arisan", "Main game"]),
    ("44. Tindakan melanggar hukum?", ["Sesuai hukum", "Melawan hukum", "Legal", "Halal"]),
    ("45. Perlindungan hukum bidan?", ["Tidak ada", "UU Kesehatan", "Hukum adat", "Hukum rimba"]),
    ("46. Pasien boleh menggugat jika?", ["Dilayani baik", "Dirugikan tindakan", "Disapa ramah", "Diberi obat"]),
    ("47. Hormati budaya pasien?", ["Keuangan", "Autonomy & Justice", "Politik", "Ego"]),
    ("48. Komunikasi efektif?", ["Judes", "Empati & jelas", "Berbelit", "Diam saja"]),
    ("49. Pelanggaran disiplin?", ["Membantu persalinan normal", "Praktik tanpa SIPB", "Cuci tangan", "Pakai APD"]),
    ("50. Tujuan hukum kesehatan?", ["Menyusahkan", "Melindungi pasien & nakes", "Cari uang", "Hukuman"]),
    ("51. Asuhan harus berdasar?", ["Katanya", "Evidence Based", "Mitos", "Dugaan"]),
    ("52. Bidan wajib merujuk jika?", ["Pasien kaya", "Di luar kewenangan", "Pasien miskin", "Senggang"]),
    ("53. Kerugian akibat kelalaian?", ["Prestasi", "Negligence", "Keberuntungan", "Hadiah"]),
    ("54. Contoh negligence?", ["Cek tensi", "Lupa cek tensi", "Mencatat", "Menyapa"]),
    ("55. Jaga kebersihan untuk?", ["Gaya", "Mencegah infeksi", "Foto", "Pamer"]),
    ("56. Otonomi ibu hamil?", ["Memaksa bidan", "Menolak tindakan", "Melawan hukum", "Tidak kontrol"]),
    ("57. Pelayanan tidak diskriminatif?", ["Ketidakadilan", "Keadilan", "Pilih kasih", "Korupsi"]),
    ("58. Surat persetujuan ditandatangani?", ["Bidan saja", "Pasien / wali", "Satpam", "Tidak perlu"]),
    ("59. Jika pasien anak, consent oleh?", ["Teman", "Orang tua", "Diri sendiri", "Tetangga"]),
    ("60. Beneficence pada nifas?", ["Membiarkan", "Memberi konseling menyusui", "Menyalahkan", "Mengabaikan"]),
    ("61. Bidan dilarang di luar?", ["Rumah", "Kompetensi", "Kota", "Negara"]),
    ("62. Tanggung jawab bidan?", ["Lari", "Tanggung gugat profesi", "Sembunyi", "Diam"]),
    ("63. Penelitian harus ada?", ["Uang", "Ethical clearance", "Izin RT", "Tidak perlu"]),
    ("64. Responden harus diberi?", ["Uang banyak", "Informed consent", "Ancaman", "Paksaan"]),
    ("65. Privasi pasien?", ["Diabaikan", "Dijaga", "Disebar", "Difoto"]),
    ("66. Bidan harus netral dalam?", ["Gaji", "Politik & SARA", "Seragam", "Jam kerja"]),
    ("67. Hak bidan?", ["Menghina pasien", "Mendapat perlindungan hukum", "Minta uang berlebih", "Menolak tanpa alasan"]),
    ("68. Kewajiban K3?", ["Membahayakan", "Menjaga keselamatan", "Acuh", "Tidak peduli"]),
    ("69. Laporan malpraktik ke?", ["Polisi tidur", "Majelis Kehormatan Etik", "RT", "Medsos"]),
    ("70. Pelanggar etik disidang oleh?", ["Ketua RT", "Majelis etik IBI", "Kades", "Teman"]),
    ("71. Pertolongan perdarahan?", ["Lambat", "Cepat & sesuai prosedur", "Dibiarkan", "Difoto dulu"]),
    ("72. Non-maleficence obat?", ["Asal kasih", "Tidak salah dosis", "Dosis berlebih", "Tidak dicek"]),
    ("73. Dokumentasi harus?", ["Bohong", "Jujur & lengkap", "Kosong", "Asal"]),
    ("74. Jika pasien meninggal?", ["Menyembunyikan", "Memberi penjelasan jujur ke keluarga", "Menyalahkan", "Kabur"]),
    ("75. Asuhan sayang ibu?", ["Membentak", "Menghormati & mendukung ibu", "Menyalahkan", "Mengabaikan"]),
    ("76. Kelalaian sebabkan kematian?", ["Pujian", "Pidana", "Hadiah", "Naik gaji"]),
    ("77. Jaga kompetensi?", ["Tidur", "Pelatihan & seminar", "Main HP", "Gosip"]),
    ("78. Hubungan bidan-pasien?", ["Kecurigaan", "Kepercayaan", "Uang", "Paksaan"]),
    ("79. Contoh veracity?", ["Berbohong", "Menjelaskan kondisi sebenarnya", "Menutupi", "Melebih-lebihkan"]),
    ("80. Bidan tidak boleh terima suap?", ["Biasa", "Etik & hukum", "Wajib", "Bagus"]),
    ("81. ASI eksklusif hak?", ["Bidan", "Bayi", "RS", "Suami"]),
    ("82. Bidan dukung program?", ["Balapan", "Stunting & KIA", "Game", "Arisan"]),
    ("83. Kekerasan dalam pelayanan?", ["Menyapa ramah", "Membentak pasien", "Memberi edukasi", "Mendengarkan"]),
    ("84. Bidan harus menolak jika diminta?", ["Menolong persalinan", "Menggugurkan tanpa indikasi medis", "Memberi vitamin", "Mengukur tensi"]),
    ("85. Saat rujukan, bidan wajib?", ["Melepas saja", "Mendampingi & kirim dokumen", "Tidak peduli", "Minta uang"]),
    ("86. SOP dibuat untuk?", ["Menyusahkan", "Keselamatan pasien", "Formalitas", "Pajangan"]),
    ("87. Praktik mandiri harus punya?", ["Cuma nekat", "Tempat & izin sesuai aturan", "Tidak perlu izin", "Cuma HP"]),
    ("88. Etika medsos bidan?", ["Posting semua", "Tidak memposting rahasia pasien", "Buka aib", "Flexing"]),
    ("89. Jika pasien komplain?", ["Marah balik", "Mendengarkan & menjelaskan", "Blokir", "Acuh"]),
    ("90. Prinsip utama pelayanan?", ["Bidan untung", "Ibu & anak selamat", "Cepat selesai", "Murah"]),
    ("91. Hak reproduksi?", ["Dipaksa", "Hak memilih kontrasepsi", "Dilarang", "Diabaikan"]),
    ("92. Tindakan invasif harus dengan?", ["Diam-diam", "Izin pasien", "Paksaan", "Tanpa alat"]),
    ("93. Dokumen legal?", ["Coretan", "Partograf & rekam medis", "Foto selfie", "Chat"]),
    ("94. Laporkan penyakit menular ke?", ["Tetangga", "Dinas Kesehatan", "Media", "Tidak perlu"]),
    ("95. Saat bencana, bidan tetap wajib?", ["Kabur", "Memberi pertolongan", "Sembunyi", "Libur"]),
    ("96. Etika profesi bedakan bidan dengan?", ["Dokter", "Dukun", "Perawat", "Semua nakes"]),
    ("97. Bidan jaga nama baik?", ["Diri sendiri saja", "Profesi", "Tidak perlu", "Orang lain"]),
    ("98. Konflik sejawat?", ["Berantem", "Musyawarah & etik", "Gosip", "Diam"]),
    ("99. Tujuan belajar etika & hukum?", ["Lulus saja", "Praktik aman & bermoral", "Gelar saja", "Gaji"]),
    ("100. Moto pelayanan etis?", ["Cepat kaya", "Sayang ibu, sayang bayi, profesional", "Terkenal", "Santai"]),
]

# KUNCI DIAMBIL DARI SECRETS - TIDAK ADA DI GITHUB
# Cara isi Secrets ada di bawah
try:
    KUNCI = st.secrets["kunci_jawaban"].split(",")
except:
    # fallback kalau belum set secrets - biar app tetap jalan
    KUNCI = ["A","B","C","D"]*25

# ACAK POSISI JAWABAN BIAR GAK BISA DIHAFAL - tapi kunci tetap ngikut
random.seed(42)
SOAL_ACAK = []
for i, (q, opsi) in enumerate(SOAL):
    benar_huruf = KUNCI[i].strip()
    benar_text = opsi[["A","B","C","D"].index(benar_huruf)]
    random.shuffle(opsi)
    new_kunci = ["A","B","C","D"][opsi.index(benar_text)]
    SOAL_ACAK.append((q, opsi, new_kunci))
SOAL_FINAL = SOAL_ACAK

def save_to_sheet(nama, nim, kelas, benar, nilai):
    try:
        import gspread
        client = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
        sheet = client.open_by_url(SHEET_URL).sheet1
        sheet.append_row([str(datetime.datetime.now()), nama, nim, kelas, str(benar), str(nilai)])
        return True
    except Exception as e:
        return False

jawaban_user = {}
for q, opsi, kunci in SOAL_FINAL:
    jawaban_user[q] = st.radio(q, opsi, key=q)

if st.button("KUMPUL & LIHAT NILAI"):
    if not nama or not nim:
        st.warning("Isi Nama & NIM dulu!")
    else:
        benar = 0
        for q, opsi, kunci in SOAL_FINAL:
            idx = opsi.index(jawaban_user[q])
            huruf = ["A","B","C","D"][idx]
            if huruf == kunci:
                benar += 1
        nilai = benar * 1
        st.success(f"Halo {nama} ({nim}) - Kelas {kelas}")
        st.success(f"Benar: {benar} dari 100 - NILAI: {nilai}")
        st.balloons()
        save_to_sheet(nama, nim, kelas, benar, nilai)
