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
import argparse
import base64

# Basic logging setup
logging.basicConfig(filename="./kmipclient.log", level=logging.DEBUG)
log = logging.getLogger("register")


def storeKeyInKMIPServer(keyFilename):
    log.debug("Creating KMIP client")
    kmipClient = client.ProxyKmipClient(
        config = "client",
        config_file = "./client.conf"
    )

    log.debug("Reading key from file: %s", keyFilename)
    with open(keyFilename, 'r') as keyFile:
        log.debug("Opened file for reading")
        keyFileData = keyFile.read().strip()

    log.debug("Read key data: %s", keyFileData)
    decodedData = base64.decodestring(keyFileData)
    log.debug("Size of decoded data: %d", len(decodedData))
    
    symmetric_key = objects.SymmetricKey(
        enums.CryptographicAlgorithm.RSA,
        256,
        decodedData
    )
    with kmipClient:
         result = kmipClient.register(symmetric_key)
         log.info("Result of registering = %s", result)


# Parse the command line arguments
parser = argparse.ArgumentParser(description='Register sysmetric key')
parser.add_argument('--key', dest='keyFile', action='store', metavar='FILE', help='path to key to store', nargs='?')
parser.add_argument('--apply', dest='apply', action='store_const', default='false', const='true', help='add this to actually apply the change, otherwise no server operation is performed')

args = parser.parse_args()

if args.apply == 'true':
    log.info("Storing key into KMIP server")
    log.debug("Using filename: %s", args.keyFile)
    storeKeyInKMIPServer(args.keyFile)

else:
    log.info("NOT applying any change to server")




