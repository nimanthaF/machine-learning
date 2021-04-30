from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

xs=np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array([5,4,6,5,6,7], dtype=np.float64)

def bestfit_slopes_and_intercept(xs,ys):
    m=((mean(xs)*mean(ys))-(mean(xs*ys)))/((mean(xs)**2)-mean(xs**2))
    c=mean(ys)-(m*mean(xs))
    return m,c

def squared_error(ys_original,ys_line):
    return sum((ys_line-ys_original)**2)

def coefficient_of_determiantion(ys_original,ys_line):
    y_mean_line=[mean(ys_original) for y in ys_original]
    squared_error_regression=squared_error(ys_original,ys_line)
    squared_y_mean=squared_error(ys_original,y_mean_line)
    return 1-(squared_error_regression/squared_y_mean)
    

m,c=bestfit_slopes_and_intercept(xs,ys)

regressionline=[(m*x)+c for x in xs]

predict_x=7
predict_y=(m*predict_x)+c

r_squared=coefficient_of_determiantion(ys,regressionline)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y,color='c')

plt.plot(xs,regressionline)
plt.show()
