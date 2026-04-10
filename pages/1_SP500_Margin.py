import streamlit as st

st.set_page_config(page_title="S&P 500 & Margin Debt", layout="wide")

st.markdown("<h1>Quant Vision - S&P 500 & Margin Debt</h1>", unsafe_allow_html=True)
st.write("전체 주식시장 추이 및 신용 거래 기반의 차입 투자 정도를 파악하는 지표입니다.")

# 1. 차트를 넣을 빈 공간 컨테이너
with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("---")

# 2. 메인 화면으로 돌아가기 버튼
if st.button("⬅ 메인 화면으로 돌아가기", use_container_width=True):
    st.switch_page("app.py")
