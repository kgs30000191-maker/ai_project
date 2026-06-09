import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="어린이보호구역 CCTV 분석", layout="wide")

st.title("🚸 전국 어린이보호구역 CCTV 설치 비율 분석")
st.markdown("지역을 선택하면 해당 지역의 **시설종류별 CCTV 설치 비율**을 확인할 수 있어요.")

@st.cache_data
def load_data():
    df = pd.read_csv("전국어린이보호구역표준데이터 (1).csv", encoding="cp949")

    df["지역"] = df["소재지도로명주소"].fillna(df["소재지지번주소"]).str.split().str[0]
    df["CCTV설치여부"] = df["CCTV설치여부"].fillna("N")

    return df

df = load_data()

regions = sorted(df["지역"].dropna().unique())
selected_region = st.selectbox("📍 지역을 선택하세요", regions)

region_df = df[df["지역"] == selected_region]

summary = (
    region_df
    .groupby("시설종류")
    .agg(
        전체개수=("CCTV설치여부", "count"),
        CCTV설치수=("CCTV설치여부", lambda x: (x == "Y").sum())
    )
    .reset_index()
)

summary["CCTV설치비율"] = round(summary["CCTV설치수"] / summary["전체개수"] * 100, 1)
summary = summary.sort_values("CCTV설치비율", ascending=False)

colors = []
for i in range(len(summary)):
    if i == 0:
        colors.append("#FFF3A3")
    else:
        fade = 230 - i * 18
        fade = max(fade, 120)
        colors.append(f"rgb({fade}, {fade + 10}, 255)")

fig = px.bar(
    summary,
    x="시설종류",
    y="CCTV설치비율",
    text="CCTV설치비율",
    hover_data=["전체개수", "CCTV설치수"],
    title=f"{selected_region} 시설종류별 CCTV 설치 비율"
)

fig.update_traces(
    marker_color=colors,
    texttemplate="%{text}%",
    textposition="outside"
)

fig.update_layout(
    yaxis_title="CCTV 설치 비율 (%)",
    xaxis_title="시설종류",
    yaxis=dict(range=[0, 110]),
    template="plotly_white",
    title_font_size=22,
    font=dict(size=14),
    height=550
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 상세 데이터")
st.dataframe(summary, use_container_width=True)
