#!/usr/bin/python

import argparse
from sf.sfinstance import Sfinstance

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='sf', usage="%(prog)s [action] [options]")
    parser.add_argument("-v", "--version", help="sf version number", action="version")
    subparser = parser.add_subparsers(help="sub-command help",title="subcommands")

    parser_bootstrap = subparser.add_parser('bootstrap')
    parser_bootstrap.add_argument("-b", "--backend", help="The backend to deploy SF on", choices=["openstack", "lxc", "aws"], metavar="BACKEND", required=True)
    parser_bootstrap.add_argument("-c", "--configuration", help="Path to the configuration file")
    parser_bootstrap.add_argument("--credentials", help="Path to the credentials file")
    parser_bootstrap.add_argument("-e", "--environment", help="Path to the environement directory", default="~/.sf")
    parser_bootstrap.add_argument("name", help="name of the SF instance", metavar="name")
    args = parser.parse_args()

    print "[Start]"
    e = Sfinstance(name=args.name, path=args.environment, configuration_file=args.configuration, credential_file=args.credentials)
    e.bootstrap()
    print "[Finish]"
