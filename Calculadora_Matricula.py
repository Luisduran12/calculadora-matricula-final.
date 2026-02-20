import streamlit as st

# ==============================================================================
# 1) DATOS DE CONFIGURACIÓN (TABLAS)
# ==============================================================================

# Diccionario con valores de créditos por año y por tipo de estudio
VALORES_CREDITO = {
    "2006-1": {"pregrado": [43000, 60000], "especializacion": [170000]},
    "2006-2": {"pregrado": [46000, 60000], "especializacion": [170000]},
    "2007-1": {"pregrado": [46000, 61000], "especializacion": [171000]},
    "2007-2": {"pregrado": [49000, 61000], "especializacion": [182000]},
    "2008-1": {"pregrado": [52000, 65000], "especializacion": [194000]},
    "2009-1": {"pregrado": [56000, 70000], "especializacion": [209000]},
    "2010-1": {"pregrado": [58000, 72000], "especializacion": [216000]},
    "2011-1": {"pregrado": [60000, 75000], "especializacion": [225000]},
    "2012-1": {"pregrado": [63000, 79000], "especializacion": [238000]},
    "2013-1": {"pregrado": [66000, 82000], "especializacion": [248000]},
    "2014": {"pregrado": [69000, 87000], "especializacion": [259000]},
    "2015": {"pregrado": [70000, 90000], "especializacion": [271000], "maestria": [419000]},
    "2016": {"pregrado": [77000, 84700], "especializacion": [290000], "maestria": [448000]},
    "2017": {"pregrado": [83000, 91000], "especializacion": [310000], "maestria": [480000]},
    "2018": {"pregrado": [88000, 97000], "tecnologia": [88000, 97000], "especializacion": [328000], "maestria": [508000], "homologacion": [23000]},
    "2019": {"pregrado": [93000, 102000], "tecnologia": [93000, 102000], "especializacion": [348000], "maestria": [538000], "homologacion": [25000]},
    "2020": {"pregrado": [98000, 108000], "tecnologia": [98000, 107500], "especializacion": [369000], "maestria": [571000], "homologacion": [26000]},
    "2021": {"pregrado": [102000, 112000], "tecnologia": [91000, 100000], "especializacion": [382000], "maestria": [591000], "homologacion": [27000]},
    "2022": {"pregrado": [112000, 123000], "tecnologia": [100000, 110000], "especializacion": [420000], "maestria": [650000], "homologacion": [30000]},
    "2023": {"pregrado": [123000, 135000], "tecnologia": [110000, 121000], "especializacion": [462000], "maestria": [715000], "homologacion": [35000]},
    "2024": {"pregrado": [146000, 160000], "tecnologia": [130000, 143000], "especializacion": [462000], "maestria": [715000], "homologacion": [39000]},
    "2025": {"pregrado": [159000, 175000], "tecnologia": [142000, 157000], "especializacion": [598000], "maestria": [925000], "homologacion": [43000]},
}

# Diccionario con valores de inscripción por año y tipo
VALORES_INSCRIPCION_POR_TIPO = {
    "2006-1": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0},
    "2006-2": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0},
    "2007-1": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0},
    "2007-2": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0},
    "2008-1": {"pregrado": 65000, "especializacion": 103000, "maestria": 0, "tecnologia": 0},
    "2009-1": {"pregrado": 70000, "especializacion": 111000, "maestria": 0, "tecnologia": 0},
    "2010-1": {"pregrado": 72000, "especializacion": 115000, "maestria": 0, "tecnologia": 0},
    "2011-1": {"pregrado": 75000, "especializacion": 119000, "maestria": 0, "tecnologia": 0},
    "2012-1": {"pregrado": 79000, "especializacion": 126000, "maestria": 0, "tecnologia": 0},
    "2013-1": {"pregrado": 82000, "especializacion": 130000, "maestria": 0, "tecnologia": 0},
    "2014": {"pregrado": 87000, "especializacion": 137000, "maestria": 0, "tecnologia": 0},
    "2015": {"pregrado": 90000, "especializacion": 144000, "maestria": 0, "tecnologia": 0},
    "2016": {"pregrado": 97000, "especializacion": 154000, "maestria": 0, "tecnologia": 0},
    "2017": {"pregrado": 103000, "especializacion": 165000, "maestria": 0, "tecnologia": 0},
    "2018": {"pregrado": 109000, "especializacion": 185000, "maestria": 0, "tecnologia": 109000},
    "2019": {"pregrado": 116000, "especializacion": 196000, "maestria": 185000, "tecnologia": 116000},
    "2020": {"pregrado": 123000, "especializacion": 203000, "maestria": 196000, "tecnologia": 123000},
    "2021": {"pregrado": 127000, "especializacion": 223000, "maestria": 203000, "tecnologia": 127000},
    "2022": {"pregrado": 140000, "especializacion": 259000, "maestria": 223000, "tecnologia": 140000},
    "2023": {"pregrado": 162000, "especializacion": 290000, "maestria": 259000, "tecnologia": 162000},
    "2024": {"pregrado": 182000, "especializacion": 317000, "maestria": 290000, "tecnologia": 182000},
    "2025": {"pregrado": 199000, "especializacion": 0, "maestria": 317000, "tecnologia": 199000},
}

