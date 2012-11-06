#!/usr/bin/env python
# vim : set fileencoding=utf-8
import os,sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--dest", help="��ָ�� asp �������ڵ��ļ���", dest="asp_root", default=".")
[option, args] = parser.parse_args()
asp_root = option.asp_root

if not os.path.isdir(asp_root):
    asp_root = os.path.dirname(asp_root)
    exit(1)

if not os.path.exists(asp_root) :
    print "�������·��������"
    exit(1)

if not os.path.exists(asp_root + "/bin/asp") or not os.path.exists(asp_root + "/bin/reload" ):
    print "�������·������ asp ����ĸ�Ŀ¼"
    exit(1)

precompile_path = os.path.abspath( os.path.dirname( os.path.abspath( sys.argv[0] ) ) + '/..')
src_path = precompile_path + "/src"
tools_path = precompile_path + "/tools"

os.system("cp %s/compile.py %s/Template.py %s/bin/" % (src_path, src_path, asp_root) )
os.system("cp %s/reload.py %s/bin/" % (tools_path, asp_root) )

print "��װ�ɹ�!"
print "���ڸ���ģ��ʱ��ʹ�� %ASP_ROOT%/bin Ŀ¼�µ� reload.py , �����ƶ��˿ڣ������Զ�������ģ���ļ����µ� index.html Ԥ����Ϊ page.html, �����¼���ģ�� "
