# -*- coding: utf-8 -*-
from flask_script import Manager, Server

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import config as config

app = Flask(__name__)
app.config.from_object(config)
manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=8001))


db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from models import CPU_utilization
        utilization = CPU_utilization.from_json(request.json)
        db.session.add(utilization)
        db.session.commit()
        print(utilization.utilization)
        return jsonify(utilization.to_json())
    else:
        from models import CPU_utilization
        utilizations = CPU_utilization.query.all()
        return render_template('index.html', data={'utilizations': [CPU_utilization.to_json() for CPU_utilization in utilizations]})



if __name__ == '__main__':
    manager.run()


