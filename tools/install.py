#!/usr/bin/env python
# vim : set fileencoding=utf-8
import os,sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--dest", help="请指定 asp 程序所在的文件夹", dest="asp_root", default=".")
[option, args] = parser.parse_args()
asp_root = option.asp_root

if not os.path.isdir(asp_root):
    asp_root = os.path.dirname(asp_root)
    exit(1)

if not os.path.exists(asp_root) :
    print "您输入的路径不存在"
    exit(1)

if not os.path.exists(asp_root + "/bin/asp") or not os.path.exists(asp_root + "/bin/reload" ):
    print "您输入的路径不是 asp 程序的根目录"
    exit(1)

precompile_path = os.path.abspath( os.path.dirname( os.path.abspath( sys.argv[0] ) ) + '/..')
src_path = precompile_path + "/src"
tools_path = precompile_path + "/tools"

os.system("cp %s/compile.py %s/Template.py %s/bin/" % (src_path, src_path, asp_root) )
os.system("cp %s/reload.py %s/bin/" % (tools_path, asp_root) )

print "安装成功!"
print "请在更新模板时，使用 %ASP_ROOT%/bin 目录下的 reload.py , 不需制定端口，即可自动将各个模板文件夹下的 index.html 预编译为 page.html, 并重新加载模板 "
