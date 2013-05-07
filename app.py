# coding: utf-8
import sys
import os.path
from bottle import route, run, static_file
from jinja2 import Environment, FileSystemLoader

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import config

env = Environment(loader=FileSystemLoader(config.TEMPLATEM_ROOT, encoding='utf-8'))


@route('/')
def index():
    t = env.get_template('index.html')
    return t.render()


@route('/static/<path:path>')
def static_image(path):
    return static_file(path, root=config.STATIC_ROOT)


def main():
    run(host=config.SERVER_HOST, port=config.SERVER_PORT,
        server=config.SERVER_MODULE, debug=True, reloader=True)

if __name__ == '__main__':
    main()
