#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

from cloudshell.networking.ipinfusion.flows.ipinfusion_enable_snmp_flow import (
    IPInfusionEnableSnmpFlow,
)


class TestIPInfusionEnableSnmpFlow(TestCase):
    def test_import(self):
        self.assertTrue(IPInfusionEnableSnmpFlow)
