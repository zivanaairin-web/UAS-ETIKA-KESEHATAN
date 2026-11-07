import streamlit as st
import random

st.title("UAS ETIKA PROFESI")

nama = st.text_input("Nama")
nim = st.text_input("NIM")

# 17=A 18=B 19=C 20=D - disembunyiin jadi angka, bukan huruf
D = [
 ("Prinsip mengutamakan kebaikan pasien?", ["Beneficence","Non-maleficence","Justice","Autonomy"], 17),
 ("Prinsip tidak merugikan pasien?", ["Beneficence","Non-maleficence","Veracity","Fidelity"], 18),
 ("Hak pasien menentukan sendiri?", ["Justice","Beneficence","Autonomy","Confidentiality"], 19),
 ("Informed consent wajib sebelum?", ["Pembayaran","Pulang","Makan","Tindakan medis"], 20),
 ("Kode etik bidan?", ["Diskriminasi","Membocorkan rahasia","Menjaga rahasia pasien","Menolak tanpa alasan"], 19),
 ("UU praktik kebidanan?", ["UU 36/2009","UU 44/2009","UU 4/2019","UU 36/2014"], 19),
 ("Sanksi etik berat?", ["Teguran lisan","Bonus","Kenaikan jabatan","Pencabutan STR"], 20),
 ("Asas keadilan?", ["Yang kaya dulu","Semua sesuai kebutuhan","Yang kenal dulu","Acak"], 18),
 ("Kerahasiaan rekam medis?", ["KUHP","Permenkes","KUHAP","UU ITE"], 18),
 ("Tindakan bidan harus sesuai?", ["TikTok","Standar profesi","Kemauan keluarga","Perasaan"], 18),
]
# Gandakan jadi 100 biar gak kepanjangan paste, kunci tetap beda-beda
while len(D) < 100:
    D.extend(D[:100-len(D)])
D = D[:100]

if "F" not in st.session_state:
    T=[]
    for q,o,k in D:
        bt=o[k-17]
        o2=o.copy()
        random.shuffle(o2)
        T.append((q,o2,o2.index(bt)))
    random.shuffle(T)
    st.session_state.F=T

J={}
for i,(q,o,k) in enumerate(st.session_state.F):
    J[i]=st.radio(f"{i+1}. {q}",o,key=f"q{i}")

if st.button("KUMPUL"):
    if not nama or not nim:
        st.warning("Isi Nama NIM dulu")
    else:
        b=sum(1 for i,(q,o,k) in enumerate(st.session_state.F) if o.index(J[i])==k)
        st.success(f"{nama} ({nim}) - Benar {b}/100 Nilai {b}")
        st.balloons()
