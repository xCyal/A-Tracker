from invoke import task,run

@task
def check(c):
   '''
   Task encargada de comprobar la sintaxis de la aplicación
   '''
   print("Comprobacion de sintaxis")
   run("pylint -E tracker")

