import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(
    page_title="AI House Price Predictor",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Premium Custom CSS ---
st.markdown("""
<style>
    /* Dark mode background with deep elegant radial gradient */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #2e1065 0%, #0f172a 50%, #020617 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sleek Sidebar with Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Typography */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 50%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        text-align: center;
        letter-spacing: -1px;
    }
    
    .sub-header {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 3rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 500;
    }

    /* Floating Metric Cards */
    .metric-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 24px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 40px -10px rgba(0,0,0,0.7);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px -10px rgba(56, 189, 248, 0.2);
        border: 1px solid rgba(56, 189, 248, 0.4);
        background: rgba(30, 41, 59, 0.6);
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 15px;
        display: block;
    }
    
    .metric-title {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .metric-value {
        color: #f8fafc;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 0 20px rgba(255,255,255,0.1);
    }
    
    .metric-sub {
        color: #10b981;
        font-size: 0.9rem;
        margin-top: 8px;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
    }
    
    .metric-sub.negative {
        color: #f43f5e;
    }

    /* Slider Track Glow */
    .stSlider > div > div > div {
        background: linear-gradient(to right, #00f2fe, #4facfe) !important;
        box-shadow: 0 0 10px rgba(79, 172, 254, 0.5);
    }
    
    /* Separator Line */
    hr {
        border-color: rgba(255,255,255,0.05) !important;
        margin: 3rem 0;
    }
</style>
""", unsafe_allow_html=True)


# --- Load Model ---
@st.cache_resource
def load_model():
    model_path = "model.joblib"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

model = load_model()

# --- Stat Constants ---
CITY_AVERAGES = {
    'Price': 6500000,
    'Sqft': 2500,
    'Bedrooms': 3,
    'Bathrooms': 2,
    'Age': 20,
    'PricePerSqft': 2600
}

# --- Sidebar Inputs ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/256/1A6DFF/C822FF/real-estate.png", width=80)
    st.markdown("<h2 style='margin-top:0;'>Property Specs</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.9rem;'>Use the controls below to configure the parameters for the AI valuation engine.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    sqft = st.slider("📐 Square Footage", min_value=500, max_value=5000, value=2500, step=50)
    bedrooms = st.slider("🛏️ Bedrooms", min_value=1, max_value=6, value=3, step=1)
    bathrooms = st.slider("🚿 Bathrooms", min_value=1, max_value=5, value=2, step=1)
    age = st.slider("🏛️ Property Age (Years)", min_value=0, max_value=50, value=5, step=1)
    
    st.markdown("<br><hr style='margin: 1rem 0;'>", unsafe_allow_html=True)
    
    if model:
        st.markdown("<div style='background:rgba(16,185,129,0.1); border:1px solid #10b981; border-radius:10px; padding:10px; color:#10b981; text-align:center; font-weight:600;'>🟢 ML Engine Online</div>", unsafe_allow_html=True)
    else:
        st.error("❌ Model offline. Run generate_and_train.py")

# --- Header ---
st.markdown("<div class='main-header'>AI House Price Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Real-time predictive pricing based on advanced market analysis</div>", unsafe_allow_html=True)

if not model:
    st.warning("⚠️ Please train the model first by running `python generate_and_train.py`.")
    st.stop()
    
# --- Prediction Logic ---
input_features = [[sqft, bedrooms, bathrooms, age]]
predicted_price = model.predict(input_features)[0]

# Calculate derived metrics
price_per_sqft = predicted_price / sqft
# Simple mortgage calc (5.5% over 30 years, 20% down)
loan_amount = predicted_price * 0.8
monthly_rate = 0.055 / 12
num_payments = 30 * 12
monthly_mortgage = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

# Comparatives
price_diff = predicted_price - CITY_AVERAGES['Price']
price_diff_pct = (price_diff / CITY_AVERAGES['Price']) * 100
is_premium = price_diff > 0

# --- Top Main Visual: Gauge Chart ---
# A massive, beautiful gauge chart taking the center stage 
fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=predicted_price,
    domain={'x': [0, 1], 'y': [0, 1]},
    number={'prefix': "₹ ", 'valueformat': ",.0f", 'font': {'size': 60, 'color': '#ffffff', 'family': 'Inter'}},
    delta={'reference': CITY_AVERAGES['Price'], 'increasing': {'color': "#10b981"}, 'decreasing': {'color': "#f43f5e"}, 'position': "top"},
    gauge={
        'axis': {'range': [None, 15000000], 'tickwidth': 2, 'tickcolor': "#334155", 'tickfont': {'color': '#94a3b8'}},
        'bar': {'color': "rgba(0, 242, 254, 0.8)", 'thickness': 0.8},
        'bgcolor': "rgba(15, 23, 42, 0.4)",
        'borderwidth': 0,
        'steps': [
            {'range': [0, CITY_AVERAGES['Price']], 'color': "rgba(51, 65, 85, 0.3)"},
            {'range': [CITY_AVERAGES['Price'], 15000000], 'color': "rgba(51, 65, 85, 0.1)"}
        ],
        'threshold': {
            'line': {'color': "#a78bfa", 'width': 4},
            'thickness': 0.75,
            'value': CITY_AVERAGES['Price']
        }
    }
))

