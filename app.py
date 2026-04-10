import streamlit as st
import streamlit.components.v1 as components
import time

# 기본 설정 (와이드 레이아웃 설정, 기본 사이드바 접은 상태로 시작)
st.set_page_config(
    page_title="Quant Vision 3D",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 사이드바 숨김, 여백 및 스크롤바 제거 CSS
st.markdown("""
<style>
    /* 브라우저 강제 스크롤 문제 해결 */
    body {
        overflow: auto !important;
    }
    
    /* 상하좌우 여백 제거 */
    .stApp {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important; 
    }
    
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        width: 100vw !important;
    }
    
    /* 최상단 장식선 및 헤더 숨김 (투명 레이어 방해 완전 차단) */
    header { display: none !important; }
    
    /* 기본 사이드바 여는 컨트롤러 아예 숨김 */
    [data-testid="collapsedControl"] { display: none !important; }
    
    /* Streamlit이 생성하는 부모 컨테이너가 마우스를 가로채지 않도록 처리 */
    .element-container {
        pointer-events: auto !important;
        position: static !important;
        z-index: 999 !important;
    }
    
    /* iframe 제어: 16% 확대된 크기(116vw, 116vh)로 워터마크 마스킹 처리 및 최상단 렌더링 */
    iframe {
        height: 116vh !important;
        width: 116vw !important;
        border: none !important;
        display: block !important;
        pointer-events: auto !important; /* 클릭 이벤트 필수 보장 */
        position: absolute !important;   /* 플로우를 무시하고 최상단 배치 */
        left: -8vw !important;
        top: -8vh !important;
        z-index: 99999 !important;       /* 가장 위에 떠서 클릭 방해 최소화 */
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 1. 스플라인 URL 지정 공간
# -------------------------------------------------------------
# Spline 서버 자체(CDN)의 악질적인 캐싱을 확실히 뚫기 위해 실행 시마다 달라지는 타임스탬프를 강제로 붙입니다.
SPLINE_URL = f"https://my.spline.design/particles-IHksl0HfcSFe2DI7PICo1NYf/?t={int(time.time())}"

# 이중 iframe 구조로 인한 강력한 브라우저 캐싱과 components 패키지의 Deprecation 경고를 피하기 위해,
# st.markdown을 이용해 React DOM 상단에 직접 iframe 태그를 꽂아 넣어 렌더링합니다.
st.markdown(f"""
    <iframe src="{SPLINE_URL}" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking"></iframe>
""", unsafe_allow_html=True)
