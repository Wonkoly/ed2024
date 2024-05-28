## Instalación
Nota: Es importante aclarar que este repositorio cuenta con dos proyectos juntos los dos elaborados con Flask asi que la instalacion sera similar.

Primero, has `cd` en el proyecto a desplegar y activa el entorno virtual en de Python. Es de aclarar que si te encuentras en Windows de preferencia usa Git Bash.

```bash
cd
source /env/bin/activate
```
Despues, instala las dependencias que se dentro del requirement.txt.

```bash
pip install -r requirements.txt
pip freeze //Para checar si se instalaron
```

Por ultimo exporta las variables de entorno `FLASK_APP` y `FLASK_DEBUG`. Y corre flask con `flask run`.

```bash
export FLASK_APP=main.py && export FLASK_DEBUG=1
flask run
```

Y si no te jala date un tiro. :)
