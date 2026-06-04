import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="서울 기온 그래프", layout="centered")

st.title("🌤️ 서울 최고기온 · 최저기온 그래프")
st.write("날짜를 선택하면 해당 날짜의 최고기온과 최저기온을 선 그래프로 보여줘요.")

df = pd.read_csv("seoul.csv", encoding="cp949")

df.columns = df.columns.str.strip()

df["날짜"] = pd.to_datetime(df["날짜"], errors="coerce")
df = df.dropna(subset=["날짜"])

df["최고기온(℃)"] = pd.to_numeric(df["최고기온(℃)"], errors="coerce")
df["최저기온(℃)"] = pd.to_numeric(df["최저기온(℃)"], errors="coerce")

df = df[["날짜", "최고기온(℃)", "최저기온(℃)"]].dropna()

selected_date = st.date_input(
    "날짜를 선택하세요",
    value=df["날짜"].min().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

selected_date = pd.to_datetime(selected_date)

selected_data = df[df["날짜"] == selected_date]

if selected_data.empty:
    st.warning("선택한 날짜의 기온 데이터가 없습니다.")
else:
    max_temp = selected_data["최고기온(℃)"].values[0]
    min_temp = selected_data["최저기온(℃)"].values[0]

    chart_df = pd.DataFrame({
        "구분": ["최저기온", "최고기온"],
        "최저기온": [min_temp, None],
        "최고기온": [None, max_temp]
    })

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(
        chart_df["구분"],
        chart_df["최고기온"],
        marker="o",
        linewidth=3,
        markersize=10,
        color="#FFF4A3",
        label="최고기온"
    )

    ax.plot(
        chart_df["구분"],
        chart_df["최저기온"],
        marker="o",
        linewidth=3,
        markersize=10,
        color="#AEEBFF",
        label="최저기온"
    )

    ax.set_title(f"{selected_date.date()} 서울 기온", fontsize=16)
    ax.set_ylabel("기온(℃)")
    ax.grid(True, alpha=0.3)
    ax.legend()

    st.pyplot(fig)

    st.success(f"🌡️ 최고기온: {max_temp}℃")
    st.info(f"❄️ 최저기온: {min_temp}℃")
