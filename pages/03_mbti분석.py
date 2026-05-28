import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="🌍 국가별 MBTI 분석",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 비율을 그래프로 보여줘요!")

# 데이터 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요 ✈️",
    df["Country"].unique()
)

# 선택된 국가 데이터
selected = df[df["Country"] == country]

# MBTI 컬럼만 추출
mbti_data = selected.drop(columns=["Country"]).iloc[0]

# 내림차순 정렬
mbti_data = mbti_data.sort_values(ascending=False)

# 색상 설정
colors = []

# 1등 색상 (연노랑)
top_color = np.array([255, 245, 180]) / 255

# 스카이블루 시작/끝 색상
start_blue = np.array([180, 230, 255]) / 255
end_blue = np.array([230, 245, 255]) / 255

for i in range(len(mbti_data)):
    if i == 0:
        colors.append(top_color)
    else:
        ratio = i / (len(mbti_data) - 1)
        color = start_blue * (1 - ratio) + end_blue * ratio
        colors.append(color)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    mbti_data.index,
    mbti_data.values,
    color=colors
)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.002,
        f"{height:.2f}",
        ha='center',
        fontsize=9
    )

# 그래프 꾸미기
ax.set_title(f"{country}의 MBTI 비율", fontsize=18, pad=20)
ax.set_xlabel("MBTI 유형", fontsize=12)
ax.set_ylabel("비율", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

# 스트림릿 출력
st.pyplot(fig)

# 최고 MBTI 출력
top_mbti = mbti_data.idxmax()
top_value = mbti_data.max()

st.success(
    f"🏆 {country}에서 가장 높은 MBTI는 "
    f"'{top_mbti}' ({top_value:.2f}) 입니다!"
)
