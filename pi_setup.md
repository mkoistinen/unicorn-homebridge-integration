# Prepping new Pi Zero:

These instructions were written for Raspberry Pi OS Lite Kernel version 5.10 released March 4th, 2021

## Gain access to Zero
Via host computer, put Raspian image on SD card (balenaEtcher is a good recommendation)

After balenaEtcher has completed you may be notified that the drive needs to be formatted if using Windows. You must click on No if you get this pop up. Also if using Windows Eject the MicroSD card and reinsert it before continuing.

Via host computer, create a file `/wpa_supplicant.conf` that contains:

    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="[your wifi station ID here]"
        psk="[your wifi password here]"
        key_mgmt=WPA-PSK
    }

Via host computer, create another file `/ssh` that is empty.

Eject SD card, put into Pi, boot up!

Log into device using its default zero-conf name:

    ssh pi@raspberrypi.local

Immediately change the default password to something stronger.

    passwd

## Update hostname

    ifconfig -a

Examine the last 4 hex digits in the WLAN0's HW address, replace the following
'X's accordingly:

    sudo su -c 'echo unicornXXXX > /etc/hostname'

Also, change the hosts file to reflect this change by doing:

    sudo vi /etc/hosts

And edit the line that contains `rasberrypi` to contain your hostname (be sure
to change the `XXXX` accordingly):

    ...
    127.0.0.1        unicornXXXX
    ...



## Setup SSH

This section is optional, but will help you set up and use RSA key pairs to log
into the Pi Zero going forward. You can choose to not do this, and continue to
use your login credentials defined earlier.

    mkdir .ssh

From your host, copy your public key to the Pi Zero. In this example, my RSA 
key is called `zero`, so the public key portion is `zero.pub`, obviously, use 
your own key's filename here.

    scp ~/.ssh/zero.pub pi@[IPADDRESS]:.ssh/authorized_keys

Now, back on the Zero, set the permissions correctly:

    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/authorized_keys

Now, back on your host computer, in a new terminal, verify you can log in with
your RSA keys:

    ssh -i ~/.ssh/zero pi@[IPADDRESS]

At this point you have *added convenience*, and *reduced security* because you
now have 2 methods of logging in: one using a password, and one using an RSA
key. Consider now disabling the weaker method of password authentication. There
are numerous resources online for this. It's easy to do too!


## Update System

    sudo apt-get update
    sudo apt-get -y upgrade

Now install fail2ban, git, and pip.

    sudo apt-get update
    sudo apt-get install fail2ban git python-pip
    sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

    sudo reboot

Make sure you can log in via SSH and zero_pub key!

## Localize System Configuration

Configure system using:

    sudo raspi-config

1. Localisation Options -> Locale: "en-US" (use your own, of course)
2. Localization Options -> Time Zones: (choose your own, of course)
3. Localization Options -> Keyboard: (choose your own, of course)
4. Advanced Options -> Expand Filesystem (reboot again)


## Install Node
Check to see which version is latest for your system first! In my case, on my
Pi Zero, when I do:

    more /proc/cpuinfo

I see that this is an ARMv6-compatible processor, so, I need to find the latest
version of node that supports this. At the time of this writing (April, 2021),
this appears to be v11.15.0. So, these are the commands I need to run:

    curl -o node-v11.15.0-linux-armv6l.tar.gz https://nodejs.org/dist/v11.15.0/node-v11.15.0-linux-armv6l.tar.gz
    tar -xzf node-v11.15.0-linux-armv6l.tar.gz
    sudo cp -r node-v11.15.0-linux-armv6l/* /usr/local/

## Setup System Users

    sudo useradd --system homebridge
    sudo useradd --system unicorn
    sudo usermod -aG sudo unicorn
    sudo mkdir /var/homebridge
    sudo mkdir /var/unicorn
    sudo chown homebridge:homebridge /var/homebridge
    sudo chown unicorn:unicorn /var/unicorn
    sudo usermod -d /var/unicorn unicorn
    sudo usermod -d /var/homebridge homebridge

## Install unicorn-homebridge-integration

    cd /var/unicorn
    sudo su unicorn -c "git clone https://github.com/mkoistinen/unicorn-homebridge-integration.git unicorn"

### Copy init scripts to system locations
Copy the daemons to the right place:

    sudo su root -c "cp /var/unicorn/unicorn/init.d/homebridge /etc/init.d/"
    sudo su root -c "cp /var/unicorn/unicorn/init.d/unicorn /etc/init.d/"

Register the daemons:

    sudo update-rc.d homebridge defaults
    sudo update-rc.d unicorn defaults

## Install Homebridge Node package Requirements

Note, these are installed globally.

    sudo npm install -g --unsafe-perm homebridge
    sudo npm install -g --unsafe-perm homebridge-better-http-rgb

NOTE: At the time of this writing (April, 2021), the homebridge-better-http-rgb
package has been deprecated, but it still installs and works.


### Copy config.json

    sudo cp /var/unicorn/unicorn/homebridge/config.json /var/homebridge/


## Install The Unicorn Service

### Create Virtual Env

    cd /var/unicorn
    sudo -H pip install virtualenv
    sudo su unicorn -c "virtualenv venv"

### Install requirements

This installs the code as a module

    sudo su unicorn -c "source venv/bin/activate && pip install -e unicorn/."

Reboot, and you're done!


## Proceed only if HW button also installed (on GPIO23) (This feature is not yet complete nor supported)

Install Access Point packages
Create new service: unicorn-configuration-mode (from file in repo)
Add to rc2.d

    cd /home/pi
    git clone https://github.com/WiringPi/WiringPi.git

    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.ap.conf
    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.normal.conf

Update dhcpcd.ap.conf for AP mode
Modify /etc/init.d/hostapd

    cd /etc/cd2.d
    sudo rm S01hostapd
    sudo rm S01dhcpcd
    sudo ln -s ../init.d/unicorn-configuration-mode S01unicorn-configuration-mode


### Install dnsmasq hostapd

    sudo apt install dnsmasq hostapd
    sudo systemctl stop dnsmasq
    sudo systemctl stop hostapd

#### Make 2 DHCPCD Service configurations

Copy the dhcpcd.conf into 2 different files, and symlink the normal one

    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.ap.conf
    sudo vi /etc/dhcpcd.ap.conf
    sudo mv /etc/dhcpcd.conf /etc/dhcpcd.normal.conf
    sudo ln -s /etc/dhcpcd.normal.conf /etc/dhcpcd.conf

#### Configure DNSMASQ

    sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
    sudo vi /etc/dnsmasq.conf

#### Configure HOSTAPD

    sudo vi /etc/hostapd/hostapd.conf
    sudo vi /etc/default/hostapd

    sudo systemctl unmask hostapd
    sudo systemctl enable hostapd
    sudo systemctl start hostapd
