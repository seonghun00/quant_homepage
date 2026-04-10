import streamlit as st

st.set_page_config(page_title="Long Term Holder", layout="wide")

st.markdown("<h1>Quant Vision - Long Term Holder</h1>", unsafe_allow_html=True)
st.write("장기 투자자(장기 보유자)들의 가격 및 행동 데이터를 바탕으로 시장의 강세장 여력을 분석합니다.")

# 1. 차트를 넣을 빈 공간 컨테이너
with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("---")

# 2. 메인 화면으로 돌아가기 버튼
if st.button("⬅ 메인 화면으로 돌아가기", use_container_width=True):
    st.switch_page("app.py")
