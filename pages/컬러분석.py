import streamlit as st

# 웹 애플리케이션 제목
st.title('색에 따른 성격 분석')

# 사용자 이름 입력 받기
name = st.text_input('이름을 입력해주세요 : ')

# 좋아하는 색 선택
color = st.selectbox('좋아하는 색을 선택해주세요:', 
                     ['빨강', '파랑', '노랑', '초록', '검정', '흰색', '보라', '핑크', '주황'])

# 색에 따른 성향 분석
def analyze_color(color):
    if color == '빨강':
        return '열정적이고 에너지가 넘치며 리더십이 강합니다.'
    elif color == '파랑':
        return '침착하고 신뢰할 수 있으며 평화를 중요시합니다.'
    elif color == '노랑':
        return '낙관적이고 창의적이며 즐거움을 추구합니다.'
    elif color == '초록':
        return '균형을 중요시하며 자연을 사랑하고 안정적입니다.'
    elif color == '검정':
        return '강렬하고 권위적이며 신비로운 매력을 지녔습니다.'
    elif color == '흰색':
        return '순수하고 깔끔하며 단순함을 추구하는 성향입니다.'
    elif color == '보라':
        return '창의적이고 신비로우며 예술적인 감각이 뛰어납니다.'
    elif color == '핑크':
        return '사랑스럽고 친절하며 배려심이 많습니다.'
    elif color == '주황':
        return '활기차고 외향적이며 모험을 즐깁니다.'
    else:
        return '색에 대한 분석 정보가 없습니다.'

# 버튼을 눌렀을 때 결과 표시
if st.button('성향 분석하기'):
    # 성향 분석 결과 출력
    personality = analyze_color(color)
    st.write(f'{name}님! 당신이 좋아하는 색은 {color}입니다.')
    st.write(f'{color}색을 좋아하는 사람은 {personality}')
