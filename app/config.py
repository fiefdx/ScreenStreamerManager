# -*- coding: utf-8 -*-
'''
Created on 2015-11-10
@summary:  MangaSpider yaml configuration
@author: YangHaitao
''' 
try:
    import yaml
except ImportError:
    raise ImportError("Config module requires pyYAML package, please check if pyYAML is installed!")

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import os
#
# default config
CONFIG = {}
try:
    # script in the app dir
    cwd = os.path.split(os.path.realpath(__file__))[0]
    configpath = os.path.join(cwd, "configuration.yml")
    localConf = load(stream = file(configpath), Loader = Loader)
    CONFIG.update(localConf)
    CONFIG["app_path"] = cwd
    CONFIG["pid_path"] = cwd
    CONFIG["config_path"] = cwd
    CONFIG["static_path"] = os.path.join(cwd, "static")

except Exception, e:
    print e

if __name__ == "__main__":
    print "cwd: %s"%cwd
    print "configpath: %s"%configpath
    print "CONFIG: %s"%CONFIG
    import json
    print json.dumps(CONFIG, indent = 4)



