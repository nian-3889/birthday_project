from unicodedata import name
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.birth

@app.route('/')
def home():
    return render_template('index.html')

#post
@app.route('/post', methods=["POST"])
def birth_post():
    name_receive = request.form["name_give"]
    message_receive = request.form['message_give']
    # name_receive = request.args.get('name_give')
    # message_receive = request.args.get('message_give')

    doc = {
        'name': name_receive,
        'message': message_receive
    }

    db.birth.insert_one(doc)

    return jsonify({'msg':'메시지 전송 완료'})

@app.route('/post', methods=['GET'])
def show_message():
    order_message = list(db.birth.find({}, {'_id': False}))
    return jsonify({'comments': order_message})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)