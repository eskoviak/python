import io
import json
import xmltodict

infile = 'smalldoc.xml'

with io.open(infile) as file:
  print(json.dumps(xmltodict.parse(file.read())))


