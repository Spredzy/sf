import sf.host.base.Host

class Host(sf.host.base.Host):

    def __init__(self):
        self.memory = 2048
        self.vcpu = 2
        self.xml = _get_domain_xml()

    def _get_domain_xml(self):

        xmlDesc = "<domain type='lxc'>\n" + \
            " <name>%s</name>\n" % self.name + \
            " <memory unit='MB'>%s</memory>\n" % self.memory + \
            " <os>\n" + \
            " <type>exe</type>\n" + \
            " <init>/sbin/init</init>\n" + \
            " </os>\n" + \
            " <vcpu>%s</vcpu>\n" % self.vcpu + \
            " <clock offset='utc'/>\n" + \
            " <on_poweroff>destroy</on_poweroff>\n" + \
            " <on_reboot>restart</on_reboot>\n" + \
            " <on_crash>destroy</on_crash>\n" + \
            " <devices>\n" + \
            " <emulator>/usr/libexec/libvirt_lxc</emulator>\n" + \
            " <filesystem type='mount'>\n" + \
            " <source dir='/var/lib/lxc/%s'/>\n" % self.name + \
            " <target dir='/'/>\n" + \
            " </filesystem>\n" + \
            " <interface type='network'>\n" + \
            " <source network='%s'/>\n" % self.network.name + \
            " </interface>\n" + \
            " <console type='pty' />\n" + \
            " </devices>\n" + \
            "</domain>"

        return xmlDesc


    def _create_filesystem(self):
        subprocess.call(['qemu-nbd', '-c', "/dev/nbd%s" % self.idx, "%s/%s.qcow2" % (self.config.lxc_dir, self.name)])
        subprocess.call(['mount', "/dev/nbd%s" % self.idx, "%s/%s" % (self.config.lxc_dir, self.name)])

    def _create_cloudinit(self):
        

    def create(self):
        _create_filesystem()
        _create_cloudinit()
        create_ssh()
        update_etc_hosts()
        
        domain = conn.defineXML(self.xml)
        domain.create() 

    def delete(self):

    def get_ip(self):

    def update(self):
