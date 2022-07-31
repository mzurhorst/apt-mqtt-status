# apt-mqtt-status
Small MQTT client, which sends/receives MQTT messages about available APT updates and notifies a Telgram account. 

## Introduction
apt-mqtt-status will can run in client or server mode.

### Client mode
apt-mqtt-status will be executed periodically (e.g. via a Cronjob), update apt repositories (apt update) and creates a summary upgradable packages (apt list --upgradable).
This summary will be sumitted to the server by publishing to an MQTT topic. 

The following information will be published:  
- hostname
- IPv4 address
- total number of upgradable packages
- restart hint

Example messages:
```Client_1 (192.168.47.11) - no updates available.

Client_1 (192.168.47.11) - 57 updated packages awaiting installation.

Client_1 (192.168.47.11) - 57 updated packages awaiting installation. Restart may be required!
```


### Server mode
apt-mqtt-status will run as a permanently (e.g. as a systemd service) and subscripe to an MQTT topic.
Those messages from (multiple) clients will be forwarded to an Telegram account.



## Compatability
Developed and tested on Debian 11 ("Bullseye").  



## Todo-List 

- [x] Setup Wizzard
- [x] Identfy critical updates which require a reboot


