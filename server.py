#!/bin/python3

from flask import Flask, jsonify, abort, request, make_response, url_for
import json

app = Flask(__name__)
app.config["DEBUG"] = True

sound_files = {
    0: "sound/dumm.wav",
    1: "sound/dumm.wav",
    2: "sound/dumm.wav",
    3: "sound/dumm.wav",
    4: "sound/dumm.wav",
    5: "sound/dumm.wav",
    6: "sound/dumm.wav",
    7: "sound/dumm.wav",
    8: "sound/dumm.wav",
    9: "sound/dumm.wav",
    10: "sound/dumm.wav",
    11: "sound/dumm.wav",
    12: "sound/dumm.wav",
    13: "sound/dumm.wav",
    14: "sound/dumm.wav",
}

@app.route('/buttons', methods=["GET"])
def get_buttons():
    global sound_files

    return json.dumps(sound_files)

@app.route('/buttons', methods=["POST"])
def set_buttons():
    global sound_files

    if not request.json:
        abort(400)
    sound_files = json.loads(request.json)

def main():
    global app

    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()