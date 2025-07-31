import streamlit as st
import pandas as pd
from openai import OpenAI
import os

st.set_page_config(page_title="CSV智能问答（华为ModelArts）", page_icon="📊")
st.title(" 华为 ModelArts · CSV 文件智能问答")

st.write("上传你的 CSV 文件，并向大模型提问。")

# 初始化 Session 状态
if "openai_key" not in st.session_state:
    st.session_state.openai_key = ""
if "base_url" not in st.session_state:
    st.session_state.base_url = "https://maas-cn-southwest-2.modelarts-maas.com/v1/infers/你的模型ID/v1"  # 替换成你自己的
if "connected" not in st.session_state:
    st.session_state.connected = False
if "df" not in st.session_state:
    st.session_state.df = None
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

# 侧边栏：API 配置
with st.sidebar:
    st.subheader(" API 配置")
    st.session_state.openai_key = st.text_input("API Key", type="password", value=st.session_state.openai_key)
    st.session_state.base_url = st.text_input("API地址（base_url）", value=st.session_state.base_url)
    if st.button("连接模型"):
        if st.session_state.openai_key and st.session_state.base_url:
            st.session_state.connected = True
            st.success("✅ 连接成功，可以开始使用啦！")
        else:
            st.error("❌ 请填写 API Key 和 API 地址")

# 上传 CSV 文件
if st.session_state.connected:
    uploaded_file = st.file_uploader("上传一个 CSV 文件", type="csv")
    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.success("✅ CSV 文件已成功加载！")

    if st.session_state.df is not None:
        st.subheader("预览数据（前5行）：")
        st.dataframe(st.session_state.df.head())

        # 输入问题
        question = st.text_input(" 请输入你要询问的问题：")

        def call_model(prompt):
            try:
                client = OpenAI(
                    api_key=st.session_state.openai_key,
                    base_url=st.session_state.base_url,
                )
                messages = [
                    {"role": "system", "content": "你是一个擅长数据分析的智能助手。"},
                    {"role": "user", "content": prompt}
                ]
                response = client.chat.completions.create(
                    model="DeepSeek-R1",  # 具体模型视你接口而定
                    messages=messages,
                    temperature=0.7,
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                return f"❌ 模型调用失败：{e}"

        if question:
            df_head = st.session_state.df.head(5).to_csv(index=False)
            df_columns = list(st.session_state.df.columns)
            prompt = f"""我上传了一个表格，它的前几行数据如下：

列名包括：{', '.join(df_columns)}

请根据上述表格内容回答下面的问题：

{question}
"""
            with st.spinner("正在调用模型，请稍候..."):
                reply = call_model(prompt)
                st.subheader(" 回答：")
                st.write(reply)
                st.session_state.prompt_history.append({"q": question, "a": reply})

        # 历史记录
        if st.session_state.prompt_history:
            st.subheader(" 问答历史记录")
            for i, pair in enumerate(st.session_state.prompt_history[::-1]):
                st.markdown(f"**Q{i+1}：** {pair['q']}")
                st.markdown(f"**A{i+1}：** {pair['a']}")

        if st.button("清除记录"):
            st.session_state.prompt_history = []
            st.success("✅ 已清除问答历史。")

else:
    st.warning("请在左侧输入 API Key 并连接模型。")
