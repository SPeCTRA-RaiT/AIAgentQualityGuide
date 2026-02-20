### [코드] 스트리밍 API 호출을 통한 TTFT 측정 예시 (Python)

import time
from openai import OpenAI
# OpenAI 클라이언트를 초기화합니다.
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
user_question = "생성형 AI가 세상을 어떻게 바꿀지에 대해 상세히 설명해줘."
print(f"질문: {user_question}")
print("답변 생성을 시작합니다...")
# --- TTFT 측정을 위한 타이머 시작 ---
start_time = time.time()
first_chunk_received = False
ttft = 0
try:
 # stream=True 옵션을 반드시 사용해야 합니다.
 stream = client.chat.completions.create(
 model="gpt-4-turbo",
 messages=[{"role": "user", "content": user_question}],
 stream=True,
 )
 # 스트리밍 응답을 순회하며 데이터를 받습니다.
 for chunk in stream:
 # --- 첫 번째 데이터 조각(Chunk)을 받은 시점 ---
 if not first_chunk_received:
 # 타이머를 멈추고 TTFT를 계산합니다.
 end_time = time.time()
 ttft = end_time - start_time
 first_chunk_received = True

 # 측정된 TTFT를 출력합니다.
 print(f"\n--- 성능 측정 결과 ---")
 print(f"Time to First Token (TTFT): {ttft:.4f} 초")
 print("--------------------\n")
 # 화면에 답변을 순차적으로 출력합니다.
 if chunk.choices[0].delta.content:
 print(chunk.choices[0].delta.content, end="", flush=True)
except Exception as e:
 print(f"오류 발생: {e}")
