import streamlit as st

# 웹 애플리케이션 제목
st.title('문장 바이트 수 계산기')

# 문장 입력 받기
sentence = st.text_input('문장을 입력해주세요 : ')

# 버튼을 눌렀을 때 결과 표시
if st.button('바이트 수 계산하기'):
    # 문장을 UTF-8로 인코딩한 후 바이트 수 계산
    byte_count = len(sentence.encode('utf-8'))
    
    # 결과 출력
    st.write(f'입력하신 문장의 바이트 수는 {byte_count}입니다.')
