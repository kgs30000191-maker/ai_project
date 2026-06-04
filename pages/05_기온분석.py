import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="서울 기온 분석", layout="wide")

st.title("🌤️ 서울 날짜별 기온 변화 분석")
st.write("월과 일을 선택하면 해당 날짜의 연도별 최고기온과 최저기온을 보여줍니다.")

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

# 연도, 월, 일 추출
df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

# 월 선택
month = st.selectbox(
    "📅 월 선택",
    list(range(1, 13))
)

# 일 선택
day = st.selectbox(
    "📅 일 선택",
    list(range(1, 32))
)

# 데이터 필터링
filtered_df = df[
    (df["월"] == month) &
    (df["일"] == day)
]

if filtered_df.empty:
    st.warning("해당 날짜의 데이터가 없습니다.")
else:

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        filtered_df["연도"],
        filtered_df["최고기온(℃)"],
        color="#FFF4A3",
        linewidth=2.5,
        label="최고기온"
    )

    ax.plot(
        filtered_df["연도"],
        filtered_df["최저기온(℃)"],
        color="#AEEBFF",
        linewidth=2.5,
        label="최저기온"
    )

    ax.set_title(f"{month}월 {day}일 서울 기온 변화")
    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    hottest = filtered_df.loc[
        filtered_df["최고기온(℃)"].idxmax()
    ]

    coldest = filtered_df.loc[
        filtered_df["최저기온(℃)"].idxmin()
    ]

    st.success(
        f"🔥 가장 더웠던 {month}월 {day}일: "
        f"{hottest['연도']}년 ({hottest['최고기온(℃)']}℃)"
    )

    st.info(
        f"❄️ 가장 추웠던 {month}월 {day}일: "
        f"{coldest['연도']}년 ({coldest['최저기온(℃)']}℃)"
    )
