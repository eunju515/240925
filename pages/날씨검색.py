import streamlit as st
import requests

# 웹 애플리케이션 제목
st.title('오늘의 지역별 날씨 조회')

# API 키 입력 받기
api_key = st.text_input('API 키를 입력해주세요:', type="password")

# 지역 입력 받기
city = st.text_input('날씨를 조회할 도시 이름을 입력해주세요:')

# 버튼을 눌렀을 때 날씨 정보 조회
if st.button('날씨 조회하기'):
    if not api_key:
        st.error('API 키를 입력해주세요!')
    elif not city:
        st.error('도시 이름을 입력해주세요!')
    else:
        # OpenWeatherMap API 요청 URL
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric'

        # API 호출
        response = requests.get(url)

        # 응답이 성공적일 때 (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # 날씨 정보 출력
            st.write(f"**{city}**의 날씨 정보:")
            st.write(f"날씨: {data['weather'][0]['description']}")
            st.write(f"온도: {data['main']['temp']}°C")
            st.write(f"체감 온도: {data['main']['feels_like']}°C")
            st.write(f"최저 온도: {data['main']['temp_min']}°C")
            st.write(f"최고 온도: {data['main']['temp_max']}°C")
            st.write(f"습도: {data['main']['humidity']}%")
        else:
            st.error('날씨 정보를 불러오는 데 실패했습니다. 도시 이름이나 API 키를 확인해주세요.')
