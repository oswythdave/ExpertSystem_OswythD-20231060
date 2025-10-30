from flask import Flask, render_template, request
from engine_with_confidence import analisa_metode_belajar_with_confidence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = []
    if request.method == 'POST':
        data = {
            'tipe_kepribadian': request.form.get('tipe_kepribadian'),
            'waktu_belajar': request.form.get('waktu_belajar'),
            'kesulitan_belajar': request.form.get('kesulitan_belajar')
        }

        hasil = analisa_metode_belajar_with_confidence(data)

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
