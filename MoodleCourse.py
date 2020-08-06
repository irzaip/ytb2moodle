#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as XT
import shutil
import zipfile
import os.path

#define first activity
activityid__= 1047
section__ = 304
moduleid__ = 1204
contextid__ = 1912


def build_activity(element="", moduleid="",sectionid="",modulename="",title=""):
    """Membuat activity di moodle_backup.xml"""
    if element == "":
        a = XT.Element("activity")
    else:
        a = element
    _moduleid = XT.SubElement(a, "moduleid")
    _sectionid = XT.SubElement(a, "sectionid")
    _modulename = XT.SubElement(a, "modulename")
    _title = XT.SubElement(a, "title")
    _directory = XT.SubElement(a, "directory")
    _moduleid.text = str(moduleid)
    _sectionid.text = str(sectionid)
    _modulename.text = str(modulename)
    _title.text = str(modulename)
    dir_ = '/activities/' + str(modulename) + '_' + str(moduleid)
    _directory.text = str(dir_)
    return a

def build_section(sectionid="",title="",directory=""):
    a = XT.Element("section")
    _sectionid = XT.SubElement(a, "sectionid")
    _title = XT.SubElement(a, "title")
    _directory = XT.SubElement(a, "directory")
    _sectionid.text = str(sectionid)
    _title = str(title)
    _directory = str(directory)
    return a

# CHANGE COURSE DESCRIPTION
def build_coursename(fullname="",shortname="",deskripsi=""):
    CDSC = XT.parse('./template/course/course.xml')
    CDSCr = CDSC.getroot()
    _fullname = CDSCr.find('fullname')
    _shortname = CDSCr.find('shortname')
    _summary = CDSCr.find('summary')
    _fullname.text = str(fullname)
    _shortname.text = str(shortname)
    _summary.text = str(deskripsi)
    CDSC.write('./result/course/course.xml')
    return print("Done")

def zipdir(path, filename):
    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    # ziph is zipfile handle
    for root, _, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()

def init_course():
    try:
        shutil.rmtree('./result')
    except: pass
    try:
        os.mkdir('./result')
        shutil.copytree('./template/sections','./result/sections')
        shutil.copytree('./template/activities', './result/activities')
    except: pass
    try:
        os.mkdir('./result/course')
    except: pass
    try:
        os.mkdir('./result/activities')
    except: pass
    try:
        os.mkdir('./result/sections')
    except: pass
    try:
        shutil.copy2('./template/scales.xml','./result/scales.xml')
        shutil.copy2('./template/roles.xml','./result/roles.xml')
        shutil.copy2('./template/questions.xml','./result/questions.xml')
        shutil.copy2('./template/outcomes.xml','./result/outcomes.xml')
        shutil.copy2('./template/groups.xml','./result/groups.xml')    
        shutil.copy2('./template/gradebook.xml','./result/gradebook.xml')    
        shutil.copy2('./template/grade_history.xml','./result/grade_history.xml')    
        shutil.copy2('./template/files.xml','./result/files.xml')    
        shutil.copy2('./template/completion.xml','./result/completion.xml')
        shutil.copy2('./template/course/completiondefaults.xml','./result/course/completiondefaults.xml')
        shutil.copy2('./template/course/enrolments.xml','./result/course/enrolments.xml')
        shutil.copy2('./template/course/inforef.xml','./result/course/inforef.xml')
        shutil.copy2('./template/course/roles.xml','./result/course/roles.xml')
        shutil.copy2('./template/moodle_backup.xml','./result/moodle_backup.xml')
    except:
        pass
    return print("Done with init")

def add_activities(myroot, sectionid="304",modulename="",title="", dirname=""):
    global moduleid__
    #_activities = myroot[0][20][0]
    _activities = XT.Element('activities')
    _activity = XT.SubElement(_activities,'activity')
    _moduleid = XT.SubElement(_activity, "moduleid")
    _sectionid = XT.SubElement(_activity, "sectionid")
    _modulename = XT.SubElement(_activity, "modulename")
    _title = XT.SubElement(_activity, "title")
    _directory = XT.SubElement(_activity, "directory")
    _moduleid.text = str(moduleid__)
    _moduleid.tail = "\n"
    _sectionid.text = str(sectionid)
    _sectionid.tail = "\n"
    _modulename.text = str(modulename)
    _modulename.tail = "\n"
    _directory.text = str(dirname)
    _directory.tail = "\n"
    _title.text = str(title)
    _title.tail = "\n"
     # myc.write("hello.xml")
    #return print("Done add to moodle_backup.xml")    
    return _activity


def build_section_detail(id="",
                         number="",
                         name="",
                         summary="",
                         summaryformat="1",
                         sequence="",
                         visible="1",
                         availabilityjson="$@NULL@$",
                         timemodified="1595396449"):
    a = XT.Element("section")
    dd = {"id": id}
    a.attrib = dd
    _number = XT.SubElement(a, "number")
    _name = XT.SubElement(a, "name")
    _summary = XT.SubElement(a, "summary")
    _summaryformat = XT.SubElement(a, "summaryformat")
    _sequence = XT.SubElement(a, "sequence")
    _visible = XT.SubElement(a, "visible")
    _availabilityjson = XT.SubElement(a, "availabilityjson")
    _timemodified = XT.SubElement(a, "timemodified")
    
    _number.text = str(number)
    _name.text = str(name)
    _summary.text = str(summary)
    _summaryformat.text = str("1")
    _sequence.text = str(sequence)
    _visible.text = str(visible)
    _availabilityjson.text = str(availabilityjson)
    _timemodified.text = str(timemodified)
    return a

