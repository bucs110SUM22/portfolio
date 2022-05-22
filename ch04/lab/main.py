import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help








##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(myturtle=dart)

    #Part B
    setupWindow(mywindow=wn)
    setupAxis(myturtle=dart)
    dart.speed(0)
    drawSineCurve(myturtle=dart)
    drawCosineCurve(myturtle=dart)
    drawTangentCurve(myturtle=dart)
    wn.exitonclick()
main()
