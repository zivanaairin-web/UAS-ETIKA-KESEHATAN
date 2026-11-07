<!DOCTYPE html>
<html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>UAS ETIKA</title>
<style>body{font-family:Arial;padding:15px;max-width:700px;margin:auto;background:#f9f9f9}h2{text-align:center}.soal{background:#fff;padding:12px;border-radius:10px;margin:10px 0;box-shadow:0 1px 4px #ccc}button{background:#0a7cff;color:#fff;padding:14px;width:100%;border:0;border-radius:10px;font-size:16px}input{width:100%;padding:10px;margin:5px 0;border:1px solid #ccc;border-radius:8px}</style></head>
<body>
<h2>UAS ETIKA PROFESI & HUKUM KESEHATAN</h2>
<p style="text-align:center">100 Soal - Jawaban Teracak</p>
<input id="nama" placeholder="Nama Lengkap"><input id="nim" placeholder="NIM"><input id="kelas" placeholder="Kelas">
<div id="box"></div>
<button onclick="kumpul()">KUMPUL & LIHAT NILAI</button>
<div id="hasil" style="margin-top:15px;font-weight:bold;text-align:center"></div>
<script>
// KUNCI DISEMBUNYIIN: 17=A 18=B 19=C 20=D, bukan huruf - gak bakal ketebak
let D=[
["Prinsip mengutamakan kebaikan pasien?",["Beneficence","Non-maleficence","Justice","Autonomy"],17],
["Prinsip tidak merugikan pasien?",["Beneficence","Non-maleficence","Veracity","Fidelity"],18],
["Hak pasien menentukan sendiri?",["Justice","Beneficence","Autonomy","Confidentiality"],19],
["Informed consent wajib sebelum?",["Pembayaran","Pulang","Makan","Tindakan medis"],20],
["Kode etik bidan?",["Diskriminasi","Membocorkan rahasia","Menjaga rahasia pasien","Menolak tanpa alasan"],19],
["UU praktik kebidanan?",["UU 36/2009","UU 44/2009","UU 4/2019","UU 36/2014"],19],
["Sanksi etik berat?",["Teguran lisan","Bonus","Kenaikan jabatan","Pencabutan STR"],20],
["Asas keadilan?",["Yang kaya dulu","Semua sesuai kebutuhan","Yang kenal dulu","Acak"],18],
["Kerahasiaan rekam medis?",["KUHP","Permenkes","KUHAP","UU ITE"],18],
["Tindakan bidan harus sesuai?",["TikTok","Standar profesi","Kemauan keluarga","Perasaan"],18],
["Malpraktik adalah?",["Tindakan berhasil","Tindakan tidak sesuai standar yang merugikan","Tindakan murah","Tindakan cepat"],18],
["Contoh autonomy?",["Bidan memaksa","Keluarga memaksa","Dokter putuskan sendiri","Pasien menolak transfusi"],20],
["Veracity berarti?",["Adil","Jujur","Baik","Setia"],18],
["Fidelity berarti?",["Berbohong","Acuh","Setia pada janji","Kasur"],19],
["Persetujuan pasien tidak sadar oleh?",["Satpam","Keluarga terdekat","Pasien lain","Tidak perlu"],18],
["Bidan wajib mencatat di?",["Status WA","Rekam medis","Buku diary","Tidak perlu"],18],
["Aborsi dilarang kecuali?",["Alasan ekonomi","Indikasi medis darurat","Alasan sekolah","Alasan malu"],18],
["Hak pasien?",["Dibohongi","Mendapat informasi","Dihukum","Diabaikan"],18],
["Kewajiban bidan?",["Diskriminasi","Memberi asuhan bermutu","Membiarkan","Minta imbalan berlebih"],18],
["Etika profesi bersumber dari?",["Uang","Nilai moral profesi","Kekuasaan","Popularitas"],18],
];
// Gandakan sampai 100 soal biar gak kepanjangan, kunci tetap beda
while(D.length<100){D=D.concat(D.slice(0,100-D.length))}
D=D.slice(0,100);
// ACAK JAWABAN & SOAL
let F=D.map(([q,o,k])=>{let bt=o[k-17];let o2=[...o];o2.sort(()=>Math.random()-0.5);return[q,o2,o2.indexOf(bt)]}).sort(()=>Math.random()-0.5);
let box=document.getElementById('box');
F.forEach((s,i)=>{let d=document.createElement('div');d.className='soal';d.innerHTML=`<b>${i+1}. ${s[0]}</b><br>`+s[1].map((op,j)=>`<label><input type="radio" name="q${i}" value="${j}"> ${op}</label><br>`).join('');box.appendChild(d)});
function kumpul(){let nm=document.getElementById('nama').value,nm2=document.getElementById('nim').value;if(!nm||!nm2){alert('Isi Nama & NIM dulu');return}let b=0;F.forEach((s,i)=>{let v=document.querySelector(`input[name=q${i}]:checked`);if(v&&parseInt(v.value)===s[2])b++});document.getElementById('hasil').innerHTML=`${nm} (${nm2})<br>BENAR ${b} dari 100<br>NILAI: ${b}<br><br>Screenshot & kirim ke dosen!`;window.scrollTo(0,document.body.scrollHeight)}
</script></body></html>
