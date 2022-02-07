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
- No requerir información adicional (Tarjetas de crédito, por ejemplo) para verificar el usuario (Mención especial a la mayoría de plataformas)

## Elección de la plataforma CI

Voy a listar las diferentes opciones que he tenido en cuenta para el proyecto, aunque soy consciente de la existencia de otras multiples opciones, estas son las que más me han llamado la atención o me han parecido mejores.

### GitHub Actions

Se trata de la opción más lógica, pues es la propia de la plataforma donde estoy desarrollando el proyecto. Su dificultad de integración es nula, pues su desarrollo es de los propios creadores de GitHub, así como su configuración se hace mediante un .yaml en .workflows, sin mucha complejidad. Es completamente gratuito en principio solo para repositorios públicos. Permite el uso de Matrix, posibilitando facilmente lanzar el trabajo en las diferentes versiones de python. Además no requiere de ningún tipo de información adicional más alla de la que se da en la propia cuenta.

Es uno de los seleccionados para este proyecto, ya que me parece una opción realmente buena.

### [GitLab CI](https://docs.gitlab.com/ee/ci/)

Una buena opción a priori, fácil de integrar con GitHub mediante un "personal token" generado en GitHub que da acceso a GitLab CI sobre nuestro repositorio. La configuración bastante sencilla, similar en muchos aspectos a GitHub Actions. Lo he descartado completamente, cuando realizando los tests, con la configuración bien hecha, daba un error de "usuario no verificado". Tras investigar algo más sobre este error, resulta que requiere la confirmación de la identidad por una Tarjeta de crédito para su uso, por lo que lo he descartado y he añadido este como un criterio para la elección de las plataformas (inesperadamente, no es equivalente a un pago pero prefiero no hacerlo).

### [Circle CI](https://circleci.com/)

De las mejores opciones para lo que busco. Se trata de una plataforma fácil de integrar, con una simple "deploy key", configurable con un .yaml de sintaxis nada complicada. Tiene un tier gratis que permite además lanzar test en paralelo, durante 6000 minutos mensuales. No necesita ninguna información adicional para su uso. Se le menciona únicamente por ser una de las plataformas testeadas, y probablemente de elección segura, de no ser por que la mayoría de los compañeros ya la han utilizado.

## [Travis CI](https://www.travis-ci.com/)

Buena integración con Github, solo hay que logear en ambas y dar permisos en GitHub a TravisCI. Configuración similar al resto, bastante sencilla, con travis.yml. Es gratuito para proyectos open source, seleccionando el Trial mensual. Esta no he llegado a configurarla ya que cae en el mismo error que GitLab, pidiendo datos bancarios.

## [Appveyor](https://www.appveyor.com/)

Después de un buen tiempo buscando una plataforma que cumpla de nuevo todos los requisitos, he encontrado (no se menciona en muchos sitios) AppVeyor. Integración muy sencilla, dando permisos como una aplicacion externa en github sobre los repositorios que deseemos. Configuración similar al resto, con un .yml, con una [sintaxis](https://www.appveyor.com/docs/appveyor-yml/) fácil de entender. No permite lanzar trabajos en paralelo. Es completamente gratis, y (por fin) no requiere ningún dato bancario para su uso.


## Decisión final y conclusiones

Después de haber probado más de 10 plataformas diferentes, la mayoría han sido descartadas directamente al pasarlas por el filtro de "gratis" y "no requerir información bancaria". He plasmado aquí algunas por mencionarlas, pero hay muchas más que o bien tienen un tier gratuito muy limitado, o los requisitos para acceder a este tier no se adaptan a lo que buscaba.

Respecto a la forma de integrarse con GitHub, la gran mayoría utilizan o un una deploy key, o se añaden a GitHub como una aplicación externa, por lo que esto no varía demasiado.

La configuración suele ser similar, cambiando algo la sintaxis de cada plataforma, pero todas se manejan con un único archivo .yml, y realmente no hay diferencias tan grandes.

Teniendo en cuenta lo mencionado previamente, he optado por AppVeyor y GitHub Actions. GitHub Actions me parece la opción natural, siendo de la propia plataforma de GitHub, y completamente gratuita y rápida, no he tenido muchas dudas al seleccionarla. Respecto a la segunda opción, he tenido bastantes problemas para elegirla, hasta que finalmente, encontré una plataforma no muy conocida (al menos, no mencionada en muchos sitios como el resto), AppVeyor, que me parece una maravilla, en comparación con las otras. Como he dicho su integración y configuración no varian mucho del resto, pero **no requiere ningún tipo de información bancaria y es completamente gratis**. 

Quizás alguno de los problemas que podemos encontrar aquí sea el hecho de que no permite lanzar trabajos en paralelo, por lo que si decidimos lanzar aquí varios tests, tardará algo más. Por eso, he decidido que esta plataforma se encargue de lanzar el contenedor de Docker con la versión en la que se realizó el proyecto (3.8), dejando así la versión 3.9 y 3.10 a GitHub Actions, de esta forma no estaremos testeando dos veces una misma versión, como se pide en la lista de comprobación.

## Sobre la configuración de appveyor

Appveyor por defecto, cuando sincronizas la plataforma con GitHub, tiene configurados dos tests por defecto, uno para el PR y otro para cada branch, que tan solo se encargan de construir el respositorio para comprobar su funcionamiento. 

Voy a explicar brevemente como funciona appveyor dado que su uso no parece estar muy extendido.

Para cambiar el funcionamiento de esto necesitamos configurar [appveyor.yml](../appveyor.yml) de la siguiente forma:

Para evitar lanzar los tests dos veces, eliminamos el test por branch y dejamos solo el del PR:

```yml
skip_branch_with_pr : true 
```

Como he mencionado, por defecto va a construir el proyecto, en este caso vamos a desactivarlo para que no lo haga:

```yml
build: off
```

Luego se debe especificar los servicios que vamos a utilizar, en este caso docker:

```yml
services:
  - docker
````

Ahora, existe una directiva específica para indicar que ordenes queremos lanzar en el script de los tests:

```yml
test_script:
   - docker run -t -v $(pwd):/app/test xcyal/a-tracker
```
La forma de actuar, al no tener la imagen del contenedor en el servidor local, será la de descargar la imagen desde nuestro Docker Hub y lanzar los tests dentro, dando continuidad al objetivo 5. 
