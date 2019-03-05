#!/usr/bin/env python
#
# Simple script to take an RSA key and register it with KMIP
#
# Copied from the PyKMIP demos
#
#

from kmip.pie import objects
from kmip.pie import client
from kmip import enums

import logging

logging.basicConfig(filename="./kmipclient.log", level=logging.DEBUG)

kmipClient = client.ProxyKmipClient(
    config = "client",
    config_file = "./client.conf"
)

symmetric_key = objects.SymmetricKey(
    enums.CryptographicAlgorithm.AES,
    128,
    (
        b'\x00\x01\x02\x03\x04\x05\x06\x07'
        b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    )
)
with kmipClient:
    result = kmipClient.register(symmetric_key)
    print "Result of registering = " + result



