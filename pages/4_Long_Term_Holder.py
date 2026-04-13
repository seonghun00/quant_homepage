import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import apply_global_style, render_page_header, render_footer

st.set_page_config(page_title="Long Term Holder", layout="wide")
apply_global_style()

render_page_header(
    title="Long Term Holder",
    description="장기 투자자(장기 보유자)들의 가격 및 행동 데이터를 바탕으로 시장의 강세장 여력을 분석합니다."
)

with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2, 1, 2])
with c2:
    if st.button("⬅ Back to Home", use_container_width=True):
        st.switch_page("app.py")

render_footer()
