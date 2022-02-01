'''

Archivo de tareas del proyecto A-Tracker

Es necesario invoke: 'pip install invoke'

Modo de uso: 'inv <tarea>'

'''

from invoke import task,run

@task
def check(c):
    '''
    
    Task encargada de comprobar la correcta sintaxis del código
   
    Comprueba que el código es correcto, no errores lógicos o del estilo de dicho código.
    
    '''
    
    print("Comprobando sintaxis")
    run("python -m py_compile tracker/*.py")

    
@task
def test(c):
   '''
   Task encargada de realizar los tests 
   
   Encargado de correr pytest sobre el proyecto 
   '''
   print("Realizando tests")
   run("pytest")

@task
def dbuild(c):
	"""
	Task encargada de construir el contenedor a partir de el repositorio del proyecto
	"""
	run("docker build --tag xcyal/tracker .")
