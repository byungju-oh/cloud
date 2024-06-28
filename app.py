from flask import Flask, render_template

import os
import json
from models import db

app = Flask(__name__)

# 현재있는 파일의 디렉토리 절대경로
base_dir = os.path.abspath(os.path.dirname(__file__))

# basdir 경로안에 DB파일 만들기
db_file = os.path.join(base_dir, 'db.sqlite')

# SQLAlchemy 설정

# 내가 사용 할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ubuntu:ubuntu@34.69.95.212/data'
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY

# secret_file = os.path.join(base_dir, 'secrets.json')  # secrets.json 파일 위치를 명시
# with open(secret_file) as f:
#     secrets = json.loads(f.read())['SECRET_KEY']
# app.config['SECRET_KEY'] = secrets

db.init_app(app)
db.app = app
db.create_all()


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/shop')
def home1():
   return render_template('shop.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)