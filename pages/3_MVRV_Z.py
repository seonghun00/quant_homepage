import streamlit as st

st.set_page_config(page_title="MVRV Z-Score", layout="wide")

st.markdown("<h1>Quant Vision - MVRV Z-Score</h1>", unsafe_allow_html=True)
st.write("시장 가치와 실현 가치의 차이를 바탕으로 자산 가격 사이클의 과열과 바닥을 분석합니다.")

# 1. 차트를 넣을 빈 공간 컨테이너
with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("---")

# 2. 메인 화면으로 돌아가기 버튼
if st.button("⬅ 메인 화면으로 돌아가기", use_container_width=True):
    st.switch_page("app.py")
