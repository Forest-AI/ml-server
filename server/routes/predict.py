from flask import jsonify, request
from server import app
import joblib
from server.services.Detector import Detector
from server.services.Database import Database

detector = Detector() 
db = Database()

@app.route("/predict")
def predict():
    """Predict route"""
    audio_id = request.args.get('id')
    db.download(audio_id)

    y = detector.predict("data//audio.wav")
    state = {"status": str(y)}
    return jsonify(state)

