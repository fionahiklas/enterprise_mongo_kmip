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
pip install requests # This seems to be missing from the dependencies in PyKMIP
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

Remove the passphrase from the key using the following command

```
openssl rsa -in kmipserver-secure.key -out kmipserver.key
```


### Starting the server

Run the following command

```
./matrix/bin/pykmip-server -f server.conf -l ./pykmip.log &
```

You can monitor progress from the `pykmip.log` file


### Examining the DB

The PyKMIP server uses [SQLite](https://www.sqlite.org/index.html) so you can view the database it uses to keep
track of keys with the following command

```
sqlite3 pykmip.sqlite
```

this is as executed on Ubuntu 18.10 - there is both `sqlite` and `sqlite3` only the latter works correctly.

### Create Client Key and Cert

Using [easyrsa](https://github.com/OpenVPN/easy-rsa) as setup above for the server (re-use same setup)

```
easyrsa gen-req kmipclient # Used 'password' for passphrase
```

Under the `mongo_enterprise_ca` project run the following

```
easyrsa import-req ../enterprise_mongo_kmip/pki/reqs/kmipclient.req kmipclient
easyrsa sign-req client kmipclient
```

Remove the passphrase from the key using the following command

```
openssl rsa -in kmipclient-secure.key -out kmipclient.key
```
