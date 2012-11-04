#!/usr/bin/python
from optparse import OptionParser
import sys
import Template

optparser = OptionParser()
optparser.add_option("-o", "--output", dest="output_file", help="Set the path compiled template saved")
optparser.add_option("-c", "--compress", action="store_true", default=False, help="Minify the template without any depress impact")

(options, files) = optparser.parse_args()

if options.output_file != None:
    output_fd = open(options.output_file, "w")
    _stdout = sys.stdout
    sys.stdout = output_fd

content = ""
for file in files:
    tpl = Template.Template(file)
    tpl.compile()
    content += tpl.content 

print content
