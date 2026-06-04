import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="서울 기온 분석", layout="wide")

st.title("🌤️ 서울 날짜별 기온 변화 & 미래 기온 예측")
st.write("월과 일을 선택하면 연도별 최고기온·최저기온을 보여주고, 미래 연도의 기온을 예측합니다.")

# 데이터 불러오기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 컬럼 정리
df.columns = df.columns.str.strip()

# 날짜 변환
df["날짜"] = pd.to_datetime(df["날짜"], errors="coerce")

# 숫자 변환
df["최고기온(℃)"] = pd.to_numeric(df["최고기온(℃)"], errors="coerce")
df["최저기온(℃)"] = pd.to_numeric(df["최저기온(℃)"], errors="coerce")

# 결측치 제거
df = df.dropna(subset=["날짜", "최고기온(℃)", "최저기온(℃)"])

# 연도, 월, 일 만들기
df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

# 선택 영역
col1, col2, col3 = st.columns(3)

with col1:
    month = st.selectbox("📅 월 선택", list(range(1, 13)))

with col2:
    day = st.selectbox("📅 일 선택", list(range(1, 32)))

with col3:
    future_year = st.selectbox(
        "🔮 예측할 미래 연도 선택",
        list(range(2020, 2051))
    )

# 선택한 월/일 데이터
filtered_df = df[(df["월"] == month) & (df["일"] == day)]

if filtered_df.empty:
    st.warning("해당 날짜의 데이터가 없습니다.")
else:
    filtered_df = filtered_df.sort_values("연도")

    years = filtered_df["연도"].values
    max_temps = filtered_df["최고기온(℃)"].values
    min_temps = filtered_df["최저기온(℃)"].values

    # 선형 회귀로 미래 기온 예측
    max_model = np.polyfit(years, max_temps, 1)
    min_model = np.polyfit(years, min_temps, 1)

    predicted_max = np.polyval(max_model, future_year)
    predicted_min = np.polyval(min_model, future_year)

    # 그래프
    fig, ax = plt.subplots(figsize=(13, 6))

    ax.plot(
        filtered_df["연도"],
        filtered_df["최고기온(℃)"],
        color="#FFF4A3",
        linewidth=2.5,
        marker="o",
        label="최고기온"
    )

    ax.plot(
        filtered_df["연도"],
        filtered_df["최저기온(℃)"],
        color="#AEEBFF",
        linewidth=2.5,
        marker="o",
        label="최저기온"
    )

    # 예측값 표시
    ax.scatter(
        future_year,
        predicted_max,
        color="#FFD966",
        s=150,
        marker="*",
        label=f"{future_year}년 예측 최고기온"
    )

    ax.scatter(
        future_year,
        predicted_min,
        color="#7DDCFF",
        s=150,
        marker="*",
        label=f"{future_year}년 예측 최저기온"
    )

    ax.set_title(f"{month}월 {day}일 서울 기온 변화 및 {future_year}년 예측", fontsize=16)
    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    st.subheader("🔮 미래 기온 예측 결과")
    st.success(f"🌡️ {future_year}년 {month}월 {day}일 예측 최고기온: {predicted_max:.1f}℃")
    st.info(f"❄️ {future_year}년 {month}월 {day}일 예측 최저기온: {predicted_min:.1f}℃")

    st.caption("※ 이 예측은 과거 데이터의 기온 변화 추세를 이용한 단순 선형 예측입니다.")
