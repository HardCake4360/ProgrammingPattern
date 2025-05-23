from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.2:latest"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # 여기서 응답 로직 (예: ChatGPT API 등) 처리
    try:
        # Ollama에 POST 요청
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,  # 또는 llama3 등
                "messages": [{"role": "user", "content": user_message}]
            }
        )
        res_data = response.json()

        #print(response)
        response_message = res_data.get("message", {}).get("content", "응답 없음")
    except Exception as e:
        response_message = f"❌ 서버 오류: {e}"

    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(port=5001)
