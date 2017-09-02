def comoestas(condicion1):
	print("hola como etay")
	if condicion1 =="estoy contenta" :
		print("sigue programando")
	elif condicion1== "estoy triste" :
		print ("no estes triste vamos a comer")
	elif condicion1 =="estoy con mucha hambre" :
		print ("no interesa SIGUE PROGRAMANDO")
	elif condicion1 =="rodeada de muggles" :
		print ("ve a hogwards .... y dale un calcetin a dobby !!") 		 
	else:
		print("ve a la casa")
condiciones=["estoy contenta","estoy triste","estoy con mucha hambre","rodeada de muggles"]
for i in range(0,4):
	print(condiciones[i])
	comoestas(condiciones[i])
	print(i)			