
class Sfinstance(object):

    def __init__(self, name=None, path='~/.sf'):
        self.name = name 
        self.path = '%s/%s' % (path, name)
        self.images = None
        self.edeploy_basedir = '/home/yguenane/enovance/edeploy-software-factory'
        self.edeploy_roles = ['gerrit', 'jenkins', 'mysql', 'redmine']


    def _build_env(self):
        if not os.path.exists(self.path):
            os.create(self.path)

    def _build_edeploy_roles(self,refresh=False,remote=False):
        if refresh:
            backend.images_delete(self, remote)
        backend.images_create(self)
