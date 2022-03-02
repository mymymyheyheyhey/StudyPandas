#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_outliers(df):
    import numpy as np
    print("이상치를 체크합니다.")
    print("조회하려는 컬럼의 이름을 입력하세요.")
    colname = input()
    q1, q3 = np.percentile(df[colname], [25, 75])
    iqr = q3 - q1
    ceil = q3 + 1.5 * iqr
    floor = q1 - 1.5 * iqr
    check = df[(df[colname] > ceil)
             | (df[colname] < floor)]
    return(check)

