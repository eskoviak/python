import io
import json
import xmltodict

infile = 'smalldoc.xml'

with io.open(infile) as file:
    print('Here is the data')
    print(json.dumps(xmltodict.parse(file.read())))


