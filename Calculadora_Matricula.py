import streamlit as st

# ==============================================================================
# 1) DATOS DE CONFIGURACIÓN
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
            padding: 15px;
            border: 2px solid #1E90FF;
            border-radius: 10px;
            margin-top: 25px;
            background-color: rgba(30, 144, 255, 0.1);
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

    # Entrada de datos
    valor_creditos_neto = st.number_input(
        "Valor NETO de los Créditos ($)",
        min_value=0,
        step=1000,
        format="%d"
    )

    opciones_anos = list(VALORES_CREDITO.keys())
    ano = st.selectbox("Selecciona el año de la matrícula", options=opciones_anos)
    
    valores_ano = VALORES_CREDITO.get(ano, {})
    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano
    ])

    tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=tipos_disponibles)
    valores_credito = valores_ano.get(tipo_estudio, [0])

    st.markdown("---")
    
    # Botón de cálculo
    if st.button("Deducir Distribución de Créditos"):
        solucion_encontrada = False
        detalle_creditos = ""
        total_creditos = 0

        # Lógica para Pregrado/Tecnología (2 tarifas)
        if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
            v1, v2 = sorted(valores_credito)
            # Probamos combinaciones
            for x in range(min(int(valor_creditos_neto / v2) + 1, 40)):
                resto = valor_creditos_neto - (v2 * x)
                if resto >= 0 and resto % v1 == 0:
                    y = resto // v1
                    total_creditos = int(y + x)
                    detalle_creditos = f"""
* **{int(y)}** créditos a **${v1:,}** (Ordinarios)
* **{int(x)}** créditos a **${v2:,}** (Extraordinarios)
"""
                    solucion_encontrada = True
                    break

        # Lógica para Tarifa Única
        elif len(valores_credito) >= 1 and valores_credito[0] > 0:
            v1 = valores_credito[0]
            if valor_creditos_neto % v1 == 0:
                total_creditos = valor_creditos_neto // v1
                detalle_creditos = f"* **{total_creditos}** créditos a **${v1:,}** c/u"
                solucion_encontrada = True

        # MOSTRAR RESULTADOS (Solo si se presiona el botón)
        if solucion_encontrada:
            st.subheader("✅ Resultado de la Distribución")
            st.markdown(f"**Total de Créditos Deducidos:** {total_creditos}")
            st.markdown(detalle_creditos)
            
            # Caja del total
            st.markdown(
                f'<div class="stTotalCreditos">COSTO TOTAL EVALUADO: ${valor_creditos_neto:,}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.error("❌ No se encontró una combinación exacta para ese valor neto.")

if __name__ == "__main__":
    apply_custom_css()
    main_app()
