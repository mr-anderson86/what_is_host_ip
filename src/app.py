from flask import Flask
from requests import get

app = Flask(__name__)


@app.route("/health_check")
def health_check():
    return {"status": "OK", "status_code": 200}, 200


@app.route("/", methods=["GET", "POST"])
def home():
    try:
        ip = get('https://api.ipify.org').text
        return {'ip': ip, 'status_code': 200, 'err_msg': ''}, 200
    except Exception as e:
        err_name = type(e).__name__
        err_msg = str(e)
        return {'ip': '', 'status_code': 500, 'err_msg': err_name + "exception: " + err_msg}, 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
