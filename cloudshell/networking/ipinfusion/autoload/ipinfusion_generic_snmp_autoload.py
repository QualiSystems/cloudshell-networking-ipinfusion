#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.snmp.autoload.generic_snmp_autoload import GenericSNMPAutoload

from cloudshell.networking.ipinfusion.autoload.snmp_system_info import (
    IPInfusionSnmpSystemInfo,
)


class IPInfusionGenericSNMPAutoload(GenericSNMPAutoload):
    def __init__(self, snmp_handler, logger):
        super(IPInfusionGenericSNMPAutoload, self).__init__(snmp_handler, logger)

    @property
    def system_info_service(self):
        if not self._system_info:
            self._system_info = IPInfusionSnmpSystemInfo(self.snmp_handler, self.logger)
        return self._system_info
