from sf.backend.base import Backend
from sf.image.openstack import Image

class Backend(sf.backend.base.Backend):

    def __init__(self):

    def image_upload(self):
        for role in self.edeploy_roles:
            Image(self.edeploy_path, self.edeploy_roles).upload()

    def images_create(self):
        for role in self.edeploy_roles:
            Image(self.edeploy_path, self.edeploy_roles).create()

    def images_delete(self,edeploy_basedir,edeploy_roles):
        for role in edeploy_roles:
            Image(self.edeploy_path, self.edeploy_roles).delete()
