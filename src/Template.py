import os
import re
import io

class Template:
    path = None
    content = None   
 
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.content = unicode( Template._load_tpl(self.path) )

    def _include(self, path):
        old_cwd = os.getcwd() 
        os.chdir(os.path.dirname(self.path))
        path = os.path.abspath(path)
        cwd = os.path.dirname(path)
        os.chdir(cwd)
        tpl = Template(path)
        tpl.preprocess()
        os.chdir(old_cwd)
        return tpl.content

    def save(self):
        fp = open(self.path, 'w')
        fp.write(self.content)


    @staticmethod
    def _load_tpl(path):
        path = os.path.abspath(path)
        fp = io.open(path, 'r', encoding='GBK', newline='\n')
        return fp.read()

    def preprocess(self):
        self.content = re.sub("\$([a-z]+?)\\s+(.+?)\\s*\$", lambda regex: self._dispatch(regex.groups()[0], regex.groups()[1], regex.group()), self.content) 

    def _dispatch(self, command, args, origin): 
        command = "_" + command
        if command in dir(self):
            cmd = getattr(self, command)
            return cmd(args)
        else:
            return origin
