from flask import Flask, request, jsonify
from models.user import db, User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

db.init_app(app)

@app.route('/')
def home():
    return {'mensagem': 'API Flask rodando com sucesso!'}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Dados insuficientes"}), 400
    
    user_exists = User.query.filter_by(username=data['username']).first()
    if user_exists:
        return jsonify()

with app.app_context():
    print("Criando o banco de dados...")
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
