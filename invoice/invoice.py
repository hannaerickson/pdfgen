from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp # import the template
from invoice_data import *  # get all data required for invoice
import os
my_path = os.path.expanduser('~/Documents/invoice.pdf')

#my_prod={1:['Hard Disk',80,1],2:['RAM',90,2],3:['Monitor',75,2]}
c = canvas.Canvas(my_path,pagesize=letter)
c=my_temp(c) # run the template

c.setFillColorRGB(0,0,1) # font colour
c.setFont("Helvetica", 20)
row_gap=0.6 # gap between each row
line_y=7.9 # location of fist Y position
total=0

for items in my_sale:
    c.drawString(0.1*inch,line_y*inch,my_prod[items][0]) # p Name
    # first is x coord, then y coord. the y coord is set to line_y as above, because we want all of our lines to stay in line at the same starting position.
    c.drawRightString(4.5*inch,line_y*inch,str(my_prod[items][1])) # p Price
    # once again, x coord, y coord, then the thing we are displaying. the price is listed further to the right, so the x coord is increasing. y coord is the same. the y coords for each item will be the same, since they're on the same "line". the str function is needed to display a number.
    # honestly not sure the difference rn between drawString and drawRightString. has to do with alignment. in the video, when it was just drawString, the numbers were right aligned. changing it to drawRightString is what put them more in the middle.
    c.drawRightString(5.5*inch,line_y*inch,str(my_sale[items])) # p Quant
    sub_total=my_prod[items][1]*my_sale[items] # finding the subtotal by accessing the item price, then multiplying it by the quantity.
    c.drawRightString(7*inch,line_y*inch,str(sub_total)) # Sub Total
    total=round(total+sub_total,1) # total from above, it was set to 0 initially. the round() is to show the decimal places. finally, the 1 notes we want one decimal place to show.
    line_y=line_y-row_gap # this increments the y, or the up and down coordinate. reassigning the line_y variable, with each loop iteration, by subtracting the row gap, which is the space between each row. by decreasing the y value, we are moving down the page.

# we are outside of the product loop now.
c.drawRightString(7*inch,2.1*inch,str(float(total))) # Total
discount=round((discount_rate/100) * total,2)
c.drawRightString(4*inch,1.8*inch,str(discount_rate)+'%') # showing discount rate
c.drawRightString(7*inch,1.8*inch,'-'+str(discount)) # showing the dollar amount that is discounted

tax=round((tax_rate/100) * (total-discount),2)
c.drawRightString(4*inch,1.2*inch,str(tax_rate)+'%') # tax
c.drawRightString(7*inch,1.2*inch,str(tax)) # tax

total_final=total-discount+tax
c.setFont("Times-Bold", 22)
c.setFillColorRGB(1,0,0) # font colour
c.drawRightString(7*inch,0.8*inch,str(total_final)) # final total, accounting for tax and discount

c.showPage()
c.save()
