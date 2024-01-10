import streamlit as st
import requests
import datetime

# WeatherstackのAPIキーを指定します
API_KEY = '2ecc8c0806837e5ce6d7905b07fe89de'

# 対象となる都市を指定します
cities = {
    'Sapporo': '札幌',
    'Sendai': '仙台',
    'Tokyo': '東京',
    'Nagoya': '名古屋',
    'Osaka': '大阪',
    'Fukuoka': '福岡'
}

city_names = list(cities.values())

st.title('天気アプリ')
st.write('都市と日付を選択して天気情報を取得します。')

# Streamlitのサイドバーに都市選択のプルダウンメニューを作成します
city_jp = st.selectbox('都市を選択してください。', city_names)

# Streamlitのサイドバーに日付選択の機能を追加します
date = st.date_input('日付を選択してください。')

# ボタンを追加します
if st.button('天気情報を取得'):

    # 対応する英語の都市名を取得
    city_en = list(cities.keys())[city_names.index(city_jp)]

    # WeatherstackのAPIを使って天気情報を取得します
    response = requests.get(f'http://api.weatherstack.com/current?access_key={API_KEY}&query={city_en}&historical_date={date}')

    # 取得したデータをJSON形式に変換します
    data = response.json()

    # 天気情報を取得します
    weather_info = data.get('current', {})

    # 天気情報を表示します
    if weather_info:
        st.markdown(f'**{city_jp}**の{date}の天気')
        st.markdown(f'**温度:** {weather_info.get("temperature", "データなし")}℃')
        st.markdown(f'**天候の説明:** {weather_info.get("weather_descriptions", ["データなし"])[0]}')
    else:
        st.error('天気情報を取得できませんでした。')
