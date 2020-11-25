# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:39:15 2020

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.optimize import curve_fit

plt.style.use('default')


def func_exp(x, a, b, c):
    return a * np.exp(b * x) + c


def fit_function(func, x, y):
    # fit to find parameters
    popt, pcov = curve_fit(func, x, y)
    
    # https://stackoverflow.com/a/37899817
    # residuals
    residuals = y - func(x, *popt)
    # residual sum of squares 
    ss_res = np.sum(residuals**2 )
    # total sum of squares
    ss_tot = np.sum((y - np.mean(y))**2)
    # r-squared
    r_squared = 1 - (ss_res / ss_tot)
    
    return popt, pcov, r_squared


def plot_data_with_fit(xdata, ydata, fit_func, title='title'):
    popt, pcov, r_squared = fit_function(fit_func, xdata, ydata)
    
    plt.figure()
    plt.scatter(xdata, ydata, label='data')
    plt.plot(xdata, fit_func(xdata, *popt), '--r',
             label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.text(x=0.25, y=0.3, ha='center', va='center', 
            transform = plt.gca().transAxes,
            s=f'$r^2$ = {r_squared:.3f}', 
            fontsize=14)
    plt.title(title)
    plt.legend()
    plt.show()
    
    

# n=4, t=1, s=x
x = np.array([1,2,3,4,6,8,10])
y = np.array([46,468,1698,4168,14556,35088,69220])
plot_data_with_fit(x, y, func_exp, title='n=4, t=1')


# n=4, s=3, t=x
x = np.array([1, 2, 3, 4, 5])
y = np.array([204, 1698, 8946, 32886, 88200])
plot_data_with_fit(x, y, func_exp, title='n=4, s=3')


# n=6, s=2, t=x
x = np.array([1, 2, 3, 4, 5])
y = np.array([228, 2136, 12676, 52424, 157752])
plot_data_with_fit(x, y, func_exp, title='n=6, s=2')


# s=2, t=2, n=x
x = np.array([2, 3, 4, 5, 6])
y = np.array([12, 138, 468, 1102, 2136])
plot_data_with_fit(x, y, func_exp, title='s=2, t=2')


# n=8, s=5, t=x
x = np.array([1, 2, 3])
y = np.array([2760, 94990, 2167600])
plot_data_with_fit(x, y, func_exp, title='n=8, s=5')


# n=10, s=1, t=x
x = np.array([1, 2, 3, 4, 5])
y = np.array([170, 1426, 7424, 26139, 64152])
plot_data_with_fit(x, y, func_exp, title='n=10, s=1')


# n=10, t=3, s=x
x = np.array([1, 2, 3, 4])
y = np.array([7424, 139084, 734100, 2364872])
plot_data_with_fit(x, y, func_exp, title='n=10, t=3')


df = pd.DataFrame({'n': [4, 4, 4, 4, 4, 4, 4, 
                         10, 10, 10, 10, 
                         6, 6, 6, 6, 6, 
                         4, 4, 4, 4, 4, 
                         8, 8, 8, 
                         2, 3, 4, 5, 6, 
                         10, 10, 10, 10, 10], 
                   's': [1, 2, 3, 4, 6, 8, 10, 
                         1, 2, 3, 4, 
                         2, 2, 2, 2, 2, 
                         2, 2, 2, 2, 2, 
                         5, 5, 5, 
                         3, 3, 3, 3, 3, 
                         1, 1, 1, 1, 1], 
                   't': [1, 1, 1, 1, 1, 1, 1, 
                         3, 3, 3, 3, 
                         1, 2, 3, 4, 5, 
                         2, 2, 2, 2, 2, 
                         1, 2, 3, 
                         1, 2, 3, 4, 5, 
                         1, 2, 3, 4, 5], 
                   'num': [46, 468, 1698, 4168, 14556, 35088, 69220, 
                           7424, 139084, 734100, 2364872, 
                           228, 2136, 12676, 52424, 157752, 
                           12, 138, 468, 1102, 2136, 
                           2760, 94990, 2167600, 
                           204, 1698, 8946, 32886, 88200, 
                           170, 1426, 7424, 26139, 64152]
                   })

    
df2 =

# ML regression

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error, r2_score


models = {'LR': LinearRegression(), 
          'SVM': SVR(gamma='auto'), 
          'RF': RandomForestRegressor(n_estimators=50)}


X = df[['n', 's', 't']].copy()
y = df['num'].copy()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


mses = {}
r2s = {}
preds = {}
cv_means = {}
cv_stds = {}
cv = 3

df_validate = pd.DataFrame({'actual': y_test})

for name, model in models.items():
    print(name)
    cv_scores = np.sqrt(-cross_val_score(model, X_train, y_train, cv=cv, 
                                    scoring='neg_mean_squared_error'))
    cv_means[name] = np.mean(cv_scores)
    cv_stds[name] = np.std(cv_scores)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2s[name] = r2_score(y_test, y_pred)
    mses[name] = mean_squared_error(y_test, y_pred)
    preds[name] = y_pred

    col_pred_name = '_'.join(['pred', name])
    df_validate[col_pred_name] = preds[name]

df_scores = pd.DataFrame({'mse': mses, 'r2': r2s, 
                          'CV': cv_means, 'CVstd': cv_stds})
    
    
print(df_scores.round(3))
