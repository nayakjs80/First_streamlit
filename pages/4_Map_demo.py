import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
import geocoder

st.set_page_config(page_title="Display Self", page_icon="")

st.markdown("Display Self")


try:
    # JavaScript를 사용하여 GPS 위치 가져오기
    st.markdown("""
        <script>
        navigator.geolocation.getCurrentPosition(function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            document.getElementById('latitude').value = latitude;
            document.getElementById('longitude').value = longitude;
        });
        </script>
    """, unsafe_allow_html=True)

    # Streamlit에서 GPS 위치 가져오기
    latitude = st.text_input("Latitude", "0")
    longitude = st.text_input("Longitude", "0")

    # 지도의 중심을 내 위치로 설정
    map = folium.Map(location=[float(latitude), float(longitude)], zoom_start=15)

    # 내 위치에 마커 추가
    folium.Marker([float(latitude), float(longitude)], popup="내 위치").add_to(map)

    # Streamlit 앱 설정
    st.title("내 위치 지도")
    sShow = "아래 지도에서 내 위치를 확인하세요:" + "latitude:" + latitude + ", longitude:" + longitude
    st.write(sShow)

    # 지도를 Streamlit 앱에 표시
    folium_static(map)


# import streamlit as st
# import folium
# from streamlit_folium import folium_static

# # JavaScript를 사용하여 GPS 위치 가져오기
# st.markdown("""
#     <script>
#     navigator.geolocation.getCurrentPosition(function(position) {
#         const latitude = position.coords.latitude;
#         const longitude = position.coords.longitude;
#         document.getElementById('latitude').value = latitude;
#         document.getElementById('longitude').value = longitude;
#     });
#     </script>
# """, unsafe_allow_html=True)

# # Streamlit에서 GPS 위치 가져오기
# latitude = st.text_input("Latitude", "0")
# longitude = st.text_input("Longitude", "0")

# # 지도의 중심을 내 위치로 설정
# map = folium.Map(location=[float(latitude), float(longitude)], zoom_start=15)

# # 내 위치에 마커 추가
# folium.Marker([float(latitude), float(longitude)], popup="내 위치").add_to(map)

# # Streamlit 앱 설정
# st.title("내 위치 지도")
# st.write("아래 지도에서 내 위치를 확인하세요:")

# # 지도를 Streamlit 앱에 표시
# folium_static(map)



    # import streamlit as st
    # import folium
    # import geocoder
    # from streamlit_folium import folium_static

    # # 핸드폰의 GPS 위치 가져오기
    # g = geocoder.ip('me')
    # latitude, longitude = g.latlng

    # # 지도의 중심을 내 위치로 설정
    # map = folium.Map(location=[latitude, longitude], zoom_start=15)

    # # 내 위치에 마커 추가
    # folium.Marker([latitude, longitude], popup="내 위치").add_to(map)

    # # Streamlit 앱 설정
    # st.title("내 위치 지도")
    # st.write("아래 지도에서 내 위치를 확인하세요:")

    # # 지도를 Streamlit 앱에 표시
    # folium_static(map)



    # # 내 위치를 가져오기 위한 Geolocator 설정
    # geolocator = Nominatim(user_agent="geoapiExercises")
    # location = geolocator.geocode("경기도, 대한민국")

    # # 지도의 중심을 내 위치로 설정
    # map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

    # # 내 위치에 마커 추가
    # folium.Marker([location.latitude, location.longitude], popup="내 위치").add_to(map)

    # # Streamlit 앱 설정
    # st.title("내 위치 지도")
    # st.write("아래 지도에서 내 위치를 확인하세요:")

    # # 지도를 Streamlit 앱에 표시
    # folium_static(map)

except RuntimeError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )

# import streamlit as st
# import folium
# from geopy.geocoders import Nominatim
# from streamlit_folium import folium_static

# # 사용자 에이전트 설정
# geolocator = Nominatim(user_agent="my_app")

# # 내 위치를 가져오기
# location = geolocator.geocode("경기도, 대한민국")

# # 지도의 중심을 내 위치로 설정
# map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

# # 내 위치에 마커 추가
# folium.Marker([location.latitude, location.longitude], popup="내 위치").add_to(map)

# # Streamlit 앱 설정
# st.title("내 위치 지도")
# st.write("아래 지도에서 내 위치를 확인하세요:")

# # 지도를 Streamlit 앱에 표시
# folium_static(map)
