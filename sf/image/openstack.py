import sf.image.base import Image

class Image(sf.image.base.Image):

    def __init__(self, path=None, role=None):
        super(self, path, role)

    def create(self):
        system.call(['make', '%s/%s' % (edeploy_basedir, role), ' VIRTUALIZED=%s.virt' % role]) 

    def upload(self):
        if not gc.images.list():
            self.id = gc.images.upload()
        return

    def delete(self,remote=False):
        if remote:
            gc.images.delete(self.id)
        system.call(['rm', '-rf', '%s/%s*' % (edeploy_basedir, role)]) 
        return
