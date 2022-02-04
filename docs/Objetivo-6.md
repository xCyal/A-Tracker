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
- No requerir información adicional (Tarjetas de crédito, por ejemplo) para verificar el usuario (Mención especial a GitLab CI)
- Posibilidad de uso de "Matrix" para lanzar los tests sobre varias versiones diferentes

