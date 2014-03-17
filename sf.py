#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(prog='sf', usage="%(prog)s [action] [options]")
parser.add_argument("-v", "--version", help="sf version number", action="version")
subparser = parser.add_subparsers(help="sub-command help",title="subcommands")
parser_bootstrap = subparser.add_parser('bootstrap')
parser_bootstrap.add_argument("-b", "--backend", help="The backend to deploy SF on", choices=["openstack", "lxc", "aws"], metavar="BACKEND", required=True)
parser_bootstrap.add_argument("-c", "--credential", help="Path to the credientail file")
parser_bootstrap.add_argument("-e", "--environment", help="Path to the environement directory", default="~/.sf")
parser_bootstrap.add_argument("sf-instance-name", help="name of the SF instance", metavar="name")
parser_manage = subparser.add_parser('manage')
parser_manage.add_argument("-p", "--project", help="Project definition file")
parser_manage.add_argument("-s", "--sf", help="Software Factory definition file")
args = parser.parse_args()


