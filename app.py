from flask import Flask, render_template, request

app = Flask(__name__)

# fungsi rekursif
def cetak_nilai_rekursif(data, index=0):
    if index >= len(data):
        return []
    return [data[index]] + cetak_nilai_rekursif(data, index + 1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nilai = {
    'Algoritma Pemrograman': 'B',
    'Kewirausahaan Digital': 'AB',
    'Bahasa Inggris': 'B',
    'Pendidikan Agama': 'AB',
    'Ekonomi Micro': 'B'
    }


        # FILTER (misal: ambil nilai selain AB)
        filter_nilai = {k: v for k, v in nilai.items() if v != 'AB'}

        # REKURSIF
        list_nilai = list(nilai.values())
        hasil_rekursif = cetak_nilai_rekursif(list_nilai)

        data = {
            'nama': request.form['nama'],
            'nim': request.form['nim'],
            'nilai': nilai,
            'filter': filter_nilai,
            'rekursif': hasil_rekursif
        }

        return render_template('result.html', data=data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)