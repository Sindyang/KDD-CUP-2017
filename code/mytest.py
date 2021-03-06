#!/usr/bin/python
import numpy as np
import scipy.sparse
import pickle
import xgboost as xgb

### simple example
# load file from text file, also binary buffer generated by xgboost
dtrain = xgb.DMatrix('/home/wangsy/Documents/XgBoost_Example/demo/data/training_final_format.txt')
dtest = xgb.DMatrix('/home/wangsy/Documents/XgBoost_Example/demo/data/test2_final_format.txt')
dsubmit = xgb.DMatrix('/home/wangsy/Documents/XgBoost_Example/demo/data/submit_final_format.txt')

# specify parameters via map, definition are same as c++ version
param = {'max_depth':6, 'min_child_weight':5,'eta':0.021,'gamma':0, 'silent':1, 'objective':'reg:linear', 'colsample_bytree':0.8}

# specify validations set to watch performance
watchlist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 103
bst = xgb.train(param, dtrain, num_round, watchlist)

# this is prediction
preds = bst.predict(dtest)
np.savetxt('/home/wangsy/Documents/XgBoost_Example/demo/data/result.csv', preds, delimiter = ',') 
labels = dtest.get_label()
mape = 0
for i in range(len(preds)):
    mape+=abs((preds[i]-labels[i])/labels[i]) 
mape = mape/float(len(preds)) 
print ('mape=%f' % mape)
