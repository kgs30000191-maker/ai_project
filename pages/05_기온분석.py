import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="서울 기온 분석", layout="centered")

st.title("🌤️ 서울 최고기온 · 최저기온 분석")
st.write("날짜를 선택하면 그 날짜의 최고기온과 최저기온을 선 그래프로 보여줍니다.")

# 파일 불러오기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 컬럼 이름 공백 제거
df.columns = df.columns.str.strip()

# 날짜 변환 오류 방지
df["날짜"] = pd.to_datetime(df["날짜"], errors="coerce")

# 기온 데이터 숫자로 변환
df["최고기온(℃)"] = pd.to_numeric(df["최고기온(℃)"], errors="coerce")
df["최저기온(℃)"] = pd.to_numeric(df["최저기온(℃)"], errors="coerce")

# 필요한 데이터만 남기기
df = df[["날짜", "최고기온(℃)", "최저기온(℃)"]]
df = df.dropna()

# 날짜 기준 정렬
df = df.sort_values("날짜")

# 날짜 선택
selected_date = st.date_input(
    "📅 날짜를 선택하세요",
    value=df["날짜"].min().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

selected_date = pd.to_datetime(selected_date)

# 선택한 날짜의 데이터 찾기
selected_data = df[df["날짜"] == selected_date]

if selected_data.empty:
    st.warning("선택한 날짜의 기온 데이터가 없습니다.")
else:
    max_temp = selected_data["최고기온(℃)"].values[0]
    min_temp = selected_data["최저기온(℃)"].values[0]

    # 그래프용 데이터
    graph_df = pd.DataFrame({
        "기온 종류": ["최저기온", "최고기온"],
        "기온": [min_temp, max_temp]
    })

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(
        graph_df["기온 종류"],
        graph_df["기온"],
        marker="o",
        linewidth=3,
        markersize=10,
        color="#FFF4A3",
        label="최고기온"
    )

    ax.scatter(
        "최저기온",
        min_temp,
        color="#AEEBFF",
        s=120,
        label="최저기온"
    )

    ax.scatter(
        "최고기온",
        max_temp,
        color="#FFF4A3",
        s=120
    )

    ax.set_title(f"{selected_date.date()} 서울 기온", fontsize=16)
    ax.set_ylabel("기온(℃)")
    ax.grid(True, alpha=0.3)
    ax.legend()

    st.pyplot(fig)

    st.success(f"🌡️ 최고기온: {max_temp}℃")
    st.info(f"❄️ 최저기온: {min_temp}℃")
