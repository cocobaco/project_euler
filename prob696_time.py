# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:39:15 2020

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np

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


# n=10, t=3, s=x
x = np.array([1, 2, 3, 4])
y = np.array([7424, 139084, 734100, 2364872])
plot_data_with_fit(x, y, func_exp, title='n=10, t=3')


# n=4, s=3, t=x
x = np.array([1, 2, 3, 4, 5])
y = np.array([204, 1698, 8946, 32886, 88200])
plot_data_with_fit(x, y, func_exp, title='n=4, s=3')

