# HACKMTY-2021
## Health-Path
Nuestra inspiración fue el hecho de que cuando uno sale, es imposible no tener contacto con otras personas. Lo que representa un riesgo de contagio de Covid-19. Es sumamente complicado saber en dónde hay más gente y con que ruta se podría evitar a todas estas personas, por lo que pensamos que sería genial si un programa lo hiciera por nosotros.

Es un programa que te permite navegar por zonas, buscando dentro de lo posible estar en la menor presencia de personas durante tu camino. Haciendo la ruta que te llevaría a tu destino, evitando grandes conglomerados de personas.

Usamos una variación del algoritmo de A* , agregando además de la distancia, un valor total de las probabilidades de que se pueda llegar a haber un contagio, tomando una de las rutas que menos contagios puede tener. Además se utlizó pygame y matplotlib para la representación gráfica:

![Image Text](https://github.com/axelqc/HACKMTY-2021/blob/main/gallery.jpg)
Donde el color verde representa una zona segura (con poca gente), la zona naranja poco segura (una cantidad considerable de gente), la zona roja representa peligro (mucha gente) y los puntitos blancos representan el camino más corto evitando los conglomerados.

Estamos orgullosos de haber conseguido estos resultados en tan poco tiempo (24 horas), debido a que no fue fácil lograrlo.

Aprendimos a usar algoritmos de búsqueda de manera más fácil y efectiva, mientras que a la vez descubrimos a hacer aplicaciones más graficas a nuestros programas. En especial adaptarnos para nuevos programas y opciones en Python.
