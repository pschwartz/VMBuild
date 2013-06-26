from __future__ import print_function
import simplejson as json


class Config(object):
    """docstring for Config"""
    def __init__(self, config):
        """initialize by passing in a dictionary repr of the config"""
        self.config = config

    def addConfigItem(self, name, value):
        self.config[name] = value

    def __getattr__(self, name):
        try:
            return self.config[name]
        except KeyError:
            return None

    @property
    def package(self):
        return "{base}{version}{post}".format(base=self.packageBase,
                                              version=self.version,
                                              post=self.packagePost,
                                              )

    @property
    def localPackage(self):
        return "{dest}/{package}".format(dest=self.dest, package=self.package)

    @property
    def remotePackage(self):
        if self.stagingMethod == "http":
            return "http://{staging}/builds/{build}/bin/platform/{package}".format(
                    staging=self.staging,
                    build=self.build,
                    package=self.package
                    )
        elif self.stagingMethod == "ssh":
            return "{dir}/{build}/bin/platform/{package}".format(
                    dir=self.buildDir,
                    build=self.build,
                    package=self.package
                    )
        else:
            raise Exception("Invalid stagingMethod [{}]".format(self.stagingMethod))

    @staticmethod
    def loadJson(fp):
        with open(fp) as f:
            return json.load(f)

    @staticmethod
    def ConfigFactory_fromJson(jsonFile):
        config = Config.loadJson(jsonFile)
        return Config(config)
