from flask import render_template
from . import main


@main.app_errorhandler(404)  # 定义404报错页面
def page_not_found(e):
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500) # 定义500报错页面
def internal_server_error(e):
    return render_template('errors/500.html'), 500
