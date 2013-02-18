#from Module import Module
#mod = Module("index.html")
#print mod._Module__html
#print mod._Module__style
#print mod._Module__script
import Parser

parser = Parser.Parser()
print parser.parse("index.html")
