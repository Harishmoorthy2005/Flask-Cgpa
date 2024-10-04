import numpy as np
import pandas as pd
ser1=pd.Series(['a','b','c','d'])
ser2=pd.Series(['e','f','g','h','i'],dtype=np.char)
res=pd.DataFrame({'col1':ser1,'col2':ser2})
print(res.info())