import pandas as pd
import streamlit as st
st.markdown('# 🐈 小猫 椰果-数字档案')
st.image("https://img95.699pic.com/photo/60061/0609.jpg_wh860.jpg",width=150)
st.markdown('## 基础信息')
st.markdown('#### 注册时间:green[2025-10-20]|精神状态:✅非常棒棒')
st.markdown('#### 当前位置:green[快乐小家]|安全等级:green[绝密]')

st.markdown('# 🐾椰果技能矩阵')
import streamlit as st  # 导入Streamlit并用st代表它


st.subheader('椰果技能矩阵')
st.metric(label="当日进食", value="三碗猫粮一根猫条")

st.subheader('椰果每日事必')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="睡觉", value="30%",delta="2.5%")
c2.metric(label="上厕所", value="45%", delta="6%")
c3.metric(label="吃饭", value="50%", delta="45%", delta_color="off")

st.subheader('心情状态')
st.metric(label="满分一百分", value="100!", delta="10", label_visibility='hidden')
st.markdown('# 🐱椰果任务日志')
import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '早上':['床头唤醒', '陪伴入睡', '外出玩耍', '发呆', '觅食'],
    '中午':['奔跑', '钻进被窝', '觅食', '喝水',' 散步'],
    '晚上':['玩游戏', '陪慌兮兮看电视', '吃零食', '上厕所', '和慌兮兮睡觉'],
}
# 定义数据框所用的索引
index = pd.Series(['06月', '07月', '08月', '09月', '010月'], name='月份')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('静态表')
st.table(df)
st.markdown('# 🍊椰果主人最新代码成果')
st.title("代码")
str ='''a=1
   b=2
   print(a + b)
   '''
st.code(str,language=None)
st.caption('这是Python代码')
st.code(str,language="python",line_numbers=True)
st.markdown('***')
st.markdown('#### >>SYSTEM MESSAGE:下一个任务已解锁...')
st.markdown('#### >>TARGET:课程管理系统')
st.markdown('#### >>COUNTDOWN:2025-10-20')