#!/usr/bin/env python
# coding: utf-8


from flask import Flask, jsonify,render_template
from http import HTTPStatus    
import sqlite3 


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

## 데이터 베이스 연결
def get_db_connection():
    conn = sqlite3.connect('gptconnect.db')
    conn.row_factory  = sqlite3.Row
    return conn

# 모든 사용자 정보 조회 
@app.route('/api', methods=['GET']) 
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        select p.id,a.name,p.contents
        from presentation p 
        join attendant a on p.user_id = a.id
        """)
    users_info = cur.fetchall()
    conn.close()
    users = [dict(ix) for ix in users_info]
    return jsonify(users) 

# main page - check page about works normally? 
@app.route('/', methods=['GET']) 
def index():
    return "main Pages here"

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)