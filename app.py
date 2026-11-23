from flask import Flask, request, jsonify
import re

app = Flask(__name__)
COMMON_PASSWORDS = {"123456", "password", "qwerty", "12345678", "admin"}

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({'error': 'Передайте пароль в поле "password"'}), 400
        
    password = data.get('password', '')
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("Пароль должен быть не короче 8 символов.")
    if re.search(r'\d', password): score += 1
    else: feedback.append("Добавьте хотя бы одну цифру.")
    if re.search(r'[A-Z]', password): score += 1
    else: feedback.append("Добавьте хотя бы одну заглавную букву.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    else: feedback.append("Добавьте спецсимвол.")
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Этот пароль слишком распространён.")
        score = 0 

    if score >= 4: strength = "Очень надежный"
    elif score == 3: strength = "Надежный"
    elif score == 2: strength = "Средний"
    else: strength = "Слабый"

    return jsonify({'strength': strength, 'score': score, 'feedback': feedback})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
