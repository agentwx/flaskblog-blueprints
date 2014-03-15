#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
cache = Cache(app)


from apps.about.views import about
app.register_blueprint(about,url_prefix='/about')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/404')
def error_404():
    return render_template('404.html'), 404


@app.route('/error')
def error_temp(content='404'):
    return render_template('error.html', content=content)
