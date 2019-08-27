NOTE: If you plan to install more than one of homebridge device on your network
you will need to ensure that each has a unique "username", "pin", and "name" as
defined in the "bridge" section of the `config.json` file. Also, define a unique
"name" in the "accessories" section too.

It is suggested that to determine a unique "username" is to use your devices
MAC address in all uppercase hexidecimal. You can find this easily with:

```
> ifconfig
```

Which will return something like this:

```
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        .
        .
        ether b8:27:eb:73:62:3e  txqueuelen 1000  (Ethernet)
        .
        .
```

The value you want is the sextant of hexidecimals that follows "ether" here.

Convert this to uppercase:

"b8:27:eb:73:62:3e" > "B8:27:EB:73:62:3E"

And use that. =)
