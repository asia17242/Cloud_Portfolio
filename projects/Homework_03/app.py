import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 設定網頁標題與寬度
st.set_page_config(
    page_title="Cosmos3 Super Text2Image | 作業 03：文字生圖 App (手機版)",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隱藏 Streamlit 預設的頁首/頁尾與邊距，讓網頁看起來像獨立網站
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    display: block;
    border: none;
    height: 100vh;
    width: 100vw;
}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 讀取並嵌入 index.html
path_to_html = Path(__file__).parent / "index.html"

if path_to_html.exists():
    html_content = path_to_html.read_text(encoding="utf-8")
    # 渲染 HTML (高度設定 1000px，支援滾動)
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("找不到 index.html 檔案！")
