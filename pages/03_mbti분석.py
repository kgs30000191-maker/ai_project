import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🌍 MBTI 국가 분석",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 MBTI 유형별 국가 TOP10")
st.markdown("MBTI 유형을 선택하면 비율이 가장 높은 나라 TOP10을 보여줘요!")

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼 목록
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# -----------------------------
# MBTI 선택
# -----------------------------
selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요 💡",
    mbti_types
)

# -----------------------------
# TOP10 국가 추출
# -----------------------------
top10 = df[['Country', selected_mbti]] \
    .sort_values(by=selected_mbti, ascending=False) \
    .head(10)

# -----------------------------
# 색상 설정
# 1등: 연노랑
# 나머지: 스카이블루 그라데이션
# -----------------------------
colors = []

top_color = np.array([255, 245, 180]) / 255

start_blue = np.array([120, 200, 255]) / 255
end_blue = np.array([220, 245, 255]) / 255

for i in range(len(top10)):
    if i == 0:
        colors.append(top_color)
    else:
        ratio = i / (len(top10) - 1)
        color = start_blue * (1 - ratio) + end_blue * ratio
        colors.append(color)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    top10['Country'],
    top10[selected_mbti],
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

# -----------------------------
# 그래프 꾸미기
# -----------------------------
ax.set_title(
    f"{selected_mbti} 비율이 높은 나라 TOP10 🌎",
    fontsize=18,
    pad=20
)

ax.set_xlabel("국가", fontsize=12)
ax.set_ylabel("비율", fontsize=12)

plt.xticks(rotation=30)
plt.tight_layout()

# -----------------------------
# 출력
# -----------------------------
st.pyplot(fig)

# 1위 국가 출력
first_country = top10.iloc[0]['Country']
first_score = top10.iloc[0][selected_mbti]

st.success(
    f"🏆 {selected_mbti} 비율 1위 국가는 "
    f"{first_country} ({first_score:.2f}) 입니다!"
)

# -----------------------------
# 표도 함께 출력
# -----------------------------
st.subheader("📋 TOP10 데이터")

top10_display = top10.reset_index(drop=True)
top10_display.index = top10_display.index + 1

st.dataframe(top10_display)
