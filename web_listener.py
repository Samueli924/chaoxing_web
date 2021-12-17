from flask import Flask, redirect, request
from flask_cors import CORS
import requests
import api

app = Flask(__name__)


def resp_ok(resp_data):
    resp = {'code': 200, 'data': resp_data}
    return resp


@app.route('/')
def index():
    return redirect('/static/index.html', code=302)

@app.route('/menu.html?<params>')
def menu(params):
    return redirect('/static/menu.html?'+params)


@app.route('/api/get_info', methods=['GET'])
def get_info():
    usernm = request.args.get("usernm")
    passwd = request.args.get("passwd")
    session = requests.session()
    user = api.User(usernm,passwd)
    user.login(session=session, need_cookies=False)
    msg = user.get_info(session)
    return resp_ok(msg)


@app.route('/api/get_all_user', methods=['GET'])
def get_all_user():
    ret = api.get_all_user()
    return resp_ok(ret)


@app.route('/api/refresh_user', methods=['GET'])
def refresh_user():
    usernm = request.args.get("usernm")
    ret = api.refresh_user(usernm)
    return resp_ok(ret)


@app.route('/api/refresh_course', methods=['GET'])
def refresh_course():
    usernm = request.args.get("usernm")
    ret = api.refresh_course(usernm)
    return resp_ok(ret)


@app.route('/api/delete_user', methods=['GET'])
def delete_user():
    usernm = request.args.get("usernm")
    ret = api.delete_user(usernm)
    return resp_ok(ret)


@app.route('/api/delete_course', methods=['GET'])
def delete_course():
    usernm = request.args.get("usernm")
    courseid = request.args.get("courseid")
    ret = api.delete_course(usernm,courseid)
    return resp_ok(ret)


@app.route('/api/start_learn', methods=['GET'])
def start_learn():
    usernm = request.args.get("usernm")
    courseid = request.args.get("courseid")
    speed = request.args.get("speed")
    ret = api.start_learn(usernm, courseid, speed)
    return resp_ok(ret)

@app.route('/api/stop_learn', methods=['GET'])
def stop_learn():
    usernm = request.args.get("usernm")
    courseid = request.args.get("courseid")
    ret = api.stop_learn(usernm, courseid)
    return resp_ok(ret)


@app.route('/api/get_update', methods=['GET'])
def get_update():
    usernm = request.args.get("usernm")
    courseid = request.args.get("courseid")
    ret = api.get_update(usernm, courseid)
    return resp_ok(ret)


if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port=7777, debug=True)