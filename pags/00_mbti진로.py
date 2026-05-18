import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="💼",
    layout="centered"
)

# MBTI별 추천 데이터
mbti_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 분석가",
            "major": "데이터사이언스학과 / 컴퓨터공학과",
            "personality": "논리적이고 계획 세우는 걸 좋아하는 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "창의적이면서도 꼼꼼한 사람에게 잘 맞아!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "컴퓨터공학과",
            "personality": "혼자 집중하는 걸 좋아하고 호기심 많은 성격!",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "🔬 연구원",
            "major": "화학과 / 물리학과",
            "personality": "탐구심 많고 분석적인 사람에게 추천!",
            "salary": "평균 연봉 약 4,600만원"
        }
    ],

    "ENTJ": [
        {
            "job": "📈 CEO / 경영인",
            "major": "경영학과",
            "personality": "리더십 강하고 추진력 있는 성격!",
            "salary": "평균 연봉 약 6,000만원 이상"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "말 잘하고 전략적인 사람에게 잘 맞아!",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ENTP": [
        {
            "job": "📺 방송기획자",
            "major": "미디어학과",
            "personality": "아이디어 많고 새로운 걸 좋아하는 성격!",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "🚀 마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "트렌드에 민감하고 말 잘하는 사람 추천!",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],

    "INFJ": [
        {
            "job": "🩺 상담심리사",
            "major": "심리학과",
            "personality": "공감 능력 좋고 사람 고민 잘 들어주는 성격!",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "✍️ 작가",
            "major": "문예창작학과",
            "personality": "상상력 풍부하고 감수성 있는 사람 추천!",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감성적이고 창의적인 성격!",
            "salary": "평균 연봉 약 3,600만원"
        },
        {
            "job": "🎵 작곡가",
            "major": "실용음악과",
            "personality": "예술 감각 있고 자유로운 성향 추천!",
            "salary": "평균 연봉 약 3,700만원"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람 챙기는 걸 좋아하고 책임감 강한 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🎤 아나운서",
            "major": "신문방송학과",
            "personality": "말 잘하고 밝은 에너지 가진 사람 추천!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "ENFP": [
        {
            "job": "📱 크리에이터",
            "major": "미디어콘텐츠학과",
            "personality": "활발하고 끼 많은 사람에게 딱!",
            "salary": "평균 연봉 다양함!"
        },
        {
            "job": "🌍 여행기획자",
            "major": "관광경영학과",
            "personality": "사람 만나는 거 좋아하고 자유로운 성격!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "세무회계학과",
            "personality": "꼼꼼하고 책임감 강한 성격!",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙 중요하게 생각하는 사람 추천!",
            "salary": "평균 연봉 약 4,700만원"
        }
    ],

    "ISFJ": [
        {
            "job": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🏫 사회복지사",
            "major": "사회복지학과",
            "personality": "사람 돕는 걸 좋아하는 사람 추천!",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESTJ": [
        {
            "job": "🏢 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 성격!",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "📊 경영 관리자",
            "major": "경영학과",
            "personality": "조직 관리 잘하는 사람 추천!",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],

    "ESFJ": [
        {
            "job": "💄 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교성 좋은 성격!",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "🍽️ 호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신 강한 사람 추천!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 자동차 정비사",
            "major": "자동차학과",
            "personality": "손으로 직접 만드는 걸 좋아하는 성격!",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "✈️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력 좋은 사람 추천!",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ISFP": [
        {
            "job": "💅 메이크업 아티스트",
            "major": "뷰티미용학과",
            "personality": "감각적이고 섬세한 성격!",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "예술 감각 뛰어난 사람 추천!",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],

    "ESTP": [
        {
            "job": "🏎️ 스포츠 코치",
            "major": "체육학과",
            "personality": "에너지 넘치고 활동적인 성격!",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "사람 상대 잘하고 자신감 있는 사람 추천!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "ESFP": [
        {
            "job": "🎭 배우",
            "major": "연극영화과",
            "personality": "끼 많고 주목받는 걸 좋아하는 성격!",
            "salary": "평균 연봉 다양함!"
        },
        {
            "job": "🎤 아이돌 트레이너",
            "major": "실용무용과",
            "personality": "밝고 활발한 사람 추천!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ]
}

st.title("✨ MBTI 진로 추천기 💼")
st.write("너의 MBTI에 어울리는 진로를 알아보자 😎")

mbti = st.selectbox(
    "🧩 MBTI를 선택해줘!",
    list(mbti_data.keys())
)

if st.button("🔍 진로 추천 보기"):
    st.success(f"{mbti} 유형에게 추천하는 진로야! 💖")

    for career in mbti_data[mbti]:
        st.markdown("---")
        st.subheader(career["job"])
        st.write(f"🎓 **추천 학과:** {career['major']}")
        st.write(f"💡 **잘 맞는 성격:** {career['personality']}")
        st.write(f"💰 **평균 연봉:** {career['salary']}")

    st.balloons()

st.markdown("---")
st.caption("🌟 재미로 보는 MBTI 진로 추천이야! 참고용으로 봐줘 😆")
