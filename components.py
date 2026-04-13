import streamlit as st
import os
import base64
from config import SITE_CONFIG

def find_image_path(base_name):
    """
    assets 폴더 내에서 .png, .jpg, .jpeg 파일 확장자가 달라도 자동으로 찾아줍니다.
    """
    if os.path.exists(base_name):
        return base_name
        
    name, _ = os.path.splitext(base_name)
    extensions = ['.png', '.jpg', '.jpeg', '.webp', '.PNG', '.JPG']
    for ext in extensions:
        if os.path.exists(name + ext):
            return name + ext
    return base_name

def get_bg_css():
    """
    main_bg 사진을 찾아 마법 같은 다중 그라데이션 오버레이 CSS를 생성합니다.
    """
    bg_path = find_image_path("assets/main_bg.png")
    if os.path.exists(bg_path):
        with open(bg_path, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        ext = bg_path.split('.')[-1].lower()
        mime = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
        
        return f"""
        .stApp {{
            background-color: #050505 !important;
            background-image: 
                linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                linear-gradient(to bottom, transparent 650px, #050505 900px),
                url("data:{mime};base64,{encoded_string}"),
                linear-gradient(to top, transparent 400px, #050505 600px),
                url("data:{mime};base64,{encoded_string}");
            background-position: 
                top left,
                top center, top center,
                bottom center, bottom center;
            background-repeat: 
                repeat,
                no-repeat, no-repeat,
                no-repeat, no-repeat;
            background-size: 
                100% 100%,
                100% 900px, 100% 900px,
                100% 600px, 100% 600px;
        }}
        """
    return ".stApp { background-color: #050505 !important; }"

def apply_global_style():
    """
    모든 페이지에 공통으로 적용될 전역 CSS 스타일 (유리막, 폰트, 버튼 호버 등)을 주입합니다.
    """
    st.markdown(f"""
    <style>
        {get_bg_css()}
        
        [data-testid="stHeader"] {{
            display: none;
        }}
        
        [data-testid="block-container"] {{
            padding-top: 2rem !important; 
        }}
        
        .stApp, div, h1, h2, h3, p, span {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}

        /* 알약 모양의 상단 뱃지 */
        .pill-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 50px;
            padding: 6px 16px;
            font-size: 0.85rem;
            color: #dedede;
            margin-bottom: 20px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }}
        .pill-dot {{
            width: 6px;
            height: 6px;
            background-color: #dedede;
            border-radius: 50%;
        }}

        /* Hero(최상단) 텍스트 디자인 */
        .hero-title {{
            font-size: 4.8rem;
            font-weight: 500;
            line-height: 1.1;
            text-align: center;
            color: #ffffff;
            margin-bottom: 25px;
            letter-spacing: -2px;
        }}
        .hero-subtitle {{
            font-size: 1.1rem;
            text-align: center;
            color: #bbbbbb;
            margin-bottom: 45px;
            font-weight: 300;
            line-height: 1.6;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
        }}

        /* 푸터 타이틀용 */
        .footer-title {{
            font-size: 3.2rem;
            font-weight: 500;
            line-height: 1.1;
            text-align: center;
            color: #ffffff;
            margin-top: 10px;
            margin-bottom: 40px;
            letter-spacing: -1.5px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }}

        /* 각 섹션별 제목 및 본문 폰트 */
        .section-title {{
            color: #ffffff;
            font-size: 3.8rem;
            font-weight: 500;
            line-height: 1.1;
            margin-bottom: 20px;
            letter-spacing: -1.5px;
        }}
        .section-desc {{
            color: #bbbbbb; 
            font-size: 1.15rem;
            line-height: 1.6;
            margin-bottom: 40px;
            font-weight: 300;
            word-break: keep-all; 
        }}

        /* 유리막 버튼 형태 복구 + 대각선 빛 반사 효과 */
        .stButton>button {{
            background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 40%, rgba(255,255,255,0.05) 100%) !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            border-top: 1px solid rgba(255,255,255,0.6) !important;
            border-left: 1px solid rgba(255,255,255,0.5) !important;
            color: #ffffff !important;
            border-radius: 40px !important; 
            padding: 0.6rem 1.2rem !important; 
            min-height: 42px !important; 
            font-weight: 500;
            font-size: 0.95rem !important;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: 
                inset 2px 2px 5px rgba(255,255,255,0.1),
                0 4px 10px rgba(0,0,0,0.3) !important; 
            width: 100%;
            max-width: 250px; 
            margin: 0 auto;
        }}
        .stButton>button:hover {{
            border-color: rgba(255, 255, 255, 0.7) !important;
            background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0.05) 40%, rgba(255,255,255,0.1) 100%) !important;
            box-shadow: 0 0 15px rgba(255,255,255,0.15), inset 2px 2px 5px rgba(255,255,255,0.3);
            transform: translateY(-1px);
        }}

        /* 이미지 기본 설정 및 날카롭게 렌더링 (모든 페이지 공통 적용) */
        img {{
            border-radius: 20px;
            image-rendering: -webkit-optimize-contrast;
            image-rendering: crisp-edges;
            -ms-interpolation-mode: nearest-neighbor;
        }}
        
        /* 로고나 아이콘이 들어가는 컨테이너 해상도 고정 */
        .stImage > img {{
            width: auto;
            max-width: 100%;
        }}
        
        /* 하단 트레이딩뷰 링크 전용 호버 효과 (순수 SVG) */
        .tv-link {{
            color: rgba(255,255,255,0.7) !important;
            text-decoration: none !important;
            transition: all 0.3s ease;
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 0px; 
            cursor: pointer;
        }}
        .tv-link svg {{
            opacity: 0.7;
            transition: all 0.3s ease;
        }}
        .tv-link:hover {{
            color: #ffffff !important;
            transform: translateY(-3px);
        }}
        .tv-link:hover svg {{
            opacity: 1;
            filter: drop-shadow(0px 4px 10px rgba(255,255,255,0.15));
        }}
    </style>
    """, unsafe_allow_html=True)


def render_image(image_path):
    """
    이미지 렌더링 헬퍼 컴포넌트
    """
    path = find_image_path(image_path)
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.markdown(f"""
        <div style="width:100%; height:400px; background:rgba(255,255,255,0.03); border-radius:20px; border:1px solid rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:#555; font-size: 1.2rem;">
            📷 이미지 셋업 필요 ({image_path} / jpg, png 지원)
        </div>
        """, unsafe_allow_html=True)


def render_footer():
    """
    모든 페이지 하단에 공통으로 렌더링될 푸터 컴포넌트
    """
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin-top: 50px;">
        <div class="pill-badge"><span class="pill-dot"></span>{SITE_CONFIG['footer']['badge']}</div>
        <div class="footer-title">{SITE_CONFIG['footer']['title']}</div>
    </div>
    """, unsafe_allow_html=True)

    blog_url = SITE_CONFIG["footer"]["blog_url"]

    tv_svg_html = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 6 24 12.5" width="60" height="32" style="margin-bottom: 5px;">
      <path fill="currentColor" d="M15.8654 8.2789c0 1.3541-1.0978 2.4519-2.452 2.4519-1.354 0-2.4519-1.0978-2.4519-2.452 0-1.354 1.0978-2.4518 2.452-2.4518 1.3541 0 2.4519 1.0977 2.4519 2.4519zM9.75 6H0v4.9038h4.8462v7.2692H9.75Zm8.5962 0H24l-5.1058 12.173h-5.6538z"/>
    </svg>
    """

    st.markdown(f"""
    <div style="text-align:center; margin: 40px 0;">
    <a href="{blog_url}" target="_blank" class="tv-link">
    {tv_svg_html}
    <div style="font-size: 1.1rem; font-weight: 400; letter-spacing: 0.5px; margin-top:12px;">{SITE_CONFIG['footer']['btn']}</div>
    </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; padding-bottom: 25px; font-size: 0.9rem; color: #ffffff;">
        <div>{SITE_CONFIG['footer']['platform']}</div>
        <div>{SITE_CONFIG['footer']['copyright']}</div>
    </div>
    """, unsafe_allow_html=True)

def render_page_header(title, description):
    """
    서브 페이지의 타이틀 및 설명을 렌더링하는 공통 컴포넌트
    """
    st.markdown(f"<h1 class='section-title' style='text-align:left; font-size: 3.2rem;'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-desc' style='text-align:left; font-size: 1.15rem; color: #bbbbbb;'>{description}</div>", unsafe_allow_html=True)

