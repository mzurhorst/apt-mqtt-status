#!/usr/bin/python3
#
#File           :  __init__.py
# Author        :  Marcus Zurhorst
#Email          :  marcuszurhorst@gmail.com
# License       :  MIT License
# Copyright     :  (c) 2022 Marcus Zurhorst
#
# Description   :  This module provides functions to gather the hostname, IPv4 address
#                  and upgradeable apt packages and publishs those to an MQTT broker.


# TOOD:   https://github.com/python-telegram-bot/python-telegram-bot


class HostInformation:
    # This class gethers all required information in Client mode

    import apt
    import socket

    def __init__(self, telegram_message):
        self.hostname = "hostname unknown"
        self.ip_string = "IPv4 unknown"
        self.apt_status = "apt status unknown"
        self.telegram_message = "message unknown"

    def hostname_ip():
        # This function gathers the hostname and IPv4 address of the client
        import os

        # TODO:  make interface name configurable
        hostname = os.popen('cat /etc/hostname').read().strip()
        ipv4 = os.popen(
            'ip addr show enp8s0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()

        return hostname, ipv4

    def apt_status():
        # This function updates the package repositories and reports the number of upgradable packages
        # Source:  https://apt-team.pages.debian.net/python-apt/library/apt.cache.html#the-cache-class

        from apt.cache import FilteredCache, Cache, MarkedChangesFilter

        cache = apt.Cache()
        cache.update()

        cache.open(None)
        changed = apt.FilteredCache(cache)
        changed.set_filter(MarkedChangesFilter())

        package_count = len(changed)

        # TODO:  Identify critical upgrades which require a reboot of the OS.
        cache.close()

        if package_count > 0:
            if package_count == 1:
                apt_status = "1 updated package awaiting installation."
            else:
                apt_status = str(package_count) + \
                    " updated packages awaiting installation."
        else:
            apt_status = "no updates available."

        return apt_status

    def compile_telegram_message():
        # This function comppiles the final telegram message

        hostname, ipv4 = self.hostname_ip()
        apt_status = self.apt_status()

        # Sample output for Telegram:    Client_1(192.168.47.11) - 57 updated packages awaiting installation.
        telegram_message = hostname + "(" + ipv4 + "):  " + apt_status

        print(telegram_message)

        return telegram_message

    pass
