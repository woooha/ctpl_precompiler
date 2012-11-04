import os
import re

class Template:
    path = None
    content = None   
 
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.content = Template._load_tpl(self.path)

    def _include(self, path):
        __include = lambda regex: (Template(regex.groups()[0]))._include()
        self.content = re.sub("\$include\\s+(.+?)\\s*\$", __include, self.content)
        return self.content

    def save(self):
        fp = open(self.path, 'w')
        fp.write(self.content)

    def compile(self):
        self._include()

    @staticmethod
    def _load_tpl(path):
        path = os.path.abspath(path)
        fp = open(path, 'r')
        return fp.read()

    def preprocess(self):
        re.sub("\$([a-z]+?)\\s+(.+?)\\s*\$", lambda regex: return self._dispatch(regex.groups()[0], regex.groups()[1]), self.content) 

    def _dispatch(self, command, args): 
        command = "_" + command
        if command in dir(self):
            cmd = getattr(self, command)
            cmd(args)
