# !/usr/bin/pythoncloudshell
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate

SAVE_CONFIG_REMOTE = CommandTemplate("copy {src} {protocol_type} {dst} vrf {vrf}")
LOAD_CONFIG_REMOTE = CommandTemplate(
    "copy {protocol_type} {src} {dst} [append{append}] [store{store}] vrf {vrf}")
SAVE_CONFIG_LOCAL = CommandTemplate("write [file {file_path}]")
LOAD_CONFIG_LOCAL = CommandTemplate(
    "copy file {file_path} {config} [append{append}] [store{store}]")

"""
DCSG-02-Lab#copy file q startup-config 
DCSG-02-Lab#copy file q startup-config ?
  <cr>

DCSG-02-Lab#copy file q running-config 
append  store   
DCSG-02-Lab#copy file q running-config ?
  append  Append the configuration into the running-config
  store   Store the running-configuration
  <cr>

"""

"""
Use this command to clear the contents of the startup configuration. 
Command Syntax
copy empty-config startup-config


Use this command to copy the running configuration to an FTP server, an SCP server, an SFTP server, a TFTP server 
or an HTTP server. 
Command Syntax
copy running-config (tftp TFTP-URL|ftp FTP-URL|scp SCP-URL|sftp SFTP-URL|http HTTP-
URL) (vrf (NAME|management)|) 
Parameters
TFTP-URL Destination: tftp:[//server[:port]][/path]
FTP-URL Destination: ftp:[//server][/path]
SCP-URL Destination: scp:[//server][/path]
SFTP-URL Destination: sftp:[//server][/path]
HTTP-URL Destination: http:[//server][/path]
NAME Virtual Routing and Forwarding name
management Management Virtual Routing and Forwarding


Use this command to copy the start up configuration from an FTP server to the local device.
Command Syntax
copy ftp FTP-URL startup-config (vrf (NAME|management)|)


Use this command to append the running configuration from an FTP server to the local device.
Command Syntax
copy ftp FTP-URL running-config append (store|) (vrf (NAME|management)|)


Use this command to copy and store a local file into the startup configuration.
Command Syntax
copy file FILE startup-config


Use this command to copy and store a file into the running configuration.
Command Syntax
copy file FILE running-config (append|) store


Use this command to copy the start-up configuration to the running configuration.
Command Syntax
copy startup-config running-config


Use this command to a write the configuration to the file used at startup or to a specified file. This is the same as the 
copy running-config startup-config command.
Command Syntax
write file FILE


This example shows writing the configuration to the startup configuration file:
#write
Building configuration... 

"""
