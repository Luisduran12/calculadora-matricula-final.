import streamlit as st
from PIL import Image
import os

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
    "2026": {"pregrado": [170000, 187000], "tecnologia": [152000], "especializacion": [598000], "maestria": [925000], "doctorado": [1032000]},
}

VALORES_INSCRIPCION_POR_TIPO = {
    "2006-1": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2006-2": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2007-1": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2007-2": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2008-1": {"pregrado": 65000, "especializacion": 103000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2009-1": {"pregrado": 70000, "especializacion": 111000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2010-1": {"pregrado": 72000, "especializacion": 115000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2011-1": {"pregrado": 75000, "especializacion": 119000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2012-1": {"pregrado": 79000, "especializacion": 126000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2013-1": {"pregrado": 82000, "especializacion": 130000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2014": {"pregrado": 87000, "especializacion": 137000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2015": {"pregrado": 90000, "especializacion": 144000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2016": {"pregrado": 97000, "especializacion": 154000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2017": {"pregrado": 103000, "especializacion": 165000, "maestria": 0, "tecnologia": 0, "doctorado": 0},
    "2018": {"pregrado": 109000, "especializacion": 185000, "maestria": 0, "tecnologia": 109000, "doctorado": 0},
    "2019": {"pregrado": 116000, "especializacion": 196000, "maestria": 185000, "tecnologia": 116000, "doctorado": 0},
    "2020": {"pregrado": 123000, "especializacion": 203000, "maestria": 196000, "tecnologia": 123000, "doctorado": 0},
    "2021": {"pregrado": 127000, "especializacion": 223000, "maestria": 203000, "tecnologia": 127000, "doctorado": 0},
    "2022": {"pregrado": 140000, "especializacion": 259000, "maestria": 223000, "tecnologia": 140000, "doctorado": 0},
    "2023": {"pregrado": 162000, "especializacion": 290000, "maestria": 259000, "tecnologia": 162000, "doctorado": 0},
    "2024": {"pregrado": 182000, "especializacion": 317000, "maestria": 290000, "tecnologia": 182000, "doctorado": 0},
    "2025": {"pregrado": 199000, "especializacion": 0, "maestria": 317000, "tecnologia": 199000, "doctorado": 0},
    "2026": {"pregrado": 245000, "especializacion": 390000, "maestria": 390000, "tecnologia": 245000, "doctorado": 390000},
}

VALOR_SEGURO_FIJO = 9000


# ==============================================================================
# 2) ESTILOS (CSS)
# ==============================================================================

def apply_custom_css():
    st.markdown("""
        <style>
        .block-container {
            max-width: 680px;
            margin: auto;
            padding-top: 0rem;
        }
        .header-institucional {
            background: #0d2137;
            border-radius: 14px 14px 0 0;
            padding: 0;
            margin-bottom: 0;
        }
        .franja-dorada {
            height: 5px;
            background: linear-gradient(to right, #C8962A, #E8670A, #C8962A);
        }
        .stTotalCreditos {
            font-size: 13px;
            font-weight: 600;
            color: #854F0B;
            padding: 14px 18px;
            background: #fffbf0;
            border-left: 4px solid #C8962A;
            border-radius: 0 10px 10px 0;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        input[type="number"] {
            font-size: 20px !important;
            padding: 10px !important;
            text-align: center;
            border: 2px solid #C8962A !important;
            border-radius: 10px !important;
        }
        .stSelectbox > div > div {
            border-radius: 10px !important;
        }
        button[kind="primary"], .stButton > button {
            background-color: #0d2137 !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 12px 24px !important;
            letter-spacing: 0.5px !important;
            width: 100% !important;
        }
        .footer-institucional {
            background: #0d2137;
            border-radius: 0 0 14px 14px;
            padding: 8px 20px;
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)


# ==============================================================================
# 3) ENCABEZADO INSTITUCIONAL
# ==============================================================================

def mostrar_encabezado():
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if os.path.exists("unad.png"):
            img = Image.open("unad.png")
            st.image(img, width=90)

    with col2:
        st.markdown("""
            <div style="text-align:center; padding: 8px 0;">
                <div style="color:#C8962A; font-size:11px; letter-spacing:2px; text-transform:uppercase; margin-bottom:3px;">
                    Universidad Nacional Abierta y a Distancia
                </div>
                <div style="color:white; font-size:20px; font-weight:500; line-height:1.2;">
                    CCAV Cúcuta
                </div>
                <div style="color:#a0bdd4; font-size:12px; letter-spacing:1px; margin-top:2px;">
                    Registro y Control
                </div>
                <div style="height:2px; background:linear-gradient(to right,transparent,#C8962A,transparent); margin:8px auto; width:80%;"></div>
                <div style="color:white; font-size:16px; font-weight:400;">
                    Calculadora de Distribución de Créditos
                </div>
                <div style="color:#a0bdd4; font-size:12px; margin-top:2px;">
                    Luis Emir Guerrero Duran &nbsp;·&nbsp; Asesor Académico
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        if os.path.exists("edunat.png"):
            img2 = Image.open("edunat.png")
            st.image(img2, width=90)

    st.markdown('<div class="franja-dorada"></div>', unsafe_allow_html=True)


# ==============================================================================
# 4) APLICACIÓN PRINCIPAL
# ==============================================================================

def main_app():

    st.markdown("""
        <div style="background:#0d2137; border-radius:14px 14px 0 0; padding:16px 20px 0;">
    """, unsafe_allow_html=True)

    mostrar_encabezado()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div style="background:var(--background-color); padding:20px; border:0.5px solid #C8962A; border-top:none; border-radius:0 0 14px 14px;">', unsafe_allow_html=True)

    valor_creditos_neto = st.number_input(
        "Valor NETO de los Créditos ($)",
        min_value=0,
        step=1000,
        format="%d",
        help="Ingrese el costo total que cubren solo los créditos académicos."
    )

    opciones_anos = list(VALORES_CREDITO.keys())
    col_a, col_b = st.columns(2)
    with col_a:
        ano = st.selectbox("Año de la matrícula", options=opciones_anos)
    with col_b:
        valores_ano = VALORES_CREDITO.get(ano, {})
        tipos_disponibles = sorted([
            t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "doctorado", "homologacion"]
            if t in valores_ano and isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0
        ])
        if not tipos_disponibles:
            st.error(f"❌ No hay tipos definidos para {ano}.")
            return
        try:
            default_index = tipos_disponibles.index("pregrado")
        except ValueError:
            default_index = 0
        tipo_estudio = st.selectbox("Tipo de estudio", options=tipos_disponibles, index=default_index, key=f"tipo_{ano}")

    tipo_estudio_key = "pregrado" if tipo_estudio == "homologacion" else tipo_estudio
    valor_inscripcion = VALORES_INSCRIPCION_POR_TIPO.get(ano, {}).get(tipo_estudio_key, 0)
    valor_seguro = VALOR_SEGURO_FIJO
    valores_credito = valores_ano.get(tipo_estudio, [0])
    costo_total_creditos = valor_creditos_neto

    st.markdown("---")

    presiono_boton = st.button("🔍 Deducir Distribución de Créditos")

    solucion_encontrada = False
    total_creditos_deducidos = 0
    detalle_creditos = ""

    if presiono_boton:

        if tipo_estudio in ["pregrado"] and len(valores_credito) == 2:
            v1, v2 = sorted(valores_credito)
            for x in range(min(int(costo_total_creditos / v2) + 1, 31)):
                resto = costo_total_creditos - v2 * x
                if resto >= 0 and resto % v1 == 0:
                    creditos_v1, creditos_v2 = int(resto // v1), int(x)
                    total_creditos_deducidos = creditos_v1 + creditos_v2
                    detalle_creditos = f"- **{creditos_v1}** créditos ordinarios a **${v1:,}** (Total: ${v1*creditos_v1:,})\n- **{creditos_v2}** créditos extraordinarios a **${v2:,}** (Total: ${v2*creditos_v2:,})"
                    solucion_encontrada = True
                    break
            if not solucion_encontrada:
                st.error(f"❌ No existe combinación exacta de créditos de **${v1:,}** y **${v2:,}** para ${costo_total_creditos:,}.")

        elif tipo_estudio == "tecnologia" and len(valores_credito) == 2:
            v1, v2 = sorted(valores_credito)
            for x in range(min(int(costo_total_creditos / v2) + 1, 31)):
                resto = costo_total_creditos - v2 * x
                if resto >= 0 and resto % v1 == 0:
                    creditos_v1, creditos_v2 = int(resto // v1), int(x)
                    total_creditos_deducidos = creditos_v1 + creditos_v2
                    detalle_creditos = f"- **{creditos_v1}** créditos a **${v1:,}** (Total: ${v1*creditos_v1:,})\n- **{creditos_v2}** créditos a **${v2:,}** (Total: ${v2*creditos_v2:,})"
                    solucion_encontrada = True
                    break
            if not solucion_encontrada:
                st.error(f"❌ No existe combinación exacta para ${costo_total_creditos:,}.")

        elif len(valores_credito) >= 1 and valores_credito[0] > 0:
            v1 = valores_credito[0]
            if costo_total_creditos % v1 == 0:
                total_creditos_deducidos = costo_total_creditos // v1
                detalle_creditos = f"- **{total_creditos_deducidos}** créditos a **${v1:,}** cada uno (Total: ${costo_total_creditos:,})"
                solucion_encontrada = True
            else:
                st.error(f"❌ El valor neto (${costo_total_creditos:,}) no corresponde a un número entero de créditos a ${v1:,}. Resultado: {costo_total_creditos/v1:,.2f} créditos.")
        else:
            st.warning("El valor del crédito es 0 o no está definido.")

        if solucion_encontrada:
            st.markdown(f"""
                <div style="background:#f0faf6; border-left:4px solid #1D9E75; border-radius:0 10px 10px 0; padding:14px 18px; margin:12px 0; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="font-size:11px; font-weight:600; color:#085041; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;">✅ Distribución Deducida</div>
                        <div style="font-size:13px; color:#0F6E56;">{detalle_creditos.replace("**","").replace("- ","")}</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:11px; color:#085041; text-transform:uppercase; letter-spacing:1px;">Créditos</div>
                        <div style="font-size:36px; font-weight:500; color:#0d2137;">{total_creditos_deducidos}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("---")

    st.markdown(
        f'<div class="stTotalCreditos">COSTO NETO TOTAL DE CRÉDITOS &nbsp;·&nbsp; <span style="font-size:22px; color:#633806;">${costo_total_creditos:,}</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(f"""
        <div style="border:0.5px solid #e0e0e0; border-radius:10px; overflow:hidden; margin-top:8px;">
            <div style="background:#0d2137; padding:10px 16px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:12px; font-weight:500; color:#C8962A; text-transform:uppercase; letter-spacing:1px;">Valores de Referencia</span>
                <span style="font-size:12px; color:#a0bdd4;">{ano} · {tipo_estudio.capitalize()}</span>
            </div>
            <div style="padding:14px 16px; display:flex; flex-direction:column; gap:10px;">
    """, unsafe_allow_html=True)

    if tipo_estudio == "pregrado" and len(valores_credito) == 2:
        v1, v2 = sorted(valores_credito)
        st.markdown(f"""
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🪙 Crédito ordinario</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${v1:,}</span></div>
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🪙 Crédito extraordinario (+10%)</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${v2:,}</span></div>
        """, unsafe_allow_html=True)
    elif tipo_estudio == "tecnologia" and len(valores_credito) == 2:
        v1, v2 = sorted(valores_credito)
        st.markdown(f"""
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🪙 Crédito ordinario</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${v1:,}</span></div>
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🪙 Crédito extraordinario</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${v2:,}</span></div>
        """, unsafe_allow_html=True)
    elif len(valores_credito) >= 1:
        st.markdown(f"""
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🪙 Valor del crédito</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${valores_credito[0]:,}</span></div>
        """, unsafe_allow_html=True)

    if valor_inscripcion > 0:
        st.markdown(f"""
            <div style="height:0.5px;background:#eee;margin:4px 0;"></div>
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">📄 Inscripción ({tipo_estudio_key.capitalize()})</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${valor_inscripcion:,}</span></div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
            <div style="display:flex;justify-content:space-between;font-size:13px;"><span style="color:gray;">🛡 Seguro (fijo)</span><span style="font-weight:500;background:#f5f5f5;padding:3px 10px;border-radius:20px;">${valor_seguro:,}</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if ano == "2026" and tipo_estudio == "pregrado":
        st.info("ℹ️ El crédito de **$187,000** aplica a Ciencias de la Salud, Ciencias Básicas, Ingeniería, Tecnología y Ciencias Agrícolas (+10%).")

    st.markdown("""
        <div style="background:#0d2137; border-radius:0 0 14px 14px; padding:8px 20px; display:flex; justify-content:space-between; margin-top:1.5rem;">
            <span style="color:#a0bdd4; font-size:11px;">UNAD · CCAV Cúcuta · Registro y Control</span>
            <span style="color:#C8962A; font-size:11px; font-weight:500;">2026</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 5) PUNTO DE ENTRADA
# ==============================================================================

apply_custom_css()
main_app()
