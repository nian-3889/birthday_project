from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://sigure:1234@cluster0.ldppc.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.birth

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=["POST"])
def birth_post():
    message_receive = request.form['message_give']
    name_receive = request.form['name_give']

    doc = {
        'message': message_receive,
        'name': name_receive
    }

    db.birthday.insert_one(doc)

    return jsonify({'msg': '테스트 코멘트'})

@app.route("/post", methods=["GET"])
def birth_get():
    message_list = list(db.birth.find({}, {'_id':False}))
    return jsonify({'messages': message_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)