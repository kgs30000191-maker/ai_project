import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 책 & 영화 추천기",
    page_icon="📚",
    layout="centered"
)

st.title("📚✨ MBTI별 책 & 영화 추천기")
st.write("너의 MBTI에 딱 맞는 책이랑 감성 영화 추천해줄게 😎🍿")

# MBTI 데이터
mbti_data = {
    "INFP": {
        "books": [
            {
                "title": "데미안",
                "author": "헤르만 헤세",
                "year": "1919",
                "desc": "자아를 찾아가는 감성 성장소설 🌙"
            },
            {
                "title": "아몬드",
                "author": "손원평",
                "year": "2017",
                "desc": "감정을 배우는 특별한 이야기 🫧"
            }
        ],
        "movies": [
            {
                "title": "로마의 휴일",
                "year": "1953",
                "desc": "감성 폭발 클래식 로맨스 🎞️"
            },
            {
                "title": "사운드 오브 뮤직",
                "year": "1965",
                "desc": "따뜻한 음악 영화 🎶"
            }
        ]
    },

    "ENFP": {
        "books": [
            {
                "title": "위대한 개츠비",
                "author": "F. 스콧 피츠제럴드",
                "year": "1925",
                "desc": "화려하지만 공허한 꿈 이야기 ✨"
            },
            {
                "title": "불편한 편의점",
                "author": "김호연",
                "year": "2021",
                "desc": "사람 냄새 가득한 힐링 소설 🍱"
            }
        ],
        "movies": [
            {
                "title": "티파니에서 아침을",
                "year": "1961",
                "desc": "자유로운 분위기의 뉴욕 감성 🗽"
            },
            {
                "title": "사랑은 비를 타고",
                "year": "1952",
                "desc": "기분 좋아지는 뮤지컬 영화 ☔"
            }
        ]
    },

    "INTJ": {
        "books": [
            {
                "title": "1984",
                "author": "조지 오웰",
                "year": "1949",
                "desc": "통제 사회를 다룬 명작 🔍"
            },
            {
                "title": "지구 끝의 온실",
                "author": "김초엽",
                "year": "2021",
                "desc": "SF와 감성을 동시에 🌱"
            }
        ],
        "movies": [
            {
                "title": "시민 케인",
                "year": "1941",
                "desc": "영화 역사상 최고의 명작 중 하나 🎥"
            },
            {
                "title": "카사블랑카",
                "year": "1942",
                "desc": "깊은 분위기의 클래식 영화 🖤"
            }
        ]
    },

    "INFJ": {
        "books": [
            {
                "title": "어린 왕자",
                "author": "생텍쥐페리",
                "year": "1943",
                "desc": "순수한 시선으로 보는 세상 🌟"
            },
            {
                "title": "달러구트 꿈 백화점",
                "author": "이미예",
                "year": "2020",
                "desc": "꿈을 파는 신비한 백화점 💤"
            }
        ],
        "movies": [
            {
                "title": "오즈의 마법사",
                "year": "1939",
                "desc": "상상력 가득한 판타지 🌈"
            },
            {
                "title": "바람과 함께 사라지다",
                "year": "1939",
                "desc": "웅장한 클래식 로맨스 💃"
            }
        ]
    },

    "ISTJ": {
        "books": [
            {
                "title": "노인과 바다",
                "author": "어니스트 헤밍웨이",
                "year": "1952",
                "desc": "끈기와 인내의 상징 🎣"
            },
            {
                "title": "세이노의 가르침",
                "author": "세이노",
                "year": "2023",
                "desc": "현실적인 조언이 가득 💼"
            }
        ],
        "movies": [
            {
                "title": "12인의 성난 사람들",
                "year": "1957",
                "desc": "논리와 토론의 끝판왕 ⚖️"
            },
            {
                "title": "모던 타임즈",
                "year": "1936",
                "desc": "찰리 채플린의 풍자 코미디 🤖"
            }
        ]
    },

    "ISFP": {
        "books": [
            {
                "title": "채식주의자",
                "author": "한강",
                "year": "2007",
                "desc": "강렬한 분위기의 작품 🌿"
            },
            {
                "title": "나미야 잡화점의 기적",
                "author": "히가시노 게이고",
                "year": "2012",
                "desc": "따뜻한 위로를 주는 이야기 📮"
            }
        ],
        "movies": [
            {
                "title": "로마의 휴일",
                "year": "1953",
                "desc": "감성적인 여행 영화 🛵"
            },
            {
                "title": "웨스트 사이드 스토리",
                "year": "1961",
                "desc": "음악과 사랑의 클래식 🎵"
            }
        ]
    }
}

# 나머지 MBTI 자동 채우기
all_mbti = [
    "INTP", "ENTP", "ENTJ", "ENFJ",
    "ISTP", "ISFJ", "ESTP", "ESFP",
    "ESTJ", "ESFJ"
]

default_data = {
    "books": [
        {
            "title": "동물농장",
            "author": "조지 오웰",
            "year": "1945",
            "desc": "짧지만 강렬한 풍자소설 🐷"
        },
        {
            "title": "미드나잇 라이브러리",
            "author": "매트 헤이그",
            "year": "2020",
            "desc": "삶의 선택을 돌아보게 하는 이야기 🌌"
        }
    ],
    "movies": [
        {
            "title": "카사블랑카",
            "year": "1942",
            "desc": "분위기 미쳤던 클래식 🎬"
        },
        {
            "title": "사브리나",
            "year": "1954",
            "desc": "몽글몽글한 로맨스 💕"
        }
    ]
}

for mbti in all_mbti:
    mbti_data[mbti] = default_data

selected_mbti = st.selectbox(
    "🧠 너의 MBTI를 골라봐!",
    list(mbti_data.keys())
)

st.divider()

data = mbti_data[selected_mbti]

st.subheader(f"💖 {selected_mbti}에게 추천하는 책")

for book in data["books"]:
    st.markdown(
        f"""
### 📘 {book['title']}
- ✍️ 작가: {book['author']}
- 📅 출간년도: {book['year']}
- 💬 한줄 소개: {book['desc']}
"""
    )

st.divider()

st.subheader("🎬 추천 영화")

for movie in data["movies"]:
    st.markdown(
        f"""
### 🍿 {movie['title']}
- 📅 개봉년도: {movie['year']}
- 💬 한줄 소개: {movie['desc']}
"""
    )

st.divider()

st.success("✨ 오늘의 추천 끝! 친구들이랑도 공유해봐 😆")
