import datetime
import hashlib
#스마트컨트랙트를 통한 토큰 발행 예시
#Layer2 코인 NUN 발행

block_body =  { "transaction1": {
                            '판매자' : 'NUN',
                            '구매자' : '',
                            '개수' : '0개',
                            'timestamp' : 1652247422892844,
                            'smart_contract' :  { '토큰명':    'NUN',
                                                  '토큰설명':    'NUN 코인',
                                                  '토큰발행개수':  100
                                                  } 
                               },
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


block2 =  { 'header' : block_header,
            'transaction' : block_body
           }

print(block2 )