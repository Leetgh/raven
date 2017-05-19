import os
#from modules.registry import regparse
#from modules import Command
from registryApp.modules.registry import regparse

def test(plugin):
  return regparse.runPlugins(["/Users/HappyDay/Documents/python-regparse/Registry/system"], plugin)





#https://github.com/yampelo/samparser/blob/master/samparser.py
#https://github.com/mandiant/ShimCacheParser/blob/master/ShimCacheParser.py