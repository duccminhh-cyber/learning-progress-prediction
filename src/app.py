import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import shap
import joblib
from streamlit_shap import st_shap
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# =============================================================================
# 1. CẤU HÌNH TRANG & CSS (DARK MODE THEME)
# =============================================================================
st.set_page_config(
    page_title="Learning Analytics Dark",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS DARK MODE ---
st.markdown("""
<style>
    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        color: #FAFAFA; /* Chữ trắng */
    }

    /* Nền tổng thể của App (Màu đen sâu của Streamlit) */
    .stApp {
        background-color: #0E1117;
    }

    /* Tiêu đề Gradient (Neon effect) */
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        padding-bottom: 10px;
        text-shadow: 0px 0px 10px rgba(58, 123, 213, 0.3);
    }

    /* Card Style (Dark Card) */
    .dashboard-card {
        background-color: #262730; /* Màu xám đen của card */
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #363945; /* Viền nhẹ */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }

    /* KPI Card Styling */
    .kpi-title {
        color: #A6A9B6; /* Chữ xám nhạt */
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        color: #FFFFFF;
        font-size: 2rem;
        font-weight: 700;
        margin-top: 5px;
        text-shadow: 0 0 5px rgba(255,255,255,0.1);
    }
    .kpi-delta {
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 5px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #262730;
        border-right: 1px solid #363945;
    }

    /* Input Number & Selectbox */
    .stNumberInput input {
        color: white;
    }

    /* Dataframe */
    .stDataFrame {
        border: 1px solid #363945;
    }
</style>
""", unsafe_allow_html=True)

# Hàm vẽ KPI Card Dark Mode
def display_kpi(col, title, value, subtext, color_border="#00d2ff"):
    col.markdown(f"""
    <div class="dashboard-card" style="border-left: 4px solid {color_border};">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-delta" style="color: {color_border}">{subtext}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# 2. DATA LOADING CORE
# =============================================================================
@st.cache_data
def load_data_pro():
    try:
        data = joblib.load('../dashboard/dashboard_data.pkl')
    except:
        return None, None, None, None, None

    try:
        tc_dangky = np.array(data['tc_dangky'], dtype=float)
        raw_y = np.array(data['y_valid'], dtype=float)
        model = data['model']
        X_valid = data['X_valid']
        shap_values = data['shap_values']
        ids = data['student_ids']

        raw_preds = np.array(model.predict(X_valid), dtype=float)

        def normalize(vals, tcdk):
            if np.nanmean(vals) <= 1.5: return vals * tcdk
            return vals

        actual = normalize(raw_y, tc_dangky)
        preds = normalize(raw_preds, tc_dangky)

        # Post-process
        preds = np.clip(preds, 0, tc_dangky)
        mask_zero = (tc_dangky == 0)
        preds[mask_zero] = 0
        actual[mask_zero] = 0

        df = pd.DataFrame({
            'MA_SO_SV': ids, 'TC_DANGKY': tc_dangky,
            'Thực tế': actual, 'Dự báo': preds
        })
        df['Sai số'] = df['Thực tế'] - df['Dự báo']
        df['Sai số tuyệt đối'] = df['Sai số'].abs()

        return df, shap_values, X_valid, model, ids
    except:
        return None, None, None, None, None

df, shap_values, X_valid, model, ids = load_data_pro()

if df is None:
    st.error("❌ Không thể tải dữ liệu. Vui lòng kiểm tra file 'dashboard_data.pkl'.")
    st.stop()

# =============================================================================
# 3. SIDEBAR (DARK THEME)
# =============================================================================
with st.sidebar:
    st.markdown("### 🎓 **Dashboard 4_chị_em_412**")
    st.markdown("---")

    st.write("🔍 **Tra cứu Sinh viên**")

    st.info("Nhập số thứ tự (Index) của sinh viên để xem phân tích chi tiết.")

    if len(df) > 0:
        max_idx = len(df) - 1
        selected_idx = st.number_input(
            f"Nhập STT sinh viên (0 - {max_idx}):",
            min_value=0, max_value=max_idx, value=0, step=1
        )

        st.markdown("---")
        st.write("📌 **Sinh viên đang chọn:**")
        curr_row = df.iloc[selected_idx]
        st.write(f"**Mã SV:** {curr_row['MA_SO_SV']}")
        st.write(f"**Đăng ký:** {curr_row['TC_DANGKY']:.0f} tín chỉ")
    else:
        st.warning("Chưa có dữ liệu.")
        st.stop()

    st.markdown("---")
    st.caption("© 2026 DarkMode UI Version")

# =============================================================================
# 4. MAIN DASHBOARD AREA
# =============================================================================

# --- Header ---
st.markdown('<div class="gradient-text">🔮 Dự báo Kết quả Học tập</div>', unsafe_allow_html=True)
st.markdown("---")

# --- KPI Section ---
try:
    rmse = np.sqrt(mean_squared_error(df['Thực tế'], df['Dự báo']))
    mae = mean_absolute_error(df['Thực tế'], df['Dự báo'])
    r2 = r2_score(df['Thực tế'], df['Dự báo'])
    acc = np.mean(df['Sai số tuyệt đối'] <= 2.0) * 100

    col1, col2, col3, col4 = st.columns(4)
    # Sử dụng các màu Neon sáng trên nền đen
    display_kpi(col1, "RMSE (Sai số chuẩn)", f"{rmse:.2f}", "Tín chỉ", "#00d2ff") # Cyan
    display_kpi(col2, "MAE (Sai số TB)", f"{mae:.2f}", "Tín chỉ", "#00e676") # Neon Green
    display_kpi(col3, "R² Score", f"{r2:.1%}", "Variance", "#ffab00") # Amber
    display_kpi(col4, "Độ chính xác (±2 tín)", f"{acc:.1f}%", "Confidence", "#ff1744") # Neon Red

except Exception as e:
    st.error(f"Lỗi tính toán KPI: {e}")

st.markdown("<br>", unsafe_allow_html=True)

# --- Charts Section ---
c1, c2 = st.columns(2)

# Cấu hình chung cho biểu đồ tối màu
layout_dark = dict(
    paper_bgcolor='rgba(0,0,0,0)', # Nền trong suốt
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FAFAFA'),
    xaxis=dict(showgrid=True, gridcolor='#444'),
    yaxis=dict(showgrid=True, gridcolor='#444')
)

with c1:
    st.markdown("##### 📉 Tương quan (Thực tế - Dự báo)")

    fig_scatter = px.scatter(
        df, x='Thực tế', y='Dự báo',
        color='Sai số tuyệt đối',
        # Dùng dải màu tối (Magma/Plasma) cho nổi trên nền đen
        color_continuous_scale='Plasma_r',
        hover_data=['MA_SO_SV', 'TC_DANGKY'],
        height=500
    )
    fig_scatter.update_layout(**layout_dark)
    fig_scatter.add_shape(type="line", x0=0, y0=0, x1=df['TC_DANGKY'].max(), y1=df['TC_DANGKY'].max(),
                          line=dict(dash='dash', color='#ff1744', width=2))

    st.plotly_chart(fig_scatter, width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown("##### 📊 Phân phối Độ lệch (Thực tế - Dự báo)")

    fig_hist = px.histogram(
        df, x='Sai số', nbins=50, marginal="box",
        color_discrete_sequence=['#00d2ff'], # Màu Cyan nổi bật
        height=500
    )
    fig_hist.update_layout(**layout_dark)
    fig_hist.add_vline(x=0, line_dash="dash", line_color="#ff1744")

    st.plotly_chart(fig_hist, width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# 5. STUDENT DETAIL & SHAP
# =============================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="gradient-text" style="font-size: 1.8rem;">🧬 Phân tích Chi tiết (Explainable AI)</div>', unsafe_allow_html=True)

col_metric, col_viz = st.columns([1, 2])

with col_metric:
    st.markdown(f"#### Hồ sơ: `{curr_row['MA_SO_SV']}`")
    st.markdown("---")

    delta = curr_row['Thực tế'] - curr_row['Dự báo']
    delta_color = "normal"
    if abs(delta) > 3: delta_color = "inverse"

    st.metric("Số tín chỉ Đăng ký", f"{curr_row['TC_DANGKY']:.0f}")
    st.metric("Mô hình Dự báo", f"{curr_row['Dự báo']:.2f}", help="AI dự đoán")
    st.metric("Thực tế đạt được", f"{curr_row['Thực tế']:.2f}", delta=f"{delta:.2f}", delta_color=delta_color)

    percent = (curr_row['Dự báo'] / (curr_row['TC_DANGKY'] + 0.01)) * 100
    st.write(f"Tiến độ dự báo: **{percent:.1f}%**")
    st.progress(min(int(percent), 100))

    if percent < 50:
        st.error("⚠️ RỦI RO CAO")
    elif percent < 80:
        st.warning("⚠️ CẢNH BÁO")
    else:
        st.success("✅ AN TOÀN")

with col_viz:
    st.markdown("##### Yếu tố tác động (SHAP Waterfall)")
    try:
        # SHAP Waterfall mặc định nền trắng, hơi khó chỉnh CSS can thiệp sâu
        # Nhưng st_shap vẫn hiển thị tốt trên nền đen
        st_shap(shap.plots.waterfall(shap_values[selected_idx], max_display=10), height=400)
    except:
        st.warning("Dữ liệu SHAP không khả dụng.")

st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# 6. FOOTER
# =============================================================================
with st.expander("📂 Xem dữ liệu chi tiết (Raw Data)"):
    st.dataframe(df, width="stretch", height=300)
