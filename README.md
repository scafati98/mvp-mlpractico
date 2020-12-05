# mvp-mlpractico
MVP del curso Machine Learning Práctico de Pablo Zivic. El plan es construirlo de forma colaborativa.
Partimos del código que fue desarrollando y explicando en las clases
Tendremos por un lado los archivos limpios del curso
Por el otro los desarrollos de: 
  /arquitectura 
  /modelado
  /presentación


# Como empezar

Ejecutar en una consola

```
python setup.py develop
```

Luego desde cualquier jupyter notebook van a poder hacer esto

```
from mlp_mvp.transformers import CrewFeatures
```


# Cómo contribuir?

* Hacé un checkout del branch develop: `git checkout develop`
* Asegurate de estar al día: `git pull origin HEAD`
* Crea un branch nuevo con un nombre descriptivo. Si vas a hacer el modelo de rating podrías poner: `git checkout feature/rating_prediction`
* Hacé tu trabajo pusheando en ese branch: `git push origin HEAD`
* Crea un [pull request](https://github.com/pabloromero17143/mvp-mlpractico/pulls) de tu branch al branch `develop`
