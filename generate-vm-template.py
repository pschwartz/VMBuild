#!/usr/bin/env python

from __future__ import print_function
import argparse

from vmgen.config import Config
from vmgen.scp import SCP
from vmgen.template import Template

def main():
    parser = argparse.ArgumentParser("Generate a Vagrant VM Build.")
    parser.add_argument("--template=", dest='template', default='template',
                        help='Template to use for the Build.'
                        )
    parser.add_argument("--dest", dest='dest', default="/tmp",
                        help='The destination to create the Build.'
                        )
    parser.add_argument("--key", dest='key', default="",
                        help='SSH Key to use to get file from staging.'
                        )
    parser.add_argument("version", metavar="VERSION", type=str, default="",
                        help='Version to build.'
                        )
    parser.add_argument("build", metavar="BUILD", type=str, default="",
                        help='Build to locate on staging.'
                        )
    args = parser.parse_args()

    try:
        conf = Config.ConfigFactory_fromJson("HPCCSystemsVM.json")
        conf.addConfigItem("template", args.template)
        conf.addConfigItem("dest", args.dest+"/"+args.version)
        conf.addConfigItem("key", args.key)
        conf.addConfigItem("version", args.version)
        conf.addConfigItem("build", args.build)

        #sClient = SCP.SCPFactory(conf)
        #sClient.get(conf.remotePackage, conf.dest)


        rep = [
            ("{{NAME}}", conf.name),
            ("{{PACKAGE}}", conf.package),
            ("{{VERSION}}", conf.version)
        ]

        for temp in conf.templates:
            Template.TemplateFactory(conf, conf.templateFile(temp), rep).write()

        #print(temp.txt)


    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
