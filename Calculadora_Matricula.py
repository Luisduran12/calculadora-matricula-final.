import streamlit as st

# ==============================================================================
# 1) DATOS DE CONFIGURACIÓN (TABLAS)
# ==============================================================================

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

VALOR_SEGURO_FIJO = 9000


# ==============================================================================
# 2) ESTILOS (CSS)
# ==============================================================================

def apply_custom_css():
    st.markdown(
        """
        <style>
        .block-container {
            text-align: center;
            max-width: 600px;
            margin: auto;
            padding-top: 1rem;
        }
        input[type="number"] {
            font-size: 20px !important;
            padding: 10px !important;
            text-align: center;
        }
        button {
            font-size: 18px !important;
            padding: 12px 20px !important;
            border-radius: 10px !important;
            margin-top: 15px;
        }
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

    st.title("Calculadora de Distribución de Créditos 🛠️")
    st.header("Luis Emir Guerrero Duran")

    col1, col2 = st.columns([3, 1])

    with col1:
        valor_creditos_neto = st.number_input(
            "Valor NETO de los Créditos ($)",
            min_value=0,
            step=1000,
            format="%d",
            help="Ingrese el costo total que cubren solo los créditos académicos."
        )

    opciones_anos = list(VALORES_CREDITO.keys())
    ano = st.selectbox("Selecciona el año de la matrícula", options=opciones_anos)

    valores_ano = VALORES_CREDITO.get(ano, {})

    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano and isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0
    ])

    if not tipos_disponibles:
        st.error(f"❌ Error: No hay tipos de estudio con valores de crédito definidos para el año {ano}.")
        return

    try:
        default_index = tipos_disponibles.index("pregrado")
    except ValueError:
        default_index = 0

    tipo_estudio = st.selectbox(
        "Selecciona el tipo de estudio",
        options=tipos_disponibles,
        index=default_index,
        key=f"tipo_estudio_{ano}"
    )

    tipo_estudio_key = "pregrado" if tipo_estudio == "homologacion" else tipo_estudio

    valor_inscripcion = VALORES_INSCRIPCION_POR_TIPO.get(ano, {}).get(tipo_estudio_key, 0)
    valor_seguro = VALOR_SEGURO_FIJO
    valores_credito = valores_ano.get(tipo_estudio, [0])

    st.markdown("---")

    # ==============================================================================
    # ✅ COSTO NETO TOTAL — siempre visible
    # ==============================================================================
    costo_total_creditos = valor_creditos_neto

    st.markdown(
        f'<div class="stTotalCreditos">COSTO NETO TOTAL DE CRÉDITOS: ${costo_total_creditos:,}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ==============================================================================
    # ✅ BOTÓN — encima de Valores Fijos y de Referencia
    # ==============================================================================
    presiono_boton = st.button("Deducir Distribución de Créditos")

    solucion_encontrada = False
    total_creditos_deducidos = 0
    detalle_creditos = ""

    if presiono_boton:

        # Caso A: pregrado/tecnología con 2 tarifas
        if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:

            v1, v2 = sorted(valores_credito)

            max_creditos_v2 = int(costo_total_creditos / v2) + 1
            max_creditos_v2 = min(max_creditos_v2, 30)

            for x in range(max_creditos_v2 + 1):
                costo_v2 = v2 * x
                resto = costo_total_creditos - costo_v2

                if resto < 0:
                    continue

                if resto % v1 == 0:
                    y = resto // v1
                    creditos_v1 = int(y)
                    creditos_v2 = int(x)
                    total_creditos_deducidos = creditos_v1 + creditos_v2

                    detalle_creditos = f"""
- **{creditos_v1}** créditos a **${v1:,}** cada uno (Total: ${v1 * creditos_v1:,})
- **{creditos_v2}** créditos a **${v2:,}** cada uno (Total: ${v2 * creditos_v2:,})
"""
                    solucion_encontrada = True
                    break

            if not solucion_encontrada:
                st.error(
                    f"❌ No existe una combinación exacta de créditos de **${v1:,}** y **${v2:,}** "
                    f"que sume el valor neto ingresado (${costo_total_creditos:,})."
                )

        # Caso B: tipos con un solo valor de crédito
        elif len(valores_credito) >= 1 and valores_credito[0] > 0:

            v1 = valores_credito[0]

            if costo_total_creditos % v1 == 0:
                total_creditos_deducidos = costo_total_creditos // v1
                detalle_creditos = f"- **{total_creditos_deducidos}** créditos a **${v1:,}** cada uno (Total: ${costo_total_creditos:,})"
                solucion_encontrada = True
            else:
                creditos_calculados = costo_total_creditos / v1
                st.error(f"""
❌ El valor neto (${costo_total_creditos:,}) no corresponde a un número entero válido de créditos a ${v1:,} cada uno.
- El cálculo arroja **{creditos_calculados:,.2f}** créditos.
""")
        else:
            st.warning("El valor del crédito es 0 o no está definido. No se puede calcular.")

        if solucion_encontrada:
            st.subheader("✅ Distribución de Créditos Deducida ✅")
            st.markdown("#### Detalle de la Distribución:")
            st.markdown(f"**Total de Créditos Deducidos:** **{total_creditos_deducidos}**")
            st.markdown(detalle_creditos)
            st.markdown("---")

    # ==============================================================================
    # ✅ VALORES FIJOS Y DE REFERENCIA — siempre al final
    # ==============================================================================
    st.subheader("Valores Fijos y de Referencia por Año")

    st.markdown(
        f"""
        <div style="background-color:#e8f4fd; padding:10px; border-radius:5px; text-align:center;">
            <span style="color:#1E90FF;"><strong>Año:</strong> {ano} | <strong>Tipo de Estudio:</strong> {tipo_estudio.capitalize()}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
        v1, v2 = sorted(valores_credito)
        st.markdown(f"🪙 **Crédito Ordinario:** ${v1:,}")
        st.markdown(f"**Crédito Extraordinario:** ${v2:,}")
    elif len(valores_credito) >= 1:
        st.markdown(f"🪙 **Valor del Crédito:** ${valores_credito[0]:,}")

    if valor_inscripcion > 0:
        st.markdown(f"📄 **Costo de Inscripción ({tipo_estudio_key.capitalize()}):** ${valor_inscripcion:,}")
    else:
        st.markdown(f"📄 **Costo de Inscripción:** No definido para este año/tipo")

    st.markdown(f"🛡 **Costo del Seguro (Fijo):** ${valor_seguro:,}")


# ==============================================================================
# 4) PUNTO DE ENTRADA
# ==============================================================================

apply_custom_css()
main_app()
