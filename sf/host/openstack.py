import novaclient.v1_1.client as novaclient
import sf.host.base


class Host(sf.host.base.Host):

    __allowed = ('address', 'role', 'cloudinit', 'id', 'ip')

    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.iteritems():
            assert(k in self.__class__.__allowed)
            setattr(self, k, v)
        super(sf.host.base.Host, self)

    def associate_floating_ip(self, credentials):
        nova = novaclient.Client(**credentials)
        floating_ip = nova.floating_ips.create()
        instance = nova.servers.get(self.id)
        instance.add_floating_ip(floating_ip)
        self.ip = floating_ip

    def disassociate_floating_ip(self, credentials):
        nova = novaclient.Client(**credentials)
        instance = nova.servers.get(self.id)
        instance.remove_floating_ip(self.ip)

    def create(self, credentials, environment):
        nova = novaclient.Client(**credentials)
        print ' Creating node %s' % self.name

        if not nova.keypairs.findall(name="softwarefactory"):
            with open('%s/data/softwarefactory.pub' % environment) as fpubkey:
                nova.keypairs.create(name="softwarefactory", public_key=fpubkey.read())

        image = nova.images.find(name="Ubuntu 12.04 LTS x86_64")
        flavor = nova.flavors.find(name="small")
        instance = nova.servers.create(name=self.name, image=image,flavor=flavor, key_name="softwarefactory")
        self.id = instance.id
        self.associate_floating_ip(credentials)
        print '%s has id %s' % (self.name, self.id)

    def delete(self, credentials):
        nova = novaclient.Client(**credentials)
        nova.servers.delete(self.id)
        print ' Node %s deleted' % self.name
