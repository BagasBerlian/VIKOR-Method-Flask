-- 1. Membuat Database
CREATE DATABASE IF NOT EXISTS vikor_mahasiswa;
USE vikor_mahasiswa;

-- 2. Membuat Tabel Mahasiswa
CREATE TABLE mahasiswa (
    id INT auto_increment PRIMARY KEY,
    nama varchar(100),
    nilai_ipk float,
    nilai_organisasi float,
    nilai_keaktifan float,
    nilai_kepemimpinan float
);
desc mahasiswa;

-- 3. Memasukkan Data Dummy Mahasiswa
INSERT INTO mahasiswa VALUES 
(1, "Alex", 3.8, 80, 85, 90),
(2, "Bella", 3.6, 75, 82, 88),
(3, "Charlie", 3.9, 85, 90, 92),
(4, "Diana", 3.7, 78, 80, 85),
(5, "Edward", 3.5, 70, 75, 80),
(6, "Fiona", 3.8, 82, 88, 86),
(7, "George", 3.4, 65, 70, 78),
(8, "Hannah", 3.9, 90, 92, 91);
select * from mahasiswa;