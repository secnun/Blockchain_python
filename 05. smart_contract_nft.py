import datetime
import hashlib

#"구매자"가 "판매자"에게 어떤 "파일"을 "몇개의 코인"을 통해 구매한 거래내역 예시
#일종의 스마트컨트랙트를 활용한 NFT 예시
block_body =  { "transaction1": {
                            '판매자' : '장영희',
                            '구매자' : '이박사',
                            '개수' : '3개',
                            'timestamp' : 1652247422892844,
                            'smart_contract' :  { '파일명':    'wedding.jpg',
                                                  '파일소개':  '장영희 결혼식 기념사진',
                                                  '파일데이터' : 'bf9ed7487a7f0dfc'} #(이미지정보)
                               },
                    "transaction2": {
                            '판매자' : '김민수',
                            '구매자' : '최영호',
                            '개수' : '1개',
                             'timestamp' : 165224743233231,
                            'smart_contract' :  { '파일명':    '이력서.jpg',
                                                  '파일소개':  '김민수의 생애 첫 이력서',
                                                  '파일데이터' : 'ef394130e1eb1'} #(이미지정보)
                               }
                   }


block_header =  {  'Block_height' : 0,
                   'Block_created_at' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   'Miner' : "0xea674fdde714fd979de3edf0f56aa9716b898ec8",
                   'Block_Reward' : 2.132,
                   'Difficulty' : 12382889997310022,
                   'Nonce'  : '0x7ccf42b8e05d031f',
                   'Block_size' : '178556 bytes',
                   'Parent_hash' : '0xe1f3d0e83542e20735d453006cc6d8975920e7aec951c3b974eade52901e97e7',
                   'Body_hash' : hashlib.sha256(str(block_body).encode()).hexdigest()
                }


#body_hash = hashlib.sha256(str(block_body).encode()).hexdigest()


block1 =  { 'header' : block_header,
            'transaction' : block_body
           }

print(block1)