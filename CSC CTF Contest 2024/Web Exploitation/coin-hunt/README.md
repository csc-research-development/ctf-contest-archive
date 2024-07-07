# Coin Hunt

Kita harus membeli barang misterius dengan harga yang gak masuk akal dan membaca `secret.txt` untuk mendapatkan flag. Chall ini memanfaatkan vulnerability prototype pollution pada `Object.assign()` untuk mengubah role kita menjadi admin dan untuk menjalankan RCE (Remote Code Execution) pada `child_process.fork`. Tapi, ada sedikit blacklist untuk memfilter karakter `_` sehingga kita tidak bisa langsung menggunakan `__proto__`. Makanya, kita bisa menggunakan double URL encoding untuk meng bypass blacklist tersebut.

## Intended Solve

cek [solver.py](./src/solver.py) untuk full solvernya

## Flag

```
CSC{g4Cor_cuyy_udh_b1s4_b3l1_Mclarenn}
```
