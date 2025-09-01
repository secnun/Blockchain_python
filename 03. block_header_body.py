import datetime
import hashlib
import json
#주의. 데이터 타입이 조금 들쭉날쭉하지만, 현재는 간단한 부분이니 pass

# 블록 해시 계산 함수
# str은 파이썬 내부 표현이라 블록체인 특성상 고정되어야 하는 값들이니, JSON 직렬화하는게 안정적.
# 필요시 활용 가능
def calc_hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

genesis_block_body = { "거래내역1": {
                            '판매자' : None,
                            '구매자' : None,
                            '개수' : None,
                            '거래시간' : None,
                            '거래수수료' : None     
                            }
                    }

genesis_block_header = { '블록의 생성 번호' : 0,
                   '블록의 생성 시간' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   '블록 사이즈' : '100000 bytes',
                   '이번 블록 몸통 내역의 해시값' : hashlib.sha256(json.dumps(genesis_block_body, sort_keys=True).encode()).hexdigest(),                
                   '이전 블록 해시값': '0x0'  # 제네시스 블록은 이전 블록이 없음
                   }

genesis_block = {
    'header': genesis_block_header,
    'transaction': genesis_block_body
}

# 제네시스 블록의 전체 해시 계산
genesis_block_hash = calc_hash(genesis_block)


block_body =  {   "거래내역1": {
                            '판매자' : '파공블',
                            '구매자' : '김민수',
                            '개수' : '3개',
                            '거래시간' : '1990년 1월 1일 00시 00분 00초',
                            '거래수수료' : '0.001개'     
                               },
                    "거래내역2": {
                            '판매자' : '김민수',
                            '구매자' : '김영수',
                            '개수' : '3개',
                            '거래시간' : '1990년 1월 2일 01시 02분 03초',
                            '거래수수료' : '0.001개'                        
                               }
                   }


block_header =  {  '블록의 생성 번호' : 1,
                   '블록의 생성 시간' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   '블록의 채굴자' : "0xea674fdde714fd979de3edf0f56aa9716b898ec8",
                   '블록 채굴자의 보상 값' : 2.132,
                   '블록 채굴 난이도' : 12382889997310022,
                   'Nonce'  : '0x7ccf42b8e05d031f',
                   '블록 사이즈' : '178556 bytes',
                   '이전 블록의 해시값' : genesis_block_hash,
                   '이번 블록 몸통 내역의 해시값' : hashlib.sha256(str(block_body).encode()).hexdigest() 
                }

block1 =  { 'header' : block_header,
            'transaction' : block_body
           }

print(block1)