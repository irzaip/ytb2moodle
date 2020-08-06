import MoodleCourse as M
import xml.etree.ElementTree as XT

from lxml import etree

course_detail = {
  'fullname': 'Long course',
  'shortname': 'shortname',
  'description': 'this is the description',
}
course = [
  ["Ini Test url link", 'http://url1'],
  ["Ini test 2 nomor url", 'http://url2'],
  ["Course nomor 3",'http://url3']
]


M.init_course()

#myc = etree.parse('./template/moodle_backup.xml')
#yroot = myc.getroot()
for i in course:
  M.activity_url_link_builder(myroot, name=i[0], urllink=i[1])
  M.activity_assignment_link_builder(myroot, name=i[0], assignlink=i[1])
#print("")

#mmm = M.activity_url_link_builder(myroot, name="Ini test tambahan", urllink="http://url1")
#myc.write("./result/moodle_backup.xml", encoding="UTF-8", xml_declaration=True)

M.build_coursename()
#M.zipdir('./result/','course.mbz')

import os
os.chdir('./result')
M.zipdir('.','../_file_backup.zip')











