# Data Kamus

Dalam `\data\` ada kamus dalam bentuk PDF, XLSX dan CSV. Yang PDF itu sumbernya. Yang XLSX itu adalah data mentah yang aku dapat dari `@UBMalaysia`. Yang CSV itu aku proses guna kod `\src\main.py`. Aku gunakan pemisah `|` kerana ada penggunaan koma dalam komentar.
- Satu benda baru yang aku buat ialah pisahkan "Komentar" dan "Alias"
- Kotak "Warna" aku tak masukkan sebab maklumat warna itu sudah ada dalam kod heksa dan kita boleh hasilkan semula secara aturcara.
- Fail `Bunyi Ajukan (Onom).txt` dipetik dari PDF Wilkinson dan disusun begini:
    - `Bunyi`. Ada bunyi yang mempunyai variasi lain, seperti yang ditulis begini `Bor/ce-/de-/le-`. Itu maksudnya `bor`, `cebor`, `debor`, dan `lebor` merujuk kepada bunyi yang sama. Kalau tiada tanda sempang di hujung, maknanya ambil seluruh ejaan tanpa disambungkan ke bunyi pertama, seperti dalam `Ketimpung/ketimbung`.
    - `Jawi`. Ejaan jawi
    - `Keterangan`. Keterangan (dalam bahasa Melayu) yang aku faham daripada keterangan Wilkinson

## Tambahan
- Aku dapati dalam PDF ada data bahasa Malaysia tapi fail XLSX hanya menyediakan padanan bahasa Indonesia sahaja.
    - [ ] Kutip data bahasa Malaysia itu juga.
- Tak semestinya projek ini guna Python. Aku guna Python sebab itu yang aku kenal jadi dapat proses dengan cepat.