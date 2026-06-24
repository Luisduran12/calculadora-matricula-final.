import streamlit as st
import base64
import os

# ==============================================================================
# 1) DATOS DE CONFIGURACIÓN - VALORES OFICIALES 2026
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
    "2014":   {"pregrado": [69000, 87000], "especializacion": [259000]},
    "2015":   {"pregrado": [70000, 90000], "especializacion": [271000], "maestria": [419000]},
    "2016":   {"pregrado": [77000, 84700], "especializacion": [290000], "maestria": [448000]},
    "2017":   {"pregrado": [83000, 91000], "especializacion": [310000], "maestria": [480000]},
    "2018":   {"pregrado": [88000, 97000],   "tecnologia": [88000, 97000],   "especializacion": [328000], "maestria": [508000], "homologacion": [23000]},
    "2019":   {"pregrado": [93000, 102000],  "tecnologia": [93000, 102000],  "especializacion": [348000], "maestria": [538000], "homologacion": [25000]},
    "2020":   {"pregrado": [98000, 108000],  "tecnologia": [98000, 107500],  "especializacion": [369000], "maestria": [571000], "homologacion": [26000]},
    "2021":   {"pregrado": [102000, 112000], "tecnologia": [91000, 100000],  "especializacion": [382000], "maestria": [591000], "homologacion": [27000]},
    "2022":   {"pregrado": [112000, 123000], "tecnologia": [100000, 110000], "especializacion": [420000], "maestria": [650000], "homologacion": [30000]},
    "2023":   {"pregrado": [123000, 135000], "tecnologia": [110000, 121000], "especializacion": [462000], "maestria": [715000], "homologacion": [35000]},
    "2024":   {"pregrado": [146000, 160000], "tecnologia": [130000, 143000], "especializacion": [462000], "maestria": [715000], "homologacion": [39000]},
    "2025":   {"pregrado": [159000, 175000], "tecnologia": [142000, 157000], "especializacion": [598000], "maestria": [925000], "homologacion": [43000]},
    # 2026: Acuerdo 004 — Tecnología 0.087 SMLMV / Profesional 0.097 SMLMV
    # Valores de escuelas especiales (+10%) incluidos automáticamente
    "2026": {
        "tecnologia":      [152000, 167000],   # ordinario / especiales +10%
        "profesional":     [170000, 187000],   # ordinario / especiales +10%
        "especializacion": [598000],
        "maestria":        [925000],
        "doctorado":       [1032000],
    },
}

