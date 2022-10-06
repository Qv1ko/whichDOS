# MANUAL

***Idioma***
- 🇪🇸 Español
- [🇺🇸 Inglés](./README.md)

__Para que el script funcione correctamente:__

  *Tienes dos opciones al ejecutar el script de python3.*

* Introduzca el script en una ruta absoluta de su sistema (puede ejecutar el script desde cualquier otra ruta).

  1. Introduzca el script de python3 en un directorio de su ruta absoluta.
  2. Dele permisos de ejecución al script (`chmod +x whichDOS.py`).
  3. Para ejecutar el script, tienes que escribir el nombre del script y la ip de destino (`whichDOS.py {target ip}`).

  Ejemplo: `whichDOS.py 10.10.10.21`

* Añadir el script a una ruta no absoluta en su sistema (debe ejecutar el script en la misma ruta donde se encuentra el script).

    1. Inserte el script de python3 en su directorio actual.
    2. Para ejecutar el script, debes escribir python3, el nombre del script y la ip objetivo (`python3 whichDOS.py {ip target}`).

  Ejemplo: `python3 whichDOS.py 10.10.10.21`
 
 __Conceptos:__
 
 * whichDOS: Which Default Operating System.
 * TTL: Time To Live. Es el tiempo que el sistema operativo indica a los servidores que almacenen un registro DNS en la memoria local antes de que sea descartado. Se puede modificar manualmente.

> Autor: s4vitar

> Modificador: Qv1ko
