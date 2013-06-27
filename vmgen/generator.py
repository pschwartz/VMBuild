from __future__ import print_function
import logging
import os
import shutil

from vmgen.template import Template
from vmgen.scp import SCP


class Generator(object):
    """docstring for Generator"""
    def __init__(self, config):
        self.config = config

    def getPackage(self):
        if self.config.stagingMethod == "ssh":
            sClient = SCP.SCPFactory(self.config)
            sClient.get(self.config.remotePackage, self.config.dest)
        elif self.config.stagingMethod == "http":
            pass
        elif self.config.stagingMethod == "local":
            pass
        else:
            raise Exception("Invalid stagingMethod [{}]".format(self.stagingMethod))

    def createDest(self):
        if os.path.isdir(self.config.dest):
            logging.info("Removing existing directory [{}]".format(self.config.dest))
            shutil.rmtree(self.config.dest)
        logging.info("Creating directory [{}]".format(self.config.dest))
        os.mkdir(self.config.dest)

    def generateTemplates(self):
        for temp in self.config.templates:
            Template.TemplateFactory(self.config,
                                     self.config.templateFile(temp)
                                     ).write()

    @staticmethod
    def GeneratorFactory(config):
        logging.debug("Creating Generator object.")
        gen = Generator(config)
        gen.createDest()
        gen.getPackage()
        logging.info("Using template directory [{}]".format(config.templateDir))
        gen.generateTemplates()
        return gen