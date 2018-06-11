from OpenGL.GL import *
from OpenGL.GLU import *
cameraposition=(0,0,-5)
class Material:
	def __init__(self,ks,kd,ka,a,color):
		self.ks=ks
		self.kd=kd
		self.ka=ka
		self.a=a
		self.color=color
iss=10
idd=10
iaa=10
def DotProduct(a,b):
	return (a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])
def CrossProduct(a,b):
	return ((a[1]*b[2])-(a[2]*b[1]),(a[2]*b[0])-(a[0]*b[2]),(a[0]*b[1])-(a[1]*b[0]))
def Normalize(vector):
	distance=(vector[0]**2)+(vector[1]**2)+(vector[2]**2)
	if distance==0:
		return (0,0,0)
	return (vector[0]/float(distance),vector[1]/float(distance),vector[2]/float(distance))
def Distance(vectorbeg,vectorend):
	vec=(vectorend[0]-vectorbeg[0],vectorend[1]-vectorbeg[1],vectorend[2]-vectorbeg[2])
	return vec
def PhongReflection(lm,N,V,mat):
	Rm=((N[0]*2*DotProduct(lm,N))-lm[0],(N[1]*2*DotProduct(lm,N))-lm[1],(N[2]*2*DotProduct(lm,N))-lm[2])
	return (mat.ka*iaa)+((mat.kd*DotProduct(lm,N)*idd)+(mat.ks*(DotProduct(Rm,V)**mat.a)*iss))
def ObjectQuads(verticies,surfaces,position,material,lightposition,scale=1):
	glBegin(GL_QUADS)
	q=-1
	for surface in surfaces:
		q+=1
		N=(0,0,0)
		lm=(0,0,0)
		V=(0,0,0)
		pr=0
		for vertex in range(len(surface)):
			ver=((verticies[surface[vertex]][0]+position[0])*scale,(verticies[surface[vertex]][1]+position[1])*scale,(verticies[surface[vertex]][2]+position[2])*scale)
			if vertex==0:
				ver2=(verticies[surface[vertex+1]][0]+position[0],verticies[surface[vertex+1]][1]+position[1],verticies[surface[vertex+1]][2]+position[2])
				N=CrossProduct(ver,ver2)
				N=Normalize(N)
			lm=Distance(ver,lightposition)
			lm=Normalize(lm)
			V=Distance(ver,cameraposition)
			V=Normalize(V)
			pr=PhongReflection(lm,N,V,material)
			glColor3fv((material.color[0]*(pr/255.0),material.color[1]*(pr/255.0),material.color[2]*(pr/255.0)))
			glVertex3fv(ver)
	glEnd()