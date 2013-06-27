import os
import shutil

from vmgen.template import Template
from vmgen.scp import SCP


class Generator(object):
    """docstring for Generator"""
    def __init__(self, config):
        self.config = config

    def getPackage(self):
        sClient = SCP.SCPFactory(self.config)
        sClient.get(self.config.remotePackage, self.config.dest)

    def createDest(self):
        if os.path.isdir(self.config.dest):
            shutil.rmtree(self.config.dest)
        os.mkdir(self.config.dest)

    def generateTemplates(self):
        for temp in self.config.templates:
            Template.TemplateFactory(self.config,
                                     self.config.templateFile(temp)
                                     ).write()

    @staticmethod
    def GeneratorFactory(config):
        gen = Generator(config)
        gen.createDest()
        gen.getPackage()
        gen.generateTemplates()
        return gen