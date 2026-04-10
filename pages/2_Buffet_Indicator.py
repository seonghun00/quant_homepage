import streamlit as st

st.set_page_config(page_title="Buffet Indicator", layout="wide")

st.markdown("<h1>Quant Vision - Buffet Indicator</h1>", unsafe_allow_html=True)
st.write("국내총생산(GDP) 대비 시가총액 비율을 통해 주식시장이 고평가되었는지 저평가되었는지 판단합니다.")

# 1. 차트를 넣을 빈 공간 컨테이너
with st.container(border=True):
    st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; color: gray;'>[차트가 들어갈 공간입니다]</div>", unsafe_allow_html=True)

st.markdown("---")

# 2. 메인 화면으로 돌아가기 버튼
if st.button("⬅ 메인 화면으로 돌아가기", use_container_width=True):
    st.switch_page("app.py")
