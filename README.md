Buscador Semántico de Corpus Académico en Español (SUAyED-UNAM)

Autor: Omar Velázquez López
Proyecto de investigación: Modelos de lenguaje masivos de código abierto para la búsqueda y el fortalecimiento del aprendizaje en el SUAyED
Institución: Universidad Nacional Autónoma de México (UNAM)
Aplicación disponible en: https://suayed-buscador-semantico.streamlit.app/
Versión: 1.0
Licencia: MIT

Descripción general

Este proyecto desarrolla un buscador semántico basado en modelos masivos de lenguaje de código abierto (LLMs), diseñado para explorar artículos académicos en español.
A diferencia de los buscadores tradicionales que dependen de la coincidencia exacta de palabras clave, este sistema utiliza embeddings semánticos para medir la similitud conceptual entre textos, permitiendo recuperar información por significado y no solo por palabra.

El proyecto se enmarca dentro de una línea de investigación orientada a la Inteligencia Artificial Explicable (XAI) y la Inteligencia Artificial Centrada en el Ser Humano (HCAI), promovida por instituciones como Stanford HAI y la UNESCO.

Arquitectura del sistema

El sistema se compone de cuatro fases principales:

Construcción del corpus académico

Extracción de metadatos y resúmenes desde el Repositorio Institucional de la UNAM vía OAI-PMH.

Debido a restricciones de acceso, la versión actual utiliza el corpus abierto de SciELO México (1,000 artículos en español).

Análisis exploratorio

Limpieza y validación lingüística del corpus.

Análisis de frecuencia, distribución temática y coocurrencia de términos.

Generación de embeddings semánticos

Modelos empleados:

hkunlp/instructor-large → enfoque conceptual (instrucción textual).

distiluse-base-multilingual-cased-v2 → enfoque rápido y multilingüe.

Embeddings almacenados en archivos .npy reutilizables:

emb_instructor_1000.npy

emb_distiluse_1000.npy

Despliegue del prototipo interactivo (Streamlit)

Aplicación: app_suayed_unam.py

Permite elegir modo de búsqueda, ingresar consultas, y visualizar resultados explicados mediante gráficas Altair/SHAP simuladas.
