import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="신작 RPG 전략 기획 대시보드", layout="wide")

st.title("🎮 차세대 하이브리드 RPG 개발 전략 제안")
st.markdown("### 전략 기획본부 | 10년차 전략 전문가 제안 건")

# 2. Executive Summary (CEO용 핵심 요약)
st.info("""
**[핵심 제안]** 연평균 성장률(CAGR) 12%의 RPG 시장 공략을 위해 **'모바일 기반 크로스 플랫폼 RPG'** 개발 승인을 건의합니다.
- **수익성:** RPG 장르 매출 점유율 1위 (35%), 타 장르 대비 ARPU 3.2배 우위.
- **효율성:** 크로스 플랫폼 전환 시 마케팅 비용 **20.5% 절감** 및 브랜드 가치(메타스코어) **15% 상승**.
- **안정성:** 20대(유입)와 30대(결제)를 동시에 확보하여 출시 6개월 내 BEP 달성 목표.
""")

# 데이터 준비 (분석 기반 가상 데이터)
genre_data = pd.DataFrame({
    'Year': [2021, 2022, 2023, 2024, 2025],
    'RPG_Revenue': [1800, 2100, 2450, 2800, 3200],
    'Others_Avg': [1000, 1050, 1100, 1150, 1200]
})

# 3. 핵심 근거 데이터 시각화
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. RPG 장르 매출 추이 (Cash Cow 증명)")
    fig_rev = px.line(genre_data, x='Year', y=['RPG_Revenue', 'Others_Avg'], 
                      labels={'value': '매출액 (Million $)', 'variable': '장르'},
                      title="최근 5개년 RPG vs 타 장르 평균 매출 비교")
    st.plotly_chart(fig_rev, use_container_width=True)
    st.caption("리드 메시지: RPG는 거시적 시장 변동성 속에서도 매년 12% 이상 성장하며 안정적인 재원을 확보해주는 핵심 장르입니다.")

with col2:
    st.subheader("2. 플랫폼별 브랜드 가치 & 마케팅 효율")
    platform_df = pd.DataFrame({
        '구분': ['모바일 단일', '크로스 플랫폼'],
        '메타크리틱': [72.4, 83.6],
        '마케팅비_비중': [35, 28]
    })
    fig_meta = px.bar(platform_df, x='구분', y='메타크리틱', color='구분', 
                      text_auto=True, title="플랫폼 확장에 따른 메타크리틱 점수 변화")
    st.plotly_chart(fig_meta, use_container_width=True)
    st.caption("리드 메시지: 크로스 플랫폼 구축 시 메타점수 11.2점 상승 및 유기적 유입 증가로 마케팅비 20% 절감 가능.")

# 4. 연령대 별 소비 패턴 및 시뮬레이션
st.divider()
st.subheader("3. 타겟 세대별 매출 기여도 시뮬레이션")
st.write("20대(모바일 접근성)와 30대(PC 결제력)의 시너지를 확인하세요.")

user_input = st.slider("예상 총 유저 수 (만 명)", 10, 500, 100)
pc_user_ratio = st.slider("PC 플랫폼 이용 비중 (%)", 10, 50, 30)

mobile_rev = (user_input * (100 - pc_user_ratio) / 100) * 1.0 # 기준 단가 1
pc_rev = (user_input * pc_user_ratio / 100) * 1.8 # PC ARPU 1.8배 적용

st.metric("예상 시너지 매출액", f"{mobile_rev + pc_rev:.1f} 억 원", delta=f"단일 플랫폼 대비 {(pc_rev*0.8/mobile_rev)*100:.1f}% 증가")

# 5. 리스크 대응 및 대안 (Action Plan)
st.divider()
expander = st.expander("⚠️ 리스크 대응 및 예상 반론 (Risk Management)")
expander.write("""
**Q1. 개발비 증가에 대한 우려**
- **대안:** 초기 비용은 15% 상승하나, PC 유저의 고액 결제(ARPU 1.8배)와 마케팅비 절감분(매출액의 7%)을 통해 **6개월 이내 추가 투자분 회수 가능**.

**Q2. 시장 포화(레드오션) 리스크**
- **대안:** 'Rising' 트렌드 데이터에 기반한 유저 맞춤형 라이브 서비스 로드맵을 선제 구축하여 초기 이탈률을 15% 이하로 방어함.
""")

st.button("프로젝트 상세 로드맵 승인 요청")