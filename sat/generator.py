import random
from colorsys import hsv_to_rgb

def generate_water_color():
    #Randomly select a palette
    palette = random.choices(["dirty", "clear", "white"], weights=[47,47,6],k=1)[0]
    print(palette)

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
    
    #Format as hex
    return f"#{r:02x}{g:02x}{b:02x}"

for _ in range(10):
    print(generate_water_color())
