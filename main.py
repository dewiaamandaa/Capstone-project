# main.py
from flask import Flask, request, jsonify
import recomendation as rc

app = Flask(__name__)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    data = request.get_json()

    peruntukan = data.get('peruntukan')
    banyak = data.get('banyak')
    fase = data.get('fase')

    if peruntukan == "1":
        result = rc.ayam_petelur(fase, banyak)
    elif peruntukan == "2":
        result = rc.ayam_pedaging(fase, banyak)
    else:
        result = {"error": "Masukan anda harus berupa angka 1 atau 2 pada kolom 'Peruntukan Ternak'."}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
