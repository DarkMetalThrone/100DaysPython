import colorgram

colors = colorgram.extract("image.jpg", 30)

#print a list of tuples which have RGB values 
colors_rgb = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.b
    b = i.rgb.b
    colors_rgb.append((r, g, b))
    # colors_rgb.append(rgb)
print(colors_rgb)
