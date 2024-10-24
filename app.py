from flask import Flask, render_template, request, redirect, url_for
import database.db as db

app = Flask(__name__)
# Fungsi untuk mengambil data mahasiswa dari database
def get_mahasiswa():
    conn = db.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mahasiswa ORDER BY id ASC')
    mahasiswa = cursor.fetchall()
    cursor.close()
    conn.close()
    return mahasiswa

def input_mahasiswa():
    conn = db.get_db_connection()
    cursor = conn.cursor()
    
    nama = request.form['nama']
    ipk = request.form['ipk']
    organisasi = request.form['organisasi']
    keaktifan = request.form['keaktifan']
    kepemimpinan = request.form['kepemimpinan']
    
    # Query untuk memasukkan data ke database tanpa memasukkan ID (karena auto-increment)
    query = '''
        INSERT INTO mahasiswa (nama, nilai_ipk, nilai_organisasi, nilai_keaktifan, nilai_kepemimpinan)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (nama, ipk, organisasi, keaktifan, kepemimpinan))
    conn.commit()
    
    cursor.close()
    conn.close()

def delete_mahasiswa(mahasiswa_id):
    conn = db.get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM mahasiswa WHERE id = %s', (mahasiswa_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Fungsi perhitungan VIKOR
def vikor(mahasiswa):
    # List kriteria (c1: IPK, c2: Organisasi, c3: Keaktifan, c4: Kepemimpinan)
    kriteria = ['nilai_ipk', 'nilai_organisasi', 'nilai_keaktifan',
    'nilai_kepemimpinan']
    n = len(mahasiswa)
    best = {k: max([m[k] for m in mahasiswa]) for k in kriteria}
    worst = {k: min([m[k] for m in mahasiswa]) for k in kriteria}
    
    s = []
    r = []
    
    for m in mahasiswa:
        S_i = sum([(best[k] - m[k]) / (best[k] - worst[k]) for k in kriteria])
        R_i = max([(best[k] - m[k]) / (best[k] - worst[k]) for k in kriteria])
        s.append(S_i)
        r.append(R_i)

    # Tentukan nilai Q
    S_best = min(s)
    S_worst = max(s)
    R_best = min(r)
    R_worst = max(r)
    Q = [(0.5 * (S_i - S_best) / (S_worst - S_best)) + (0.5 * (R_i - R_best) /
    (R_worst - R_best)) for S_i, R_i in zip(s, r)]
    
    # Gabungkan hasil dengan data mahasiswa
    for i, m in enumerate(mahasiswa):
        m['S'] = s[i]
        m['R'] = r[i]
        m['Q'] = Q[i]
        
    # Urutkan berdasarkan nilai Q
    mahasiswa.sort(key=lambda x: x['Q'])
    return mahasiswa

@app.route('/')
def index():
    mahasiswa = get_mahasiswa()
    return render_template('index.html', mahasiswa=mahasiswa)

# Untuk Handle add Mahasiswa
@app.route('/add_mahasiswa', methods=['POST'])
def add_mahasiswa():
    if request.form['nama'] and request.form['ipk'] and request.form['organisasi'] and request.form['keaktifan'] and request.form['kepemimpinan']:
        input_mahasiswa()
        return render_template('index.html', mahasiswa=get_mahasiswa())
    else:
        return "Data tidak lengkap", 400
    
# Handle untuk menghapus mahasiswa
@app.route('/delete/<int:mahasiswa_id>', methods=['POST'])
def delete(mahasiswa_id):
    delete_mahasiswa(mahasiswa_id)
    return redirect(url_for('index'))

@app.route('/result')
def result():
    mahasiswa = get_mahasiswa()
    hasil_vikor = vikor(mahasiswa)
    return render_template('result.html', mahasiswa=hasil_vikor)

if __name__ == '__main__':
    app.run(debug=True)