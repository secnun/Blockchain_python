import random
import string
import hashlib
#해당 버전은 가장 기본적인 형태의 채굴 로직
#실제로는 [거래 검증] → [블록 후보 생성] → [난이도 퍼즐 풀이]를 통해 최종 블록 생성


## 이더리움 네트워크가 낸 문제
PROBLEM_WORD = "a"       # 찾아야하는 단어
PROBLEM_DIFFICULTY = 1   #난이도 숫자, 숫자가 높아질수록 난이도가 높아짐
### 위의 문제의 경우 해시의 값 앞 1번째 자리가 a 이면 문제 해결(채굴 완료)

## 채굴
start_nonce = random.choice(string.ascii_letters)

i = 0
while True:
    nonce = start_nonce + str(i)
    nonce_result =  hashlib.sha256((nonce).encode()).hexdigest()
    print(i,nonce, nonce_result)
    if nonce_result[0: PROBLEM_DIFFICULTY] == PROBLEM_WORD * PROBLEM_DIFFICULTY :
        nonce = nonce_result
        break
    i += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           