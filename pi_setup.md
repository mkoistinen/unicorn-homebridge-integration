# Prepping new PiZero:

## Gain access to Zero
Via host computer, put Raspian image on SD card (balenaEtcher is a good recommendation)

After balenaEtcher has completed you may be notified that the drive needs to be formatted if using Windows. You must click on No if you get this pop up. Also if using Windows Eject the MicroSD card and reinsert it before continuing.

Via host computer, create a file `/wpa_supplicant.conf` that contains:

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="[your wifi station ID here]"
    psk="[your wifi password here]"
    key_mgmt=WPA-PSK
}
```

Via host computer, create another file `/ssh` that is empty.

Eject SD card, put into Pi, boot up!

Log into device (Find IP address in DHCP tables).

`ssh pi@[ipaddress]`

Immediately change the default password to something stronger.

`passwd`


## Setup SSH
mkdir .ssh

Via another terminal: `cp ~/.ssh/zero_pub pi@[IPADDRESS]:/.ssh/authorized_keys` (check that you can now log in via SSH)


## Update System
`sudo apt-get update`
`sudo apt-get upgrade`

The above will take like 20 minutes!

Now install fail2ban! (and htop, you'll love it)

`sudo apt-get update`
`sudo apt-get install htop fail2ban`
`cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

`sudo reboot`

Make sure you can log in via SSH and zero_pub key!

## Localize System Configuration

Configure system using: `sudo raspi-config`

1. Hostname "zero194"
2. Locale: "en-US" (use your own, of course)
3. Time Zones:
4. Keyboard:
5. Expand filesystem (reboot again)


## Install Node
Check to see which version is latest first!

`curl -o node-v11.9.0-linux-armv6.tar.gz https://nodejs.org/dist/v11.9.0/node-v11.9.0-linux-armv6l.tar.gz`

`sudo cp -r node-v11.9.0-linux-armv6l/* /usr/local/`

## Setup System Users
`sudo useradd --system homebridge`
`sudo useradd --system unicorn`
`sudo usermod -aG sudo unicorn`
`sudo mkdir /var/homebridge`
`sudo mkdir /var/unicorn`
`sudo chown homebridge:homebridge /var/homebridge`
`sudo chown unicorn:unicorn /var/unicorn`

## Install unicorn-homebridge-integration
`cd /var/unicorn`
`sudo su unicorn -c "git clone https://github.com/mkoistinen/unicorn-homebridge-integration.git unicorn"`

### Copy init scripts to system locations
Copy the daemons to the right place:

`sudo cp init.d/homebridge /etc/init.d/`
`sudo cp init.d/unicorn /etc/init.d/`

Register the daemons:

`sudo update-rc.d homebridge defaults`
`sudo update-rc.d unicorn defaults`

## Install Homebridge Node packate Requirements

Note, these are installed globally.

`sudo npm install -g --unsafe-perm homebridge`
`sudo npm install -g --unsafe-perm homebridge-better-http-rgb`

### Copy config.json
`sudo cp /var/unicorn/unicorn/homebridge/config.json /var/homebridge/`


## Install The Unicorn Service

### Create Virtual Env
`cd /var/unicorn`
`sudo -H pip install virtualenv`
`sudo su unicorn -c "virtualenv venv"`

### Install requirements
This installs the code as a module
`sudo su unicorn -c "source venv/bin/activate && pip install -e unicorn/."`
