import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Configurar página
st.set_page_config(
    page_title="Calculadora de Costos - Monterrey",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Paleta de colores moderna y profesional
COLORES = {
    "principal": "#1f77b4",      # Azul profesional
    "utilidad": "#2ca02c",        # Verde éxito
    "isr": "#d62728",             # Rojo impuesto
    "iva": "#ff7f0e",             # Naranja cálido
    "fondo": "#f8f9fa",           # Gris muy claro
    "texto": "#1a1a1a",           # Negro/Gris oscuro
    "acento": "#00d4ff"           # Cyan brillante
}

# CSS personalizado para mejor presentación
st.markdown(f"""
    <style>
    .main {{
        background-color: {COLORES['fondo']};
    }}
    .metric-card {{
        padding: 20px;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("💰 Calculadora de Costo Real del Producto")
st.write(
    "🇲🇽 Calcula el precio final de tu producto o servicio según regulaciones fiscales del SAT en México.\n"
    "Optimizada para empresas y profesionales independientes que requieren afianzar sus costos operativos."
)

# Información fiscal de México
st.info(
    "📋 **Información Fiscal de México (SAT 2026)**\n"
    "- **IVA:** 16% (tasa general)\n"
    "- **ISR:** Tarifas progresivas según ingreso (actualizadas Art. 152 LISR)\n\n"
    "⚠️ **Nota:** Esta calculadora es una herramienta orientativa. Consulta con tu contador o asesor fiscal para validar específicamente tu situación."
)

# Tarifas ISR 2026 - Artículo 152 LISR
# Tarifas actualizadas conforme a la inflación acumulada que superó el 10%

TARIFAS_ISR_2026 = {
    "Diaria": [
        {"limite_inf": 0.01, "limite_sup": 27.78, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 27.79, "limite_sup": 235.81, "cuota": 0.53, "tasa": 6.4},
        {"limite_inf": 235.82, "limite_sup": 414.41, "cuota": 13.85, "tasa": 10.88},
        {"limite_inf": 414.42, "limite_sup": 481.73, "cuota": 33.28, "tasa": 16.0},
        {"limite_inf": 481.74, "limite_sup": 576.76, "cuota": 44.05, "tasa": 17.92},
        {"limite_inf": 576.77, "limite_sup": 1163.25, "cuota": 61.08, "tasa": 21.36},
        {"limite_inf": 1163.26, "limite_sup": 1833.44, "cuota": 186.35, "tasa": 23.52},
        {"limite_inf": 1833.45, "limite_sup": 3500.35, "cuota": 343.98, "tasa": 30.0},
        {"limite_inf": 3500.36, "limite_sup": 4667.13, "cuota": 844.05, "tasa": 32.0},
        {"limite_inf": 4667.14, "limite_sup": 14001.38, "cuota": 1217.42, "tasa": 34.0},
        {"limite_inf": 14001.39, "limite_sup": float('inf'), "cuota": 4391.07, "tasa": 35.0},
    ],
    "Semanal": [
        {"limite_inf": 0.01, "limite_sup": 194.46, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 194.47, "limite_sup": 1650.67, "cuota": 3.71, "tasa": 6.4},
        {"limite_inf": 1650.68, "limite_sup": 2900.87, "cuota": 96.95, "tasa": 10.88},
        {"limite_inf": 2900.88, "limite_sup": 3372.11, "cuota": 232.96, "tasa": 16.0},
        {"limite_inf": 3372.12, "limite_sup": 4037.32, "cuota": 308.35, "tasa": 17.92},
        {"limite_inf": 4037.33, "limite_sup": 8142.75, "cuota": 427.56, "tasa": 21.36},
        {"limite_inf": 8142.76, "limite_sup": 12834.08, "cuota": 1304.45, "tasa": 23.52},
        {"limite_inf": 12834.09, "limite_sup": 24502.45, "cuota": 2407.86, "tasa": 30.0},
        {"limite_inf": 24502.46, "limite_sup": 32669.91, "cuota": 5908.35, "tasa": 32.0},
        {"limite_inf": 32669.92, "limite_sup": 98009.66, "cuota": 8521.94, "tasa": 34.0},
        {"limite_inf": 98009.67, "limite_sup": float('inf'), "cuota": 30737.49, "tasa": 35.0},
    ],
    "Decenal": [
        {"limite_inf": 0.01, "limite_sup": 277.8, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 277.81, "limite_sup": 2358.10, "cuota": 5.3, "tasa": 6.4},
        {"limite_inf": 2358.11, "limite_sup": 4144.10, "cuota": 138.5, "tasa": 10.88},
        {"limite_inf": 4144.11, "limite_sup": 4817.30, "cuota": 332.8, "tasa": 16.0},
        {"limite_inf": 4817.31, "limite_sup": 5767.60, "cuota": 440.5, "tasa": 17.92},
        {"limite_inf": 5767.61, "limite_sup": 11632.50, "cuota": 610.8, "tasa": 21.36},
        {"limite_inf": 11632.51, "limite_sup": 18334.40, "cuota": 1863.50, "tasa": 23.52},
        {"limite_inf": 18334.41, "limite_sup": 35003.50, "cuota": 3439.80, "tasa": 30.0},
        {"limite_inf": 35003.51, "limite_sup": 46671.30, "cuota": 8440.50, "tasa": 32.0},
        {"limite_inf": 46671.31, "limite_sup": 140013.80, "cuota": 12174.20, "tasa": 34.0},
        {"limite_inf": 140013.81, "limite_sup": float('inf'), "cuota": 43910.70, "tasa": 35.0},
    ],
    "Quincenal": [
        {"limite_inf": 0.01, "limite_sup": 416.7, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 416.71, "limite_sup": 3537.15, "cuota": 7.95, "tasa": 6.4},
        {"limite_inf": 3537.16, "limite_sup": 6216.15, "cuota": 207.75, "tasa": 10.88},
        {"limite_inf": 6216.16, "limite_sup": 7225.95, "cuota": 499.2, "tasa": 16.0},
        {"limite_inf": 7225.96, "limite_sup": 8651.40, "cuota": 660.75, "tasa": 17.92},
        {"limite_inf": 8651.41, "limite_sup": 17448.75, "cuota": 916.2, "tasa": 21.36},
        {"limite_inf": 17448.76, "limite_sup": 27501.60, "cuota": 2795.25, "tasa": 23.52},
        {"limite_inf": 27501.61, "limite_sup": 52505.25, "cuota": 5159.70, "tasa": 30.0},
        {"limite_inf": 52505.26, "limite_sup": 70006.95, "cuota": 12660.75, "tasa": 32.0},
        {"limite_inf": 70006.96, "limite_sup": 210020.70, "cuota": 18261.30, "tasa": 34.0},
        {"limite_inf": 210020.71, "limite_sup": float('inf'), "cuota": 65866.05, "tasa": 35.0},
    ],
    "Mensual": [
        {"limite_inf": 0.01, "limite_sup": 844.59, "cuota": 0, "tasa": 1.92},
        {"limite_inf": 844.60, "limite_sup": 7168.51, "cuota": 16.22, "tasa": 6.4},
        {"limite_inf": 7168.52, "limite_sup": 12598.02, "cuota": 420.95, "tasa": 10.88},
        {"limite_inf": 12598.03, "limite_sup": 14644.64, "cuota": 1011.68, "tasa": 16.0},
        {"limite_inf": 14644.65, "limite_sup": 17533.64, "cuota": 1339.14, "tasa": 17.92},
        {"limite_inf": 17533.65, "limite_sup": 35362.83, "cuota": 1856.84, "tasa": 21.36},
        {"limite_inf": 35362.84, "limite_sup": 55736.68, "cuota": 5665.16, "tasa": 23.52},
        {"limite_inf": 55736.69, "limite_sup": 106410.50, "cuota": 10457.09, "tasa": 30.0},
        {"limite_inf": 106410.51, "limite_sup": 141880.66, "cuota": 25659.23, "tasa": 32.0},
        {"limite_inf": 141880.67, "limite_sup": 425641.99, "cuota": 37009.69, "tasa": 34.0},
        {"limite_inf": 425642.00, "limite_sup": float('inf'), "cuota": 133488.54, "tasa": 35.0},
    ]
}

def calcular_isr_progresivo(ingreso, periodo):
    """
    Calcula el ISR según tarifas progresivas 2026 (Art. 152 LISR)
    
    Args:
        ingreso: Monto del ingreso a gravar
        periodo: "Diaria", "Semanal", "Decenal", "Quincenal" o "Mensual"
    
    Returns:
        Monto de ISR a pagar
    """
    tarifas = TARIFAS_ISR_2026.get(periodo, TARIFAS_ISR_2026["Mensual"])
    
    for tarifa in tarifas:
        if tarifa["limite_inf"] <= ingreso <= tarifa["limite_sup"]:
            isr = tarifa["cuota"] + ((ingreso - tarifa["limite_inf"]) * tarifa["tasa"] / 100)
            return isr
    
    return 0

st.divider()

# Selección de período de cálculo para tarifas progresivas
st.subheader("📅 Configuración fiscal")

col1, col2 = st.columns(2)

with col1:
    periodo_isr = st.selectbox(
        "Período de cálculo ISR (Art. 152 LISR):",
        ["Diaria", "Semanal", "Decenal", "Quincenal", "Mensual"],
        index=4,  # Mensual por defecto
        help="Tarifas progresivas actualizadas conforme a inflación acumulada >10%"
    )

with col2:
    st.metric("Período seleccionado", periodo_isr)

# Mostrar información sobre las tarifas progresivas
with st.expander("ℹ️ Información sobre tarifas ISR 2026 (Art. 152 LISR)"):
    st.write(
        """
        Estas tarifas se actualizaron conforme a lo previsto en el artículo 152 de la **Ley del ISR (LISR)**, 
        que contempla un ajuste cada vez que la inflación sobrepasa un **10%**.
        
        **Las tarifas varían según:**
        - Tu ingreso total
        - El período fiscal (diario, semanal, decenal, quincenal o mensual)
        
        **Sistema progresivo:**
        - Cuota fija + porcentaje sobre el excedente del límite inferior
        - Mayor ingreso = mayor tasa de impuesto
        """
    )
    
    # Mostrar tabla de la tarifa seleccionada
    st.write(f"\n**Tabla de Tarifa {periodo_isr} ISR 2026:**")
    
    tarifas_df = pd.DataFrame(TARIFAS_ISR_2026[periodo_isr])
    
    # Formatear para mostrar
    tarifas_display = tarifas_df.copy()
    tarifas_display["limite_inf"] = tarifas_display["limite_inf"].apply(lambda x: f"${x:,.2f}")
    tarifas_display["limite_sup"] = tarifas_display["limite_sup"].apply(
        lambda x: "En adelante" if x == float('inf') else f"${x:,.2f}"
    )
    tarifas_display["cuota"] = tarifas_display["cuota"].apply(lambda x: f"${x:,.2f}")
    tarifas_display["tasa"] = tarifas_display["tasa"].apply(lambda x: f"{x}%")
    
    tarifas_display.columns = ["Límite Inferior", "Límite Superior", "Cuota Fija", "% Sobre Excedente"]
    
    st.dataframe(tarifas_display, use_container_width=True, hide_index=True)

st.divider()

# Tasas según regulaciones SAT de México 2026
tasa_iva = 16.0  # IVA fijo en México
iva_decimal = tasa_iva / 100

# Crear columnas para entrada de datos
col1, col2 = st.columns(2)

with col1:
    # Paso 1: Costo base
    costo_base = st.number_input(
        "💵 Costo base del producto ($)",
        min_value=0.0,
        value=700.0,
        step=10.0,
        format="%.2f"
    )

with col2:
    # Porcentaje de utilidad deseada
    porcentaje_utilidad = st.number_input(
        "📈 Porcentaje de utilidad deseado (%)",
        min_value=0.0,
        max_value=200.0,
        value=30.0,
        step=1.0,
        format="%.1f"
    )

st.divider()

st.write("**ℹ️ Información de cálculo:**")
st.write(f"- **Período de cálculo ISR:** {periodo_isr}")
st.write(f"- **Tasa IVA (SAT):** {tasa_iva}%")
st.write("- **Sistema ISR:** Tarifas progresivas conforme Art. 152 LISR")

st.divider()

# Realizar cálculos automáticamente
utilidad_pct = porcentaje_utilidad / 100

# Paso 1: Calcular utilidad deseada inicial
utilidad_deseada = costo_base * utilidad_pct

# Paso 2: Usar método iterativo para encontrar la utilidad ajustada por ISR progresivo
# Como ISR es progresivo, necesitamos iterar hasta converger
utilidad_ajustada = utilidad_deseada
for _ in range(10):  # Iteraciones para convergencia
    subtotal_temp = costo_base + utilidad_ajustada
    isr_calculado = calcular_isr_progresivo(subtotal_temp, periodo_isr)
    utilidad_ajustada_nueva = utilidad_deseada + isr_calculado
    
    # Si la diferencia es mínima, convergimos
    if abs(utilidad_ajustada_nueva - utilidad_ajustada) < 0.01:
        break
    utilidad_ajustada = utilidad_ajustada_nueva

# Paso 3: Calcular subtotal (precio sin IVA)
subtotal = costo_base + utilidad_ajustada

# Paso 4: Calcular ISR final
isr_a_pagar = calcular_isr_progresivo(subtotal, periodo_isr)

# Paso 5: Calcular IVA
iva = subtotal * iva_decimal

# Paso 6: Calcular precio final
precio_final = subtotal + iva

# Mostrar desglose de cálculos
st.success("✅ Cálculo realizado automáticamente con tarifas progresivas ISR 2026")

st.subheader("📋 Desglose detallado:")

st.divider()

# Paso 1
st.write("**Paso 1: Costo base**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Costo de producción")
with col2:
    st.write(f"${costo_base:,.2f}")

st.divider()

# Paso 2
st.write("**Paso 2: Utilidad y ajuste por ISR progresivo**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"Utilidad deseada ({porcentaje_utilidad}%)")
with col2:
    st.write(f"${utilidad_deseada:,.2f}")

col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"Ajuste por ISR (Tarifa {periodo_isr})")
with col2:
    st.write(f"${isr_a_pagar:,.2f}")

col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"Utilidad ajustada")
with col2:
    st.write(f"${utilidad_ajustada:,.2f}")

st.divider()

# Paso 3
st.write("**Paso 3: Subtotal (precio sin IVA)**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Costo + Utilidad ajustada")
with col2:
    st.write(f"${subtotal:,.2f}")

st.divider()

# Paso 4
st.write("**Paso 4: Impuesto al Valor Agregado (IVA)**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"IVA ({tasa_iva}% del subtotal)")
with col2:
    st.write(f"${iva:,.2f}")

st.divider()

# Paso 5 - Resultado final
st.write("**Paso 5: PRECIO FINAL AL PÚBLICO**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("**Subtotal + IVA**")
with col2:
    st.metric(label="", value=f"${precio_final:,.2f}")

st.divider()

# Resumen de ganancia neta
st.subheader("💵 Resumen de ganancias:")

ganancia_neta = utilidad_deseada

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Utilidad neta deseada", f"${ganancia_neta:,.2f}")

with col2:
    st.metric("ISR a pagar", f"${isr_a_pagar:,.2f}")

with col3:
    st.metric("IVA recaudado", f"${iva:,.2f}")

st.divider()

# Visualizaciones del desglose de costos
st.subheader("📊 Visualización del desglose de costos")

# Datos para los gráficos con paleta de colores moderna
componentes = ["Costo Base", "Utilidad (Ganancia)", "ISR (Impuesto)", "IVA (Impuesto)"]
montos = [costo_base, ganancia_neta, isr_a_pagar, iva]
colores = [COLORES["principal"], COLORES["utilidad"], COLORES["isr"], COLORES["iva"]]

# Crear dos columnas para los gráficos
col_pie, col_bar = st.columns(2)

with col_pie:
    # Gráfico de pastel con colores modernos
    fig_pie = go.Figure(data=[go.Pie(
        labels=componentes,
        values=montos,
        marker=dict(
            colors=colores,
            line=dict(color='white', width=2)
        ),
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Monto: $%{value:,.2f}<br>Porcentaje: %{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        title="Composición del Precio Final",
        height=450,
        font=dict(size=11, family="Arial"),
        showlegend=True,
        paper_bgcolor='rgba(248, 249, 250, 0.5)',
        plot_bgcolor='rgba(248, 249, 250, 0.5)',
        hovermode='closest'
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with col_bar:
    # Gráfico de barras con colores modernos
    fig_bar = go.Figure(data=[
        go.Bar(
            x=componentes,
            y=montos,
            marker=dict(
                color=colores,
                line=dict(color='white', width=2)
            ),
            text=[f"${monto:,.2f}" for monto in montos],
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>Monto: $%{y:,.2f}<extra></extra>',
            showlegend=False
        )
    ])
    
    fig_bar.update_layout(
        title="Desglose de Costos en Dinero",
        xaxis_title="Componentes",
        yaxis_title="Monto ($)",
        height=450,
        showlegend=False,
        hovermode='x unified',
        paper_bgcolor='rgba(248, 249, 250, 0.5)',
        plot_bgcolor='rgba(248, 249, 250, 0.5)',
        font=dict(size=11, family="Arial"),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray'
        )
    )
    
    fig_bar.update_xaxes(tickangle=-45)
    
    st.plotly_chart(fig_bar, use_container_width=True)

# Tabla de desglose detallado
st.subheader("📈 Tabla de desglose detallado")

desglose_data = {
    "Componente": [
        "Costo Base",
        "Utilidad Deseada",
        "ISR a Pagar",
        "Subtotal (sin IVA)",
        "IVA",
        "Precio Final"
    ],
    "Monto": [
        f"${costo_base:,.2f}",
        f"${ganancia_neta:,.2f}",
        f"${isr_a_pagar:,.2f}",
        f"${subtotal:,.2f}",
        f"${iva:,.2f}",
        f"${precio_final:,.2f}"
    ],
    "Porcentaje del Precio Final": [
        f"{(costo_base/precio_final)*100:.1f}%",
        f"{(ganancia_neta/precio_final)*100:.1f}%",
        f"{(isr_a_pagar/precio_final)*100:.1f}%",
        f"{(subtotal/precio_final)*100:.1f}%",
        f"{(iva/precio_final)*100:.1f}%",
        "100%"
    ]
}

st.dataframe(desglose_data, use_container_width=True, hide_index=True)

st.divider()

resumen_final = f"El precio final de ${precio_final:,.2f} te permite obtener una ganancia neta de ${ganancia_neta:,.2f} después de pagar el ISR de ${isr_a_pagar:,.2f} calculado con tarifas progresivas de la tarifa {periodo_isr}.\n\nEsta calculadora está optimizada para pequeños y medianos negocios, profesionales independientes y empresas que venden productos o servicios en México, utilizando las tarifas actualizadas conforme al Art. 152 LISR."
st.info(f"📌 Resumen:\n{resumen_final}")
