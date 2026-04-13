import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import apply_global_style, render_page_header, render_footer

st.set_page_config(page_title="Buffet Indicator", layout="wide")
apply_global_style()

render_page_header(
    title="Buffet Indicator",
    description="국내총생산(GDP) 대비 시가총액 비율을 통해 주식시장이 고평가되었는지 저평가되었는지 판단합니다."
)

with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2, 1, 2])
with c2:
    if st.button("⬅ Back to Home", use_container_width=True):
        st.switch_page("app.py")

render_footer()
