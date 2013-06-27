VMBuild
=======

This application facilitates the creation of a ova based virtal machine.

Requirements
------------

+ Linux
+ Virtualbox (Latest release 4.2.14 has a bug causing vagrant to fail)
+ Vagrant (http://www.vagrantup.com version 1.2.2+)
+ Python 2.7.x
+ Paramiko


Currently this code line is based around the HPCCSystems.com VM build process.

Usage
-----

    usage: Generate a Vagrant VM Build. [-h] [--template= TEMPLATE] [--dest DEST]
                                    [--key KEY] [--level LEVEL]
                                    VERSION BUILD

    positional arguments:
        VERSION               Version to build.
        BUILD                 Build to locate on staging.

    optional arguments:
        -h, --help            show this help message and exit
        --template= TEMPLATE  Template to use for the Build.
        --dest DEST           The destination to create the Build.
        --key KEY             SSH Key to use to get file from staging.
        --level LEVEL         Set Logging level.


    ex. ./generate-vm-template.py 3.10.8-9 CE-Candidate-3.8.x


Configuration
-------------

To configure, modify HPCCSystemsVM.json.

Currently only one stagingMethod works, "ssh".
