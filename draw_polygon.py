from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawVerticalLine(min_y, max_y, x_offset, color):
    glBegin(GL_POINTS)
    for y in range(min_y, max_y + 1):
        glColor3fv(color)
        glVertex2f(x_offset, y)
    glEnd()

def drawHorizontalLine(min_x, max_x, y_offset, color):
    glBegin(GL_POINTS)
    for x in range(min_x, max_x + 1):
        glColor3fv(color)
        glVertex2f(x, y_offset)
    glEnd()

def drawLineSegment(x1, y1 , x2, y2, color):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    if(max_x == min_x):
        drawVerticalLine(min_y, max_y, min_x, color)
        return
    
    if max_y == min_y:
        drawHorizontalLine(min_x, max_x, min_y, color)
        return

    #slope ==> m
    m = (y2 - y1) / (x2 - x1)
    c = y1 - (m * x1)

    glBegin(GL_POINTS)
    glColor3fv(color)

    if m <= 1:
        for x in range(min_x, max_x + 1):
            y = int((m * x + c) + 0.5)
            glVertex2f(x, y)
    else:
        for y in range(min_y, max_y+1):
            x = int( ((y - c) / m ) + 0.5)
            glVertex2f(x, y)
    glEnd()
    return

def drawPolyline(n, x_points, y_points, color):
    for i in range(0, n-1):
        drawLineSegment(x_points[i],y_points[i], x_points[i+1], y_points[i+1], color)

def drawPolygon(n, x_points, y_points, color):
    drawPolyline(n, x_points, y_points, color)
    drawLineSegment(x_points[n-1], y_points[n-1], x_points[0], y_points[0], color)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

def myDisplay():
    gluOrtho2D(0, 600, 0, 600)
    glPointSize(2.0)
    color = [0.0, 0.0, 0.0]
    x = [300,350,400]
    y = [300,350,300] 
    drawPolygon(3, x, y, color)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("my window")
    init()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

main()
