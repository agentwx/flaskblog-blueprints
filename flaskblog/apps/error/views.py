#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, Blueprint
#from myapp import app

error = Blueprint('error', __name__,url_prefix='/error')


@error.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@error.route('/404')
def error_404():
    return render_template('404.html'), 404

@error.route('/')
def error_temp(content='404'):
    return render_template('tt/error.html', content=content)