VALORES_INSCRIPCION = {
    "2006-1": {"pregrado": 60000,  "especializacion": 96000,  "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2006-2": {"pregrado": 60000,  "especializacion": 96000,  "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2007-1": {"pregrado": 61000,  "especializacion": 97000,  "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2007-2": {"pregrado": 61000,  "especializacion": 97000,  "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2008-1": {"pregrado": 65000,  "especializacion": 103000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2009-1": {"pregrado": 70000,  "especializacion": 111000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2010-1": {"pregrado": 72000,  "especializacion": 115000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2011-1": {"pregrado": 75000,  "especializacion": 119000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2012-1": {"pregrado": 79000,  "especializacion": 126000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2013-1": {"pregrado": 82000,  "especializacion": 130000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2014":   {"pregrado": 87000,  "especializacion": 137000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2015":   {"pregrado": 90000,  "especializacion": 144000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2016":   {"pregrado": 97000,  "especializacion": 154000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2017":   {"pregrado": 103000, "especializacion": 165000, "maestria": 0,      "tecnologia": 0,      "doctorado": 0},
    "2018":   {"pregrado": 109000, "especializacion": 185000, "maestria": 0,      "tecnologia": 109000, "doctorado": 0},
    "2019":   {"pregrado": 116000, "especializacion": 196000, "maestria": 185000, "tecnologia": 116000, "doctorado": 0},
    "2020":   {"pregrado": 123000, "especializacion": 203000, "maestria": 196000, "tecnologia": 123000, "doctorado": 0},
    "2021":   {"pregrado": 127000, "especializacion": 223000, "maestria": 203000, "tecnologia": 127000, "doctorado": 0},
    "2022":   {"pregrado": 140000, "especializacion": 259000, "maestria": 223000, "tecnologia": 140000, "doctorado": 0},
    "2023":   {"pregrado": 162000, "especializacion": 290000, "maestria": 259000, "tecnologia": 162000, "doctorado": 0},
    "2024":   {"pregrado": 182000, "especializacion": 317000, "maestria": 290000, "tecnologia": 182000, "doctorado": 0},
    "2025":   {"pregrado": 199000, "especializacion": 0,      "maestria": 317000, "tecnologia": 199000, "doctorado": 0},
    "2026":   {"pregrado": 245000, "profesional": 245000,     "tecnologia": 245000,
               "especializacion": 390000, "maestria": 390000, "doctorado": 390000},
}

VALOR_SEGURO = {
    "2026": 10000,
    "default": 9000,
}

ETIQUETAS_CREDITO = {
    0: "ordinarios",
    1: "extraordinarios (+10%)",
    2: "extraordinarios (+20%)",
}

ETIQUETAS_TIPO = {
    "tecnologia": "Tecnología",
    "profesional": "Profesional",
    "pregrado": "Pregrado",
    "especializacion": "Especialización",
    "maestria": "Maestría",
    "doctorado": "Doctorado",
    "homologacion": "Homologación",
}

# ==============================================================================
# 2) LÓGICA DE DEDUCCIÓN — busca TODAS las combinaciones posibles
#    Devuelve lista de soluciones: cada una es lista de (cantidad, valor, etiqueta)
# ==============================================================================

def deducir_creditos(total, valores):
    """
    Dado un total y una lista de valores de crédito (ordenados de menor a mayor),
    encuentra todas las combinaciones no negativas (c0, c1, ...) tales que
    sum(ci * vi) == total, con ci >= 0 enteros.
    Retorna lista de soluciones, cada solución es lista de tuplas (ci, vi, etiqueta).
    Limita búsqueda a máx 120 créditos por tipo para eficiencia.
    """
    valores = sorted(set(v for v in valores if v > 0))
    if not valores:
        return []

    soluciones = []
    MAX = 120

    def buscar(idx, restante, acumulado):
        if idx == len(valores) - 1:
            v = valores[idx]
            if restante % v == 0:
                c = restante // v
                if c <= MAX:
                    sol = acumulado + [(c, v, ETIQUETAS_CREDITO.get(idx, f"tipo {idx+1}"))]
                    # Filtrar filas con 0 créditos
                    sol_limpia = [(c, v, e) for c, v, e in sol if c > 0]
                    if sol_limpia:
                        soluciones.append(sol_limpia)
            return
        v = valores[idx]
        max_c = min(restante // v, MAX)
        for c in range(max_c + 1):
            buscar(idx + 1, restante - c * v,
                   acumulado + [(c, v, ETIQUETAS_CREDITO.get(idx, f"tipo {idx+1}"))])

    buscar(0, total, [])
    # Ordenar: primero las soluciones con menos tipos distintos (más simples)
    soluciones.sort(key=lambda s: (len(s), -sum(c for c, v, e in s)))
    return soluciones

# ==============================================================================
# 3) UTILIDADES UI
# ==============================================================================

def img_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def apply_custom_css():
    st.markdown("""
        <style>
        .block-container { max-width: 720px; margin: auto; padding-top: 1rem; }
        input[type="number"] {
            font-size: 20px !important; padding: 10px !important;
            text-align: center;
            border: 2px solid #C8962A !important; border-radius: 10px !important;
        }
        .stButton > button {
            background-color: #0d2137 !important; color: white !important;
            font-size: 16px !important; font-weight: 500 !important;
            border-radius: 10px !important; border: none !important;
            padding: 12px 24px !important; width: 100% !important; margin-top: 5px;
        }
        .stButton > button:hover { background-color: #1a3a5c !important; }
        </style>
    """, unsafe_allow_html=True)

def mostrar_encabezado():
    unad_b64   = img_to_base64("unad.png")
    edunat_b64 = img_to_base64("edunat.png")
    unad_tag   = f'<img src="data:image/png;base64,{unad_b64}"   style="height:clamp(50px,8vw,80px);object-fit:contain;">' if unad_b64   else ""
    edunat_tag = f'<img src="data:image/png;base64,{edunat_b64}" style="height:clamp(50px,8vw,80px);object-fit:contain;">' if edunat_b64 else ""
    st.markdown(f"""
        <div style="background:#0d2137;border-radius:14px 14px 0 0;padding:20px 28px 16px;">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
            <div style="display:flex;align-items:center;flex-shrink:0;">{unad_tag}</div>
            <div style="text-align:center;flex:1;min-width:200px;padding:0 10px;">
              <div style="color:#C8962A;font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;margin-top:18px;">
                Universidad Nacional Abierta y a Distancia
              </div>
              <div style="color:white;font-size:22px;font-weight:500;line-height:1.2;">CCAV Cúcuta</div>
              <div style="height:2px;background:linear-gradient(to right,transparent,#C8962A,transparent);margin:8px auto;width:70%;"></div>
              <div style="color:white;font-size:15px;font-weight:400;">Calculadora de Distribución de Créditos</div>
              <div style="color:#a0bdd4;font-size:12px;margin-top:3px;">Registro y Control · 2026</div>
            </div>
            <div style="display:flex;align-items:center;">{edunat_tag}</div>
          </div>
        </div>
        <div style="height:5px;background:linear-gradient(to right,#C8962A,#E8670A,#C8962A);margin-bottom:0;"></div>
        <div style="background:white;border:1px solid #C8962A;border-top:none;border-radius:0 0 14px 14px;padding:24px;">
    """, unsafe_allow_html=True)

def fila_ref(label, valor):
    st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
                    font-size:13px;padding:6px 0;border-bottom:0.5px solid #f0f0f0;">
            <span style="color:#555;">{label}</span>
            <span style="font-weight:500;background:#f5f5f5;padding:3px 12px;
                         border-radius:20px;color:#222;">{valor}</span>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4) APLICACIÓN PRINCIPAL
# ==============================================================================

def main_app():
    mostrar_encabezado()

    # ── Inputs ────────────────────────────────────────────────────────────────
    valor_neto = st.number_input(
        "Valor NETO de los Créditos ($)",
        min_value=0, step=1000, format="%d",
        help="Ingrese solo el costo de los créditos académicos, sin inscripción ni seguro."
    )

    col_a, col_b = st.columns(2)
    with col_a:
        ano = st.selectbox("Año de la matrícula", options=list(VALORES_CREDITO.keys()))

    with col_b:
        valores_ano = VALORES_CREDITO.get(ano, {})
        tipos_disponibles = [
            t for t in valores_ano
            if isinstance(valores_ano[t], list) and any(v > 0 for v in valores_ano[t])
        ]
        if not tipos_disponibles:
            st.error(f"❌ No hay tipos definidos para {ano}.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        opciones_display = [ETIQUETAS_TIPO.get(t, t.capitalize()) for t in tipos_disponibles]
        default_idx = next(
            (i for i, t in enumerate(tipos_disponibles)
             if t in ("tecnologia", "profesional", "pregrado")), 0
        )
        tipo_display = st.selectbox("Tipo de estudio", opciones_display,
                                    index=default_idx, key=f"tipo_{ano}")
        tipo = tipos_disponibles[opciones_display.index(tipo_display)]

    valores_credito = sorted(set(v for v in valores_ano.get(tipo, []) if v > 0))
    valor_inscripcion = VALORES_INSCRIPCION.get(ano, {}).get(tipo, 0)
    valor_seguro = VALOR_SEGURO.get(ano, VALOR_SEGURO["default"])

    st.markdown("---")
    presiono = st.button("🔍 Deducir Distribución de Créditos")

    # ── Resultado ─────────────────────────────────────────────────────────────
    if presiono:
        if valor_neto == 0:
            st.warning("⚠️ Ingrese un valor mayor a $0.")
        elif not valores_credito:
            st.warning("El valor del crédito no está definido para esta selección.")
        else:
            soluciones = deducir_creditos(valor_neto, valores_credito)

            if not soluciones:
                # Mostrar con qué valores se intentó para ayudar al usuario
                vals_fmt = " / ".join(f"${v:,}" for v in valores_credito)
                st.error(
                    f"❌ **No existe combinación exacta** para **${valor_neto:,}** "
                    f"con los valores de {tipo_display} {ano} ({vals_fmt}).\n\n"
                    f"Verifique que el monto ingresado corresponda solo a créditos académicos."
                )
            else:
                # Tomar la solución más simple (menos filas distintas)
                sol = soluciones[0]
                total_creditos = sum(c for c, v, e in sol)

                # Construir líneas de detalle
                lineas_html = "".join(
                    f'<div style="font-size:14px;color:#0F6E56;margin-bottom:4px;">'
                    f'<b>{c}</b> crédito{"s" if c!=1 else ""} {e} × ${v:,} = <b>${c*v:,}</b></div>'
                    for c, v, e in sol
                )

                st.markdown(f"""
                    <div style="background:#f0faf6;border-left:4px solid #1D9E75;
                                border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;
                                display:flex;justify-content:space-between;align-items:center;">
                        <div style="flex:1;">
                            <div style="font-size:11px;font-weight:600;color:#085041;
                                        text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">
                                ✅ Distribución Deducida
                            </div>
                            {lineas_html}
                        </div>
                        <div style="text-align:center;padding-left:24px;border-left:1px solid #9FE1CB;
                                    min-width:80px;">
                            <div style="font-size:11px;color:#085041;text-transform:uppercase;
                                        letter-spacing:1px;">Total</div>
                            <div style="font-size:48px;font-weight:600;color:#0d2137;line-height:1;">
                                {total_creditos}
                            </div>
                            <div style="font-size:11px;color:#085041;">créditos</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # Si hay múltiples soluciones, mostrarlas como alternativas
                if len(soluciones) > 1:
                    with st.expander(f"Ver {len(soluciones)-1} combinación(es) alternativa(s)"):
                        for i, sol_alt in enumerate(soluciones[1:], 2):
                            total_alt = sum(c for c, v, e in sol_alt)
                            lineas_alt = " | ".join(
                                f"{c} × ${v:,} ({e})" for c, v, e in sol_alt
                            )
                            st.markdown(
                                f"**Opción {i}** ({total_alt} créditos): {lineas_alt}"
                            )

                st.markdown("---")

    # ── Costo Neto ────────────────────────────────────────────────────────────
    st.markdown(f"""
        <div style="background:#fffbf0;border-left:4px solid #C8962A;
                    border-radius:0 10px 10px 0;padding:14px 20px;margin:12px 0;
                    display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:11px;font-weight:600;color:#854F0B;
                        text-transform:uppercase;letter-spacing:1px;">Costo Neto Total de Créditos</div>
            <div style="font-size:26px;font-weight:500;color:#633806;">${valor_neto:,}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── Valores de Referencia ─────────────────────────────────────────────────
    st.markdown(f"""
        <div style="border:0.5px solid #ddd;border-radius:10px;overflow:hidden;">
            <div style="background:#0d2137;padding:10px 16px;
                        display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:600;color:#C8962A;
                             text-transform:uppercase;letter-spacing:1px;">Valores de Referencia</span>
                <span style="font-size:12px;color:#a0bdd4;">{ano} · {tipo_display}</span>
            </div>
            <div style="padding:14px 16px;">
    """, unsafe_allow_html=True)

    for idx, v in enumerate(valores_credito):
        etiqueta = ETIQUETAS_CREDITO.get(idx, f"Tipo {idx+1}")
        fila_ref(f"🪙 Crédito {etiqueta}", f"${v:,}")

    if valor_inscripcion > 0:
        fila_ref("📄 Inscripción", f"${valor_inscripcion:,}")
    fila_ref("🛡 Seguro estudiantil", f"${valor_seguro:,}")

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── Nota informativa 2026 escuelas especiales ─────────────────────────────
    if ano == "2026" and tipo in ("tecnologia", "profesional"):
        v_ord = valores_credito[0]
        v_esp = valores_credito[1] if len(valores_credito) > 1 else None
        nota = (
            f"ℹ️ La calculadora detecta automáticamente la combinación de créditos. "
            f"El valor **${v_ord:,}** corresponde a créditos ordinarios y "
        )
        if v_esp:
            nota += (
                f"**${v_esp:,}** a créditos de Escuelas Especiales "
                f"(Ciencias de la Salud, Ciencias Básicas, Ingeniería, Tecnología y Ciencias Agrícolas). "
                f"No es necesario indicar la escuela — el sistema deduce la distribución del monto ingresado."
            )
        st.info(nota)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("""
        <div style="background:#0d2137;border-radius:10px;padding:10px 20px;
                    display:flex;justify-content:space-between;align-items:center;margin-top:1.5rem;">
            <span style="color:#a0bdd4;font-size:11px;">UNAD · CCAV Cúcuta · Registro y Control</span>
            <span style="color:#a0bdd4;font-size:11px;">Luis Emir Guerrero Duran · Monitor</span>
            <span style="color:#C8962A;font-size:11px;font-weight:500;">2026</span>
        </div>
        </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# 5) PUNTO DE ENTRADA
# ==============================================================================
apply_custom_css()
main_app()