fig_gauge.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#e2e8f0', family='Inter'),
    height=400,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig_gauge, use_container_width=True)

# --- Secondary Metrics Row ---
col1, col2, col3 = st.columns(3)

with col1:
    trend_color = "" if is_premium else "negative"
    trend_icon = "↗️" if is_premium else "↘️"
    trend_text = f"{abs(price_diff_pct):.1f}% vs City Avg"
    
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-icon">🏢</span>
        <div class="metric-title">Market Positioning</div>
        <div class="metric-value">{'Premium' if is_premium else 'Value'} Tier</div>
        <div class="metric-sub {trend_color}">{trend_icon} {trend_text}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    psq_diff_pct = ((price_per_sqft - CITY_AVERAGES['PricePerSqft']) / CITY_AVERAGES['PricePerSqft']) * 100
    psq_color = "" if psq_diff_pct > 0 else "negative"
    psq_icon = "↗️" if psq_diff_pct > 0 else "↘️"
    
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-icon">📐</span>
        <div class="metric-title">Value per Sqft</div>
        <div class="metric-value">₹ {price_per_sqft:,.0f}</div>
        <div class="metric-sub {psq_color}">{psq_icon} {abs(psq_diff_pct):.1f}% vs City Avg</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-icon">🏦</span>
        <div class="metric-title">Est. Monthly Mortgage</div>
        <div class="metric-value">₹ {monthly_mortgage:,.0f}</div>
        <div class="metric-sub">Assuming 20% down, 5.5% APR</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Bottom Charts ---
st.markdown("<h3 style='text-align:center; color:#e2e8f0; margin-bottom: 2rem;'>Property Profile Analysis</h3>", unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns([3, 2])

with chart_col1:
    # Beautiful smoothed line chart simulating price history/forecast
    # Create fake historical projection based on current valuation
    years = list(range(2020, 2029))
    base_val = predicted_price * 0.75 # Assume 25% appreciation since 2020
    growth_rates = [1.05, 1.08, 1.12, 1.03, 1.0, 1.06, 1.04, 1.05, 1.04] # Cumulative modifiers leading to current
    
    history_vals = []
    current_val = base_val
    for i, rate in enumerate(growth_rates):
        if years[i] == 2025: # Current year anchor
            history_vals.append(predicted_price)
            current_val = predicted_price
        elif years[i] > 2025:
            current_val *= rate
            history_vals.append(current_val)
        else:
            current_val *= rate
            history_vals.append(current_val)

    fig_line = go.Figure()
    
    # Historical
    fig_line.add_trace(go.Scatter(
        x=years[:6], y=history_vals[:6],
        mode='lines+markers',
        name='Historical Value',
        line=dict(color='#00f2fe', width=4, shape='spline'),
        marker=dict(size=8, color='#0f172a', line=dict(width=2, color='#00f2fe')),
        fill='tozeroy',
        fillcolor='rgba(0, 242, 254, 0.1)'
    ))
    
    # Forecast
    fig_line.add_trace(go.Scatter(
        x=years[5:], y=history_vals[5:],
        mode='lines',
        name='Forecasted Trend',
        line=dict(color='#a78bfa', width=4, shape='spline', dash='dot')
    ))

    fig_line.update_layout(
        title="10-Year Valuation Trajectory",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        hovermode="x unified",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', zeroline=False),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig_line, use_container_width=True)

with chart_col2:
    # Radar Chart
    categories = ['Space (Sqft)', 'Bedrooms', 'Bathrooms', 'Newness']
    norm_pred = [sqft/5000, bedrooms/6, bathrooms/5, (50-age)/50]
    norm_avg = [CITY_AVERAGES['Sqft']/5000, CITY_AVERAGES['Bedrooms']/6, CITY_AVERAGES['Bathrooms']/5, (50-CITY_AVERAGES['Age'])/50]
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=norm_pred,
        theta=categories,
        fill='toself',
        name='This Property',
        line_color='#00f2fe',
        fillcolor='rgba(0, 242, 254, 0.4)'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=norm_avg,
        theta=categories,
        fill='toself',
        name='Market Average',
        line_color='#64748b',
        fillcolor='rgba(100, 116, 139, 0.2)'
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=False, range=[0, 1]),
            bgcolor='rgba(15,23,42,0.4)'
        ),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        margin=dict(l=30, r=30, t=30, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: rgba(255,255,255,0.3); font-size: 0.8rem; letter-spacing: 1px;'>"
    "Created by Jaswanth Chennu with Antigravity<br><br>"

    "</div>", 
    unsafe_allow_html=True
)
