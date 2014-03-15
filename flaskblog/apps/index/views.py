#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from apps import app,cache
from apps.category.models import Category
from apps.page.models import Post
from apps.tag.models import Tag
from apps.comment.models import Comment
from random import shuffle
index = Blueprint('index',__name__)
per_page = app.config['PER_PAGE']



@index.route('/')
@index.route('page/<int:pageid>')
@cache.cached(timeout=300)
def index_1(pageid=1):
    categorys = Category.query.getall()

    p = Post.query.getpost_perpage(pageid, per_page)
    hot = Post.query.hottest()[:20]
    new = Post.query.newpost()[:20]

    tag = Tag.query.getall()
    shuffle(tag)
    tag = tag[:20]

    comments = Comment.query.newcomment()[:20]
    articles = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1, p.total / per_page + 2)
    else:
        pagination = range(1, p.total / per_page + 1)

    return render_template('/index.html',
                           categorys=categorys,
                           articles=articles,
                           hotarticles=hot,
                           newpost=new,
                           tags=tag,
                           comments=comments,
                           pageid=pageid,
                           pagination=pagination[pageid - 1:pageid + 10],
                           last_page=pagination[-1],
                           nav_current="index"
                           )