import os
import zipfile

from flask import flash

from playhouse.shortcuts import model_to_dict


def file_to_zip(theorder):
    BaseDir = os.getcwd()
    filedir = BaseDir + '\\models\\Result\\' + theorder
    zipdir = BaseDir + '\\models\\Result\\zip\\'
    zipbao = theorder + '.zip'
    z = zipfile.ZipFile(zipdir + zipbao, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(filedir):
        fpath = dirpath.replace(filedir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()
    return (zipdir, zipbao)


def zip_to_file(theorder, zip_src, systemtype):
    BaseDir = os.getcwd()
    Rawipdir = BaseDir + '\\models\\Raw\\' + systemtype + '\\' + theorder
    z = zipfile.is_zipfile(zip_src)
    if z:
        try:
            fz = zipfile.ZipFile(zip_src, "r")
            for file in fz.namelist():
                fz.extract(file, Rawipdir)
        except Exception as e:
            return 'notzip'
    else:
        return 'notzip'
    return Rawipdir


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("字段 [%s] 格式有误,错误原因: %s" % (
                getattr(form, field).label.text,
                error
            ))


def query_to_list(query, exclude=None):
    list = []
    for obj in query:
        dict = model_to_dict(obj, exclude)
        list.append(dict)
    return list
