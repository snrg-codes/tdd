from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "admin" : "1234",
    "user" :  "4321"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"message": "Siz muvaffaqiyatli o'tdingiz"}), 200
    else:
        return jsonify({"message": "login yoki parol xato"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
