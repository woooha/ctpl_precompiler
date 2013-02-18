#!/usr/bin/env python
import re,os,optparse,sys,io

class Parser:
    __symbols = {}
    __if_stack = []
    def parse(self, module_path, compress = False): 
        origin_cwd = os.getcwd()
        module_path = os.path.abspath(module_path)
        os.chdir( os.path.dirname(module_path) )
        fp = io.open(module_path)
        source = fp.read()
        source = self.__traverse_ctpl_tag(source)
        os.chdir(origin_cwd)
        if compress:
            source = self.compress(source)
        return source

    def __traverse_ctpl_tag(self, source):
        process_ctpl_tag = getattr(self, "_process_ctpl_tag")
        source = re.sub("\$([^$\s]*)\\s*(.*?)\\s*\\$", process_ctpl_tag, source) 
        return source

    def _ctpl_import(self, modules):
        for module in modules:
            self.__symbols[module] = Module(module.replace('.', '/')+'.html')
        return  ""

    def _ctpl_extend(self, modules):
        parser = Parser()
        content = ""
        for module in modules:
            content += parser.parse(module)
        return content

    def _ctpl_if(self, conditions):
        self.__if_stack.append(0)
        return None

    def _ctpl_elseif(self, conditions):
        n_elseif = self.__if_stack.pop()
        n_elseif = n_elseif + 1
        self.__if_stack.append(n_elseif)
        condition = ""
        for cond in conditions:
            condition += " " + cond
        return "$else$$if"+condition+"$"

    def _ctpl_endif(self, conditions):
        n_elseif = self.__if_stack.pop()
        return "$endif$"*(n_elseif + 1)

    def is_ctpl_cmd(self, cmd):
        return ('_ctpl_'+cmd) in dir(self)

    def _process_ctpl_tag(self, regex):
        cmd = regex.groups()[0]
        params = re.split("\\s+" ,regex.groups()[1])
        if self.is_ctpl_cmd(cmd):
            result = self.dispatch_cmd(cmd, params)
            if result == None:
                return regex.group()
            else:
                return result
        elif self.get_value(cmd): 
            return self.get_value(cmd)
        else:
            return regex.group()
            
    def in_symbols(self, key):
        return key in self.__symbols

    def dispatch_cmd(self, cmd, params):
        command = getattr(self, '_ctpl_'+cmd)
        return command(params)

    def get_value(self, var):
        var  = var.split(".")
        if var[0] in self.__symbols:
            obj = self.__symbols[var[0]]
            if len(var) == 2:
                return getattr(obj, 'get_'+var[1])()
            else:
                return obj
        return None

class Module:
    __raw_source = ""
    __style=""
    __html=""
    __script=""
    __dependances=[]

    def __init__(self, path):
        self.__get_file_content(path)
        self.__parse()

    def __get_file_content(self, path):
        if os.path.exists( path ):
            parser = Parser()
            self.__raw_source = parser.parse(path)
            return self.__raw_source

    def __parse(self):
        source = self.__raw_source
        source = self.__strip_script(source)
        source = self.__strip_style(source)
        source = self.__strip_html(source)

    def get_html(self):
        return self.__html

    def get_style(self):
        return self.__style
    
    def get_script(self):
        return self.__script   

    def __strip_script(self, source):
        script_RE = re.compile("<script[\s\S]+?</script\s*>")
        scripts = script_RE.findall(source)   
        self.__script = "".join(scripts)
        return script_RE.sub("", source)
            
    def __strip_style(self, source):
        style_RE = re.compile("<style[\s\S]+?</style\s*>")
        styles = style_RE.findall(source)
        self.__style = "".join(styles)
        return style_RE.sub("", source)

    def __strip_html(self, source):
        html_begin_RE = re.compile("^[\s\S]+<body.*?>")
        html_end_RE = re.compile("</body\s*>[\s\S]*$")
        source = html_begin_RE.sub("", source)
        source = html_end_RE.sub("", source)
        self.__html = source
        return source

if __name__ == "__main__":
    optparser = optparse.OptionParser()
    optparser.add_option("-o", "--output", dest="output_file", help="Set the path compiled template saved")
    optparser.add_option("-c", "--compress", action="store_true", default=False, help="Minify the template without any depress impact")

    (options, files) = optparser.parse_args()

    output = sys.stdout
    if options.output_file != None:
        output = io.open(options.output_file, "w", encoding='GBK', newline="\n")

    content = u""
    parser = Parser()
    for file in files:
        output.write( parser.parse(file) )
