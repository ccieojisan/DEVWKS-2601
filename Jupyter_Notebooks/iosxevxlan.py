# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie import parsergen
from genie.metaparser.util.schemaengine import Any, Optional



# parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Parser for 'show nve peers'
# =============================================

class ShowNvePeersSchema(MetaParser):
    """Schema for show nve peers
    """

    schema = {
        Any():{
        #    Any(): {
                'Interface': str,
                'Peer-IP': str,

                'Router-RMAC': str,
                'Type': str,
                Optional('Crap'): str,
                'UP time': str,
                'VNI': str,
                'eVNI': str,
               'flags': str,
               'state': str,
           },
        }
   #}


class ShowNvePeers(ShowNvePeersSchema):
# class ShowNvePeers():
    """ Parser for nve peers """

    def cli(self):
        # excute command to get output
        cmd = 'show nve peers'
        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Type', 'Peer-IP', 'Router-RMAC', 'eVNI', 'state', 'flags', 'UP time']

        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

        return result.entries

# =============================================
# Parser for 'show nve vni'
# =============================================

class ShowNveVniSchema(MetaParser):
    """Schema for show vni peers
    """

    schema = {
        Any():{
        #    Any(): {
                'BD': str,
                'Interface': str,

                Optional('Mode'): str,
                'Multicast-group': str,
                Optional('Crap'): str,
                'VNI': str,
                'VNIstate': str,
                'cfg': str,
               'vrf': str
           },
        }
   #}

class ShowNveVni(ShowNveVniSchema):
# class ShowNveVni():
    """ Parser for nve vni """

    def cli(self):
        # excute command to get output
        cmd = 'show nve vni'

        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']
        label = ['Interface', 'VNI', 'Multicast-group', 'VNIstate', 'Mode', 'BD', 'cfg', 'vrf']


        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, label_fields=label, index=[0])

        return result.entries