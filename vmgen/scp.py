from thirdparty.scp import SCPClient
from .ssh import SSH

class SCP(object):
    """docstring for SCP"""
    def __init__(self, sClient):
        self.ssh = sClient
        self.client = SCPClient(self.ssh.transport)

    def put(self, files, remote_path='.', recursive=False,
            preserve_times=False):
        self.client.put(files, remove_path, recursive, preserve_times)

    def get(self, remote_path, local_path='.', recursive=False,
            preserve_times=False):
        self.client.get(remote_path, local_path, recursive, preserve_times)

    @staticmethod
    def SCPFactory(config):
        sClient = SSH.SSHFactory(config)
        return SCP(sClient)