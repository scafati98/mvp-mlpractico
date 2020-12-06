# Frontend y Back de la App

Aqui se agregaran caracteristicas del front y back de la app.


## Instalacion del ambiente

Primero crear un ambiente virtual de python

Ejemplo con conda : conda create -n "frontend"

Estando dentro del ambiente virtual instalamos las dependencias

```bash
pip install -r requirements.txt
```
## Como lanzar la app

Primero lanzar el servidor de flask utilizando :
```bash
python app.py
```
Y luego lanzar el dashboard de dash/plotly

```bash
python dash_app.py
```
Luego podran entrar a la direccion donde esta el servidor de flask y podran ver el front junto con el dashboard