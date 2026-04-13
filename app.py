import streamlit as st
import os

from config import SITE_CONFIG
from components import apply_global_style, render_image, render_footer

# [중요] Streamlit에서는 set_page_config가 무조건 가장 처음 나타나야 에러가 나지 않습니다.
st.set_page_config(
    page_title="Quant Vision Dashboard",
    page_icon="♾️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 공통 스타일스틱 (마법 같은 CSS) 주입
apply_global_style()

# ==========================================
# [Hero Section] 최상단 대문 화면
# ==========================================
st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center;">
    <div class="pill-badge"><span class="pill-dot"></span>{SITE_CONFIG['hero']['badge']}</div>
    <div class="hero-title">{SITE_CONFIG['hero']['title']}</div>
    <div class="hero-subtitle">{SITE_CONFIG['hero']['subtitle']}</div>
</div>
""", unsafe_allow_html=True)

# 버튼 (중앙 정렬을 위해 좁은 칼럼 사용)
c1, c2, c3 = st.columns([2, 0.7, 2])
with c2:
    if st.button(SITE_CONFIG['hero']['btn'], key="hero_btn", use_container_width=True):
        st.switch_page(SITE_CONFIG["indexes"][0]["page"])

# 스크롤 마우스 안내
st.markdown("""
<div style="text-align: center; margin-top: 100px; color: #888; font-size: 0.95rem;">
    Scroll down 
    <span style="display:inline-block; margin: 0 15px; border:1px solid #777; width:16px; height:24px; border-radius:8px; position:relative; top:6px;">
        <span style="display:block; width:2px; height:4px; background:#777; border-radius:2px; position:absolute; top:4px; left:6px;"></span>
    </span> 
    to see projects
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 180px;'></div>", unsafe_allow_html=True)

# ==========================================
# [Index Sections]
# ==========================================
for i, item in enumerate(SITE_CONFIG["indexes"]):
    
    if i % 2 == 0:
        c1, c2 = st.columns([1.1, 1], gap="large") 
        with c1:
            render_image(item["image"])
        with c2:
            st.markdown(f"""
            <div style='margin-top: 8%;'>
                <div class="pill-badge"><span class="pill-dot"></span>{item["badge"]}</div>
                <div class="section-title">{item["title"]}</div>
                <div class="section-desc">{item["description"]}</div>
            </div>
            """, unsafe_allow_html=True)
            
            bc1, bc2 = st.columns([0.8, 1.2])
            with bc1:
                # 고유한 키 지정 (btn_id)
                if st.button(item['btn'], key=f"btn_{item['id']}", use_container_width=True): 
                    st.switch_page(item["page"])
                    
    else:
        c1, c2 = st.columns([1, 1.1], gap="large")
        with c1:
            st.markdown(f"""
            <div style='margin-top: 8%;'>
                <div class="pill-badge"><span class="pill-dot"></span>{item["badge"]}</div>
                <div class="section-title">{item["title"]}</div>
                <div class="section-desc">{item["description"]}</div>
            </div>
            """, unsafe_allow_html=True)
            
            bc1, bc2 = st.columns([0.8, 1.2]) 
            with bc1:
                if st.button(item['btn'], key=f"btn_{item['id']}", use_container_width=True): 
                    st.switch_page(item["page"])
                    
        with c2:
            render_image(item["image"])
            
    st.markdown("<div style='height: 180px;'></div>", unsafe_allow_html=True)

# ==========================================
# [Footer Section] 푸터 및 저작권
# ==========================================
render_footer()
