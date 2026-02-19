import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import urllib.parse

# Configurar página
st.set_page_config(
    page_title="Calculadora de Costos SAT 2026",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta de colores
COLORES = {
    "principal": "#1f77b4", "utilidad": "#2ca02c", "isr": "#d62728",
    "iva": "#ff7f0e", "fondo": "#f8f9fa", "texto": "#1a1a1a", "acento": "#00d4ff"
}

st.markdown(f"<style>.main {{ background-color: {COLORES['fondo']}; }}</style>", unsafe_allow_html=True)

# Inicializar session state
if 'historial' not in st.session_state:
    st.session_state.historial = []

# TARIFAS ISR 2026 - Artículo 152 LISR
TARIFAS_ISR_2026 = {
    "Diaria": [{"limite_inf": 0.01, "limite_sup": 27.78, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 27.79, "limite_sup": 235.81, "cuota": 0.53, "tasa": 6.4},
        {"limite_inf": 235.82, "limite_sup": 414.41, "cuota": 13.85, "tasa": 10.88},
        {"limite_inf": 414.42, "limite_sup": 481.73, "cuota": 33.28, "tasa": 16.0},
        {"limite_inf": 481.74, "limite_sup": 576.76, "cuota": 44.05, "tasa": 17.92},
        {"limite_inf": 576.77, "limite_sup": 1163.25, "cuota": 61.08, "tasa": 21.36},
        {"limite_inf": 1163.26, "limite_sup": 1833.44, "cuota": 186.35, "tasa": 23.52},
        {"limite_inf": 1833.45, "limite_sup": 3500.35, "cuota": 343.98, "tasa": 30.0},
        {"limite_inf": 3500.36, "limite_sup": 4667.13, "cuota": 844.05, "tasa": 32.0},
        {"limite_inf": 4667.14, "limite_sup": 14001.38, "cuota": 1217.42, "tasa": 34.0},
        {"limite_inf": 14001.39, "limite_sup": float('inf'), "cuota": 4391.07, "tasa": 35.0}],
    "Semanal": [{"limite_inf": 0.01, "limite_sup": 194.46, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 194.47, "limite_sup": 1650.67, "cuota": 3.71, "tasa": 6.4},
        {"limite_inf": 1650.68, "limite_sup": 2900.87, "cuota": 96.95, "tasa": 10.88},
        {"limite_inf": 2900.88, "limite_sup": 3372.11, "cuota": 232.96, "tasa": 16.0},
        {"limite_inf": 3372.12, "limite_sup": 4037.32, "cuota": 308.35, "tasa": 17.92},
        {"limite_inf": 4037.33, "limite_sup": 8142.75, "cuota": 427.56, "tasa": 21.36},
        {"limite_inf": 8142.76, "limite_sup": 12834.08, "cuota": 1304.45, "tasa": 23.52},
        {"limite_inf": 12834.09, "limite_sup": 24502.45, "cuota": 2407.86, "tasa": 30.0},
        {"limite_inf": 24502.46, "limite_sup": 32669.91, "cuota": 5908.35, "tasa": 32.0},
        {"limite_inf": 32669.92, "limite_sup": 98009.66, "cuota": 8521.94, "tasa": 34.0},
        {"limite_inf": 98009.67, "limite_sup": float('inf'), "cuota": 30737.49, "tasa": 35.0}],
    "Decenal": [{"limite_inf": 0.01, "limite_sup": 277.8, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 277.81, "limite_sup": 2358.10, "cuota": 5.3, "tasa": 6.4},
        {"limite_inf": 2358.11, "limite_sup": 4144.10, "cuota": 138.5, "tasa": 10.88},
        {"limite_inf": 4144.11, "limite_sup": 4817.30, "cuota": 332.8, "tasa": 16.0},
        {"limite_inf": 4817.31, "limite_sup": 5767.60, "cuota": 440.5, "tasa": 17.92},
        {"limite_inf": 5767.61, "limite_sup": 11632.50, "cuota": 610.8, "tasa": 21.36},
        {"limite_inf": 11632.51, "limite_sup": 18334.40, "cuota": 1863.50, "tasa": 23.52},
        {"limite_inf": 18334.41, "limite_sup": 35003.50, "cuota": 3439.80, "tasa": 30.0},
        {"limite_inf": 35003.51, "limite_sup": 46671.30, "cuota": 8440.50, "tasa": 32.0},
        {"limite_inf": 46671.31, "limite_sup": 140013.80, "cuota": 12174.20, "tasa": 34.0},
        {"limite_inf": 140013.81, "limite_sup": float('inf'), "cuota": 43910.70, "tasa": 35.0}],
    "Quincenal": [{"limite_inf": 0.01, "limite_sup": 416.7, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 416.71, "limite_sup": 3537.15, "cuota": 7.95, "tasa": 6.4},
        {"limite_inf": 3537.16, "limite_sup": 6216.15, "cuota": 207.75, "tasa": 10.88},
        {"limite_inf": 6216.16, "limite_sup": 7225.95, "cuota": 499.2, "tasa": 16.0},
        {"limite_inf": 7225.96, "limite_sup": 8651.40, "cuota": 660.75, "tasa": 17.92},
        {"limite_inf": 8651.41, "limite_sup": 17448.75, "cuota": 916.2, "tasa": 21.36},
        {"limite_inf": 17448.76, "limite_sup": 27501.60, "cuota": 2795.25, "tasa": 23.52},
        {"limite_inf": 27501.61, "limite_sup": 52505.25, "cuota": 5159.70, "tasa": 30.0},
        {"limite_inf": 52505.26, "limite_sup": 70006.95, "cuota": 12660.75, "tasa": 32.0},
        {"limite_inf": 70006.96, "limite_sup": 210020.70, "cuota": 18261.30, "tasa": 34.0},
        {"limite_inf": 210020.71, "limite_sup": float('inf'), "cuota": 65866.05, "tasa": 35.0}],
    "Mensual": [{"limite_inf": 0.01, "limite_sup": 844.59, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 844.60, "limite_sup": 7168.51, "cuota": 16.22, "tasa": 6.4},
        {"limite_inf": 7168.52, "limite_sup": 12598.02, "cuota": 420.95, "tasa": 10.88},
        {"limite_inf": 12598.03, "limite_sup": 14644.64, "cuota": 1011.68, "tasa": 16.0},
        {"limite_inf": 14644.65, "limite_sup": 17533.64, "cuota": 1339.14, "tasa": 17.92},
        {"limite_inf": 17533.65, "limite_sup": 35362.83, "cuota": 1856.84, "tasa": 21.36},
        {"limite_inf": 35362.84, "limite_sup": 55736.68, "cuota": 5665.16, "tasa": 23.52},
        {"limite_inf": 55736.69, "limite_sup": 106410.50, "cuota": 10457.09, "tasa": 30.0},
        {"limite_inf": 106410.51, "limite_sup": 141880.66, "cuota": 25659.23, "tasa": 32.0},
        {"limite_inf": 141880.67, "limite_sup": 425641.99, "cuota": 37009.69, "tasa": 34.0},
        {"limite_inf": 425642.00, "limite_sup": float('inf'), "cuota": 133488.54, "tasa": 35.0}]
}

def calcular_isr_progresivo(ingreso, periodo):
    tarifas = TARIFAS_ISR_2026.get(periodo, TARIFAS_ISR_2026["Mensual"])
    for tarifa in tarifas:
        if tarifa["limite_inf"] <= ingreso <= tarifa["limite_sup"]:
            return tarifa["cuota"] + ((ingreso - tarifa["limite_inf"]) * tarifa["tasa"] / 100)
    return 0

def calcular_precio(costo_base, porcentaje_utilidad, periodo_isr):
    utilidad_deseada = costo_base * (porcentaje_utilidad / 100)
    utilidad_ajustada = utilidad_deseada
    for _ in range(10):
        isr_calc = calcular_isr_progresivo(costo_base + utilidad_ajustada, periodo_isr)
        nuevo_val = utilidad_deseada + isr_calc
        if abs(nuevo_val - utilidad_ajustada) < 0.01:
            break
        utilidad_ajustada = nuevo_val
    
    subtotal = costo_base + utilidad_ajustada
    return {
        "precio_final": subtotal * 1.16,
        "subtotal": subtotal,
        "iva": subtotal * 0.16,
        "isr": calcular_isr_progresivo(subtotal, periodo_isr),
        "ganancia": utilidad_deseada
    }

st.title("💰 Calculadora de Costo Real - SAT 2026")
st.write("🇲🇽 ISR Progresivo (Art. 152 LISR) | IVA 16%")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📊 Normal", "🎯 Objetivo", "📈 Dinámica", "📉 Sensibilidad", "🛒 Multi", "⚖️ Equilibrio"])

# TAB 1: CÁLCULO NORMAL
with tab1:
    st.subheader("Cálculo Normal")
    c1, c2, c3 = st.columns(3)
    with c1:
        costo = st.number_input("💵 Costo ($)", value=700.0, step=10.0)
    with c2:
        util = st.number_input("📈 Utilidad (%)", value=30.0, step=1.0, max_value=200.0)
    with c3:
        periodo = st.selectbox("📅 Período", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4)
    
    res = calcular_precio(costo, util, periodo)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Precio Final", f"${res['precio_final']:,.2f}")
    m2.metric("Ganancia", f"${res['ganancia']:,.2f}")
    m3.metric("ISR", f"${res['isr']:,.2f}")
    m4.metric("IVA", f"${res['iva']:,.2f}")
    
    col_hist, col_share = st.columns(2)
    with col_hist:
        if st.button("💾 Guardar Historial"):
            st.session_state.historial.append({
                "fecha": datetime.now().strftime("%d/%m %H:%M"),
                "costo": costo, "util": util, "precio": res['precio_final']
            })
            st.success("✅ Guardado")
    
    with col_share:
        st.subheader("📱 Compartir")
        msg = f"Calculadora SAT: ${costo} → ${res['precio_final']:.2f}"
        c1, c2 = st.columns(2)
        with c1:
            wa = f"https://wa.me/?text={urllib.parse.quote(msg)}"
            st.markdown(f"[📲 WhatsApp]({wa})")
        with c2:
            em = f"mailto:?subject=Cálculo&body={urllib.parse.quote(msg)}"
            st.markdown(f"[✉️ Email]({em})")

# TAB 2: PRECIO OBJETIVO
with tab2:
    st.subheader("🎯 Inversor de Fórmula")
    st.write("Precio → Costo Base máximo")
    c1, c2, c3 = st.columns(3)
    with c1:
        precio_obj = st.number_input("💰 Precio deseado", value=1000.0, step=10.0, key="p_obj")
    with c2:
        util_obj = st.number_input("📈 Utilidad", value=30.0, step=1.0, key="u_obj", max_value=200.0)
    with c3:
        per_obj = st.selectbox("P", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4, key="per_obj")
    
    if st.button("🔄 Calcular"):
        costo_max = precio_obj / 1.16 * 0.6
        for _ in range(20):
            res_temp = calcular_precio(costo_max, util_obj, per_obj)
            if abs(res_temp['precio_final'] - precio_obj) < 1:
                break
            costo_max += (precio_obj - res_temp['precio_final']) / 2.16
        
        res_obj = calcular_precio(costo_max, util_obj, per_obj)
        st.metric("Costo Base Máximo", f"${costo_max:,.2f}")
        st.metric("Precio Resultante", f"${res_obj['precio_final']:,.2f}")

# TAB 3: TABLA DINÁMICA
with tab3:
    st.subheader("📈 Comparativo de Márgenes")
    c1, c2 = st.columns(2)
    with c1:
        costo_tabla = st.number_input("Costo", 700.0, step=10.0, key="t_costo")
    with c2:
        per_tabla = st.selectbox("Período", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4, key="t_per")
    
    datos = []
    for m in [10, 15, 20, 25, 30, 35, 40, 50]:
        r = calcular_precio(costo_tabla, m, per_tabla)
        datos.append({"Margen": f"{m}%", "Precio": f"${r['precio_final']:,.2f}", "Ganancia": f"${r['ganancia']:,.2f}", "ISR": f"${r['isr']:,.2f}"})
    
    st.dataframe(pd.DataFrame(datos), use_container_width=True, hide_index=True)

# TAB 4: SENSIBILIDAD
with tab4:
    st.subheader("📉 Análisis de Sensibilidad")
    c1, c2, c3 = st.columns(3)
    with c1:
        costo_sens = st.number_input("Costo", 700.0, step=10.0, key="s_costo")
    with c2:
        util_sens = st.number_input("Utilidad", 30.0, step=1.0, key="s_util", max_value=200.0)
    with c3:
        per_sens = st.selectbox("Período", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4, key="s_per")
    
    vars = [-20, -15, -10, -5, 0, 5, 10, 15, 20]
    precios = [calcular_precio(costo_sens * (1 + v/100), util_sens, per_sens)['precio_final'] for v in vars]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[f"{v:+d}%" for v in vars], y=precios, mode='lines+markers', 
        line=dict(color=COLORES['principal'], width=3), marker=dict(size=8)))
    fig.update_layout(title="Variación de Precio por Cambios en Costo", xaxis_title="Variación", yaxis_title="Precio ($)", height=400)
    st.plotly_chart(fig, use_container_width=True)

