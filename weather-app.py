import requests
import plotly.graph_objects as go
import streamlit as st
# 设置API密钥
api_id = 27435552
app_secret = 'Itldd5UB'
# 创建一个输入框，让用户输入城市名称
user_city = st.text_input("请输入城市名称：", "苏州")
# 当用户输入城市名称后，构造API请求URL
url = f"https://v1.yiketianqi.com/free/week?unescape=1&appid={api_id}&appsecret={app_secret}&city={user_city}"

try:
    # 发送API请求时禁用SSL验证
    response = requests.get(url, verify=False)
    
    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        dates = [item['date'] for item in data['data']]
        tem_day = [int(item['tem_day']) for item in data['data']]
        tem_night = [int(item['tem_night']) for item in data['data']]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=tem_day, mode='lines+markers', name='最高气温'))
        fig.add_trace(go.Scatter(x=dates, y=tem_night, mode='lines+markers', name='最低气温'))
        fig.update_layout(title='天气预报', xaxis_title='日期', yaxis_title='温度 (°C)')

        # 使用Streamlit的plotly_chart函数来显示图表
        st.plotly_chart(fig)
    else:
        st.error(f"获取数据失败: HTTP {response.status_code}")
        
except Exception as e:
    st.error(f"发生错误: {str(e)}")
