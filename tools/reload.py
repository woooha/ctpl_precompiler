#!python
#vim : set fileencoding=utf-8
import sys,os,re

bin_path = os.path.dirname(os.getcwd() + '/' + sys.argv[0])
conf_path = os.path.abspath(bin_path + "/../conf")
asp_conf = conf_path + "/asp.conf"
templates_path = os.path.abspath( bin_path + "/../data/template" )

def get_reload_port( conf_file ):
    fd = open( conf_file )
    line = fd.readline()
    reload_port_RE = re.compile("^\\s*RELOAD_PORT\\s+:\\s+(\d+)\\s*$")
    while line:
        matched = reload_port_RE.match(line)
        if matched != None:
            return matched.groups()[0]
        line = fd.readline()
    print "无法找到 reload 端口，请检查配置文件是否正确或 ctpl_precompiler 是否成功安装"
    exit(1)
    return None

def compile_template( tpl_dir ):
    if os.path.exists(tpl_dir + "/index.html" ):
        os.system( "python %s/compile.py %s/index.html -o %s/page.html"%(bin_path, tpl_dir, tpl_dir) ) 

for entry in os.listdir( templates_path ):
    if os.path.isdir(templates_path + '/' + entry ):
        compile_template( templates_path+'/'+entry )

#get the reload port from asp.conf and reload 
reload_port = get_reload_port(asp_conf)
os.system("%s/reload -p %s" % (bin_path, reload_port))
