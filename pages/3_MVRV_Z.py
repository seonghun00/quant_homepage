import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import apply_global_style, render_page_header, render_footer

st.set_page_config(page_title="MVRV Z-Score", layout="wide")
apply_global_style()

render_page_header(
    title="MVRV Z-Score",
    description="시장 가치와 실현 가치의 차이를 바탕으로 자산 가격 사이클의 과열과 바닥을 분석합니다."
)

with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2, 1, 2])
with c2:
    if st.button("⬅ Back to Home", use_container_width=True):
        st.switch_page("app.py")

render_footer()
