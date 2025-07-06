#MADE BY SAMARTH KHANDELWAL 23BCE10647
import turtle   

#CREATING A TURTLE SCREEN OBJECT
screen=turtle.Screen()                                                                                            
screen.title('INDIAN STATES GAME')
image=r"C:\Users\Samarth Khandelwal\OneDrive\Documents\CODE\PYTHON\PYTHON CLASS B11+12+13\23BCE10647_FINAL_PYTHON_PROJECT\ezgif-1-3cb9c824d0finla resized.gif"
# ADDING SHAPE TO THE SCREEN/, ONLY GIF FORMAT IS SUPPORTED
screen.addshape(image)
turtle.shape(image)

# USED THIS PART OF CODE TO GET COORDINATES OF INDIAN STATES
# def get_mouse_coor(x,y):  
#     print(x,y)
# turtle.onscreenclick(get_mouse_coor)

#importing pandas library as this library is used for data manupilation and analysis, Here we are importing it for reading csv files.
import pandas
states_data=pandas.read_csv(r"C:\Users\Samarth Khandelwal\OneDrive\Documents\CODE\PYTHON\PYTHON CLASS B11+12+13\23BCE10647_FINAL_PYTHON_PROJECT\NEW UPDATED COORDINATES OF INDIAN STATES.csv")
stateslist=states_data.STATES.to_list()
print(stateslist)

#creating a blank list to keep track of guessed states
guessed_states=[]
name=(screen.textinput(title=f"Welcome User", prompt="Enter your name"))
screen.title(f"{name}! Let's guess states")

#creating a new turtle to write side comment
side_comment=turtle.Turtle()
side_comment.hideturtle()
side_comment.penup()
side_comment.goto(-7,-295)
side_comment.color('blue')
side_comment.write("Type 'STOP' to get complete answer")

#starting a loop until all the states are guessed or stop command is given
while len(guessed_states)<37:
    answer=(screen.textinput(title=f"{len(guessed_states)}/36 Correct", prompt="Enter the name of state"))
    try:
        answer=(answer+' ').title()
    except:
        pass
    if answer in stateslist:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates=states_data[states_data.STATES==answer]
        t.color('green')
        print(coordinates)
        t.goto(int(coordinates.x),int(coordinates.y))
        t.write(answer)
        guessed_states.append(answer)
        
    if answer=="Stop ":
        break

#creating a list using list comprehension to mark unguessed states with red color.
unguessedlist= [ i for i in stateslist if i not in guessed_states ]
for i in unguessedlist:
    coordinates=states_data[states_data.STATES==i]
    t.goto(int(coordinates.x),int(coordinates.y))
    t.color('red')
    t.write(i)
print(unguessedlist)  
turtle.mainloop()