import os

class Template(object):
    """docstring for Template"""
    def __init__(self, config, temp):
        self.config = config
        self.file = Template.getfile(temp)
        self.txt = Template.readfile(temp)

    def replaceParam(self, key, value):
        self.txt = self.txt.replace(key, value)

    @property
    def outFile(self):
        return "{dir}/{temp}".format(dir=self.config.dest,
                                     temp=self.file)

    def write(self):
        with open(self.outFile, 'w+') as f:
            f.write(self.txt)

    @staticmethod
    def getfile(fn):
        return os.path.basename(fn).replace(".in", "")

    @staticmethod
    def readfile(fn):
        with open(fn) as f:
            txt = f.read()
        return txt

    @staticmethod
    def TemplateFactory(config, temp, rep):
        temp = Template(config, temp)
        for k,v in rep:
            temp.replaceParam(k,v)
        return temp

