import random
from copy import deepcopy

import tensorflow as tf
from keras.models import load_model
import convert as c
import numpy as np

board = [
            ['bxe','bma','bvo','bsi','btu','bsi','bvo','bma','bxe'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','bph','---','---','---','---','---','bph','---'],
            ['bch','---','bch','---','bch','---','bch','---','bch'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rch','---','rch','---','rch','---','rch','---','rch'],
            ['---','rph','---','---','---','---','---','rph','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rxe','rma','rvo','rsi','rtu','rsi','rvo','rma','rxe']
]

model = load_model('C:\\Users\\OnDoing\\ChineseChess\\ml\\chinese_chess_model_better.h5')
def evaluation(board, redMove, after):
    
    X_board = c.one_hot_encode(board)   # [  [[]],[[]], ]
    # for i in (X_board):
    #     print(i)
    
    X_turn = 0 if redMove else 1

    x = np.array([X_board])
    
    xx = np.array([X_turn])
    
    
    y = model.predict([x,xx])
    return y.flatten()

print(evaluation(board, True, False))