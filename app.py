from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app) 

duyurular = []
sayac = 0 # Her duyuruya benzersiz bir ID vermek için

@app.route('/api/duyurular', methods=['GET'])
def duyurulari_getir():
    return jsonify(duyurular)

@app.route('/api/duyuru-ekle', methods=['POST'])
def duyuru_ekle():
    global sayac
    try:
        yeni_duyuru = request.json
        sayac += 1
        yeni_duyuru['id'] = sayac # Duyuruya kimlik ekle
        duyurular.insert(0, yeni_duyuru)
        return jsonify({"mesaj": "Duyuru eklendi!"}), 201
    except Exception as e:
        return jsonify({"hata": str(e)}), 500

# SİLME KAPISI (DELETE)
@app.route('/api/duyuru-sil/<int:duyuru_id>', methods=['DELETE'])
def duyuru_sil(duyuru_id):
    global duyurular
    # ID'si eşleşmeyenleri tut, eşleşeni listeden at
    duyurular = [d for d in duyurular if d.get('id') != duyuru_id]
    return jsonify({"mesaj": "Duyuru başarıyla silindi!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)