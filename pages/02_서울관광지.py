import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🇰🇷 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("서울의 인기 관광지를 지도에서 확인해보세요! ✨")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "location": [37.579617, 126.977041],
        "station": "경복궁역 (3호선)",
        "description": "한복 체험, 궁궐 산책, 사진 찍기 📸"
    },
    {
        "name": "N서울타워",
        "location": [37.551169, 126.988227],
        "station": "명동역 (4호선)",
        "description": "야경 감상, 사랑의 자물쇠, 케이블카 🌃"
    },
    {
        "name": "명동",
        "location": [37.563757, 126.985302],
        "station": "명동역 (4호선)",
        "description": "쇼핑, 길거리 음식 먹방 🛍️"
    },
    {
        "name": "홍대거리",
        "location": [37.556268, 126.922641],
        "station": "홍대입구역 (2호선)",
        "description": "버스킹, 카페 투어, 쇼핑 🎤"
    },
    {
        "name": "북촌한옥마을",
        "location": [37.582604, 126.983998],
        "station": "안국역 (3호선)",
        "description": "전통 한옥 구경, 감성 사진 📷"
    },
    {
        "name": "롯데월드",
        "location": [37.511115, 127.098167],
        "station": "잠실역 (2호선)",
        "description": "놀이기구, 아이스링크, 퍼레이드 🎢"
    },
    {
        "name": "코엑스",
        "location": [37.512547, 127.058944],
        "station": "삼성역 (2호선)",
        "description": "별마당도서관, 쇼핑, 아쿠아리움 📚"
    },
    {
        "name": "한강공원",
        "location": [37.528316, 126.932690],
        "station": "여의나루역 (5호선)",
        "description": "치킨 먹기, 자전거 타기, 피크닉 🚲"
    },
    {
        "name": "인사동",
        "location": [37.574389, 126.985489],
        "station": "안국역 (3호선)",
        "description": "전통 기념품 쇼핑, 찻집 체험 🍵"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "location": [37.566526, 127.009223],
        "station": "동대문역사문화공원역 (2호선)",
        "description": "야경, 전시회, 디자인 감상 ✨"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 빨간색 마커 추가
for place in places:
    folium.Marker(
        location=place["location"],
        tooltip=f"가까운 지하철역: {place['station']}",
        popup=f"{place['name']}",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=600)

st.markdown("---")
st.header("🚇 관광지 & 가까운 지하철역 정보")

# 관광지 설명 출력
for idx, place in enumerate(places, start=1):
    st.subheader(f"{idx}. {place['name']}")
    st.write(f"🚉 가까운 지하철역: {place['station']}")
    st.write(f"🎈 놀거리: {place['description']}")
    st.markdown("---")