# Valor fijo del seguro
VALOR_SEGURO_FIJO = 9000


# ==============================================================================
# 2) ESTILOS (CSS)
# ==============================================================================

def apply_custom_css():
    """Aplica estilos para centrar y mejorar visualmente la app."""
    st.markdown(
        """
        <style>
        /* Centra el contenido y limita ancho */
        .block-container {
            text-align: center;
            max-width: 600px;
            margin: auto;
            padding-top: 1rem;
        }

        /* Agranda el input numérico */
        input[type="number"] {
            font-size: 20px !important;
            padding: 10px !important;
            text-align: center;
        }

        /* Estilo del botón */
        button {
            font-size: 18px !important;
            padding: 12px 20px !important;
            border-radius: 10px !important;
            margin-top: 15px;
        }

        /* Caja del total */
        .stTotalCreditos {
            font-size: 24px;
            font-weight: bold;
            color: #1E90FF;
            padding: 10px;
            border: 2px solid #1E90FF;
            border-radius: 5px;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# 3) APLICACIÓN PRINCIPAL
# ==============================================================================

def main_app():
    """Ejecuta la interfaz principal y la lógica de cálculo."""

    # Título principal de la aplicación
    st.title("Calculadora de Distribución de Créditos 🛠️")

    # Nombre del usuario/encabezado (como en tu captura)
    st.header("Luis Emir Guerrero Duran")

    # Sección de entrada del valor neto de los créditos
    col1, col2 = st.columns([3, 1])

    # Input numérico del valor neto
    with col1:
        valor_creditos_neto = st.number_input(
            "Valor NETO de los Créditos ($)",  # Título del campo
            min_value=0,                      # No permite negativos
            step=1000,                        # Incrementos de 1000
            format="%d",                      # Muestra sin decimales
            help="Ingrese el costo total que cubren solo los créditos académicos."
        )

    # Lista de años disponibles (desde el diccionario)
    opciones_anos = list(VALORES_CREDITO.keys())

    # Selector de año
    ano = st.selectbox("Selecciona el año de la matrícula", options=opciones_anos)

    # Se obtiene el diccionario de tipos disponibles para el año seleccionado
    valores_ano = VALORES_CREDITO.get(ano, {})

    # Se filtran tipos de estudio disponibles para ese año
    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano and isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0
    ])

    # Si no hay tipos, se muestra error y se detiene
    if not tipos_disponibles:
        st.error(f"❌ Error: No hay tipos de estudio con valores de crédito definidos para el año {ano}.")
        return

    # Se intenta poner pregrado como valor por defecto
    try:
        default_index = tipos_disponibles.index("pregrado")
    except ValueError:
        default_index = 0

    # Selector de tipo de estudio
    tipo_estudio = st.selectbox(
        "Selecciona el tipo de estudio",
        options=tipos_disponibles,
        index=default_index,
        key=f"tipo_estudio_{ano}"
    )

    # Si es homologación, se usa inscripción de pregrado (como tu lógica original)
    tipo_estudio_key = "pregrado" if tipo_estudio == "homologacion" else tipo_estudio

    # Se obtiene el valor de inscripción según año y tipo (si existe)
    valor_inscripcion = VALORES_INSCRIPCION_POR_TIPO.get(ano, {}).get(tipo_estudio_key, 0)

    # Valor fijo de seguro
    valor_seguro = VALOR_SEGURO_FIJO

    # Valores del crédito del año/tipo seleccionado
    valores_credito = valores_ano.get(tipo_estudio, [0])

    # Línea separadora visual
    st.markdown("---")

    # ✅ Botón ubicado como en la imagen (antes de los valores fijos)
    presiono_boton = st.button("Deducir Distribución de Créditos")

    # Variables para resultados
    solucion_encontrada = False
    total_creditos_deducidos = 0
    detalle_creditos = ""
    costo_total_creditos = valor_creditos_neto

    # Si el usuario presiona el botón, se ejecuta el cálculo
    if presiono_boton:

        # Caso A: pregrado/tecnología con 2 tarifas (ordinario y extraordinario)
        if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:

            # Ordena para garantizar v1 menor y v2 mayor
            v1, v2 = sorted(valores_credito)

            # Máximo de créditos extraordinarios a probar (límite práctico)
            max_creditos_v2 = int(costo_total_creditos / v2) + 1
            max_creditos_v2 = min(max_creditos_v2, 30)

            # Se prueban combinaciones de extraordinarios (x) y ordinarios (y)
            for x in range(max_creditos_v2 + 1):

                # Costo total de x créditos extraordinarios
                costo_v2 = v2 * x

                # Resto que debe cubrirse con ordinarios
                resto = costo_total_creditos - costo_v2

                # Si el resto es negativo, se salta
                if resto < 0:
                    continue

                # Si el resto es divisible por v1, se encontró combinación exacta
                if resto % v1 == 0:

                    # Número de créditos ordinarios
                    y = resto // v1

                    # Se guarda la solución
                    creditos_v1 = int(y)
                    creditos_v2 = int(x)
                    total_creditos_deducidos = creditos_v1 + creditos_v2

                    # Se arma el detalle en pantalla
                    detalle_creditos = f"""
   - **{creditos_v1}** créditos a **${v1:,}** cada uno (Total: ${v1 * creditos_v1:,})
   - **{creditos_v2}** créditos a **${v2:,}** cada uno (Total: ${v2 * creditos_v2:,})
   """

                    # Se marca como encontrada
                    solucion_encontrada = True
                    break

            # Si no se encontró solución, se muestra error
            if not solucion_encontrada:
                st.error(
                    f"❌ No existe una combinación exacta de créditos de **${v1:,}** y **${v2:,}** "
                    f"que sume el valor neto ingresado (${costo_total_creditos:,})."
                )

        # Caso B: tipos con un solo valor de crédito (especialización, maestría, etc.)
        elif len(valores_credito) >= 1 and valores_credito[0] > 0:

            # Se toma el valor único del crédito
            v1 = valores_credito[0]

            # Si el valor neto es divisible, hay número entero de créditos
            if costo_total_creditos % v1 == 0:

                # Total de créditos deducidos
                total_creditos_deducidos = costo_total_creditos // v1

                # Detalle del cálculo
                detalle_creditos = f"- **{total_creditos_deducidos}** créditos a **${v1:,}** cada uno (Total: ${costo_total_creditos:,})"

                # Se marca como solución encontrada
                solucion_encontrada = True

            else:
                # Si no da entero, se muestra el cálculo decimal
                creditos_calculados = costo_total_creditos / v1
                st.error(f"""
   ❌ El valor neto (${costo_total_creditos:,}) no corresponde a un número entero válido de créditos a ${v1:,} cada uno.
   - El cálculo arroja **{creditos_calculados:,.2f}** créditos.
   """)
        else:
            # Si no hay valor definido, se avisa
            st.warning("El valor del crédito es 0 o no está definido. No se puede calcular.")

        # Si se encontró la solución, se muestran resultados
        if solucion_encontrada:
            st.subheader("✅ Distribución de Créditos Deducida ✅")
            st.markdown("#### Detalle de la Distribución:")
            st.markdown(f"**Total de Créditos Deducidos:** **{total_creditos_deducidos}**")
            st.markdown(detalle_creditos)
            st.markdown("---")


# ==============================================================================
# 4) EJECUCIÓN
# ==============================================================================

if __name__ == "__main__":
    apply_custom_css()
    main_app()
