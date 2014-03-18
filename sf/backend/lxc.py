
import sf.backend.base
from sf.host.lxc import Host


class Backend(sf.backend.base.Backend):

    def __init__(self):
        super(sf.backend.base.Backend, self)

    def load_hosts(self, hosts=[]):
        """ Load hosts definition from YAML file."""
        host_list = []
        for host in hosts:
            host_list.append(Host(host['name'], address=host['address'], role=host['role']))
        return host_list
