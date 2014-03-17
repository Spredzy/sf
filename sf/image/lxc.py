import sf.image.base import Image

class Image(sf.image.base.Image):

    def __init__(self, path=None, role=None):
        super(self, path, role)

    def create(self):
        system.call(['make', '%s/%s' % (edeploy_basedir, role)]) 

    def upload(self):
        return

    def delete(self):
        return
