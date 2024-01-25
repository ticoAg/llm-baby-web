# -*- encoding: utf-8 -*-
"""
@Time    :   2024-01-25 23:53:47
@desc    :   registration and login page
@Author  :   ticoAg
@Contact :   1627635056@qq.com
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(Path(__file__).parent.parent.parent.as_posix())
from src.llm_baby_web.utils.tool import dumpJS, loadJS

auth_path = Path("data", "user_config", "auth.json")
if not auth_path.exists():
    if not auth_path.exists():
        auth_path.parent.mkdir(exist_ok=True, parents=True)
    dumpJS({}, auth_path)
user_config = loadJS(auth_path)

def login_or_register(_):
    st.session_state.status = "unverified"
    st.title("Login or Register")
    st.subheader("Please enter your credentials")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")


    def login(user, password):
        if user_config.get(user) and user_config[user].get("password") == password:
            return True
        else:
            return False


    # 写注册和登陆的逻辑
    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
            st.session_state.status = "success"
            # 登陆成功后，跳转到主页
        else:
            st.error("Invalid username or password.")
            st.session_state.status = "incorrect"

    if st.button("Register"):
        if username in user_config:
            st.error("Username already exists.")
        else:
            user_config[username] = {"password": password}
            dumpJS(user_config, auth_path)
            st.success("Registration successful!")
            st.session_state.status = "success"
    if st.session_state.status == "success":
        st.experimental_rerun()