
"""Base class for all Software Factory backends"""

class Backend(object):

    def __init__(self):
        """ Initialize the backend."""

    def images_upload(self):
        """ Upload image to the backend."""
        pass

    def images_create(self):
        """ Create edeploy images."""
        pass

    def images_delete(self):
        """ Delete edeploy images. Eventually on the remote (Glance) services also."""
        pass

    def nodes_create(self):
        """ Create all nodes on the backend."""

    def nodes_delete(self):
        """ Delete all nodes on the backend."""

    def node_create(self):
        """ Create a node on the backend."""

    def node_delete(self):
        """ Delete a node on the backend."""

