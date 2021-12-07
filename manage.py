#!/usr/bin/python3
# -*- coding:utf-8 -*-

from app import create_app
from gevent import pywsgi
# Since I
if __name__ == '__main__':
    fapp = create_app()
    # fapp.run(host='0.0.0.0',port='8000')
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), fapp)
    server.serve_forever()
