# Judul Soal

mengenalkan player tentang:
- request header
- tac commandline to stdout
- environment variable yang bisa dipanggil dalam cmd
  
```
WU:
setelah memasukan regis, melakukan get request yang diubah secara manual dari post pada page "Inject.php".
tak lupa player harus mendecode random yaitu $randy untuk mendapatkan angkanya.
dari sana player dengan intended payload "tac${IFS}${HOME:0:1}tmp${HOME:0:1}flag_$randy.txt", melakukan command injection
```
