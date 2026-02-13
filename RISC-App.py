import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------------------
# Configuration & Style
# -----------------------------------------------
st.set_page_config(
    page_title="RISC: The Resilience Paradox",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌱"
)

# Sustainability-themed CSS
st.markdown("""
<style>
    /* Main sustainability theme colors */
    :root {
        --primary-green: #2ecc71;
        --dark-green: #27ae60;
        --danger-red: #e74c3c;
        --warning-amber: #f39c12;
        --earth-brown: #8b6f47;
        --sky-blue: #3498db;
        --background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
    }

    /* Background with subtle sustainability gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
    }

    /* Enhanced metric cards */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.1);
        border-left: 4px solid #2ecc71;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(46, 204, 113, 0.2);
    }

    /* Headers with sustainability accent */
    h1, h2, h3 {
        color: #27ae60;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    /* Comprehensive text visibility rules with high specificity */
    body .main, body .main * {
        color: #2c3e50 !important;
    }

    /* Streamlit specific elements */
    body .main .stMarkdown, body .main .stMarkdown * {
        color: #2c3e50 !important;
    }

    /* All text elements */
    body .main p, body .main li, body .main span, body .main div, body .main label, body .main h4, body .main h5, body .main h6 {
        color: #2c3e50 !important;
    }

    /* Target all divs with content */
    body .main div[style] {
        color: #2c3e50 !important;
    }

    /* Metric components */
    .main [data-testid="stMetricLabel"],
    .main [data-testid="stMetricValue"],
    .main [data-testid="stMetricDelta"] {
        color: #2c3e50 !important;
    }

    /* Tab labels */
    .stTabs [data-baseweb="tab"] {
        color: #2c3e50 !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white !important;
    }

    /* Caption and helper text */
    .main .stCaptionContainer, .main .css-1v0mbdj, .main small {
        color: #2c3e50 !important;
    }

    /* Checkbox and radio labels */
    .main .stCheckbox label, .main .stRadio label {
        color: #2c3e50 !important;
    }

    /* Selectbox and slider labels */
    .main .stSelectbox label, .main .stSlider label {
        color: #2c3e50 !important;
    }

    /* Input field values - ensure they are visible */
    .main .stNumberInput input,
    .main .stTextInput input,
    .main .stSelectbox select,
    .main input[type="number"],
    .main input[type="text"],
    .main select {
        color: #2c3e50 !important;
        background-color: white !important;
    }

    /* EXCEPTIONS: Only preserve white text in DARK backgrounds */
    /* Dark blue gradients */
    body div[style*="background:linear-gradient"][style*="#3498db"] *,
    body div[style*="background:linear-gradient"][style*="#2980b9"] * {
        color: white !important;
    }

    /* Dark red/danger gradients */
    body div[style*="background:linear-gradient"][style*="#e74c3c"] *,
    body div[style*="background:linear-gradient"][style*="#c0392b"] * {
        color: white !important;
    }

    /* Dark green gradients (but NOT light green) */
    body div[style*="background:linear-gradient"][style*="#1e3a2e"] *,
    body div[style*="background:linear-gradient"][style*="#27ae60"] * {
        color: white !important;
    }

    /* Explicit color:white in dark backgrounds only */
    body div[style*="background:#3498db"][style*="color:white"],
    body div[style*="background:#2980b9"][style*="color:white"],
    body div[style*="background:#e74c3c"][style*="color:white"],
    body div[style*="background:#c0392b"][style*="color:white"] {
        color: white !important;
    }

    /* Children of explicitly white-text elements in dark backgrounds */
    body div[style*="background:#3498db"][style*="color:white"] *,
    body div[style*="background:#2980b9"][style*="color:white"] *,
    body div[style*="background:#e74c3c"][style*="color:white"] *,
    body div[style*="background:#c0392b"][style*="color:white"] * {
        color: white !important;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a2e 0%, #27ae60 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Custom alert boxes */
    .stAlert {
        border-radius: 12px;
        border-left: 5px solid;
        animation: slideIn 0.5s ease-out;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    /* Enhanced buttons */
    .stButton>button {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 10px rgba(46, 204, 113, 0.3);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(46, 204, 113, 0.4);
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
    }

    /* Progress indicators */
    .sustainability-badge {
        display: inline-block;
        padding: 8px 16px;
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        box-shadow: 0 2px 8px rgba(46, 204, 113, 0.3);
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------
# Helper Functions (Enhanced Data Generators)
# -----------------------------------------------
def calculate_risk_multiplier(warming, sea_level, storm_freq, persona):
    """Calculate combined risk multiplier based on all parameters."""
    base_risk = warming / 1.5  # Normalized to 1.5°C baseline

    # Persona-specific risk factors
    persona_weights = {
        "Coastal Homeowner (Florida)": {"sea": 2.5, "storm": 2.0, "heat": 1.2},
        "Subsistence Farmer (Bangladesh)": {"sea": 2.8, "storm": 2.3, "heat": 1.8},
        "Wildland Interface (California)": {"sea": 0.5, "storm": 1.0, "heat": 2.5},
        "Urban Heat Island (Phoenix)": {"sea": 0.2, "storm": 0.8, "heat": 3.5},
        "Mountain Community (Colorado)": {"sea": 0.1, "storm": 1.5, "heat": 1.5}
    }

    weights = persona_weights.get(persona, {"sea": 1.0, "storm": 1.0, "heat": 1.0})

    risk = base_risk * (1 +
        (sea_level / 50) * weights["sea"] +
        (storm_freq / 100) * weights["storm"]
    )

    return max(1.0, risk)

def generate_enhanced_cost_curve(years=30, risk_multiplier=1.0, storm_frequency=15):
    """
    Enhanced model with realistic disaster events, insurance, and opportunity costs.
    """
    np.random.seed(42)  # Reproducible randomness
    time = np.arange(years)

    # Base costs
    initial_bau = 100
    initial_resilient = 280

    # Business as Usual
    bau_base = initial_bau + (8 * time)  # Regular maintenance
    bau_insurance = 15 * time * risk_multiplier  # Rising insurance

    # Generate disaster events (probability increases with risk)
    disaster_probability = 0.15 * risk_multiplier  # Base 15% annual probability
    disaster_events = np.random.binomial(1, disaster_probability, years)

    # Disaster costs compound over time (aging infrastructure)
    disaster_costs = np.zeros(years)
    for i in range(years):
        if disaster_events[i]:
            # Cost increases with age and risk
            disaster_costs[i] = 150 * (1 + i/10) * risk_multiplier
            # Ripple effect: next 3 years have elevated costs
            for j in range(1, 4):
                if i + j < years:
                    disaster_costs[i + j] += 30 * (4 - j)

    # Cumulative approach
    bau_cumulative = np.cumsum(bau_base + bau_insurance) + np.cumsum(disaster_costs)

    # Add opportunity cost (money that could have been invested)
    opportunity_cost = np.cumsum(disaster_costs) * 0.05  # 5% annual return lost
    bau_total = bau_cumulative + opportunity_cost

    # Resilient Investment
    res_base = initial_resilient + (4 * time)  # Lower maintenance
    res_insurance = 5 * time  # Much lower insurance (stable)
    res_disasters = np.zeros(years)

    # Resilient infrastructure still faces events but much lower impact
    for i in range(years):
        if disaster_events[i]:
            res_disasters[i] = 25  # Fixed, low impact

    res_cumulative = np.cumsum(res_base + res_insurance) + np.cumsum(res_disasters)

    # Calculate crossover point
    crossover_year = None
    for i in range(years):
        if bau_total[i] > res_cumulative[i]:
            crossover_year = i
            break

    df = pd.DataFrame({
        "Year": time,
        "BAU_Total": bau_total,
        "Resilient_Total": res_cumulative,
        "BAU_Base": np.cumsum(bau_base),
        "BAU_Insurance": np.cumsum(bau_insurance),
        "BAU_Disasters": np.cumsum(disaster_costs),
        "Disaster_Events": disaster_events,
        "Crossover": crossover_year
    })

    return df, crossover_year

def get_persona_description(persona, warming, sea_level, storm_freq):
    """Get detailed persona context."""
    descriptions = {
        "Coastal Homeowner (Florida)": {
            "icon": "🏖️",
            "risk_profile": "High exposure to hurricanes and sea level rise",
            "annual_loss": f"${int(5000 * (warming/1.5) * (1 + sea_level/100)):,}",
            "primary_hazards": ["Storm surge", "Hurricane winds", "Flooding"],
            "adaptation_needs": "Elevation, storm shutters, flood insurance"
        },
        "Subsistence Farmer (Bangladesh)": {
            "icon": "🌾",
            "risk_profile": "Extreme vulnerability to flooding and cyclones",
            "annual_loss": f"${int(800 * (warming/1.5) * (1 + storm_freq/50)):,}",
            "primary_hazards": ["Monsoon flooding", "Cyclones", "Soil erosion"],
            "adaptation_needs": "Early warning systems, raised housing, crop insurance"
        },
        "Wildland Interface (California)": {
            "icon": "🔥",
            "risk_profile": "High wildfire risk with increasing heat",
            "annual_loss": f"${int(8000 * (warming/1.5) * (1 + storm_freq/100)):,}",
            "primary_hazards": ["Wildfires", "Air quality", "Drought"],
            "adaptation_needs": "Defensible space, fire-resistant materials, evacuation routes"
        },
        "Urban Heat Island (Phoenix)": {
            "icon": "🌡️",
            "risk_profile": "Extreme heat with grid vulnerability",
            "annual_loss": f"${int(3000 * (warming/1.5)**2):,}",
            "primary_hazards": ["Heat waves", "Power outages", "Water stress"],
            "adaptation_needs": "Cooling centers, solar+battery, green infrastructure"
        },
        "Mountain Community (Colorado)": {
            "icon": "⛰️",
            "risk_profile": "Wildfire smoke, avalanche, extreme weather",
            "annual_loss": f"${int(4000 * (warming/1.5) * (1 + storm_freq/80)):,}",
            "primary_hazards": ["Wildfire smoke", "Avalanche", "Flash floods"],
            "adaptation_needs": "Air filtration, emergency access, water storage"
        }
    }
    return descriptions.get(persona, descriptions["Coastal Homeowner (Florida)"])

# -----------------------------------------------
# Sidebar: Enhanced Choice Architecture
# -----------------------------------------------
with st.sidebar:
    # Sustainability header
    st.markdown("### 🌱 RISC: Resilient Infrastructure & Sustainable Communities")
    st.markdown("*Data-driven climate adaptation*")

    # Navigation
    selected = option_menu(
        "Journey",
        ["The Concept", "The Diagnosis", "The Solution", "The Experiment"],
        icons=['lightbulb', 'activity', 'tools', 'science'],
        menu_icon="leaf",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "rgba(255,255,255,0.1)"},
            "icon": {"color": "#2ecc71", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "2px"},
            "nav-link-selected": {"background-color": "rgba(46, 204, 113, 0.3)"}
        }
    )

    st.markdown("---")

    # Enhanced Context Simulator - Always visible
    st.markdown("### 🌍 Climate Scenario Builder")
    st.caption("Adjust parameters to model different futures")

    # Temperature
    warming_level = st.slider(
        "🌡️ Global Warming (°C above pre-industrial)",
        min_value=1.0,
        max_value=4.0,
        value=1.5,
        step=0.1,
        help="IPCC scenarios: 1.5°C (Paris goal), 2.0°C (Current policies), 3.5°C+ (Worst case)"
    )

    # Visual indicator for warming level
    if warming_level <= 1.5:
        warming_status = "🟢 Paris Agreement Target"
        warming_color = "#2ecc71"
    elif warming_level <= 2.5:
        warming_status = "🟡 Current Trajectory"
        warming_color = "#f39c12"
    else:
        warming_status = "🔴 Catastrophic Scenario"
        warming_color = "#e74c3c"

    st.markdown(f"<div style='background:{warming_color}20; padding:10px; border-radius:8px; border-left:4px solid {warming_color}; margin:10px 0;'>"
                f"<strong>{warming_status}</strong></div>", unsafe_allow_html=True)

    # Sea Level Rise
    sea_level_rise = st.slider(
        "🌊 Sea Level Rise (cm by 2100)",
        min_value=20,
        max_value=200,
        value=int(warming_level * 30),  # Rough correlation
        step=10,
        help="Higher warming = more ice melt. Range: 20cm (best) to 200cm (worst)"
    )

    # Storm Frequency
    storm_frequency = st.slider(
        "⛈️ Extreme Storm Increase (%)",
        min_value=0,
        max_value=100,
        value=int((warming_level - 1.0) * 30),
        step=5,
        help="Increase in Category 4-5 hurricanes and extreme weather events"
    )

    # Persona Selection
    st.markdown("---")
    st.markdown("### 👤 Vulnerability Context")
    persona = st.selectbox(
        "Who faces this climate future?",
        (
            "Coastal Homeowner (Florida)",
            "Subsistence Farmer (Bangladesh)",
            "Wildland Interface (California)",
            "Urban Heat Island (Phoenix)",
            "Mountain Community (Colorado)"
        ),
        help="Different communities face different climate risks"
    )

    # Get persona details
    persona_info = get_persona_description(persona, warming_level, sea_level_rise, storm_frequency)

    # Display persona card
    st.markdown(f"""
    <div style='background:rgba(255,255,255,0.15); padding:15px; border-radius:10px; margin:10px 0;'>
        <div style='font-size:32px; text-align:center;'>{persona_info['icon']}</div>
        <div style='font-size:12px; margin-top:10px;'>
            <strong>Risk Profile:</strong><br/>
            {persona_info['risk_profile']}<br/><br/>
            <strong>Est. Annual Loss:</strong><br/>
            <span style='font-size:20px; color:#e74c3c;'>{persona_info['annual_loss']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Calculate combined risk
    risk_multiplier = calculate_risk_multiplier(warming_level, sea_level_rise, storm_frequency, persona)

    # Risk dashboard
    st.markdown("---")
    st.markdown("### 📊 Risk Multiplier")
    st.progress(min(risk_multiplier / 3.0, 1.0))
    st.caption(f"**{risk_multiplier:.2f}x** baseline risk")

    if risk_multiplier < 1.5:
        st.success("Manageable with current systems")
    elif risk_multiplier < 2.5:
        st.warning("Adaptation investment needed")
    else:
        st.error("Urgent transformation required")

# -----------------------------------------------
# Tab 1: The Concept (The Hook)
# -----------------------------------------------
if selected == "The Concept":
    # Hero section
    st.markdown("<h1 style='text-align:center; font-size:48px;'>🌱 The Resilience Paradox</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#7f8c8d;'>Why we engineered a system that pays us to be fragile.</h3>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#27ae60; margin-top:0;'>💡 The Core Insight</h3>
<p style='color:#2c3e50; font-size:16px;'>The <strong>worst impacts</strong> of natural disasters aren't just acts of nature. They are <strong>market failures</strong> — systems that reward the wrong behaviors.</p>
<h4 style='color:#27ae60; margin-top:20px;'>We've engineered fragility through:</h4>
<ol style='color:#2c3e50; font-size:15px; line-height:1.8;'>
<li><strong>🏗️ Short-termism:</strong><br/>Building cheap in dangerous places because upfront costs look lower</li>
<li><strong>🔒 Opacity:</strong><br/>Hiding risk data from buyers, renters, and communities</li>
<li><strong>🔄 Rigidity:</strong><br/>Funding reactive rebuilding instead of proactive adaptation</li>
</ol>
<hr style='border-color:#e0e0e0; margin:20px 0;'/>
<h3 style='color:#27ae60;'>🎯 The Proposition</h3>
<p style='color:#2c3e50; font-size:16px;'>We don't need a bigger sea wall. We need <strong>Data Products</strong> that:</p>
<ul style='color:#2c3e50; font-size:15px; line-height:1.8;'>
<li>✅ Correct the price of risk (make fragility expensive)</li>
<li>✅ Provide liquidity for adaptation (make resilience affordable)</li>
<li>✅ Trigger action <em>before</em> the disaster strikes (prevention &gt; recovery)</li>
</ul>
</div>""", unsafe_allow_html=True)

    with col2:
        # Dynamic impact metrics
        impact_increase = int((risk_multiplier - 1.0) * 100)

        st.markdown(f"""<div style='background:linear-gradient(135deg, #e74c3c, #c0392b); padding:25px; border-radius:15px; color:white; box-shadow:0 4px 20px rgba(231,76,60,0.4);'>
<h3 style='color:white; margin:0;'>⚠️ Current Scenario</h3>
<div style='font-size:14px; margin-top:15px; opacity:0.95;'>
<strong>Climate:</strong> +{warming_level}°C warming<br/>
<strong>Context:</strong> {persona.split('(')[0]}<br/>
<strong>Sea Level:</strong> +{sea_level_rise}cm by 2100<br/>
<strong>Storms:</strong> +{storm_frequency}% frequency
</div>
<hr style='border-color:rgba(255,255,255,0.3); margin:15px 0;'/>
<div style='font-size:32px; font-weight:bold; text-align:center; margin:10px 0;'>
+{impact_increase}%
</div>
<div style='text-align:center; font-size:14px;'>
Increase in Business-as-Usual costs
</div>
</div>""", unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        # Sustainability badge
        st.markdown("""<div style='background:linear-gradient(135deg, #2ecc71, #27ae60); padding:20px; border-radius:15px; color:white; text-align:center; box-shadow:0 4px 20px rgba(46,204,113,0.4);'>
<div style='font-size:36px;'>🌍</div>
<div style='font-size:16px; font-weight:600; margin-top:10px;'>
Green Infrastructure<br/>Creates Value
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("---")

    # Simplified Key Metrics
    st.markdown("## 📊 Why Resilience Pays Off")

    # Generate simplified data
    time_horizon = 30
    chart_data, crossover_year = generate_enhanced_cost_curve(
        years=time_horizon,
        risk_multiplier=risk_multiplier,
        storm_frequency=storm_frequency
    )

    # Display key metrics in a clean grid
    if crossover_year is not None:
        col_i1, col_i2, col_i3 = st.columns(3)

        with col_i1:
            st.metric(
                "🎯 Break-Even Point",
                f"Year {crossover_year}",
                f"Resilient becomes cheaper"
            )

        with col_i2:
            total_savings = chart_data["BAU_Total"].iloc[-1] - chart_data["Resilient_Total"].iloc[-1]
            st.metric(
                "💰 30-Year Savings",
                f"${total_savings:,.0f}k",
                f"{int(total_savings/chart_data['BAU_Total'].iloc[-1]*100)}% reduction"
            )

        with col_i3:
            initial_premium = 180  # $280k - $100k initial investment difference
            roi = total_savings / initial_premium if initial_premium > 0 else 0
            st.metric(
                "📈 Return on Investment",
                f"{roi:.1f}x",
                f"on resilient infrastructure"
            )

        st.markdown("""<div style='background:#e8f5e9; padding:20px; border-radius:10px; border-left:5px solid #2ecc71; margin:20px 0;'>
<strong style='color:#27ae60;'>💡 The Bottom Line:</strong>
<p style='color:#2c3e50; margin:10px 0;'>
Resilient infrastructure costs <strong>$180k more upfront</strong> but saves <strong>${0:,.0f}k over 30 years</strong>.
The break-even happens in year <strong>{1}</strong> — after that, it's pure savings plus peace of mind.
</p>
</div>""".format(int(total_savings), crossover_year), unsafe_allow_html=True)
    else:
        st.info("✅ In your scenario, resilient investment is cost-effective from day one!")

# -----------------------------------------------
# Tab 2: The Diagnosis
# -----------------------------------------------
if selected == "The Diagnosis":
    st.markdown("<h1 style='text-align:center; font-size:48px;'>🔍 The Four-Front War</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#7f8c8d;'>We are fighting four distinct enemies — each needs a different strategy</h3>", unsafe_allow_html=True)

    st.markdown("---")

    # Interactive hazard selector
    st.markdown("### 🎯 Select a Hazard to Explore:")
    hazard_tabs = st.tabs(["🌪️ Violent Force", "🌋 Sudden Shock", "🌡️ Silent Killer", "🔥 Total Consumption"])

    with hazard_tabs[0]:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""<div style='background:linear-gradient(135deg, #e74c3c, #c0392b); padding:30px; border-radius:15px; color:white; text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center;'>
<div style='font-size:64px;'>🌪️</div>
<h2 style='color:white; margin:15px 0;'>The Violent Force</h2>
<h4 style='color:white; opacity:0.9;'>Hurricanes & Cyclones</h4>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#e74c3c; margin-top:0;'>The Market Failure: EXPOSURE</h3>
<p style='color:#2c3e50;'><strong>The Problem:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>We subsidize flood insurance through NFIP, making coastal living artificially cheap</li>
<li>Development is allowed in evacuation-hostile areas (single bridge access)</li>
<li>Rebuilding grants incentivize returning to the same vulnerable location</li>
</ul>
<p style='color:#2c3e50;'><strong>The Impact:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>40% of US population lives in coastal counties</li>
<li>$1 trillion in coastal real estate at risk</li>
<li>Evacuation costs: $1M per coastal mile</li>
</ul>
<p style='color:#2c3e50;'><strong>The Solution:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>🎯 Risk-reveal labels on real estate listings</li>
<li>💧 Liquidity triggers for pre-evacuation funding</li>
<li>📍 Managed retreat with dignity (buyout programs)</li>
</ul>
</div>""", unsafe_allow_html=True)

            # Show risk for current scenario
            if "Coastal" in persona or "Bangladesh" in persona:
                st.error(f"⚠️ Your selected scenario ({persona}) is HIGH RISK for this hazard")
            else:
                st.info("ℹ️ This hazard has moderate impact on your selected scenario")

    with hazard_tabs[1]:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""<div style='background:linear-gradient(135deg, #f39c12, #d68910); padding:30px; border-radius:15px; color:white; text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center;'>
<div style='font-size:64px;'>🌋</div>
<h2 style='color:white; margin:15px 0;'>The Sudden Shock</h2>
<h4 style='color:white; opacity:0.9;'>Earthquakes</h4>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#f39c12; margin-top:0;'>The Market Failure: FRAGILITY</h3>
<p style='color:#2c3e50;'><strong>The Problem:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>Seismic retrofit data is NOT disclosed in real estate transactions</li>
<li>Landlords have no incentive to retrofit (renters bear the risk)</li>
<li>Cheap unreinforced masonry looks identical to safe construction</li>
</ul>
<p style='color:#2c3e50;'><strong>The Impact:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>75% of pre-1980 buildings in California are not retrofitted</li>
<li>30-second earthquake can cause 30 years of economic loss</li>
<li>Soft-story buildings: 8x higher collapse risk</li>
</ul>
<p style='color:#2c3e50;'><strong>The Solution:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>🏚️ Mandatory seismic risk labels (like Energy Star)</li>
<li>📊 Computer vision to detect unreinforced masonry</li>
<li>💰 Green bonds for retrofit financing</li>
</ul>
</div>""", unsafe_allow_html=True)

    with hazard_tabs[2]:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""<div style='background:linear-gradient(135deg, #3498db, #2980b9); padding:30px; border-radius:15px; color:white; text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center;'>
<div style='font-size:64px;'>🌡️</div>
<h2 style='color:white; margin:15px 0;'>The Silent Killer</h2>
<h4 style='color:white; opacity:0.9;'>Extreme Heat</h4>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#3498db; margin-top:0;'>The Market Failure: EFFICIENCY</h3>
<p style='color:#2c3e50;'><strong>The Problem:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>We optimized the grid for cheap power on normal days, guaranteeing failure on the extreme days.</li>
<li>When AC fails, deaths cascade through hospitals, water systems</li>
<li>Poor & elderly populations are invisible until it's too late</li>
</ul>
<p style='color:#2c3e50;'><strong>The Impact:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>Heat is the #1 weather killer in the US</li>
<li>Phoenix: 120°F+ days increasing 400% by 2050</li>
<li>3-day blackout during heatwave = humanitarian crisis</li>
</ul>
<p style='color:#2c3e50;'><strong>The Solution:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>🔌 Smart meter data for vulnerability detection</li>
<li>⚡ Distributed solar+battery for resilience</li>
<li>🏥 Automated alerts to social workers (not police)</li>
</ul>
</div>""", unsafe_allow_html=True)

            if "Phoenix" in persona or warming_level > 2.5:
                st.error(f"⚠️ Your selected scenario ({persona} at +{warming_level}°C) is HIGH RISK for this hazard")

    with hazard_tabs[3]:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""<div style='background:linear-gradient(135deg, #e67e22, #d35400); padding:30px; border-radius:15px; color:white; text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center;'>
<div style='font-size:64px;'>🔥</div>
<h2 style='color:white; margin:15px 0;'>The Total Consumption</h2>
<h4 style='color:white; opacity:0.9;'>Wildfires</h4>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#e67e22; margin-top:0;'>The Market Failure: THE INTERFACE</h3>
<p style='color:#2c3e50;'><strong>The Problem:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>We allow suburbs to sprawl into wildland-urban interface (WUI)</li>
<li>Insurance doesn't verify defensible space compliance</li>
<li>Fire prevention is a collective action problem (tragedy of commons)</li>
</ul>
<p style='color:#2c3e50;'><strong>The Impact:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>46 million US homes in WUI zones</li>
<li>California losses: $20B+ annually</li>
<li>100ft of defensible space reduces loss by 90%</li>
</ul>
<p style='color:#2c3e50;'><strong>The Solution:</strong></p>
<ul style='color:#2c3e50; font-size:15px;'>
<li>🔥 Defensible Space DAO with satellite verification</li>
<li>🎮 Gamified prevention with insurance rebates</li>
<li>🤖 AI brush clearance monitoring</li>
</ul>
</div>""", unsafe_allow_html=True)

            if "California" in persona or "Mountain" in persona:
                st.error(f"⚠️ Your selected scenario ({persona}) is HIGH RISK for this hazard")

    st.markdown("---")

    # Risk Triangle Visualization
    st.markdown("### 🔺 The Risk Triangle")
    st.markdown("Disasters happen at the intersection of **Hazard**, **Exposure**, and **Vulnerability**. All three must align for catastrophe.")

    col_tri1, col_tri2 = st.columns([1, 1])

    with col_tri1:
        # Interactive diagram
        st.graphviz_chart('''
        graph {
            bgcolor="transparent"
            node [fontsize=14, shape=circle, style=filled, fontname="Arial", width=2.5, height=2.5]

            Hazard [fillcolor="#e74c3c", fontcolor="white", label="HAZARD\n\nClimate Change\nExtreme Weather"]
            Exposure [fillcolor="#f39c12", fontcolor="white", label="EXPOSURE\n\nLocation\nDevelopment Patterns"]
            Vulnerability [fillcolor="#3498db", fontcolor="white", label="VULNERABILITY\n\nInfrastructure Quality\nSocial Factors"]

            Hazard -- Exposure [penwidth=3, color="#d35400"]
            Exposure -- Vulnerability [penwidth=3, color="#c0392b"]
            Vulnerability -- Hazard [penwidth=3, color="#8e44ad"]

            node [shape=box, style="filled,rounded", fillcolor="#27ae60", fontcolor="white", fontsize=16, width=3, height=1.5]
            Solution [label="🌱 RISC SOLUTIONS\n\nData Products that\nbreak the chain"]

            Solution -- Hazard [style=dashed, color="#2ecc71", penwidth=2]
            Solution -- Exposure [style=dashed, color="#2ecc71", penwidth=2]
            Solution -- Vulnerability [style=dashed, color="#2ecc71", penwidth=2]
        }
        ''')

    with col_tri2:
        st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#27ae60; margin-top:0;'>🎯 Breaking the Chain</h3>
<p style='color:#2c3e50; font-size:15px;'><strong>Traditional disaster response treats these as unavoidable acts of nature.</strong></p>
<p style='color:#2c3e50; font-size:15px;'><strong>We treat them as market failures that can be corrected:</strong></p>
<div style='margin:20px 0; padding:15px; background:#ffe6e6; border-radius:8px; color:#2c3e50;'>
<strong style='color:#e74c3c;'>❌ Can't control HAZARD</strong><br/>
<span style='color:#2c3e50;'>Climate change is happening</span>
</div>
<div style='margin:20px 0; padding:15px; background:#fff4e6; border-radius:8px; color:#2c3e50;'>
<strong style='color:#f39c12;'>✅ CAN reduce EXPOSURE</strong><br/>
<span style='color:#2c3e50;'>Risk labels + liquidity for managed retreat</span>
</div>
<div style='margin:20px 0; padding:15px; background:#e6f7ff; border-radius:8px; color:#2c3e50;'>
<strong style='color:#3498db;'>✅ CAN reduce VULNERABILITY</strong><br/>
<span style='color:#2c3e50;'>Transparent data + prevention incentives</span>
</div>
<div style='margin:20px 0; padding:20px; background:#e6f9f0; border-radius:8px; border:2px solid #27ae60; color:#2c3e50;'>
<strong style='color:#27ae60; font-size:18px;'>💡 Break ANY link = Prevent disaster</strong>
</div>
</div>""", unsafe_allow_html=True)

# -----------------------------------------------
# Tab 3: The Solution
# -----------------------------------------------
if selected == "The Solution":
    st.markdown("<h1 style='text-align:center; font-size:48px;'>🌱 The RISC Product Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#7f8c8d;'>Data Products, not just policy papers</h3>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""<div style='background:linear-gradient(135deg, #2ecc71, #27ae60); padding:30px; border-radius:15px; color:white; text-align:center; box-shadow:0 6px 20px rgba(46,204,113,0.3); margin:20px 0;'>
<h2 style='color:white; margin:0;'>🎯 The Core Philosophy</h2>
<p style='font-size:18px; margin-top:15px;'>
We borrow tools from <strong>Fintech</strong> and <strong>Big Tech</strong> to solve disaster resilience.<br/>
Real-time data + Behavioral nudges + Financial incentives = Sustainable adaptation
</p>
</div>""", unsafe_allow_html=True)

    st.markdown("### 🚀 Select a Product to Explore:")

    product_tabs = st.tabs([
        "💧 Liquidity Trigger",
        "🏚️ Risk Reveal",
        "🔥 Defensible DAO",
        "🔌 Welfare Pulse"
    ])

    # Product 1: Liquidity Trigger
    with product_tabs[0]:
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h2 style='color:#3498db; margin-top:0;'>💧 The Liquidity Trigger</h2>
<h4 style='color:#7f8c8d;'>Parametric Disaster Finance</h4>
<div style='background:#e8f5e9; padding:15px; border-radius:8px; margin:15px 0; color:#2c3e50;'>
<strong style='color:#2c3e50;'>The Insight:</strong> People don't stay in hurricanes because they're stubborn.
They stay because they <strong>can't afford to leave</strong>.
</div>
<h4 style='color:#27ae60;'>How It Works:</h4>
<ol style='font-size:16px; line-height:1.8; color:#2c3e50;'>
<li style='color:#2c3e50;'><strong>Monitor:</strong> Satellite wind speed + forecast models (NASA/NOAA)</li>
<li style='color:#2c3e50;'><strong>Trigger:</strong> When 48hr forecast exceeds 110 mph</li>
<li style='color:#2c3e50;'><strong>Deploy:</strong> Instant mobile money transfer ($100 per household)</li>
<li style='color:#2c3e50;'><strong>Track:</strong> Evacuation compliance via cell tower data</li>
</ol>
<div style='background:#fff3cd; padding:15px; border-radius:8px; margin:15px 0; border-left:4px solid #f39c12; color:#2c3e50;'>
<strong style='color:#2c3e50;'>💡 The Tech Stack:</strong> Parametric insurance + Mobile money + Forecast APIs
</div>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("#### 📊 Impact Metrics")

            # Interactive demo
            demo_trigger = st.checkbox("🌪️ Simulate Hurricane Approach", value=False)

            if demo_trigger:
                st.error("⚠️ TRIGGER ACTIVATED")
                st.metric("Wind Speed", "115 mph", "+15 mph")
                st.metric("Forecast Confidence", "85%", "+5%")
                st.metric("Funds Deployed", "$2.5M", "25,000 households")

                st.success("✅ Evacuation rate increased from 60% to 85%")

                # Outcome visualization
                outcome_data = pd.DataFrame({
                    'Status': ['Control Group', 'Liquidity Trigger'],
                    'Evacuation Rate': [60, 85],
                    'Lives Saved (est)': [0, 375]
                })

                fig_outcome = px.bar(
                    outcome_data,
                    x='Status',
                    y='Evacuation Rate',
                    title='Evacuation Compliance',
                    color='Status',
                    color_discrete_map={
                        'Control Group': '#e74c3c',
                        'Liquidity Trigger': '#2ecc71'
                    }
                )
                fig_outcome.update_layout(showlegend=False, height=300)
                st.plotly_chart(fig_outcome, use_container_width=True)

            else:
                st.info("✅ MONITORING ACTIVE")
                st.metric("Wind Speed", "45 mph", "Normal")
                st.metric("Forecast Confidence", "70%", "Stable")
                st.metric("Status", "Standby", "Ready to deploy")

            st.markdown("---")
            st.markdown("""
            **📚 Evidence Base:**
            - Bangladesh forecast-based financing: 40% improvement in evacuation
            - Cost: $100/household
            - ROI: 4-8x (lives + assets saved)
            """)

    # Product 2: Risk Reveal
    with product_tabs[1]:
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h2 style='color:#e67e22; margin-top:0;'>🏚️ The Risk Reveal</h2>
<h4 style='color:#7f8c8d;'>Climate Risk Labels for Real Estate</h4>
<div style='background:#ffe6e6; padding:15px; border-radius:8px; margin:15px 0; color:#2c3e50;'>
<strong style='color:#2c3e50;'>The Problem:</strong> You can see calorie counts on food, energy ratings on appliances,
but <strong>the market is trading broken assets because the risk is unpriced.</strong>
</div>
<h4 style='color:#27ae60;'>How It Works:</h4>
<ol style='font-size:16px; line-height:1.8; color:#2c3e50;'>
<li style='color:#2c3e50;'><strong>Integrate:</strong> Plugin for Zillow, Redfin, Apartments.com</li>
<li style='color:#2c3e50;'><strong>Display:</strong> Climate Risk Score (0-100) on every listing</li>
<li style='color:#2c3e50;'><strong>Detail:</strong> Flood zone, fire risk, seismic vulnerability, heat exposure</li>
<li style='color:#2c3e50;'><strong>Recommend:</strong> Adaptation actions + cost estimates</li>
</ol>
<div style='background:#e6f7ff; padding:15px; border-radius:8px; margin:15px 0; border-left:4px solid #3498db; color:#2c3e50;'>
<strong style='color:#2c3e50;'>💡 The Behavior Shift:</strong> Information asymmetry correction forces landlords
to compete on safety, not just aesthetics.
</div>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("#### 🏠 Example Risk Label")

            # Mock property
            st.markdown("""<div style='background:#f8f9fa; padding:20px; border-radius:10px; border:2px solid #dee2e6; color:#2c3e50;'>
<h4 style='margin-top:0; color:#2c3e50;'>123 Coastal Ave, Miami FL</h4>
<p style='color:#2c3e50;'><strong>$450,000</strong> • 3 bed, 2 bath</p>
</div>""", unsafe_allow_html=True)

            # Risk score
            risk_score = int(risk_multiplier * 30)
            risk_color = "#2ecc71" if risk_score < 30 else ("#f39c12" if risk_score < 60 else "#e74c3c")

            st.markdown(f"""<div style='background:{risk_color}; padding:20px; border-radius:10px; color:white; text-align:center; margin:15px 0;'>
<h2 style='color:white; margin:0;'>Climate Risk Score</h2>
<div style='font-size:48px; font-weight:bold; margin:10px 0;'>{risk_score}/100</div>
<p style='margin:0;'>{"High Risk" if risk_score > 60 else ("Moderate" if risk_score > 30 else "Low Risk")}</p>
</div>""", unsafe_allow_html=True)

            # Risk breakdown
            st.markdown("**Risk Factors:**")
            st.progress(0.7, text="🌊 Flood Zone: High (AE)")
            st.progress(0.3, text="🔥 Wildfire: Low")
            st.progress(0.8, text="🌡️ Heat Exposure: Extreme")
            st.progress(0.4, text="🌪️ Hurricane: Moderate")

            st.markdown("---")
            st.markdown("**💰 Recommended Actions:**")
            st.markdown("- Elevation: ~$35k")
            st.markdown("- Flood insurance: $2,400/yr")
            st.markdown("- Solar + battery: $28k")

    # Product 3: Defensible DAO
    with product_tabs[2]:
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h2 style='color:#e67e22; margin-top:0;'>🔥 The Defensible Space DAO</h2>
<h4 style='color:#7f8c8d;'>Cryptographic Proof of Compliance</h4>
<div style='background:#fff4e6; padding:15px; border-radius:8px; margin:15px 0; color:#2c3e50;'>
<strong style='color:#2c3e50;'>The Problem:</strong> Fire prevention is a tragedy of the commons.
Insurance requires "defensible space" but never verifies compliance.
</div>
<h4 style='color:#27ae60;'>How It Works:</h4>
<ol style='font-size:16px; line-height:1.8; color:#2c3e50;'>
<li style='color:#2c3e50;'><strong>Monitor:</strong> Satellite/drone imagery analyzes vegetation within 100ft</li>
<li style='color:#2c3e50;'><strong>Score:</strong> AI assigns Defensible Space Score (0-100)</li>
<li style='color:#2c3e50;'><strong>Verify:</strong> Immutable proof triggers automatic premium reduction</li>
<li style='color:#2c3e50;'><strong>Gamify:</strong> Neighborhood leaderboards + Digital Verification Certificate badges for top performers</li>
</ol>
<div style='background:#e6f9f0; padding:15px; border-radius:8px; margin:15px 0; border-left:4px solid #27ae60; color:#2c3e50;'>
<strong style='color:#2c3e50;'>💡 The Sustainability Win:</strong> Prevention is 10x cheaper than rebuilding.
Creates green jobs in brush clearance + ecological restoration.
</div>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("#### 🎮 Your Defensible Space Score")

            # Interactive simulation
            user_compliance = st.slider(
                "Adjust your brush clearance",
                0, 100, 65,
                help="Slide to see impact on insurance discount"
            )

            score_color = "#2ecc71" if user_compliance > 70 else ("#f39c12" if user_compliance > 40 else "#e74c3c")

            st.markdown(f"""<div style='background:{score_color}; padding:20px; border-radius:10px; color:white; text-align:center; margin:15px 0;'>
<h3 style='color:white; margin:0;'>Your Score</h3>
<div style='font-size:48px; font-weight:bold; margin:10px 0;'>{user_compliance}/100</div>
</div>""", unsafe_allow_html=True)

            # Calculate rewards
            insurance_base = 2400
            discount_pct = int(user_compliance * 0.3)
            discount_amt = int(insurance_base * discount_pct / 100)

            st.metric("💰 Annual Insurance Savings", f"${discount_amt}", f"{discount_pct}% discount")

            if user_compliance > 80:
                st.success("🏆 GOLD TIER: Earned Digital Verification Certificate!")
            elif user_compliance > 60:
                st.info("🥈 SILVER TIER: Keep improving!")
            else:
                st.warning("⚠️ BRONZE TIER: Action needed")

            st.markdown("---")
            st.markdown("**🌳 Impact:**")
            st.markdown(f"- Risk reduction: {int(user_compliance * 0.9)}%")
            st.markdown(f"- Neighborhood safety: +{int(user_compliance * 0.5)}%")
            st.markdown("- Jobs created: 12 local contractors")

    # Product 4: Welfare Pulse
    with product_tabs[3]:
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h2 style='color:#9b59b6; margin-top:0;'>🔌 The Welfare Pulse</h2>
<h4 style='color:#7f8c8d;'>Smart Meter Early Warning System</h4>
<div style='background:#f4e6f9; padding:15px; border-radius:8px; margin:15px 0; color:#2c3e50;'>
<strong style='color:#2c3e50;'>The Silent Crisis:</strong> Heat is the #1 weather killer, but deaths are invisible
until it's too late. Elderly & poor suffer alone.
</div>
<h4 style='color:#27ae60;'>How It Works:</h4>
<ol style='font-size:16px; line-height:1.8; color:#2c3e50;'>
<li style='color:#2c3e50;'><strong>Monitor:</strong> Smart meter detects zero AC usage during extreme heat</li>
<li style='color:#2c3e50;'><strong>Pattern Match:</strong> Cross-reference with age/income vulnerability data</li>
<li style='color:#2c3e50;'><strong>Alert:</strong> Notify local non-profits, NOT police (avoid surveillance state)</li>
<li style='color:#2c3e50;'><strong>Intervene:</strong> Wellness checks + cooling center transport</li>
</ol>
<div style='background:#ffe6e6; padding:15px; border-radius:8px; margin:15px 0; border-left:4px solid #e74c3c; color:#2c3e50;'>
<strong style='color:#2c3e50;'>⚖️ Privacy Design:</strong> Anonymized data, opt-in system, community-based response.
No law enforcement involvement.
</div>
</div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("#### 🌡️ Heatwave Monitor")

            # Simulation
            temp = st.slider("Current Temperature (°F)", 70, 120, 85)

            if temp > 105:
                alert_level = "🔴 EXTREME DANGER"
                alert_color = "#e74c3c"
                households_risk = 450
            elif temp > 95:
                alert_level = "🟡 WARNING"
                alert_color = "#f39c12"
                households_risk = 120
            else:
                alert_level = "🟢 SAFE"
                alert_color = "#2ecc71"
                households_risk = 0

            st.markdown(f"""<div style='background:{alert_color}; padding:20px; border-radius:10px; color:white; text-align:center; margin:15px 0;'>
<h3 style='color:white; margin:0;'>{alert_level}</h3>
<div style='font-size:48px; font-weight:bold; margin:10px 0;'>{temp}°F</div>
</div>""", unsafe_allow_html=True)

            if households_risk > 0:
                st.error(f"⚠️ {households_risk} vulnerable households detected with no AC usage")
                st.metric("Alerts Sent", households_risk, "to community partners")
                st.metric("Response Time", "< 2 hours", "average")

                st.markdown("**📍 Actions Triggered:**")
                st.markdown("- 🚐 Cooling center transport")
                st.markdown("- 💧 Water delivery")
                st.markdown("- 🏥 Medical assessment")
            else:
                st.success("✅ All vulnerable households have active cooling")

            st.markdown("---")
            st.markdown("**📊 Season Stats:**")
            st.markdown("- Lives saved: 23 (estimated)")
            st.markdown("- Hospitalizations prevented: 67")
            st.markdown("- Cost per intervention: $45")

