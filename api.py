from flask import Flask, jsonify, request
from flask_limiter import Limiter, util
from flask_cors import CORS
import random
from colorsys import hsv_to_rgb

app = Flask(__name__)
CORS(app)

limiter = Limiter(util.get_remote_address, app=app, default_limits=["1 per second"]
)
try:
    with open("/home/kovaqa/counter_base.txt", "r") as cb:
        counter = int(cb.read())
except:
    counter = 0

try:
    with open("/home/kovaqa/counter_qr.txt", "r") as cq:
        qr_counter = int(cq.read())
except:
    qr_counter = 0
print(f'{counter} || {qr_counter}')

@app.route('/api/get-counter', methods=['GET'])
@limiter.exempt
def get_counter():
    return str(counter)

@app.route('/api/increment-counter', methods=['POST'])
@limiter.limit("1/second")
def increment_counter():
    global counter
    counter += 1
    if counter % 10 == 0:
        try:
            with open("/home/kovaqa/counter_base.txt", "w") as cb:
                cb.write(str(counter))
                print(f'Counter saved: {counter}')
        except:
            pass
    return str(counter)

@app.route('/api/reset-co', methods=['GET'])
def reset_counter():
    global counter
    counter = 0
    return str(counter)

#qr counter

@app.route('/api/get-qr-counter', methods=['GET'])
@limiter.exempt
def get_qr_counter():
    return str(qr_counter)

@app.route('/api/increment-qr-counter', methods=['POST'])
@limiter.exempt
def increment_qr_counter():
    global qr_counter
    qr_counter += 1
    return str(qr_counter)

@app.route('/api/reset-qr-co', methods=['GET'])
def reset_qr_counter():
    global qr_counter
    qr_counter = 0
    return str(qr_counter)

@app.route('/api/get-colour', methods=['GET'])
@limiter.exempt
def generate_water_color():
    #Randomly select a palette
    palette = random.choices(["dirty", "clear", "white"], weights=[47,47,6],k=1)[0]

    #Generate a color based on the selected palette's rules
    if palette == "dirty":
        hue = random.uniform(15, 45)  # Hue range for dirty palette
        # Saturation varies depending on hue
        if hue < 30:
            saturation = random.uniform(0.75, 1.0)  # Closer to 15, more saturated
        else:
            saturation = random.uniform(0.6, 0.75)  # Closer to 45, less saturated
        brightness = random.uniform(0.45, 0.6)  # Darker brightness
    elif palette == 'clear':  # "clear"
        hue = random.uniform(20, 40)  # Hue range for clear palette
        saturation = random.uniform(0, 0.45)  # Less saturated for clear colors
        brightness = 1.0  # Brightness is always full for clear palette
    elif palette == 'white':
        hue = 0
        saturation = 0
        brightness = 1.0

    #Convert HSV to RGB
    r, g, b = hsv_to_rgb(hue / 360.0, saturation, brightness)  # Convert hue to 0-1 scale
    r, g, b = int(r * 255), int(g * 255), int(b * 255)

    colour = f"#{r:02x}{g:02x}{b:02x}"
    return colour

if __name__ == '__main__':
    app.run()