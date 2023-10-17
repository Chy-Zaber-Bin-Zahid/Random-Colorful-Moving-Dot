from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random
import time

W_Width, W_Height = 500,500


ballx = bally = 0
speed = .1
ball_size = 5
create_new = False
dotList = []
blink = False
spacebar = "unpressed"


class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0


def crossProduct(a, b):
    result=point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x

    return result

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, s):
    print(x,y,s)
    glPointSize(s) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

# def drawAxes():
#     glLineWidth(1)
#     glBegin(GL_LINES)
#     # glColor3f(1.0, 0.0, 0.0)
#     glVertex2f(250,0)
#     glVertex2f(-250,0)
#     # glColor3f(0.0, 0.0, 1.0)
#     glVertex2f(0,250)
#     glVertex2f(0,-250)
#     glEnd()

    # glPointSize(5)
    # glBegin(GL_POINTS)
    # glColor3f(0, 1.0, 0.0)
    # glVertex2f(0,0)
 
    # glEnd()





def keyboardListener(key, x, y):
    global spacebar
    if key==b' ':
      if spacebar == "pressed":
          spacebar = "unpressed"
          print("Start")
      else:
          spacebar = "pressed"
          print("Stop")



    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed,spacebar
    if spacebar == "unpressed":
      if key==GLUT_KEY_UP:
          speed += 0.01
          print(speed)
          print("Speed Increased")
      if key== GLUT_KEY_DOWN:		#// up arrow key
          if speed > 0:
              speed -= 0.01
              print(speed)
              print("Speed Decreased")
      glutPostRedisplay()

      


def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global ballx, bally, create_new, blink,spacebar
    if spacebar == "unpressed":
      if button==GLUT_LEFT_BUTTON:
          if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
              blink = True
              
          
      if button==GLUT_RIGHT_BUTTON:
          if state == GLUT_DOWN: 	
              create_new = convert_coordinate(x,y)
              additional_value = 0
              new_tuple = create_new + (additional_value,)
              dotList.append(new_tuple)
      
         
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    # drawAxes()
    # global ballx, bally, ball_size
    # draw_points(ballx, bally, ball_size)

    # glBegin(GL_LINES)
    # glVertex2d(180,0)
    # glVertex2d(180,180)
    # glVertex2d(180,180)
    # glVertex2d(0,180)
    # glEnd()

    if dotList != []:
        global blink
        for i in range(len(dotList)):
            if len(dotList[i]) == 3:
              m,n,c = dotList[i]
            else:
              m,n,c,rgb = dotList[i]
            glPointSize(ball_size)
            glBegin(GL_POINTS)
            if c == 0:
                r = random.uniform(0, 1)
                g = random.uniform(0, 1)
                b = random.uniform(0, 1)
                glColor3f(r, g, b)
                dotList[i] = (dotList[i][0], dotList[i][1], 1, (r, g, b))
                
            else:
                glColor3f(rgb[0],rgb[1],rgb[2])
            glVertex2f(m,n)
            glEnd()
              


    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global speed,dotList,spacebar,blink
    if spacebar == "unpressed":
        for i in range(len(dotList)):
          if blink == False:
              x,y,c,rgb = dotList[i]
              dx = random.uniform(-1, 1) * speed
              dy = random.uniform(-1, 1) * speed
              x += dx
              y += dy

              # Ensure the dots stay within the range of -250 to 250
              x = max(-250, min(x, 250))
              y = max(-250, min(y, 250))

              dotList[i] = (x, y, c, rgb)
          else:
              # Set the entire screen to black
              glClearColor(0.0, 0.0, 0.0, 1.0)
              glClear(GL_COLOR_BUFFER_BIT)
              glutSwapBuffers()
              spacebar == "pressed"
              time.sleep(1)

              spacebar == "unpressed"
              blink = False



def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Building the Amazing Box")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
