# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [
                [0,0,0],
                [0,0,self.parameters['height']],
                [self.parameters['width'],0,self.parameters['height']],
                [self.parameters['width'],0,0],
                [0,self.parameters['thickness'],0],
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],0]
                ]
        #Ici, on a défini chaques sommets 
        
        self.faces = [
                [0,3,2,1],
                [4,7,6,5],
                [0,4,5,1],
                [3,7,6,2],
                [0,4,7,3],
                [1,5,6,2]
                ]   
        #Ici, on a défini les 6 faces de notre rectangle

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        pass           
                    
    # Draws the faces
    def draw(self):
        
        for face in self.faces:
            gl.glPushMatrix()
            gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
            gl.glRotate(self.parameters['orientation'],0,0,1)
            #Crée un repère propre à mon mur 
        
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([0.5, 0.5, 0.5])
            gl.glVertex3fv(self.vertices[face[0]])
            gl.glVertex3fv(self.vertices[face[1]])
            gl.glVertex3fv(self.vertices[face[2]])
            gl.glVertex3fv(self.vertices[face[3]])
            gl.glEnd()
            gl.glPopMatrix()
