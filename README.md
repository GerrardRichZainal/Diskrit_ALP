# ALP ini Dikerjakan Oleh : 
1. Gerrard Rich Zainal (0806022410004)
2. Stella J. Chandra (0806022410009)
3. Vallerio Rayford Phoatmojo (0806022410006)

# Implementasi Teori Graf Menggunakan Python (NetworkX)

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi konsep **Teori Graf** menggunakan bahasa pemrograman **Python** dan library **NetworkX**.  
Tujuan utama proyek ini adalah untuk memahami dan menerapkan operasi dasar graf seperti penambahan simpul dan sisi, visualisasi graf, pencarian jalur terpendek, serta penerapan metode-metode graf untuk menyelesaikan soal **AFL-3** pada mata kuliah Aljabar Linear dan Diskrit.

Proyek ini mengimplementasikan konsep **Object Oriented Programming (OOP)** dengan membuat class `Graf` sebagai representasi graf.

---

## 🛠️ Tools & Library
- Python 3.x
- NetworkX
- Matplotlib

Install library yang dibutuhkan:
```bash
pip install networkx matplotlib
```

## Struktur Folder
```text
project_graf/
│
├── theorygraph.py   # Class Graf dan seluruh metode graf
├── main.py          # Implementasi dan penyelesaian soal ALP & AFL-3
└── README.md        # Dokumentasi proyek
```
## 🧩 Implementasi Kelas Graf
Class Graf berada pada file theorygraph.py dan memiliki metode dasar sebagai berikut:
## 🔹 Metode Dasar
- add_node(node) → menambahkan simpul
- add_edge(u, v, weight) → menambahkan sisi berbobot
- visualize_graph() → menampilkan visualisasi graf
- shortest_path(source, target) → mencari jalur terpendek
- visual_shortest_path(source, target) → visualisasi jalur terpendek
Semua metode dasar telah diuji dan digunakan pada file main.py.

## ➕ Metode Tambahan Gra
Untuk memenuhi instruksi tambahan, class Graf juga dilengkapi dengan metode tambahan berikut:
- node_degree() – Menentukan derajat setiap simpul
- is_connected() – Mengecek keterhubungan graf
- find_cycles() – Menentukan cycle pada graf
- bfs(start) – Breadth-First Search
- dfs(start) – Depth-First Search
- dijkstra(start) – Algoritma Dijkstra
- has_path(source, target) – Mengecek keberadaan lintasan
- graph_info() – Informasi umum graf
Semua metode tambahan berfungsi dengan baik dan digunakan dalam penyelesaian AFL-3.

## ▶️ Cara Menjalankan Program
**Jalankan perintah berikut di terminal:**
```text
python main.py
```
Program akan menampilkan:
  1.  Output hasil perhitungan di terminal
  2.  Visualisasi graf menggunakan Matplotlib (graf akan muncul satu per satu)

## 📊 Penyelesaian AFL-3
### 🔹 AFL-3 Soal 1 – Graf Tak Berarah
- Menampilkan graf sesuai himpunan simpul dan sisi
- Menentukan derajat setiap simpul
- Menentukan cycle
- Mengecek apakah graf connected

<img width="1920" height="1080" alt="Screenshot (1220)" src="https://github.com/user-attachments/assets/70a3d8c1-2f52-4fb1-b0ae-b543c5fd531b" />

```text
Hasil Derajat Simpul:
A = 2, B = 2, C = 3, D = 2, E = 3, F = 2
Graf dinyatakan connected dan memiliki cycle.
```

### 🔹 AFL-3 Soal 2 – Graf Terarah Berbobot
- Menampilkan graf terarah berbobot
- Menentukan path dari simpul 1 ke 5
- Menentukan cycle
- Mengecek strongly connected
- Menentukan lintasan terpendek dengan Dijkstra

<img width="1920" height="1080" alt="Screenshot (1221)" src="https://github.com/user-attachments/assets/27a39657-ac1d-4fab-91ee-f0c1ff87f9bf" />

```text
Contoh Jalur Terpendek:
1 → 3 → 2 → 4 → 5
Graf bersifat strongly connected.
```

### c🔹 AFL-3 Soal 3 – BFS, DFS, dan Dijkstra
- Visualisasi graf berbobot
- BFS dari simpul A
- DFS dari simpul A
- Dijkstra dari simpul A
- Jalur terpendek dari A ke G

<img width="1920" height="1080" alt="Screenshot (1222)" src="https://github.com/user-attachments/assets/38fb4a33-8f85-4e8f-8974-65c870b42ee3" />

## 📷 Dokumentasi Hasil
Hasil penyelesaian AFL-3 ditunjukkan melalui:
- **Output terminal**
- **Visualisasi graf (node, edge, bobot, dan jalur terpendek)**
Screenshot hasil visualisasi dan output dapat dilampirkan sebagai bukti pengerjaan.


