import os
import shutil
import subprocess
import yaml

from sf.backend.openstack import Backend


class Sfinstance(object):

    def __init__(self, name=None, path='~/.sf', configuration_file=None, credential_file=None):
        self.backend = Backend()
        self.name = name
        self.path = os.path.expanduser(path)
        self.environment = '%s/%s' % (os.path.expanduser(path), name)
        self.configuration_file = os.path.expanduser(configuration_file)
        self.credential_file = os.path.expanduser(credential_file)
        self.hosts = None
        self.credentials = self.backend.load_credentials(os.path.expanduser(credential_file))

    def _build_env(self):

        _directories = ("data", "cloudinit")

        if not os.path.exists(os.path.expanduser(self.path)):
            print 'Creating root environment %s' % self.path
            os.makedirs(os.path.expanduser(self.path))
        if not os.path.exists(os.path.expanduser(self.environment)):
            print 'Creating environment %s' % self.environment
            os.makedirs(os.path.expanduser(self.environment))
        shutil.copy(self.configuration_file, os.path.expanduser(self.environment))
        shutil.copy(self.credential_file, os.path.expanduser(self.environment))
        for directory in _directories:
            if not os.path.exists(os.path.expanduser('%s/%s' % (self.environment, directory))):
                print 'Creating directory %s' % directory
                os.makedirs(os.path.expanduser('%s/%s' % (self.environment, directory)))

    def _load_configuration(self):
        conf = open(self.configuration_file, 'r')
        conf_yaml = yaml.load(conf)
        self.hosts = self.backend.load_hosts(conf_yaml['hosts'])

    def _prepare_ssh(self):

        __ssh_keys = ('jenkins_rsa', 'gerrit_service_rsa', 'gerrit_admin_rsa', 'softwarefactory')

        for key in __ssh_keys:
            if not os.path.isfile('%s/data/%s' % (os.path.expanduser(self.environment), key)):
                subprocess.call(['ssh-keygen',  '-N', '', '-f', '%s/data/%s' % (os.path.expanduser(self.environment), key)])

    def bootstrap(self):
        self._build_env()
        self._load_configuration()
        #
        self._prepare_ssh()
        #self._prepare_cloudinit()
        #
        for host in self.hosts:
          host.create(self.credentials, self.environment)
