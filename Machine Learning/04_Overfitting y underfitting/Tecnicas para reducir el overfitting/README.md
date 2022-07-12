# ¿Cómo combatir el overfitting en un modelo de Deep Learning?

Código fuente de [este](https://youtu.be/QyVr3UiTYXg) video, en donde se muestran tres técnicas para reducir el overfitting. La primera de ellas consiste en simplificar el modelo (reduciendo el número de capas y el número de neuronas por capa); la segunda es el *Dropout* y la tercera es el *early stopping*.

Con estas tres técnicas se logra reducir el overfitting, pasando de un modelo con precisiones del 100% y 70% en los sets de entrenamiento y validación, a casi el 75% en ambos casos.

## Dependencias
Keras==2.2.4
numpy==1.16.3