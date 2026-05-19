import streamlit as st
import numpy as np
import pandas as pd

# 1. 앱 제목 설정
st.title("📈 실시간 함수 그래프 시각화")
st.write("사이드바의 수치를 조절하면 그래프가 실시간으로 업데이트됩니다.")

---

# 2. 사이드바 제어 요소 (파일 필요 없음)
st.sidebar.header("🎛️ 그래프 제어")
frequency = st.sidebar.slider("주파수 (Frequency)", min_value=1.0, max_value=10.0, value=2.0, step=0.5)
amplitude = st.sidebar.slider("진폭 (Amplitude)", min_value=0.5, max_value=5.0, value=1.0, step=0.1)

---

# 3. 데이터 실시간 생성 (Numpy 연산)
# 0부터 10까지 500개의 구간으로 나눔
x = np.linspace(0, 10, 500)
# 사용자 입력값(진폭, 주파수)을 반영한 사인 함수 계산
y = amplitude * np.sin(frequency * x)

# 스트림릿 차트용 데이터프레임 만들기
chart_data = pd.DataFrame({
    'X축 (시간)': x,
    'Y축 (값)': y
}).set_index('X축 (시간)')

---

# 4. 결과 출력
st.subheader("📊 생성된 사인파(Sine Wave) 그래프")
st.line_chart(chart_data)

# 미니 통계 데이터 보여주기
st.subheader("📋 데이터 요약")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="최대값 (Max)", value=f"{chart_data['Y축 (값)'].max():.2f}")
with col2:
    st.metric(label="최소값 (Min)", value=f"{chart_data['Y축 (값)'].min():.2f}")
