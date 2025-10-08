# 🧠 Buscador Semántico de Corpus Académico en Español (SUAyED-UNAM)

**Autor:** Omar Velázquez López  
**Proyecto de investigación:** *Modelos de lenguaje masivos de código abierto para la búsqueda y el fortalecimiento del aprendizaje en el SUAyED*  
**Institución:** Universidad Nacional Autónoma de México (UNAM)
**App disponible en:** https://suayed-buscador-semantico.streamlit.app/
**Versión:** 1.0  
**Licencia:** MIT  

---

## 📘 Descripción general

Este proyecto desarrolla un **buscador semántico** basado en **modelos masivos de lenguaje de código abierto (LLMs)**, diseñado para explorar artículos académicos en español.  
A diferencia de los buscadores tradicionales que dependen de la coincidencia exacta de palabras clave, este sistema utiliza **embeddings semánticos** para medir la similitud conceptual entre textos, permitiendo recuperar información por *significado* y no solo por *palabra*.

El proyecto se enmarca dentro de una línea de investigación orientada a la **Inteligencia Artificial Explicable (XAI)** y la **Inteligencia Artificial Centrada en el Ser Humano (HCAI)**, promovida por instituciones como Stanford HAI y la UNESCO.

---

## 🧩 Arquitectura del sistema

1. **Construcción del corpus académico**
   - Extracción de metadatos y resúmenes desde el *Repositorio Institucional de la UNAM* (OAI-PMH).
   - Debido a restricciones de acceso, se utilizó el corpus abierto de *SciELO México* (1,000 artículos en español).

2. **Análisis exploratorio**
   - Limpieza y validación lingüística.
   - Visualización de frecuencias y coocurrencias temáticas.

3. **Generación de embeddings**
   - Modelos:
     - 🧮 `hkunlp/instructor-large`
     - ⚡ `distiluse-base-multilingual-cased-v2`
   - Archivos generados:
     - `emb_instructor_1000.npy`
     - `emb_distiluse_1000.npy`

4. **Despliegue del prototipo (Streamlit)**
   - Aplicación: `app_suayed_unam.py`
   - Modo de búsqueda:
     - *Profundidad (Instructor)*  
     - *Relevancia y velocidad (Distiluse)*

---

## 🚀 Ejecución local

```bash
git clone https://github.com/<usuario>/<repositorio>.git
cd <repositorio>

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
streamlit run app_suayed_unam.py

