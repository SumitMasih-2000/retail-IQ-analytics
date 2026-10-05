import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ==============================================================================
# 1. APPLICATION ARCHITECTURE & THEME (MINT ENTERPRISE LUX)
# ==============================================================================
st.set_page_config(
    page_title="Retail Intelligence Suite",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Unified Style Sheets + Material Icon CDN Injection
st.markdown("""


""", unsafe_allow_html=True)

# ==============================================================================
# 2. DATA PIPELINE & GEO-COORDINATE RECOGNITION ENGINE
# ==============================================================================
DB_NAME = "retail_data.db"

COORDINATE_REGISTRY = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
    "Chicago": {"lat": 41.8781, "lon": -87.6298},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Tokyo": {"lat": 35.6762, "lon": 139.6503},
    "Paris": {"lat": 48.8566, "lon": 2.3522}
}

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            product_category TEXT,
            product_name TEXT,
            quantity INTEGER,
            unit_price REAL,
            total_revenue REAL,
            store_location TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(df):
    conn = sqlite3.connect(DB_NAME)
    df_copy = df.copy()
    df_copy['date'] = pd.to_datetime(df_copy['date']).dt.strftime('%Y-%m-%d')
    df_copy['total_revenue'] = df_copy['quantity'] * df_copy['unit_price']
    df_copy.to_sql('sales', conn, if_exists='append', index=False)
    conn.close()
    return df_copy

def fetch_analytics_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

init_db()

# ==============================================================================
# 3. SIDEBAR NAVIGATION CONTROLS
# ==============================================================================
with st.sidebar:
    try:
        st.image("logo.png", width=90)
    except Exception:
        st.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/external-analytics-marketing-flatart-icons-flat-flatarticons.png", width=70)
        with st.sidebar:
    try:
        st.image("logo.png", width=90)
    except Exception:
        st.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/external-analytics-marketing-flatart-icons-flat-flatarticons.png", width=70)
        
    st.markdown("## **Retail Intelligence**")
    st.caption("v2.9.0 • Custom Branding")
    
    # Cleaned single-line divider (No multi-line quotes)
    st.markdown("
