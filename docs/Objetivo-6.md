# Documentación sobre el Objetivo  6

## Versiones de python elegidas

Como podemos observar en la [documentación del objetivo 5](/docs/Objetivo-5.md), el motivo de elección de python 3.8 era por la etapa de desarrolo en la que se encuentra cada una de las versiones.

Un pequeño resumen de lo que se menciona allí, es que podemos observar 4 versiones con soporte a día de hoy que son 3.7, 3.8, 3.9 y 3.10. De estas, la 3.9 y 3.10 se encuentran en fase de bugfix.

Para realizar los tests primero opte por hacerlos sobre las versiones mencionadas, pero acabé por no lanzarlos sobre la 3.7. Como pude comprobar, los tests no se lanzaban correctamente en esta versión.


Después de investigar el error, pude observar que era problema de que la versión no era soportada por las versiones específicas de algunas herramientas utilizadas (en este caso pytest).

![Fail python 3.7](/docs/img/python37fail.png)

Por lo tanto, se va a lanzar los tests en 3.8, 3.9 y 3.10.


## Criterios de elección de plataforma CI

Vamos a establecer los criterios que se han utilizado para comparar las diferentes opciones existentes:

- Dificultad de integrar la plataforma con nuestro repositorio en GitHub
- Dificultad a la hora de configurarlo
- Que sea gratuito, o al menos tenga una versión gratuita durante un tiempo
- Posibilidad de uso de "Matrix" para lanzar los tests sobre varias versiones diferentes
- No requerir información adicional (Tarjetas de crédito, por ejemplo) para verificar el usuario (Mención especial a GitLab CI)

## Elección de la plataforma CI

Voy a listar las diferentes opciones que he tenido en cuenta para el proyecto, aunque soy consciente de la existencia de otras multiples opciones, estas son las que más me han llamado la atención o me han parecido mejores.

### GitHub Actions

Se trata de la opción más lógica, pues es la propia de la plataforma donde estoy desarrollando el proyecto. Su dificultad de integración es nula, pues su desarrollo es de los propios creadores de GitHub, así como su configuración se hace mediante un .yaml en .workflows, sin mucha complejidad. Es completamente gratuito en principio solo para repositorios públicos. Permite el uso de Matrix, posibilitando facilmente lanzar el trabajo en las diferentes versiones de python. Además no requiere de ningún tipo de información adicional más alla de la que se da en la propia cuenta.

Es uno de los seleccionados para este proyecto, ya que me parece una opción realmente buena.

### GitLab CI

Una buena opción a priori, fácil de integrar con GitHub mediante un "personal token" generado en GitHub que da acceso a GitLab CI sobre nuestro repositorio. La configuración bastante sencilla, similar en muchos aspectos a GitHub Actions. Lo he descartado completamente, cuando realizando los tests, con la configuración bien hecha, daba un error de "usuario no verificado". Tras investigar algo más sobre este error, resulta que requiere la confirmación de la identidad por una Tarjeta de crédito para su uso, por lo que lo he descartado y he añadido este como un criterio para la elección de las plataformas (inesperadamente, no es equivalente a un pago pero prefiero no hacerlo).

### Circle CI

De las mejores opciones para lo que busco. Se trata de una plataforma fácil de integrar, con una simple "deploy key", configurable con un .yaml de sintaxis nada complicada. Tiene un tier gratis que permite además lanzar test en paralelo, durante 6000 minutos mensuales. No necesita ninguna información adicional para su uso. Se le menciona únicamente por ser una de las plataformas testeadas, y probablemente de elección segura, de no ser por que la mayoría de los compañeros ya la han utilizado.
