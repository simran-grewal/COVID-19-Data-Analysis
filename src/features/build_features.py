import numpy as np

from sklearn import linear_model
reg = linear_model.LinearRegression(fit_intercept=True)

def get_doubling_time_via_regression(in_array):
    ''' Use a linear regression to approximate the doubling rate'''
    
    y = np.array(in_array)
    X = np.arange(-1,2).reshape(-1, 1)
    
    assert len(in_array)==3
    reg.fit(X,y)
    intercept=reg.intercept_
    slope=reg.coef_
    
    return intercept/slope

if __name__ == '__main__':
    test_data = np.array([2, 4, 6])
    result = get_doubling_time_via_regression(test_data)
    print('The test slope is: ' + str(result))