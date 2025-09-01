## 블록1
block1 =  {'INDEX':0,
            'Seller' : '파공블',
            'Buyer' : '김민수',
            'amount' : '3개',
            'time' : '1990-01-01 00:00:00',
            'previous_block' : None
          }
          
 ## 블록2
block2 =  {'INDEX':1,
            'Seller' : '김민수',
            'Buyer' : '김영수',
            'amount' : '3개',
           'time' : '1990-01-02 01:02:03',
           'previous_block' : block1
          }
   
## 블록3
block3 =  {'INDEX':3,
            'Seller' : '김영수',
            'Buyer' : '박명수',
            'amount' : '3개',
            'time' : '1990-01-03 02:03:04',
           'previous_block' : block2
          }

## 블록4
block4 =  {'INDEX':4,
            'Seller' : '박명수',
            'Buyer' : '이미래',
            'amount' : '3개',
            'time' : '1990-01-04 02:03:04',
           'previous_block' : block3
          }

## 블록5
block5 =  {'INDEX':5,
            'Seller' : '이미래',
            'Buyer' : '최용수',
            'amount' : '3개',
            'time' : '1990-01-05 02:03:04',
           'previous_block' : block4
          }

## 블록6
block6 =  {'INDEX':6,
            'Seller' : '최용수',
            'Buyer' : '강영희',
            'amount' : '3개',
            'time' : '1990-01-06 02:03:04',
           'previous_block' : block5
          }

print(block6)
