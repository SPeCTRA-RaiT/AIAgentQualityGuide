### [코드] 스트리밍 API 호출을 통한 TTLT 및 TPS 측정 예시 (Python)

import time
from openai import OpenAI
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
user_question = "생성형 AI가 세상을 어떻게 바꿀지에 대해 상세히 설명해줘."
print(f"질문: {user_question}")
print("답변 생성을 시작합니다...")
7장 여전히 중요한 성능  305
# --- 타이머 및 변수 초기화 ---
start_time = time.time()
first_chunk_received = False
ttft = 0
total_tokens = 0
response_text = ""
try:
 stream = client.chat.completions.create(
 model="gpt-4-turbo",
 messages=[{"role": "user", "content": user_question}],
 stream=True,
 )
 for chunk in stream:
 # 첫 번째 데이터 조각을 받은 시점에 TTFT를 기록합니다.
 if not first_chunk_received and chunk.choices[0].delta.content:
 end_time_for_ttft = time.time()
 ttft = end_time_for_ttft - start_time
 first_chunk_received = True
 # 답변을 이어 붙이고, 총 토큰 수를 계산합니다.
 if chunk.choices[0].delta.content:
 token_content = chunk.choices[0].delta.content
 response_text += token_content
 total_tokens += 1 # 실제로는 토크나이저로 계산하는 것이 더 정확합니다.
 print(token_content, end="", flush=True)
 # --- 스트리밍 루프가 모두 끝난 시점에 TTLT를 계산 ---
 end_time_for_ttlt = time.time()
 ttlt = end_time_for_ttlt - start_time
 # --- 최종 성능 지표 계산 및 출력 ---
 # TPS (Tokens Per Second): 순수 생성 속도
 # (TTLT - TTFT)는 첫 토큰 이후 순수하게 생성에만 걸린 시간입니다.
 tps = (total_tokens - 1) / (ttlt - ttft) if (ttlt - ttft) > 0 else 0

 print(f"\n\n--- 성능 측정 결과 ---")
 print(f"Time to First Token (TTFT): {ttft:.4f} 초")
 print(f"Time to Last Token (TTLT): {ttlt:.4f} 초")
 print(f"Total Tokens Generated: {total_tokens} 개")
 print(f"Tokens Per Second (TPS): {tps:.2f} 토큰/초")
 print("--------------------")
except Exception as e:
 print(f"오류 발생: {e}")
