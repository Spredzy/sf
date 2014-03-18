import sf.host.base


class Host(sf.host.base.Host):

    __allowed = ('address', 'role', 'network', 'cloudinit', 'memory', 'vcpu')

    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.iteritems():
            assert(k in self.__class__.__allowed)
            setattr(self, k, v)
        super(sf.host.base.Host, self)

    def create(self):
        return
