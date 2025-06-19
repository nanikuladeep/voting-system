from flask import Flask, render_template, request, redirect
from database import init_db, insert_vote, has_voted
from face_recognition import verify_face
from anomaly_detector import detect_anomaly

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    user_id = request.form['user_id']
    candidate = request.form['candidate']

    # Simulated face verification
    if not verify_face(user_id):
        return "Face not verified. Access denied."

    if has_voted(user_id):
        return "You have already voted."

    if detect_anomaly(user_id):
        return "Anomaly detected in voting behavior."

    insert_vote(user_id, candidate)
    return "Vote successfully cast!"

if __name__ == '__main__':
    app.run(debug=True)
