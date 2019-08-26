# Unicorn Homebridge Integration

This is a collection of Python code that I run on some Raspberry Pi Zero's to
convert 3D printed things into functional lamps that integrate perfection with
Apple's Siri and the iOS Home app.

You can see a video of this code in action here: https://youtu.be/6jC8ryEkgvQ.

> Notice: I wrote this code to make 3D printed lamps, but it probably has other
> uses. If you're interested in the 3D printed projects you can find my *"8-bit"
> Diamond Ore Lamp* project here: https://www.prusaprinters.org/prints/5175-8-bit-minecraft-diamond-ore-lamp-siri-enabled
> or here: https://www.thingiverse.com/thing:3817997.


I started here: https://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri
but this repo includes significant improvements over the code suggested there.

To use this, you'll want to do the following on your Zero:

### Install Hardware:

* This awesome Unicorn pHAT from Pimoroni: https://shop.pimoroni.com/products/unicorn-phat

### Install Software:

1) Homebridge: https://github.com/nfarina/homebridge
    * This will involve installing Node.js and a few JS libraries on your Zero

2) Setup system users: `homebridge` and `unicorn`
    * Add both users to sudoers
    * Create their directories `/var/homebridge` and `/var/unicorn` respectively

3) Create a virtual environment for unicorn package and activate it
    * CD to /var/unicorn
    * `virtualenv venv`
    * `source venv/bin/activate`

4) Install this software (editably so that you can pull down updates)
    * `git clone https://github.com/mkoistinen/unicorn-homebridge-integration.git homebridge`
    * `cd homebridge`
    * `pip install -e .`  (Note the dot at the end and yes, use the -e option)
    * Note that this includes Pimoroni's unicorn-hat Python libraries: https://github.com/pimoroni/unicorn-hat

5) Also:
    * Copy the contents of `config.json` file from the `homebridge` directory into `/var/homebridge`
    * Install system daemons for homebridge and unicorn (this software)
        * Copy the files `homebridge` and `unicorn` from the `init.d` directory to `/etc/init.d`
        * `sudo systemctl daemon-reload`


## License

This software is available under the MIT License.
