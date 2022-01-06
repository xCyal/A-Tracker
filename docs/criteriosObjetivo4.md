# Principios F.I.R.S.T de pruebas unitarias

 - Fast
 - Isolated/Independent
 - Repeatable
 - Self-validating
 - Thorough
 
Se ha intentado ceñir el proceso a la hora de realizar este objetivo a estos principios. 

El developer debe de encargarse de que estos tests sean rápidos, para poder utilizarlos en cualquier momento del proceso de desarrollo, los cuales no deben depender de ninguna variable de entorno, así como tener los datos necesarios para dicho test sin necesidad de proporcionarlos cada vez que se van a lanzar. A su vez, debe de ser un proceso automático que no requiera de comprobación manual de los resultados obtenidos.

Los tests deben de intentar enfocarse en probar todas las posibles entradas invalidas o posibles argumentos ilegales, así, como en caso de tener apliaciones mas complejas que la desarrollada en este proyecto, intentar testear que ocurriria con un input demasiado grande. En resumen, intentar predecir todos los escenarios posibles en los que una función o parte del código puede dar algún error, de esta forma detectando los posibles errores a la hora de implementar nuevo código.

# Test framework

Se ha seleccionado Pytest sobre su principal competidor en python Unittest. Ambas son buenas opciones, ampliamente utilizadas en la comunidad de python, pero he optado por el uso del primero, pytest, por su, en mi opinion, mayor simplicidad. En general Pytest y Unittest son muy similares, ambas permiten el uso de bibliotecas de aserciones como la utilizada en este proyecto (assertpy) y tienen las mismas funcionalidades, pero en mi opinión al utilizar ambas, la salida de Pytest es más de mi agrado y facil de comprender. He de mencionar que he tenido ciertos problemas a la hora de configurar los directorios con Pytest que no he tenido con Unittest, pero la documentación de Pytest ha resultado útil en este caso.

# Assertions library

Se ha utilizado assertpy como biblioteca de aserciones frente a otras opciones como Grappa.

En este caso, assertpy, tiene una sintaxis muy cómoda y me gustaría resaltar este aspecto respecto a otras bibliotecas, ya que parece utilizar casi el lenguaje natural. También tenemos una gran cantidad de assertions que Grappa no tiene, lo cual si el proyecto fuera de mayor tamaño podría ser un incoveniente dependiendo de que quisieramos testear.

En principio, la sintaxis de assertpy ha sido de gran utilidad y un motivo de peso para la elección.
