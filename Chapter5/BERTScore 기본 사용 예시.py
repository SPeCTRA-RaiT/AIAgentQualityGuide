### BERTScore 기본 사용 예시 (Python)

# 1. 필요한 라이브러리(도구)를 불러옵니다.
from bert_score import score
# 2. 평가의 기준이 될 '모범 답안'을 준비합니다.
reference_answer = "대한민국의 수도는 서울입니다."
# 3. 평가할 대상인 'AI의 답변'을 준비합니다.
candidate_answer = "서울은 대한민국의 수도입니다."
# 4. BERTScore 함수를 호출하여 점수를 계산합니다.
# - cands: AI의 답변 목록 (Candidates)
# - refs: 모범 답안 목록 (References)
# - lang="ko": 한국어 모델을 사용하도록 지정합니다.
(P, R, F1) = score(cands=[candidate_answer], refs=[reference_answer],
lang="ko")
# 5. 최종 F1 점수를 출력합니다. (F1은 정밀도와 재현율의 조화 평균)
print(f"BERTScore F1 점수: {F1.item():.4f}")
# 예상 출력:
# BERTScore F1 점수: 0.99XX
# (두 문장의 단어는 다르지만 의미가 거의 동일하므로 매우 높은 점수가 나옵니다.)
