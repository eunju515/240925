import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from folium.plugins import MousePosition

# 웹 애플리케이션 제목
st.title('지도에서 지역 선택하여 날씨 조회')

# API 키 입력 받기
api_key = st.text_input('API 키를 입력해주세요:', type="password")

# 지도의 기본 좌표 설정 (서울을 기본 좌표로 설정)
latitude = 37.5665
longitude = 126.9780

# 지도 생성
map = folium.Map(location=[latitude, longitude], zoom_start=5)

# 지도에 마우스 위치 표시
MousePosition().add_to(map)

# folium에 선택 이벤트를 추가하여 좌표를 얻는 기능
st.write("지도를 클릭하여 원하는 위치를 선택하세요.")
output = st_folium(map, width=700, height=500)

# 좌표 선택 여부 확인
if output and 'last_clicked' in output:
    lat = output['last_clicked']['lat']
    lon = output['last_clicked']['lng']
    st.write(f"선택한 좌표: 위도 {lat}, 경도 {lon}")

    # 날씨 조회 버튼
    if st.button('날씨 조회하기'):
        if not api_key:
            st.error('API 키를 입력해주세요!')
        else:
            # OpenWeatherMap API 요청 URL
            url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=kr&units=metric'

            # API 호출
            response = requests.get(url)

            # 응답이 성공적일 때 (status code 200)
            if response.status_code == 200:
                data = response.json()

                # 날씨 정보 출력
                st.write(f"**선택한 위치**의 날씨 정보:")
                st.write(f"날씨: {data['weather'][0]['description']}")
                st.write(f"온도: {data['main']['temp']}°C")
                st.write(f"체감 온도: {data['main']['feels_like']}°C")
                st.write(f"최저 온도: {data['main']['temp_min']}°C")
                st.write(f"최고 온도: {data['main']['temp_max']}°C")
                st.write(f"습도: {data['main']['humidity']}%")
            else:
                # 오류 발생 시, API에서 반환한 에러 메시지를 표시
                error_message = response.json().get('message', '알 수 없는 오류')
                st.error(f'날씨 정보를 불러오는 데 실패했습니다: {error_message}')
else:
    st.write("지도를 클릭하여 위치를 선택해주세요.")
