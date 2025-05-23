import streamlit as st
import requests

st.title("Flask 연동 채팅")

# 세션 상태 초기화
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# 사용자 입력 받기
user_input = st.text_input("메시지를 입력하세요", key="user_input")

# 입력이 있으면 세션에 저장
if st.button("전송") or user_input:
    # Flask 서버에 POST 요청
    try:
        res = requests.post("http://localhost:5001/chat", json={"message": user_input})
        bot_response = res.json().get("response", "⚠️ 응답 오류")

        #기록 추가
        st.session_state.messages.append({"role": "user", "text": user_input})
        st.session_state.messages.append({"role": "bot", "text": bot_response})

        #입력창 초기화
        st.session_state.user_input = ""

        # 리런으로 즉시 반영
        st.experimental_rerun()

    except Exception as e:
        bot_response = f"❌ 서버 오류: {e}"

#st.text_input

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💻 **사용자:** {msg['text']}")
    else:
        st.markdown(f"🤖 **봇:** {msg['text']}")