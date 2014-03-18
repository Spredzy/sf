
import re
import sf.backend.base
from sf.host.openstack import Host

RC_TO_NOVACLIENT = {'OS_USERNAME': 'username',
                    'OS_PASSWORD': 'api_key',
                    'OS_AUTH_URL': 'auth_url',
                    'OS_TENANT_NAME': 'project_id'}


class Backend(sf.backend.base.Backend):

    def __init__(self):
        super(sf.backend.base.Backend, self)

    def load_hosts(self, hosts=[]):
        host_list = []
        for host in hosts:
            host_list.append(Host(host['name'], role=host['role']))
        return host_list

    def load_credentials(self, credential_path):
        export_line = re.compile('export (.*)=(.*)')
        creds = {}
        conf = open(credential_path, 'r')
        for line in conf:
            m = export_line.match(line)
            creds[RC_TO_NOVACLIENT[m.group(1)]] = m.group(2)
        return creds
