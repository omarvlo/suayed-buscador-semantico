import streamlit as st
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import numpy as np
import altair as alt
from sentence_transformers import SentenceTransformer
import time

# =========================================================
# CONFIGURACIÓN INICIAL
# =========================================================
st.set_page_config(page_title="Buscador Semántico SUAyED", layout="wide")

# --- Cabecera con dos columnas ---
col1, col2 = st.columns([3, 1])  # Izquierda más ancha que la derecha

with col1:
    st.title("🔍 Buscador Semántico de Corpus Académico")
    st.markdown(
        "Este prototipo permite la exploración de un corpus de *SciELO México* de hasta **1000 artículos**"
        "utilizando **similitud semántica** basada en embeddings de los modelos masivos de lenguaje de código abierto."
    )
    st.write("Selecciona un modo de búsqueda, escribe tu consulta y explora los resultados.")

with col2:
    st.markdown(
        """
        <div style='text-align: right; font-size: 13px; line-height: 1.4;'>
            <strong>Nombre:</strong> Omar Velázquez López<br>
            <strong>COA:</strong> Investigador Ordinario Asociado “C” de tiempo completo, interino<br>
            <strong>Proyecto:</strong> Modelos de lenguaje masivos de código abierto para la búsqueda y el fortalecimiento del aprendizaje en el SUAyED
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CARGA DE MODELOS CON BARRA DE ESPERA
# =========================================================
@st.cache_resource(show_spinner=False)
def load_models():
    """Precarga ambos modelos en CPU solo una vez."""
    start = time.time()

    # Placeholder temporal para mensajes dinámicos
    status = st.empty()
    status.info("⏳ Cargando modelos, por favor espera... (~20–59 seg. la primera vez)")

    # Carga de modelos
    instructor = SentenceTransformer("hkunlp/instructor-large", device="cpu")
    distiluse = SentenceTransformer("distiluse-base-multilingual-cased-v2", device="cpu")

    elapsed = time.time() - start

    # Reemplaza el mensaje de carga por el de éxito
    status.success(f"✅ Modelos cargados en {elapsed:.1f} segundos.")

    return instructor, distiluse

instructor_model, distiluse_model = load_models()

# =========================================================
# CARGA DE EMBEDDINGS Y CORPUS
# =========================================================
@st.cache_data(show_spinner=False)
def load_corpus():
    df = pd.read_csv("corpus_scielo_mexico_1000.csv")
    emb_instructor = np.load("emb_instructor_1000.npy")
    emb_distiluse = np.load("emb_distiluse_1000.npy")
    return df, emb_instructor, emb_distiluse

df, emb_instructor, emb_distiluse = load_corpus()

# =========================================================
# INTERFAZ PRINCIPAL
# =========================================================
# --- Selector de modo ---
modo = st.selectbox(
    "Selecciona el modo de búsqueda:",
    ["Profundidad (Instructor)", "Relevancia y velocidad (Distiluse)"]
)
# =========================================================
# DISEÑO EN DOS COLUMNAS
# =========================================================
col1, col2 = st.columns([3, 1])  # [izquierda, derecha] -> puedes ajustar proporciones


# --- Columna derecha: búsqueda y resultados ---
with col1:
    # --- Caja de texto ---
    query = st.text_input("Escribe tu consulta:", "inteligencia artificial en el aprendizaje")

    # --- Botón para buscar ---
    if st.button("🔍 Ejecutar búsqueda") and query.strip():
        st.info(f"Ejecutando búsqueda con modo **{modo}**...")

        if "Instructor" in modo:
            model = SentenceTransformer("hkunlp/instructor-large")
            instruction = "Representa este texto en español para comparar su contenido temático con otros artículos académicos sobre"
            q_vec = model.encode([[instruction, query]])
            emb_matrix = emb_instructor
        else:
            model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
            q_vec = model.encode([query])
            emb_matrix = emb_distiluse

        # Similaridad
        sim = np.dot(emb_matrix, q_vec.T).flatten()
        idx = np.argsort(sim)[::-1][:3]
        results = df.iloc[idx][["Título", "Autor", "Fecha", "Resumen"]].reset_index(drop=True)

        st.subheader("Los 3 resultados más similares:")
        for i, row in results.iterrows():
            st.markdown(f"**{i+1}. {row['Título']}**")
            st.caption(f"👤 {row['Autor']} | 📅 {row['Fecha']}")
            st.write(
                row["Resumen"][:400] + "..."
                if len(row["Resumen"]) > 400
                else row["Resumen"]
            )
            st.divider()


# --- Columna izquierda: corpus ---
with col2:
# --- Mostrar corpus (limitado) ---
# Mostrar corpus truncado
    st.write("📚 Vista previa de la base de datos (1000 registros)")

    # Vista previa con desplazamiento interno
    st.dataframe(
        df[["Título", "Autor", "Materia", "Fecha"]],  # columnas visibles
        use_container_width=True,
        height=300  # controla el alto del marco
    )

# Mostrar corpus truncado
    st.write("**Análisis XAI (IA Explicable) con SHAP**")
    with st.spinner("Calculando valores SHAP (simulados)..."):
        tokens = query.split()
        vals = np.random.randn(len(tokens))
        df_shap = pd.DataFrame({"token": tokens, "valor": vals})

        chart = (
            alt.Chart(df_shap)
            .mark_bar()
            .encode(
                x=alt.X("valor:Q", title="Valor SHAP simulado"),
                y=alt.Y("token:N", sort="-x", title=None),
                color=alt.condition(
                    "datum.valor > 0",
                    alt.value("#4CAF50"),  # verde
                    alt.value("#E53935"),  # rojo
                ),
                tooltip=["token", "valor"]
            )
            .properties(
                title="Contribución de las palabras buscadas",
                width=600,
                height=300
            )
        )

        st.altair_chart(chart, use_container_width=True)




