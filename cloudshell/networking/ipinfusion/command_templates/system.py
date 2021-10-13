# !/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate

COMMIT = CommandTemplate("commit")
CREATE_FOLDER = CommandTemplate("mkdir {folder_path}")
RELOAD = CommandTemplate("reload [flush-db]")

"""
This example shows replacing a start-up configuration file and then synchronizing it to the configuration database:
#copy file /home/TEST.conf startup-config
Copy Success
#

#reload flush-db
The system has unsaved changes.
Would you like to save them now? (y/n): n
 
Configuration Not Saved!
Are you sure you would like to reset the system? (y/n): y
For both of these prompts, you must specify whether to save or discard the changes. Abnormal termination of the 
session without these inputs can impact the system behavior.
For the unsaved changes prompt:
Would you like to save them now?
You should always say “no” to this prompt because otherwise the command takes the current running configuration and 
applies it to the current start-up configuration.
"""