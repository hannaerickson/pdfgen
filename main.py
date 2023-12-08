from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
import os

# you'll need to install reportlab to try this locally. besides that, the only issue you may run into is with the logo image that is referenced in this file. I will comment it out but you can import any image and use it if you want.

# when we want to use a template, where pretty much everything stays the same but we just edit some lines, follow below:
# from template import my_template
# c=my_template(c) # this runs the template
# then write lines as normal

my_path = os.path.expanduser('~/Documents/my-pdf.pdf')
c=canvas.Canvas(my_path, pagesize=letter)
c.translate(inch, inch) # setting the margin

c.setStrokeColor('green') # creating a line
c.setLineWidth(5) # adjusting the width of the line
c.line(0, 8*inch, 7*inch, 8*inch) # coordinates of line x1y1, x2y2
# c.setFillColorCMYK(.2, .2, 0, .39) # font color in CMYK
# c.setFillColorRGB(0, 0, 1) # font color in RGB

c.setFillColor('lightblue') # font color by name
c.setFont('Helvetica', 20)
c.drawString(200, 200, 'Hello world')

# c.rotate(10) # rotate effect, seems to only adjust what comes below
# c.drawImage('logo.jpg', -0.7*inch, 8.7*inch, 2*inch, 1*inch) # image, then x and y coordinates, then width and height

c.setLineWidth(10) # border of rectangle
c.setStrokeColor('yellow') # border of rectangle
c.setFillColor('lightgreen') # fill of rectangle
c.rect(1*inch, 2*inch, 3.5*inch, 5*inch, fill=1) # x1y1, x2y2, fill set to 1 just means it is filled. If fill=0 it will be empty even if it is set like above

c.rotate(45) # setting the rotation of the watermark below
c.setFillColorCMYK(0, 0, 0, 0.08)
c.setFont('Helvetica', 100) # setting font type and size
c.drawString(2*inch, 1*inch, 'SAMPLE') # "drawing" or writing the text, the dimensions is the location
c.rotate(-45) # 'restoring' the rotation from above so it's normal for anything else below

c.showPage()
c.save()
