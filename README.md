# Proyecto de Análisis de Goles en Handball con IA

## Descripción
Este proyecto utiliza técnicas avanzadas de visión por computadora y aprendizaje profundo para automatizar la detección de goles en partidos de handball. Mediante la integración de YOLOv8 y DeepSORT, junto con FastAPI y Streamlit, este sistema identifica los momentos en que se anotan goles, mejorando la eficiencia del análisis de juego.

## Introducción
El handball es un deporte en rápido crecimiento que, hasta la fecha, no ha explotado completamente las posibilidades que la IA ofrece para el análisis del juego. Este proyecto busca cerrar esa brecha, proporcionando una herramienta que ahorra tiempo a analistas deportivos al identificar automáticamente los goles.

## Tecnologías Utilizadas
- **YOLOv8**: Para la detección en tiempo real de goles.
- **DeepSORT**: Para el seguimiento avanzado de jugadores y balón.
- **FastAPI**: Para crear una API robusta y eficiente.
- **Streamlit**: Para desarrollar una interfaz de usuario interactiva.

## Desarrollo
### Obtención de Datos
Se recopilaron y etiquetaron manualmente clips de partidos de handball para entrenar el modelo.

### Entrenamiento del Modelo
El modelo se entrenó con un conjunto inicial de 3000 imágenes, logrando una precisión del 60-70%.

### Integración y Pruebas
Se integró el modelo con FastAPI y Streamlit, permitiendo pruebas en un entorno de usuario final.

## Resultados
La herramienta demostró ser capaz de detectar goles con una precisión significativa, reduciendo considerablemente el tiempo de análisis manual.

## A Futuro
Se planea mejorar el modelo con más datos y explorar su despliegue en la nube para facilitar el acceso y la escalabilidad.

## Conclusiones
Este proyecto ilustra el potencial de la IA en el análisis deportivo, abriendo puertas a nuevas investigaciones y aplicaciones en el handball y otros deportes.

## Cómo Contribuir
¡Tus contribuciones son bienvenidas! Consulta la sección de [Issues](#issues) para ver cómo puedes ayudar.

## Licencia
Este proyecto está bajo la licencia [MIT](LICENSE).

## Contacto
Para más información, puedes contactarme a través de [mi perfil de GitHub](https://github.com/tu_usuario).
