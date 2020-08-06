from flask import Flask, request, render_template, send_file
import xml.etree.ElementTree as XT
import json
from urllib.parse import urlparse
import urllib
import shutil
import youtube as Y
import MoodleCourse as M
import os

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/')
def index():
    try:
        shutil.rmtree('./result')
    except:
        pass
    try:
        os.remove('_file_backup.zip')
    except:
        pass
    app.logger.info('User using system')
    return render_template('form.html')

@app.route('/_file_backup.zip', methods=['GET'])
def return_file():
    app.logger.info('File downloaded')
    return send_file('../_file_backup.zip')

@app.route('/', methods=['POST'])
def my_form_post():
    ytb_url = request.form.get('element_1')
    fullname = request.form.get('element_2')
    shortname = request.form.get('element_3')
    deskripsi = request.form.get('element_4')

    parsed = urlparse(ytb_url)
    app.logger.info(str(ytb_url))

    _list = str(urllib.parse.parse_qs(parsed.query, encoding="unicode")['list'])[2:-2]
    print("retrieving this list:",_list)
    data = Y.get_content(_list)

    M.init_course()

    myc = XT.parse('./template/moodle_backup.xml')
    myroot = myc.getroot()

    for i in data:
        judul = "YTB: " + i[0]
        _jd_tugas = "Tugas Essay - " + i[0]
        M.activity_url_link_builder(myroot, name=judul, urllink=i[1])
        M.activity_assignment_link_builder(myroot, name=_jd_tugas, assignlink=i[1])

    M.build_coursename(fullname=fullname,shortname=shortname,deskripsi=deskripsi)

    import os
    print("I am now in:", os.getcwd())
    os.chdir('./result')
    M.zipdir('.','../_file_backup.zip')
    os.chdir('..')
    print("final:",os.listdir())    
    data = str(data)
    data = data + "</br></br><a href='./_file_backup.zip'>_file_backup.zip</a>"

    return render_template('form.html',data=data, checked=True)

if __name__ == '__main__':
    app.run()