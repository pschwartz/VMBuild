from paramiko import SSHClient, AutoAddPolicy


class SSH(object):
    """docstring for SSH"""
    def __init__(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()

    def connect(self, server, user, key):
        self.client.connect(server, username=user,
                       key_filename=key)

    def close():
        self.client.close()

    @property
    def transport(self):
        return self.client.get_transport()


    @staticmethod
    def SSHFactory(config):
        sClient = SSH()
        sClient.connect(config.staging,
                        config.stagingUser,
                        config.key
                        )
        return sClient