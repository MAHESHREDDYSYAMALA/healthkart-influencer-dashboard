import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")

st.markdown("""
    <style>
    .metric-card {
        background: #f5f7fa;
        border-radius: 1.2rem;
        padding: 1.5rem 1.2rem 1.2rem 1.2rem;
        box-shadow: 0 2px 8px rgba(44,62,80,0.07);
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .metric-label {
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 0.2rem;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #2563eb;
    }
    .metric-icon {
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💡 HealthKart Influencer Campaign Dashboard")

# Load data
data_dir = "data"

def load_csv(filename):
    path = os.path.join(data_dir, filename)
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.warning(f"{filename} not found.")
        return pd.DataFrame()

influencers = load_csv("influencers.csv")
posts = load_csv("posts.csv")
tracking_data = load_csv("tracking_data.csv")
payouts = load_csv("payouts.csv")

# Sidebar filters
st.sidebar.image("https://placehold.co/80x80/2563EB/FFF?text=HK", width=80)
st.sidebar.title("Filters")
platforms = influencers['platform'].unique() if not influencers.empty else []
platform = st.sidebar.multiselect("Platform", platforms, default=list(platforms))

categories = influencers['category'].unique() if not influencers.empty else []
category = st.sidebar.multiselect("Category", categories, default=list(categories))

# Filter data
def filter_df(df, col, values):
    if df.empty or not values:
        return df
    return df[df[col].isin(values)]

influencers_f = filter_df(influencers, 'platform', platform)
influencers_f = filter_df(influencers_f, 'category', category)

# Metrics Section
st.markdown("---")
st.subheader("📊 Campaign Summary")

col1, col2, col3, col4 = st.columns(4)
if not tracking_data.empty and not payouts.empty:
    total_revenue = tracking_data['revenue'].sum()
    total_payout = payouts['total_payout'].sum()
    roas = total_revenue / total_payout if total_payout else 0
    n_posts = posts.shape[0]
    n_influencers = influencers.shape[0]
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-icon">💰</div><div class="metric-label">Total Revenue</div><div class="metric-value">₹{:,.0f}</div></div>'.format(total_revenue), unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-icon">🪙</div><div class="metric-label">Total Payout</div><div class="metric-value">₹{:,.0f}</div></div>'.format(total_payout), unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-icon">📈</div><div class="metric-label">ROAS</div><div class="metric-value">{:.2f}x</div></div>'.format(roas), unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-icon">🧑‍🤝‍🧑</div><div class="metric-label">Influencers</div><div class="metric-value">{}</div></div>'.format(n_influencers), unsafe_allow_html=True)

st.markdown("---")

# Section: Influencers
st.subheader("🧑‍💼 Influencers")
st.dataframe(influencers_f, use_container_width=True, hide_index=True)

# Section: Posts
st.subheader("📝 Posts")
st.dataframe(posts.head(50), use_container_width=True, hide_index=True)

# Section: Tracking Data
st.subheader("📦 Tracking Data")
st.dataframe(tracking_data.head(50), use_container_width=True, hide_index=True)

# Section: Payouts
st.subheader("💸 Payouts")
st.dataframe(payouts, use_container_width=True, hide_index=True)

st.markdown("---")
st.info("Expand this dashboard with more analytics, charts, and insights as needed!")
