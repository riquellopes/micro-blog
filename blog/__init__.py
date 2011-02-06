# -*- encoding:utf-8 -*-

from flask import Flask

import settings

app = Flask('blog')
app.config.from_object('blog.settings')


import blog.views
