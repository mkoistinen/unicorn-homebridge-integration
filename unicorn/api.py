# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
try:
    import unicornhat as uh
except ImportError:
    # This object will be mocked for non-Raspberry Pi testing anyway...
    from fake_unicorn_hat import unicornhat as uh

from color import Color
from effects.candle_light import CandleLight
from effects.ocean_boat_blue import OceanBoatBlue
from effects.rainbow import Rainbow
from unicorn import Unicorn


app = Flask('unicorn')
logger = app.logger
medium_cyan = Color(hex="007F7F")  # Siri color: "Aqua"

# Initialize the lamp to medium-brightness "Aqua" (Siri's name for this color)
unicorn = Unicorn(uh, medium_cyan, effect_modes={
    'FF9429': CandleLight,  # Siri color: "Candle Light"
    '00A2FF': OceanBoatBlue,  # Siri color: "Ocean Boat Blue"
    'FF2977': Rainbow,  # Siri color: "Razzmatazz"
})

OK = "OK"


@app.route('/unicorn/api/v1.0/status', methods=['GET', ])
def get_status():
    """
    Returns the status (on/off) of the lamp as 1 or 0.
    :return:
    """
    return "1" if unicorn.status else "0"


@app.route('/unicorn/api/v1.0/status/<string:status>', methods=['GET', ])
def set_status(status):
    """
    Sets the status of the lamp on or off.
    """
    status = status.lower()
    if status not in ('on', 'off'):
        status = 'off'

    if status == 'on':
        unicorn.set_status(True)
    elif status == 'off':
        unicorn.set_status(False)
    return "OK"


@app.route('/unicorn/api/v1.0/set', methods=['GET', ])
def get_color():
    """
    Returns the current color.
    """
    return unicorn.color.as_hex()


@app.route('/unicorn/api/v1.0/set/<string:hex_color>', methods=['GET', ])
def set_color(hex_color):
    """
    Updates the color, turning on the lamp, if necessary.
    """
    if hex_color.startswith("#"):
        hex_color = hex_color[1:]
    unicorn.set_color(Color(hex=hex_color))
    return OK


@app.route('/unicorn/api/v1.0/brightness', methods=['GET', ])
def get_brightness():
    """
    Returns the current brightness as a stringified integer between 0 and 100.
    """
    return str(unicorn.color.brightness)


@app.route('/unicorn/api/v1.0/on', methods=['GET', ])
def set_on():
    """
    Turns ON the lamp using whatever color was stored last.
    """
    unicorn.set_status(True)
    return OK


@app.route('/unicorn/api/v1.0/off', methods=['GET', ])
def set_off():
    """
    Turns OFF the lamp.
    """
    unicorn.set_status(False)
    return OK


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
