# miniproyecyto1
Mini Proyecto Drag and Drop


Mapeo y Seguimiento de manos usando OpenCV y MediaPipe

Funcionamiento:

- Captura de Video: El programa utiliza la cámara web para capturar video en tiempo real.

- Detección de Manos: Se emplea MediaPipe para detectar la mano del usuario y sus puntos de referencia (como la punta del pulgar y el dedo índice).

- Gestos de Agarre:

*-Agarre: Cuando el usuario junta el dedo índice y el pulgar, el sistema detecta este gesto y permite que el objeto virtual se arrastre.

*-Soltar: Al separar los dedos, el objeto deja de moverse.

*-Movimiento del Objeto: El objeto virtual se mueve a la posición media entre la punta del pulgar y la punta del dedo índice, lo que permite un control más natural y preciso.

Requisitos para el funcionamiento del programa:

-Python 3.x
-OpenCV
-MediaPipe

Link a Video Explicativo: https://drive.google.com/drive/folders/1y1WDFNA051QKdihN9NcxhkVd3mrQEzFH?usp=sharing
