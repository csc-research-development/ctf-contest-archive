from flask import Flask, jsonify, render_template, session
from threading import Timer
import time
import random
import os
from dotenv import load_dotenv

import lib.constants as constants
from lib.utils import generate_random_port
from lib.instance import start_instance, stop_instance
from lib.storage import instances

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '0hduaLWVIEfxa2novs12gbwJMQJJXe7yxMEC+h9f07Y='
app.config['SESSION_COOKIE_NAME'] = 'coin-hunt-instance-session'
is_development = os.getenv('ENV') == 'development'
domain = 'http://103.185.44.248' if not is_development else 'http://localhost'

def get_session():
    user_id = session.get('user_id')

    if not user_id:
        user_id = str(random.randint(100000, 999999))
        session['user_id'] = user_id
    
    return user_id

@app.route('/')
def index():
    user_id = get_session()
    instance = instances.get(user_id)
    now = round(time.time() * 1000)

    if instance != None and instance['end_time'] <= now:
        instance = None

    return render_template('index.html', instance=instance)

@app.route('/start_instance', methods=['POST'])
def start_instance_route():
    user_id = get_session()

    if user_id in instances:
        return jsonify({"error": "You already have a running instance."}), 400

    port = generate_random_port()
    instance_id, err = start_instance(port)

    if err:
        return jsonify({"error": err}), 500
    

    end_time = round(time.time() * 1000) + constants.DURATION
    
    instances[user_id] = {"instance_id": instance_id, "port": port, "end_time": end_time, "url": f"{domain}:{port}"}
    Timer((float(constants.DURATION/1000)), stop_instance, (port, instance_id, user_id)).start()
    
    return jsonify(instances[user_id])


@app.route('/stop_instance', methods=['POST'])
def stop_instance_route():
    user_id = get_session()

    if user_id not in instances:
        return jsonify({"error": "No running instance found for the user."}), 400

    instance = instances[user_id]

    port = instance['port']
    instance_id = instance['instance_id']

    _, err = stop_instance(port, instance_id, user_id)

    if err:
        return jsonify({"error": err}), 500

    return jsonify({"message": "stopped"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=is_development)