def activity_url_link_builder(myroot,name="",urllink=""):
    """Buat direktory terkait untuk activity"""
    global activityid__, moduleid__, contextid__
    _i1 = '&lt;p&gt;'
    _e1 = '&lt;br&gt;&lt;/p&gt;'
    urlXT = XT.parse('./template/url_/url.xml')
    urlr = urlXT.getroot()
    urlr.attrib['id']=str(activityid__)
    urlr.attrib['contextid']=str(contextid__)
    urlr.attrib['moduleid']=str(moduleid__)
    urlr[0].attrib['id']=str(activityid__)
    urlr[0].find('name').text = str(name)
    urlr[0].find('intro').text = str(_i1 + urllink + _e1)
    urlr[0].find('externalurl').text = str(urllink)
    fname = './result/activities/'
    dirname = fname + str("url_") + str(moduleid__)
    _dirname = 'activities/' + str("url_") + str(moduleid__)
    try:
        os.makedirs(dirname, exist_ok=True)
        print("created dir:",dirname)
    except: 
        print("Error creating dir:", dirname)
    filename = dirname + "/url.xml"
    with open(filename,'w+') as f:
        f.write(XT.tostring(urlr, encoding='utf8').decode('utf8'))


    shutil.copy2('./template/url_/grade_history.xml', dirname + '/grade_history.xml')
    shutil.copy2('./template/url_/grades.xml', dirname + '/grades.xml')
    shutil.copy2('./template/url_/inforef.xml', dirname + '/inforef.xml')
    shutil.copy2('./template/url_/module.xml', dirname + '/module.xml')
    shutil.copy2('./template/url_/roles.xml', dirname + '/roles.xml')

    _act = add_activities(myroot, modulename="url", title=name, dirname=_dirname)
    _act = str(XT.tostring(_act, encoding="unicode",method='xml'))
    re_mdl_backup(_act)

    activityid__ += 1
    moduleid__ += 1
    contextid__ += 1

    return _act

def activity_assignment_link_builder(myroot,name="",assignlink=""):
    """Buat direktory terkait untuk activity"""
    global activityid__, moduleid__, contextid__
    _i1 = '&lt;p&gt;'
    _e1 = '&lt;br&gt;&lt;/p&gt;'
    assignXT = XT.parse('./template/assign_/assign.xml')
    assignr = assignXT.getroot()
    assignr.attrib['id']=str(activityid__)
    assignr.attrib['contextid']=str(contextid__)
    assignr.attrib['moduleid']=str(moduleid__)
    assignr[0].attrib['id'] = str(activityid__)
    assignr[0].find('name').text = str(name)
    assignr[0].find('intro').text = str(_i1 + assignlink + _e1)
    #assignr[0].find('externalurl').text = str(assignlink)
    fname = './result/activities/'
    dirname = fname + str("assign_") + str(moduleid__)
    _dirname = 'activities/' + str("assign_") + str(moduleid__)
    try:
        os.makedirs(dirname, exist_ok=True)
        print("created dir:",dirname)
    except: 
        print("Error creating dir:", dirname)
    filename = dirname + "/assign.xml"
    with open(filename,'w+') as f:
        f.write(XT.tostring(assignr, encoding='utf8').decode('utf8'))

    shutil.copy2('./template/assign_/grade_history.xml', dirname + '/grade_history.xml')
    shutil.copy2('./template/assign_/grades.xml', dirname + '/grades.xml')
    shutil.copy2('./template/assign_/grading.xml', dirname + '/grading.xml')
    shutil.copy2('./template/assign_/inforef.xml', dirname + '/inforef.xml')
    shutil.copy2('./template/assign_/module.xml', dirname + '/module.xml')
    shutil.copy2('./template/assign_/roles.xml', dirname + '/roles.xml')

    _act = add_activities(myroot, modulename="assign", title=name, dirname=_dirname)
    _act = str(XT.tostring(_act, encoding="unicode",method='xml'))
    re_mdl_backup(_act)
    activityid__ += 1
    moduleid__ += 1
    contextid__ += 1

    return print("Assignment Done, next activityid:", activityid__)

def re_mdl_backup(replacewith=""):
    with open("./result/moodle_backup.xml",'r') as f:
        txt = f.read()
    txt = txt.replace('</activities>', replacewith +'</activities>')
    with open('./result/moodle_backup.xml','wt') as f:
        f.write(txt)

if __name__ == '__main__':

  init_course()

  myc = XT.parse('./template/moodle_backup.xml')
  myroot = myc.getroot()
  activity_url_link_builder(myroot, name="Youtube channel irza", urllink="http://youtube.com/irzaip")
  myc.write("./result/moodle_backup.xml", encoding="UTF-8")
  


