import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="어린이보호구역 CCTV 분석", layout="wide")

st.title("🚸 전국 어린이보호구역 CCTV 분석")
st.write("지역을 선택하면 CCTV 설치 비율과 설치 현황을 확인할 수 있어요.")

@st.cache_data
def load_data():
    df = pd.read_csv("전국어린이보호구역표준데이터 (1).csv", encoding="cp949")

    df["주소"] = (
        df["소재지도로명주소"]
        .fillna(df["소재지지번주소"])
        .fillna("")
    )

    df["시도"] = df["주소"].apply(
        lambda x: str(x).split()[0] if len(str(x).split()) > 0 else "기타"
    )

    df["시군구"] = df["주소"].apply(
        lambda x: str(x).split()[1] if len(str(x).split()) > 1 else "기타"
    )

    df["CCTV설치여부"] = df["CCTV설치여부"].fillna("N")
    df["CCTV설치대수"] = pd.to_numeric(df["CCTV설치대수"], errors="coerce").fillna(0)

    return df

df = load_data()

st.sidebar.header("🔍 선택 메뉴")

regions = sorted([
    r for r in df["시도"].dropna().unique()
    if str(r).strip() != ""
])

selected_region = st.sidebar.selectbox("지역 선택", regions)

facility_list = ["전체"] + sorted(df["시설종류"].dropna().unique())
selected_facility = st.sidebar.selectbox("시설종류 선택", facility_list)

region_df = df[df["시도"] == selected_region]

if selected_facility != "전체":
    region_df = region_df[region_df["시설종류"] == selected_facility]

total = len(region_df)
yes = (region_df["CCTV설치여부"] == "Y").sum()
no = (region_df["CCTV설치여부"] == "N").sum()
rate = round(yes / total * 100, 1) if total > 0 else 0
cctv_count = int(region_df["CCTV설치대수"].sum())

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("전체 보호구역", f"{total:,}개")
c2.metric("CCTV 설치", f"{yes:,}개")
c3.metric("CCTV 미설치", f"{no:,}개")
c4.metric("설치 비율", f"{rate}%")
c5.metric("총 CCTV 대수", f"{cctv_count:,}대")

st.divider()

summary = (
    region_df
    .groupby("시군구")
    .agg(
        보호구역수=("CCTV설치여부", "count"),
        CCTV설치수=("CCTV설치여부", lambda x: (x == "Y").sum()),
        CCTV미설치수=("CCTV설치여부", lambda x: (x == "N").sum()),
        CCTV설치대수=("CCTV설치대수", "sum")
    )
    .reset_index()
)

summary["CCTV설치비율"] = round(summary["CCTV설치수"] / summary["보호구역수"] * 100, 1)
summary = summary.sort_values("CCTV설치비율", ascending=False)

colors = []
for i in range(len(summary)):
    if i == 0:
        colors.append("#FFF3A3")
    else:
        blue = max(140, 245 - i * 8)
        colors.append(f"rgb(160, {blue}, 255)")

st.subheader(f"📊 {selected_region} 시군구별 CCTV 설치 비율")

fig = px.bar(
    summary,
    x="시군구",
    y="CCTV설치비율",
    text="CCTV설치비율",
    hover_data=["보호구역수", "CCTV설치수", "CCTV미설치수", "CCTV설치대수"],
    title=f"{selected_region} 시군구별 CCTV 설치 비율"
)

fig.update_traces(
    marker_color=colors,
    texttemplate="%{text}%",
    textposition="outside"
)

fig.update_layout(
    template="plotly_white",
    yaxis_title="CCTV 설치 비율 (%)",
    xaxis_title="시군구",
    yaxis=dict(range=[0, 110]),
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📌 CCTV 설치 / 미설치 비교")

fig2 = px.bar(
    summary.sort_values("보호구역수", ascending=False),
    x="시군구",
    y=["CCTV설치수", "CCTV미설치수"],
    barmode="group",
    title=f"{selected_region} 시군구별 CCTV 설치·미설치 수 비교"
)

fig2.update_layout(
    template="plotly_white",
    xaxis_title="시군구",
    yaxis_title="개수",
    height=600
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("🏆 CCTV 설치 비율 TOP 10")

top10 = summary.head(10)

fig3 = px.bar(
    top10.sort_values("CCTV설치비율"),
    x="CCTV설치비율",
    y="시군구",
    orientation="h",
    text="CCTV설치비율",
    title=f"{selected_region} CCTV 설치 비율 TOP 10"
)

fig3.update_traces(
    marker_color="#FFF3A3",
    texttemplate="%{text}%",
    textposition="outside"
)

fig3.update_layout(
    template="plotly_white",
    xaxis_title="CCTV 설치 비율 (%)",
    yaxis_title="시군구",
    xaxis=dict(range=[0, 110]),
    height=550
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("📋 시군구별 분석 데이터")
st.dataframe(summary, use_container_width=True)

st.subheader("🗺️ 선택 지역 원본 데이터")

show_columns = [
    "대상시설명",
    "시설종류",
    "주소",
    "CCTV설치여부",
    "CCTV설치대수",
    "위도",
    "경도",
    "관리기관명",
    "데이터기준일자"
]

real_columns = [col for col in show_columns if col in region_df.columns]

st.dataframe(region_df[real_columns], use_container_width=True)

st.caption("데이터 출처: 전국어린이보호구역표준데이터")
