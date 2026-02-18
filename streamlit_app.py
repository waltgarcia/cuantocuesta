import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Configurar página
st.set_page_config(
    page_title="Calculadora de Costos - Monterrey",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Calculadora de Costo Real del Producto")
st.write(
    "🇲🇽 Calcula el precio final de tu producto según regulaciones fiscales del SAT en México."
)

# Información fiscal de México
st.info(
    "📋 **Información Fiscal de México (SAT 2026)**\n"
    "- **IVA:** 16% (tasa general)\n"
    "- **ISR:** Varía según el régimen fiscal seleccionado\n\n"
    "⚠️ **Nota:** Esta calculadora es una herramienta orientativa. Consulta con tu contador o asesor fiscal para validar específicamente tu situación."
)

st.divider()

# Definir regímenes fiscales actualizados (SAT 2026)
regimenes_fiscales = {
    "RESICO (Régimen Simplificado de Contribuyentes)": {
        "isr": 2.7,
        "descripcion": "Régimen simplificado para pequeños negocios. ISR del 2.7% sobre ingresos netos. Vigente desde 2022.",
        "requisitos": "Ingresos anuales hasta $2,000,000. Actividades permitidas: comercio, servicios, manufactura, servicios profesionales.",
        "ventajas": "Menor carga fiscal, cálculo simple, ideal para PYMES, opción más popular.",
        "color": "🟢"
    },
    "Régimen General de Ley (Personas Morales)": {
        "isr": 30.0,
        "descripcion": "Régimen tradicional para empresas constituidas. ISR del 30% basado en utilidad neta con deducibilidad de gastos.",
        "requisitos": "Para empresas (personas morales) de cualquier tamaño. Requiere registro contable detallado y comprobantes.",
        "ventajas": "Deducción de todos los gastos operativos, mayor flexibilidad fiscal, ideal para empresas grandes.",
        "color": "🔵"
    },
    "Personas Físicas con Actividad Empresarial": {
        "isr": 20.0,
        "descripcion": "Para profesionales independientes y negocios sin constituir empresa. ISR con tasas progresivas (estimado 20% promedio).",
        "requisitos": "Personas físicas que realizan actividades empresariales. Requiere facturación y comprobantes.",
        "ventajas": "Flexible para emprendedores, permite deducir gastos relacionados.",
        "color": "🟡"
    },
}

# Selección de régimen fiscal
st.subheader("🏢 Selecciona tu régimen fiscal")

regimen_seleccionado = st.radio(
    "¿Cuál es tu régimen fiscal?",
    list(regimenes_fiscales.keys()),
    index=0,  # RESICO por defecto
    horizontal=False
)

# Mostrar información detallada del régimen seleccionado
regimen_info = regimenes_fiscales[regimen_seleccionado]
tasa_isr = regimen_info["isr"]

col1, col2 = st.columns(2)

with col1:
    st.metric("Régimen seleccionado", regimen_seleccionado.split("(")[0].strip())

with col2:
    st.metric("Tasa ISR", f"{tasa_isr}%")

# Mostrar detalles del régimen en un expander
with st.expander(f"ℹ️ Información detallada del régimen", expanded=True):
    st.write(f"**{regimen_info['color']} Descripción:**")
    st.write(regimen_info['descripcion'])
    
    st.write(f"\n**Requisitos:**")
    st.write(regimen_info['requisitos'])
    
    st.write(f"\n**Ventajas:**")
    st.write(regimen_info['ventajas'])

st.divider()

# Tasas fijas según regulaciones SAT
tasa_iva = 16.0  # IVA fijo en México
tasa_isr_decimal = tasa_isr / 100
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
st.write(f"- **Régimen fiscal:** {regimen_seleccionado}")
st.write(f"- **Tasa ISR:** {tasa_isr}%")
st.write(f"- **Tasa IVA (SAT):** {tasa_iva}%")

st.divider()

# Realizar cálculos automáticamente
# Convertir porcentajes a decimales
utilidad_pct = porcentaje_utilidad / 100

# Paso 1: Calcular utilidad deseada inicial
utilidad_deseada = costo_base * utilidad_pct

# Paso 2: Ajustar utilidad por ISR
utilidad_ajustada = utilidad_deseada / (1 - tasa_isr_decimal)

# Paso 3: Calcular subtotal (precio sin IVA)
subtotal = costo_base + utilidad_ajustada

# Paso 4: Calcular IVA
iva = subtotal * iva_decimal

# Paso 5: Calcular precio final
precio_final = subtotal + iva

# Mostrar desglose de cálculos
st.success("✅ Cálculo realizado automáticamente")

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
st.write("**Paso 2: Utilidad y ajuste por ISR**")
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"Utilidad deseada ({porcentaje_utilidad}%)")
with col2:
    st.write(f"${utilidad_deseada:,.2f}")

