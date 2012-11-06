#!/usr/bin/env python
from optparse import OptionParser
import sys
import Template
import io
import os
import re
optparser = OptionParser()
optparser.add_option("-o", "--output", dest="output_file", help="Set the path compiled template saved")
optparser.add_option("-c", "--compress", action="store_true", default=False, help="Minify the template without any depress impact")

(options, files) = optparser.parse_args()
output = sys.stdout
if options.output_file != None:
    output = io.open(options.output_file, "w", encoding='GBK', newline="\n")

content = u""
for file in files:
    tpl = Template.Template(file)
    tpl.preprocess()
    content += tpl.content 
#content = re.sub("\r\n","\n",content)
output.write(content)
