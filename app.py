from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://sigure:1234@cluster0.ldppc.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.birth

@app.route('/')
def home():
    return render_template('index.html')

#post
@app.route('/post', methods=["POST"])
def birth_post():
    name_receive = request.form['name_give']
    message_receive = request.form['message_give']
    print(name_receive, message_receive)
    return jsonify({'msg':'post 연결 완료'})








if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)