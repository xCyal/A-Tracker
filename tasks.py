from invoke import task,run

@task
def check(c):
   '''
   Task encargada de comprobar la sintaxis de la aplicación
   '''
   print("Comprobacion de sintaxis")
   run("pylint -E tracker")

@task
def test(c):
   '''
   Task encargada de realizar los tests 
   '''
   print("Realizando tests")
   run("pytest")
