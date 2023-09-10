# Generate LastBlackBox Logo
import numpy as np
import os

# Get user name
username = os.getlogin()

# Specify paths
repo_path = '/home/' + username + '/NoBlackBoxes/LastBlackBox'
boxes_path = repo_path + '/boxes'
logo_path = repo_path + '/course/designs/logo'
box_parameters_path = logo_path + "/box_parameters.csv"
svg_path = logo_path + "/output.svg"

# Params
with_text = True
if with_text:
    offset = -7.5
else:
    offset = 0.0

# Defaults
box_size = 13
box_stroke = 1
box_syle = "fill-opacity:1;stroke:#FFFFFF;stroke-width:{0};stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1".format(box_stroke)

# Draw box (add SVG text for a rectangle)
def draw_box(file, id, x, y, width, height, fill, style):
    line = "\t<rect class=\"box\" id=\"{0}\" transform=\"scale(1,1) translate(1, 1)\" x=\"{1:2f}\" y=\"{2:2f}\" height=\"{3}\" width=\"{4}\" style=\"fill:#{5};{6}\"/>\n".format(id, x, y, width, height, fill, style)
    file.write(line)
    return

# Headers
xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n"
svg_header = "<svg id=\"logo\" width=\"100mm\" height=\"100mm\" viewBox=\"0 0 100 100\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:svg=\"http://www.w3.org/2000/svg\">\n"

# Text
text_x = 10.5
text_y = 94.0 + offset
#text_fill = "000000"
text_fill = "ffffff"
text_style = "font-style:normal;font-weight:bold;font-size:9.5;line-height:1.25;font-family:'Liberation Mono';white-space:pre;display:inline;fill:#{0};fill-opacity:1;stroke:none".format(text_fill)
text_tag = "\t<text class= \"text\" id=\"nbb\" x=\"{0}\" y=\"{1}\" style=\"{2}\">The Last Black Box</text>\n".format(text_x, text_y, text_style)

# Load box positions
box_parameters = np.genfromtxt(box_parameters_path, delimiter=",", dtype=str)
num_boxes = box_parameters.shape[0]

# Open SVG ouput
svg_file = open(svg_path, "w")

# Write headers
ret = svg_file.write(xml_header)
ret = svg_file.write(svg_header)

for i in range(num_boxes):
    id = "box_{0}".format(i)
    x = float(box_parameters[i,2])
    y = float(box_parameters[i,3]) + offset
    fill = box_parameters[i,4]
    draw_box(svg_file, id, x, y, box_size, box_size, fill, box_syle)

# Add text?
if(with_text):
    ret = svg_file.write(text_tag)

# Close SVG output
ret = svg_file.write("</svg>")
svg_file.close()

#FIN