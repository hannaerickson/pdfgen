from reportlab.pdfgen import canvas # blank screen
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from student_scores.temp_marksheet import my_temp # import the template
import os

my_path = os.path.expanduser('~/Documents/my-marksheet.pdf') # where the file goes
c=canvas.Canvas(my_path, pagesize=letter)
c=my_temp(c) # running the template

# all this content could also be a part of the template. but the video didn't have it that way
c.setFillColorRGB(1, 0, 0)
c.setFont("Helvetica", 70)
c.drawRightString(6.4*inch, 7.5*inch, 'MARKSHEET') #location, x axis first, 6.4 units away from the left side, 7.5 up from the bottom. not 100% sure why it's in inches when it's not actually 6 inches from the left side
c.setFillColorRGB(0,0,0)
c.setFont("Helvetica", 24) # annoying, but you do have to redeclare font family every time you want to change the size. these are honestly similar to python functions in that they take in set arguments. you'll get an error if you forget one
c.drawRightString(2.5*inch, 6.8*inch, 'ID:') # the x coord on these are interesting. the content will END where the x coord is. that's why all of these entries have the same x coord, but they line up perfectly with their colon. so in other words the content is right justified in a way
c.drawRightString(2.5*inch, 6*inch, 'Name:')
c.drawRightString(2.5*inch, 5*inch, 'Class:')
c.drawRightString(2.5*inch, 4*inch, 'Gender:')
c.drawRightString(2.5*inch, 3*inch, 'Mark:')
c.drawRightString(3*inch, 2*inch, 'Grade:')
c.drawRightString(6*inch, -0.4*inch, 'Signature')

# connect to sample SQLite database and collect student details
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError # this is pretty necessary, per video, need to research
db_file='G:\\My drive\\testing\\my_db.db' # this is going to be different
try:
    file1 = 'sqlite:///' + db_file
    my_conn = create_engine(file1)
    # for MySQL use the below line and remove the above line that is used for SQLite files
    # my_conn = create_engine("mysql+mysqldb://root:pw@localhost/my_tutorial")
    # root will change to username, pw is password, everything else should be the same
    r_set=my_conn.execute("SELECT * FROM student WHERE id=15") # normal query, table name is student
    data = r_set.fetchone() # setting the data variable to the result of the above query
    print(data[1]) # will print the name of the student with id 15

except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(error)
## end of SQLite connection

c.setFillColorRBG(0,0,1)
c.setFont("Helvetica", 20)
c.drawString(3*inch, 6.8*inch, str(data[0])) # needs to be converted to a string since this is a number
c.drawString(3*inch, 6*inch, (data[1])) # name
c.drawString(3*inch, 5*inch, (data[2])) # class
c.drawString(3*inch, 4*inch, (data[4])) # gender
c.drawString(3*inch, 3*inch, str(data[3])) # mark, needs to also be changed to a string
if (data[3] >= 80):
    c.drawString(4*inch, 2*inch, 'A') # just examples of grades to display based on the mark
elif (data[3] >= 60):
    c.drawString(4*inch, 2*inch, 'B')
else:
    c.drawString(4*inch, 2*inch, 'C')

c.showPage()
c.save()
