import youtube as Y

from urllib.parse import urlparse
import urllib

dt = 'https://www.youtube.com/playlist?list=PLxBhf17jrfxHQq8BYVBnelNbTte6OSy0e'
dt = 'https://www.youtube.com/playlist?list=PLxBhf17jrfxFHnXhQNSLiWjnA2y6pNJ62'
dt = 'https://www.youtube.com/playlist?list=PL65CC0384A1798ADF'

dta = urlparse(dt)
dta = str(urllib.parse.parse_qs(dta.query, encoding="unicode")['list'])[2:-2]
print(dta)

result = Y.get_content(dta)
print(result)

M.init_course()

myc = etree.parse('./template/moodle_backup.xml')
myroot = myc.getroot()

for i in result:
  M.activity_url_link_builder(myroot, name=i[0], urllink=i[1])
  M.activity_assignment_link_builder(myroot, name=i[0], assignlink=i[1])

import os
os.chdir('./result')
M.zipdir('.','../_file_backup.zip')
