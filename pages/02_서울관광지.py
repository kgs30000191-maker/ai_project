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
        "description": """
🏯 조선시대 궁궐을 직접 걸어보며 전통 분위기를 느낄 수 있어요.
👘 한복 대여 후 사진 찍는 외국인 관광객이 정말 많아요.
📸 근처 국립민속박물관과 광화문 광장까지 함께 구경하기 좋아요.
☕ 삼청동 감성 카페 거리도 가까워서 산책 코스로 추천!
"""
    },
    {
        "name": "N서울타워",
        "location": [37.551169, 126.988227],
        "station": "명동역 (4호선)",
        "description": """
🌃 서울 야경 명소로 유명해서 밤에 특히 분위기가 좋아요.
🔒 사랑의 자물쇠 포토존이 인기예요.
🚠 남산 케이블카를 타고 올라가는 재미도 있어요.
🍜 명동과 가까워서 쇼핑 후 코스로 딱 좋아요!
"""
    },
    {
        "name": "명동",
        "location": [37.563757, 126.985302],
        "station": "명동역 (4호선)",
        "description": """
🛍️ K-뷰티 쇼핑과 패션 쇼핑을 즐기기 좋은 곳이에요.
🍢 길거리 음식 먹방 코스로 엄청 유명해요.
📷 밤이 되면 네온사인 때문에 분위기가 화려해져요.
🎵 외국인 관광객이 많아서 활기찬 분위기를 느낄 수 있어요.
"""
    },
    {
        "name": "홍대거리",
        "location": [37.556268, 126.922641],
        "station": "홍대입구역 (2호선)",
        "description": """
🎤 거리 버스킹 공연과 춤 공연을 자주 볼 수 있어요.
☕ 감성 카페와 포토부스 투어하기 좋아요.
🛍️ 빈티지 쇼핑과 악세사리 구경도 재밌어요.
🌙 밤 늦게까지 활기찬 분위기를 느낄 수 있어요.
"""
    },
    {
        "name": "북촌한옥마을",
        "location": [37.582604, 126.983998],
        "station": "안국역 (3호선)",
        "description": """
🏡 전통 한옥 골목을 걸으며 한국 감성을 느낄 수 있어요.
📸 골목마다 사진 스팟이 많아서 인생샷 찍기 좋아요.
🍵 전통 찻집과 공방 체험도 가능해요.
🚶 삼청동과 인사동까지 함께 둘러보기 좋아요.
"""
    },
    {
        "name": "롯데월드",
        "location": [37.511115, 127.098167],
        "station": "잠실역 (2호선)",
        "description": """
🎢 실내외 놀이기구가 많아서 하루 종일 놀 수 있어요.
🎠 퍼레이드와 야간 조명이 정말 화려해요.
🧊 아이스링크와 아쿠아리움도 함께 즐길 수 있어요.
📸 교복 대여 후 사진 찍는 학생들도 많아요!
"""
    },
    {
        "name": "코엑스",
        "location": [37.512547, 127.058944],
        "station": "삼성역 (2호선)",
        "description": """
📚 별마당 도서관은 SNS 사진 명소로 유명해요.
🛍️ 쇼핑몰과 맛집이 많아서 데이트 코스로 좋아요.
🐠 코엑스 아쿠아리움에서 다양한 해양생물을 볼 수 있어요.
🎬 영화관과 전시회도 자주 열려서 볼거리가 많아요.
"""
    },
    {
        "name": "한강공원",
        "location": [37.528316, 126.932690],
        "station": "여의나루역 (5호선)",
        "description": """
🚲 자전거 대여 후 한강 따라 달리기 좋아요.
🍗 치킨과 라면 먹으며 피크닉 즐기는 사람이 많아요.
🌅 저녁 노을과 야경이 정말 예뻐요.
🛳️ 한강 유람선 체험도 가능해요!
"""
    },
    {
        "name": "인사동",
        "location": [37.574389, 126.985489],
        "station": "안국역 (3호선)",
        "description": """
🍵 전통 찻집과 한식 디저트를 즐길 수 있어요.
🖌️ 한국 전통 기념품 쇼핑하기 좋아요.
🎨 골목마다 갤러리와 공예품 가게가 많아요.
📸 한국 전통 분위기를 느끼기 좋은 거리예요.
"""
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "location": [37.566526, 127.009223],
        "station": "동대문역사문화공원역 (2호선)",
        "description": """
✨ 밤이 되면 건물 조명이 켜져서 정말 예뻐요.
🎨 디자인 전시회와 팝업스토어가 자주 열려요.
📸 미래적인 건축 디자인 덕분에 사진 명소로 유명해요.
🛍️ 근처 동대문 쇼핑타운과 함께 구경하기 좋아요.
"""
    }
]

# 컬러 지도 생성 + 한국어 타일
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 빨간색 마커 추가
for place in places:
    folium.Marker(
        location=place["location"],
        tooltip=f"🚉 가까운 지하철역: {place['station']}",
        popup=f"📍 {place['name']}",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력 (크기 60% 정도로 축소)
st_folium(m, width=750, height=450)

st.markdown("---")

# 관광지 선택 박스
selected_place_name = st.selectbox(
    "📍 관광지를 선택해보세요!",
    [place["name"] for place in places]
)

# 선택한 관광지 정보 출력
selected_place = next(
    place for place in places if place["name"] == selected_place_name
)

st.header(f"✨ {selected_place['name']} 관광 정보")

st.write(f"🚇 가장 가까운 지하철역: {selected_place['station']}")
st.markdown(selected_place["description"])
