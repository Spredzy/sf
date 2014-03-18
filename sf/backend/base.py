
"""Base class for all Software Factory backends"""


class Backend(object):

    def __init__(self):
        """ Initialize the backend."""

    def load_hosts(self, hosts=[]):
        """ Load hosts definition from YAML file."""
        pass

    def load_credentials(self, credentials_file):
        """ Load credentials from file."""
        pass

    def delete_nodes(self):
        """ Delete all nodes on the backend."""
        pass
