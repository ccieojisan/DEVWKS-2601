"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Simon Hart"
__email__ = "sihart@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"



from genie.conf import Genie
from genie import parsergen
from pprint import pprint

#open marked up text file and read into variable
f = open('markup.txt', 'r')
markedupIOSX = f.read()

#initiate testbed
testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

#extend parsergen markup with text file indicating elements to parse
parsergen.extend_markup(markedupIOSX)

#identify which parsed element to check as true
attrValPairsToCheck = [
    ('nve.intf.encap', 'Vxlan'),]

#parsergen will connect to device and issue show nve interface nve1
#Will check for elements to be parsed and create a dictionary
pgfill = parsergen.oper_fill(device=uut,
    show_command=\
('show_nve_interface', [], {'ifname':'nve1'}),
attrvalpairs=attrValPairsToCheck,
refresh_cache=True, regex_tag_fill_pattern='nve\.intf')

result = pgfill.parse()
print(result)
print("Parsing details : {}".format(parsergen.ext_dictio[uut.name]))
pprint(parsergen.ext_dictio)