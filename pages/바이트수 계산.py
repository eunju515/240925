import streamlit as st

# 웹 애플리케이션 제목
st.title('문장 바이트 수 계산기')

# 문장 입력 받기 (text_area를 사용하여 긴 문장 입력 시 자동 줄바꿈)
sentence = st.text_area('문장을 입력해주세요 :')

# 최대 허용 바이트 수 설정
max_bytes = 1500

# 버튼을 눌렀을 때 결과 표시
if st.button('바이트 수 계산하기'):
    # 문장을 UTF-8로 인코딩한 후 바이트 수 계산
    byte_count = len(sentence.encode('utf-8'))
    
    # 바이트 수 출력
    st.write(f'입력하신 문장의 바이트 수는 {byte_count}입니다.')
    
    # 1500바이트를 넘을 경우 경고 메시지 출력
    if byte_count > max_bytes:
        # 초과한 바이트 수 계산
        excess_bytes = byte_count - max_bytes
        
        # 몇 글자를 줄여야 하는지 계산 (대략적 계산, 유니코드 문자에 따라 다를 수 있음)
        avg_bytes_per_char = byte_count / len(sentence)  # 한 글자가 차지하는 평균 바이트 수
        chars_to_remove = int(excess_bytes / avg_bytes_per_char)  # 초과 바이트에 해당하는 글자 수 계산
        
        # 경고 메시지 출력
        st.warning(f'문장이 너무 깁니다. {chars_to_remove}글자를 줄여주세요.')
