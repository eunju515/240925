import streamlit as st

# 웹 애플리케이션 제목
st.title('MBTI 성격검사')

# 사용자 이름 입력 받기
name = st.text_input('이름을 입력해주세요 : ')

# MBTI 질문 리스트
st.header('질문에 답해주세요')

q1 = st.selectbox('1. 사교적인 편인가요?', ['예', '아니오'])
q2 = st.selectbox('2. 직관적인가요?', ['예', '아니오'])
q3 = st.selectbox('3. 감정을 중시하나요?', ['예', '아니오'])
q4 = st.selectbox('4. 계획적인 편인가요?', ['예', '아니오'])

# 버튼을 눌렀을 때 결과 표시
if st.button('결과 확인하기'):
    # MBTI 계산
    mbti = ''
    mbti += 'E' if q1 == '예' else 'I'
    mbti += 'N' if q2 == '예' else 'S'
    mbti += 'F' if q3 == '예' else 'T'
    mbti += 'J' if q4 == '예' else 'P'
    
    # 결과 출력
    st.write(f'{name}님의 MBTI 성격 유형은 {mbti}입니다!')
    st.write(f'{mbti} 유형은 매우 독특한 성격을 가지고 있답니다!')

