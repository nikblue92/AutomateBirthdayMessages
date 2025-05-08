from flask import Flask,request, jsonify
import webbrowser
import threading

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def home(user_id):
    user_date = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    extra = request.args.get('extra')
    if extra:
        user_date['extra'] = extra
    return jsonify(user_date),200

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/get-user/123?extra=cake")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)