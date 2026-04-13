# config.py

SITE_CONFIG = {
    # << 메인 히어로 섹션 >>
    "hero": {
        "badge": "beyond emotion",
        "title": "Precision in Every Wave,<br>Quant Vision", 
        "subtitle": "감정을 배제하고 검증된 지표와 온체인 데이터로 시장을 정의합니다.",
        "btn": "Explore Metrics"
    },
    
    # << 인덱스(메뉴) 리스트 >>
    "indexes": [
        {
            "id": 1,
            "badge": "Market Sentiment & Leverage", 
            "title": "S&P 500 / FINIRA Margin Debt Ratio",
            "description": "S&P 500의 지수 흐름과 투자자들의 신용 융자 잔고(Margin Debt)를 대조하여 시장의 과열 상태를 진단합니다. 레버리지가 극점에 달했을 때의 리스크를 데이터로 확인하세요.",
            "image": "assets/index1.png", 
            "page": "pages/1_SP500_Margin.py",
            "btn": "Analyze Margin Debt"
        },
        {
            "id": 2,
            "badge": "Macro Valuation",
            "title": "Buffit Indicator",
            "description": "워런 버핏이 가장 신뢰하는 지표로 알려진 버핏 지수는 국가 전체 GDP 대비 시가총액의 비율을 통해 현재 주식 시장의 저평가 혹은 고평가 여부를 거시적으로 판단합니다.",
            "image": "assets/index2.png",
            "page": "pages/2_Buffet_Indicator.py",
            "btn": "Check Valuation"
        },
        {
            "id": 3,
            "badge": "On-chain Analysis",
            "title": "MVRV Z-Score",
            "description": "비트코인의 실현 가치(Realized Value)와 시가 총액 사이의 괴리를 분석합니다. Z-Score를 통해 자산이 역사적으로 과매수 되었는지, 혹은 매력적인 매수 구간에 진입했는지 포착합니다.",
            "image": "assets/index3.png",
            "page": "pages/3_MVRV_Z.py",
            "btn": "View Z-Score"
        },
        {
            "id": 4,
            "badge": "Smart Money Supply",
            "title": "Long Term Holder",
            "description": "155일 이상 코인을 보유한 장기 보유자들의 물량 변화를 추적합니다. '스마트 머니'의 매집과 분산 과정을 통해 다음 메이저 트렌드의 방향성을 예측합니다.",
            "image": "assets/index4.png",
            "page": "pages/4_Long_Term_Holder.py",
            "btn": "Track Holder Data"
        }
    ],
    
    # << 푸터(하단 영역) >>
    "footer": {
        "badge": "Available For Work",
        "title": "See More On TradingView Below",
        "email": "baeseonghun@naver.com",
        "platform": "Design by seonghun",
        "copyright": "All rights reserved, ©2026",
        "blog_url": "https://kr.tradingview.com/u/baeseonghun/",
        "btn": "Visit Blog"
    }
}
