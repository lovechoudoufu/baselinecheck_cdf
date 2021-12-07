# -*- coding: utf-8 -*-
import os
import zipfile

from flask import flash

from playhouse.shortcuts import model_to_dict

# 文件夹to压缩包
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
    return (zipdir,zipbao)


# zip解压到文件夹
def zip_to_file(theorder,zip_src,systemtype):
# zip_src是传入的上传上来的zip压缩包保存在系统中的路径，systemtype是系统类型（windows、linux），不同的系统解压到不同的目录。
    BaseDir = os.getcwd()
    Rawipdir = BaseDir + '\\models\\Raw\\'+systemtype+'\\' + theorder
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


# peewee转list  把数据库中查询出来的数据，用这个函数转换成dict字典的形式，提供给后面web的报告下载页面的显示
def query_to_list(query, exclude=None):
    list = []
    for obj in query:
        dict = model_to_dict(obj, exclude)
        list.append(dict)
    return list
