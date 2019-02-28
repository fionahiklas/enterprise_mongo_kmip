## Overview

Setup and configuration for test KMIP (Key Management Interoperability Protocol) server.

Using [PyKMIP](https://github.com/OpenKMIP/PyKMIP)

## Getting started

### Install PyKMIP

Setup a python virtual environment using `virtualenv`

```
virtualenv matrix
. ./matrix/bin/activate
```

Install the [PyKMIP](https://github.com/OpenKMIP/PyKMIP) package using `pip`

```
pip install pykmip
```


### Create KMIP certs

Using [easyrsa](https://github.com/OpenVPN/easy-rsa)

```
easyrsa init-pki
easyrsa gen-req kmipserver # Used 'password' for passphrase
```

Under the `mongo_enterprise_ca` project run the following

```
easyrsa import-req ../enterprise_mongo_kmip/pki/reqs/kmipserver.req kmipserver
easyrsa sign-req server kmipserver
```