col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"Utilidad ajustada por ISR ({tasa_isr}%)")
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

# Calcular ISR a pagar
isr_a_pagar = utilidad_ajustada - utilidad_deseada

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Utilidad neta deseada", f"${utilidad_deseada:,.2f}")

with col2:
    st.metric("ISR a pagar", f"${isr_a_pagar:,.2f}")

with col3:
    st.metric("IVA recaudado", f"${iva:,.2f}")

st.divider()

# Visualizaciones del desglose de costos
st.subheader("📊 Visualización del desglose de costos")

# Datos para los gráficos
componentes = ["Costo Base", "Utilidad (Ganancia)", "ISR (Impuesto)", "IVA (Impuesto)"]
montos = [costo_base, utilidad_deseada, isr_a_pagar, iva]
colores = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12"]

# Crear dos columnas para los gráficos
col_pie, col_bar = st.columns(2)

with col_pie:
    # Gráfico de pastel
    fig_pie = go.Figure(data=[go.Pie(
        labels=componentes,
        values=montos,
        marker=dict(colors=colores),
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Monto: $%{value:,.2f}<br>Porcentaje: %{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        title="Composición del Precio Final",
        height=450,
        font=dict(size=11),
        showlegend=True
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with col_bar:
    # Gráfico de barras
    fig_bar = go.Figure(data=[
        go.Bar(
            x=componentes,
            y=montos,
            marker=dict(color=colores),
            text=[f"${monto:,.2f}" for monto in montos],
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>Monto: $%{y:,.2f}<extra></extra>'
        )
    ])
    
    fig_bar.update_layout(
        title="Desglose de Costos en Dinero",
        xaxis_title="Componentes",
        yaxis_title="Monto ($)",
        height=450,
        showlegend=False,
        hovermode='x unified'
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
        f"${utilidad_deseada:,.2f}",
        f"${isr_a_pagar:,.2f}",
        f"${subtotal:,.2f}",
        f"${iva:,.2f}",
        f"${precio_final:,.2f}"
    ],
    "Porcentaje del Precio Final": [
        f"{(costo_base/precio_final)*100:.1f}%",
        f"{(utilidad_deseada/precio_final)*100:.1f}%",
        f"{(isr_a_pagar/precio_final)*100:.1f}%",
        f"{(subtotal/precio_final)*100:.1f}%",
        f"{(iva/precio_final)*100:.1f}%",
        "100%"
    ]
}

st.dataframe(desglose_data, use_container_width=True, hide_index=True)

st.divider()

resumen_final = (
    f"El precio final de ${precio_final:,.2f} te permite obtener "
    f"una ganancia neta de ${utilidad_deseada:,.2f} después de pagar el ISR "
    f"bajo el régimen {regimen_seleccionado.split('(')[0].strip()}.\n\n"
    f"Esta calculadora está optimizada para contribuyentes del SAT en México."
)
st.info(f"📌 **Resumen:** {resumen_final}")
