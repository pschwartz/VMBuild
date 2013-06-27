#!/usr/bin/env python

from __future__ import print_function
import argparse
import logging
import os
import paramiko
import sys

from vmgen.config import Config
from vmgen.scp import SCP
from vmgen.template import Template
from vmgen.generator import Generator
from vmgen.logger import Logger



def main():

    parser = argparse.ArgumentParser("Generate a Vagrant VM Build.")
    parser.add_argument("--template=", dest='template', default='template',
                        help='Template to use for the Build.'
                        )
    parser.add_argument("--dest", dest='dest', default="/tmp",
                        help='The destination to create the Build.'
                        )
    parser.add_argument("--key", dest='key', default="~/.ssh/id_rsa",
                        help='SSH Key to use to get file from staging.'
                        )
    parser.add_argument("--level", dest='level', default="info",
                        help='Set Logging level.'
                        )
    parser.add_argument("version", metavar="VERSION", type=str, default="",
                        help='Version to build.'
                        )
    parser.add_argument("build", metavar="BUILD", type=str, default="",
                        help='Build to locate on staging.'
                        )
    args = parser.parse_args()

    try:
        log = Logger(args.level)

        #Move paramiko logging to WARNINGS+ only.
        if args.level != "debug":
            logging.debug("Setting paramiko logging to WARNING")
            logging.getLogger("paramiko").setLevel(logging.WARNING)
        else:
            logging.debug("Setting paramiko logging to INFO")
            logging.getLogger("paramiko").setLevel(logging.INFO)

        logging.info("Launching VM Build Generation.")
        conf = Config.ConfigFactory_fromJson("HPCCSystemsVM.json")
        conf.addConfigItem("template", args.template)
        conf.addConfigItem("dest", args.dest+"/"+args.version)
        conf.addConfigItem("key", os.path.abspath(args.key))
        conf.addConfigItem("version", args.version)
        conf.addConfigItem("build", args.build)
        gen = Generator.GeneratorFactory(conf)

        #print(temp.txt)

    except Exception as e:
        logging.critical(e)
    except KeyboardInterrupt:
        logging.critical("Keyboard Interrupt Caught.")

if __name__ == "__main__":
    main()
