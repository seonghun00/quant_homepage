import streamlit as st
import sys
import os

# 모듈 탐색 경로를 상위 폴더로 확장하여 components 임포트 허용
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import apply_global_style, render_page_header, render_footer

st.set_page_config(page_title="S&P 500 & Margin Debt", layout="wide")
apply_global_style()

render_page_header(
    title="S&P 500 & Margin Debt", 
    description="전체 주식시장 추이 및 신용 거래 기반의 차입 투자 정도를 파악하는 지표입니다."
)

with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2, 1, 2])
with c2:
    if st.button("⬅ Back to Home", use_container_width=True):
        st.switch_page("app.py")

render_footer()
