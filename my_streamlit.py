
import streamlit as st
import pandas as pd
import numpy as np

# 1. 앱 제목 및 텍스트 설정
st.title("🚀 나의 첫 스트림릿 웹 앱")
st.header("간단한 데이터 시각화 및 입력 예제")
st.write("스트림릿을 사용하면 파이썬 코드가 그대로 멋진 웹 사이트가 됩니다.")

---

# 2. 사이드바 만들기
st.sidebar.header("⚙️ 설정 메뉴")
user_name = st.sidebar.text_input("이름을 입력하세요:", "홍길동")
sample_size = st.sidebar.slider("생성할 데이터 개수", min_value=10, max_value=200, value=100)

---

# 3. 데이터 입력 및 사용자 반응 (Widget)
st.subheader(f"👋 환영합니다, {user_name}님!")

# 버튼 클릭 이벤트
if st.button("인사말 건네기"):
    st.success(f"{user_name}님, 오늘도 좋은 하루 되세요!")

---

# 4. 데이터프레임 및 차트 그리기
st.subheader("📊 무작위 데이터 시각화")

# 사이드바에서 선택한 개수만큼 랜덤 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(sample_size, 3),
    columns=['데이터 A', '데이터 B', '데이터 C']
)

# 데이터프레임 출력
st.write("생성된 데이터의 일부입니다:")
st.dataframe(chart_data.head())

# 라인 차트 출력
st.write("선 그래프 차트:")
st.line_chart(chart_data)

---

# 5. 선택 상자 (Selectbox) 예시
st.subheader("🔍 보기 선택")
option = st.selectbox(
    '가장 좋아하는 프로그래밍 언어는?',
    ['Python', 'Java', 'JavaScript', 'C++']
)
st.write(f'선택하신 언어는 **{option}** 입니다.')