# TAB 5: MULTI-PRODUCTO
with tab5:
    st.subheader("🛒 Múltiples Productos")
    num = st.number_input("Cantidad", 1, 5, 2)
    
    datos_multi = []
    cols = st.columns(num)
    for i, col in enumerate(cols):
        with col:
            st.write(f"**Producto {i+1}**")
            c = st.number_input(f"Costo", 500+i*200, step=10.0, key=f"m_c{i}")
            u = st.number_input(f"Utilidad", 30.0, step=1.0, key=f"m_u{i}", max_value=200.0)
            datos_multi.append({"num": i+1, "costo": c, "util": u})
    
    per_multi = st.selectbox("Período", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4, key="m_per")
    
    if st.button("📊 Comparar"):
        tabla = []
        for p in datos_multi:
            r = calcular_precio(p["costo"], p["util"], per_multi)
            tabla.append({
                "Producto": f"#{p['num']}", "Costo": f"${p['costo']:,.2f}",
                "Precio": f"${r['precio_final']:,.2f}", "Ganancia": f"${r['ganancia']:,.2f}",
                "Margen": f"{(r['ganancia']/r['precio_final']*100):.1f}%"
            })
        st.dataframe(pd.DataFrame(tabla), use_container_width=True, hide_index=True)

# TAB 6: PUNTO EQUILIBRIO
with tab6:
    st.subheader("⚖️ Punto de Equilibrio")
    c1, c2 = st.columns(2)
    with c1:
        costo_eq = st.number_input("Costo", 700.0, step=10.0, key="eq_costo")
    with c2:
        per_eq = st.selectbox("Período", ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"], index=4, key="eq_per")
    
    res_eq = calcular_precio(costo_eq, 0, per_eq)
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Costo", f"${costo_eq:,.2f}")
    m2.metric("Precio Mínimo (P.E.)", f"${res_eq['precio_final']:,.2f}")
    m3.metric("ISR", f"${res_eq['isr']:,.2f}")
    
    st.success(f"🎯 Debes vender a mínimo **${res_eq['precio_final']:.2f}** para no perder")

# SIDEBAR HISTORIAL
with st.sidebar:
    st.subheader("📜 Historial")
    if st.session_state.historial:
        df_h = pd.DataFrame(st.session_state.historial)
        st.dataframe(df_h, use_container_width=True, hide_index=True)
        if st.button("🗑️ Limpiar"):
            st.session_state.historial = []
            st.rerun()
    else:
        st.info("Sin cálculos guardados")

st.divider()
st.markdown("📌 La información fiscal es orientativa. Consulta con tu contador.")
