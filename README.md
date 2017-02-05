# Cisco REST
Everybody is talking about network automation.
Everybody is talking about API.

So why not making it available ?

This project is the idea to add a API for the majority of Cisco Enterprise networking gear.
At the moment these capabilities are only availble on high-end routers and switches. 
The current provided SDN controllers are limited in capabilities.

## Prerequisites
- Python
- Flask
- Pexpect

## Usage
Start the cisco-rest daemon
```
# export FLASK_APP=cisco-rest.py
# flask run --host 0.0.0.0

```


## Changelog

v0.1 First version to provide a REST API for simple enable/shutdown of interfaces without any basic failure checks