# -----------------------------------------------
# Tab 4: The Experiment
# -----------------------------------------------
if selected == "The Experiment":
    st.markdown("<h1 style='text-align:center; font-size:48px;'>🧪 The Liquidity Trigger Pilot</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#7f8c8d;'>Real-time parametric disaster finance simulation</h3>", unsafe_allow_html=True)

    st.markdown("---")

    # Pilot setup section
    st.markdown("### 🎯 Pilot Configuration")

    config_col1, config_col2, config_col3 = st.columns(3)

    with config_col1:
        budget = st.number_input(
            "💰 Pilot Budget ($)",
            min_value=10000,
            max_value=500000,
            value=75000,
            step=5000,
            help="Total funding available for the pilot program"
        )

    with config_col2:
        payout_per_household = st.number_input(
            "💵 Payout per Household ($)",
            min_value=50,
            max_value=500,
            value=100,
            step=25,
            help="Amount transferred to each eligible household"
        )

    with config_col3:
        location = st.selectbox(
            "📍 Pilot Location",
            ["Puerto Rico", "Bangladesh (Coastal)", "Philippines", "Florida Keys", "Mozambique"],
            help="Geographic context for the pilot"
        )

    households = int(budget / payout_per_household)

    # Display pilot summary
    st.markdown(f"""<div style='background:linear-gradient(135deg, #3498db, #2980b9); padding:25px; border-radius:15px; color:white; margin:20px 0; box-shadow:0 6px 20px rgba(52,152,219,0.3);'>
<h3 style='color:white; margin-top:0;'>📋 Pilot Summary</h3>
<div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; margin-top:15px;'>
<div>
<div style='font-size:32px; font-weight:bold; color:white !important;'>{households:,}</div>
<div style='opacity:0.9; color:white !important;'>Target Households</div>
</div>
<div>
<div style='font-size:32px; font-weight:bold; color:white !important;'>${budget:,}</div>
<div style='opacity:0.9; color:white !important;'>Total Budget</div>
</div>
<div>
<div style='font-size:32px; font-weight:bold; color:white !important;'>{location}</div>
<div style='opacity:0.9; color:white !important;'>Location</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # The hypothesis section
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#27ae60; margin-top:0;'>🔬 The Hypothesis</h3>
<div style='background:#e8f5e9; padding:20px; border-radius:10px; margin:15px 0; color:#2c3e50;'>
<h4 style='margin-top:0; color:#27ae60;'>IF...</h4>
<p style='color:#2c3e50;'>We provide immediate cash transfers ($100) to at-risk families 48 hours <strong>before</strong> a hurricane makes landfall...</p>
<h4 style='color:#27ae60;'>THEN...</h4>
<p style='color:#2c3e50;'>Evacuation compliance will increase by <strong>25-40%</strong> compared to the control group...</p>
<h4 style='color:#27ae60;'>BECAUSE...</h4>
<p style='color:#2c3e50;'><strong>Financial liquidity</strong> is the primary barrier to evacuation. People don't stay because they're irrational — they stay because they can't afford gas, hotels, or missing work.</p>
</div>
<div style='background:#fff3cd; padding:15px; border-radius:8px; margin:15px 0; border-left:4px solid #f39c12; color:#2c3e50;'>
<strong style='color:#2c3e50;'>📚 Evidence Base:</strong><br/>
<span style='color:#2c3e50;'>
- Bangladesh: 40% increase in evacuation (Red Cross 2019)<br/>
- Mozambique: 33% increase (Start Network 2020)<br/>
- Philippines: 35% increase (WFP 2021)
</span>
</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div style='background:white; padding:25px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); color:#2c3e50;'>
<h3 style='color:#e74c3c; margin-top:0;'>🎯 Success Metrics</h3>
<div style='padding:15px 0;'>
<h4 style='color:#3498db; margin-bottom:5px;'>Primary Outcome:</h4>
<ul style='font-size:16px; color:#2c3e50;'>
<li>Evacuation rate in treatment vs control</li>
<li>Target: +25% improvement</li>
</ul>
<h4 style='color:#3498db; margin-bottom:5px; margin-top:20px;'>Secondary Outcomes:</h4>
<ul style='font-size:16px; color:#2c3e50;'>
<li>Mortality reduction</li>
<li>Asset protection (homes, livestock)</li>
<li>Return time (faster recovery)</li>
<li>Household economic stability</li>
</ul>
<h4 style='color:#3498db; margin-bottom:5px; margin-top:20px;'>Cost-Effectiveness:</h4>
<ul style='font-size:16px; color:#2c3e50;'>
<li>Cost per life saved</li>
<li>ROI (asset protection value)</li>
<li>Target: 4-8x return</li>
</ul>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Live simulation section
    st.markdown("## 🌪️ Live Hurricane Simulation")
    st.markdown("Adjust the parameters to simulate a hurricane approach and trigger deployment.")

    sim_col1, sim_col2 = st.columns([1, 2])

    with sim_col1:
        st.markdown("#### 🎮 Control Panel")

        wind_speed = st.slider(
            "🌬️ Forecast Wind Speed (mph)",
            0, 180, 75, 5,
            help="Maximum sustained winds in forecast"
        )

        confidence = st.slider(
            "📊 Forecast Confidence (%)",
            0, 100, 75, 5,
            help="Model confidence in the prediction"
        )

        time_to_landfall = st.slider(
            "⏰ Time to Landfall (hours)",
            0, 96, 48, 6,
            help="Estimated hours until landfall"
        )

        st.markdown("---")

        # Trigger logic
        # Parametric Trigger Logic: Implements tiered payouts to mitigate 'basis risk' (the risk of binary cliffs)
        if wind_speed >= 130 and confidence > 80:
            trigger_status = "🚨 FULL TRIGGER (100% Payout)"
            payout_ratio = 1.0
            color = "error"
        elif wind_speed >= 90 and confidence > 60:
            trigger_status = "⚠️ PARTIAL TRIGGER (50% Payout)"
            payout_ratio = 0.5
            color = "warning"
        else:
            trigger_status = "✅ MONITORING (No Payout)"
            payout_ratio = 0.0
            color = "success"

        # Display Status
        if color == "error":
            st.error(trigger_status)
        elif color == "warning":
            st.warning(trigger_status)
        else:
            st.success(trigger_status)

    with sim_col2:
        st.subheader("Expected ROI Dashboard")
        
        # Dynamic Economic Modeling
        # Asset preservation is modeled as an exponential function of hazard intensity.
        # Rationale: Damage scales non-linearly (Wind^2.5) relative to wind speed.
        deployed_funds = budget * payout_ratio
        
        if deployed_funds > 0:
            # Baseline: 60mph is used as the threshold for minor damage onset
            damage_avoidance_factor = (wind_speed / 60) ** 2.5 
            est_asset_savings = int(deployed_funds * damage_avoidance_factor)
            roi = round(est_asset_savings / deployed_funds, 1)
        else:
            est_asset_savings = 0
            roi = 0

        # Visualization Data
        funding_levels = [0, 0, 0, 0]
        if payout_ratio > 0:
            # Assumes 48h distribution curve: 20% immediate, 60% mid-window, 100% pre-impact
            funding_levels = [0, deployed_funds*0.2, deployed_funds*0.6, deployed_funds] 
            
        st.bar_chart(pd.DataFrame({"Funds Deployed ($)": funding_levels}, index=["T-48h", "T-24h", "T-12h", "IMPACT"]))
        
        if payout_ratio > 0:
            st.markdown(f"""
            ### 📊 Impact Projection
            * **Funds Deployed:** ${int(deployed_funds):,} ({int(payout_ratio*100)}% of Cap)
            * **Households Reached:** {int(households * payout_ratio)}
            * **Est. Asset Savings:** ${est_asset_savings:,} (**{roi}x ROI**)
            """, unsafe_allow_html=True)
            
            # Model Calibration Feedback
            # Flag low-efficiency triggers to indicate potential model sensitivity issues
            if roi < 2.0:
                st.caption("⚠️ **Low Efficiency:** Storm intensity marginal relative to payout cost. Threshold calibration recommended.")
            else:
                st.caption("✅ **High Efficiency:** Liquidity deployment aligns with high-impact damage prevention.")
        else:
            st.info("System Standby. Adjust Wind Speed (>90mph) or Confidence (>60%) to test trigger.")

    st.markdown("---")

    # Implementation roadmap
    st.markdown("### 🗺️ Implementation Roadmap")

    roadmap_cols = st.columns(4)

    with roadmap_cols[0]:
        st.markdown("""<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; color:#2c3e50;'>
<h3 style='color:#3498db; margin-top:0;'>Phase 1</h3>
<h4 style='color:#2c3e50;'>Setup</h4>
<p style='font-size:14px; color:#2c3e50;'>
• Secure Mobile Money API Access (e.g., Bkash/M-Pesa)<br/>
• Mobile money integration<br/>
• Baseline survey<br/>
• IRB approval
</p>
<strong style='color:#2c3e50;'>3 months</strong>
</div>""", unsafe_allow_html=True)

    with roadmap_cols[1]:
        st.markdown("""<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; color:#2c3e50;'>
<h3 style='color:#f39c12; margin-top:0;'>Phase 2</h3>
<h4 style='color:#2c3e50;'>Pilot</h4>
<p style='font-size:14px; color:#2c3e50;'>
• Live 'Shadow Mode' Testing (No Payouts)<br/>
• Deploy on trigger<br/>
• Track evacuations<br/>
• Real-time adjustments
</p>
<strong style='color:#2c3e50;'>1 hurricane season</strong>
</div>""", unsafe_allow_html=True)

    with roadmap_cols[2]:
        st.markdown("""<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; color:#2c3e50;'>
<h3 style='color:#9b59b6; margin-top:0;'>Phase 3</h3>
<h4 style='color:#2c3e50;'>Evaluation</h4>
<p style='font-size:14px; color:#2c3e50;'>
• Impact assessment<br/>
• Cost-benefit analysis<br/>
• Qualitative interviews<br/>
• Academic publication
</p>
<strong style='color:#2c3e50;'>6 months</strong>
</div>""", unsafe_allow_html=True)

    with roadmap_cols[3]:
        st.markdown("""<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; color:#2c3e50;'>
<h3 style='color:#2ecc71; margin-top:0;'>Phase 4</h3>
<h4 style='color:#2c3e50;'>Scale</h4>
<p style='font-size:14px; color:#2c3e50;'>
• Policy recommendations<br/>
• Reinsurance Backstop Integration<br/>
• Insurance integration<br/>
• Open-source toolkit
</p>
<strong style='color:#2c3e50;'>Ongoing</strong>
</div>""", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Call to action
    st.markdown("""<div style='background:linear-gradient(135deg, #2ecc71, #27ae60); padding:30px; border-radius:15px; color:white; text-align:center; box-shadow:0 6px 20px rgba(46,204,113,0.4); margin:30px 0;'>
<h2 style='color:white; margin:0;'>🚀 Ready to Launch</h2>
<p style='font-size:18px; margin:15px 0; color:white;'>
This pilot can be operational in <strong>3 months</strong> with a budget of <strong>${budget:,}</strong>.<br/>
The next hurricane season is the deadline — lives depend on action, not more studies.
</p>
<p style='font-size:16px; margin-top:20px; opacity:0.95; color:white;'>
<strong>Demonstration for portfolio purposes</strong> — Data-driven climate adaptation solutions
</p>
</div>""".format(budget=budget), unsafe_allow_html=True)

    st.markdown("---")

    # Data disclaimer
    st.markdown("""<div style='background:#f8f9fa; padding:25px; border-radius:10px; border:2px solid #dee2e6; margin:20px 0;'>
<h4 style='color:#7f8c8d; margin-top:0;'>📊 Data & Methodology Note</h4>
<p style='color:#2c3e50; font-size:14px; line-height:1.6;'>
<strong>All projections, cost models, and impact estimates in this application are demonstration data</strong> created for portfolio and conceptual purposes. The underlying models are based on:
</p>
<ul style='color:#2c3e50; font-size:14px; line-height:1.6;'>
<li><strong>Climate scenarios:</strong> IPCC AR6 warming pathways and sea level rise projections</li>
<li><strong>Disaster cost modeling:</strong> Synthetic data using probabilistic simulation with realistic parameter ranges</li>
<li><strong>Evacuation impact:</strong> Informed by published research (Bangladesh Red Cross 2019, Start Network 2020, WFP 2021) but scaled for demonstration</li>
<li><strong>ROI calculations:</strong> Simplified economic modeling for illustrative purposes</li>
</ul>
<p style='color:#2c3e50; font-size:14px; line-height:1.6;'>
For a real-world implementation, all models would require:
</p>
<ul style='color:#2c3e50; font-size:14px; line-height:1.6;'>
<li>Peer-reviewed validation and sensitivity analysis</li>
<li>Location-specific historical disaster data</li>
<li>Actuarial assessment for insurance integration</li>
<li>Rigorous impact evaluation methodology (RCT or quasi-experimental design)</li>
</ul>
</p>
</div>""", unsafe_allow_html=True)
