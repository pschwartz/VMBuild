from __future__ import print_function
import logging
import os
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

    def logging(self, logger):
        self.logger = logger

    @property
    def name(self):
        return "{baseName}-{version}".format(baseName=self.baseName,
                                             version=self.version
                                             )

    @property
    def package(self):
        return "{base}-{version}{post}".format(base=self.packageBase,
                                              version=self.version,
                                              post=self.packagePost,
                                              )

    @property
    def configDir(self):
        return "{dir}".format(dir=os.path.abspath(os.path.curdir))


    @property
    def templateDir(self):
        return "{dir}/{template}".format(dir=os.path.abspath(os.path.curdir),
                                         template=self.template
                                         )
    def templateFile(self, temp):
        return "{dir}/{temp}".format(dir=self.templateDir, temp=temp)


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
        elif self.stagingMethod == "local":
            return "file://{dir}/{build}/bin/platform/{package}".format(
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
        logging.info("Creating Config obect from [{}]".format(jsonFile))
        config = Config.loadJson(jsonFile)
        return Config(config)
