import matplotlib.pyplot as plt
import tkinter as tk
from sympy import symbols, Eq, solve
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
y_Var=tk.StringVar()
x_Var=tk.StringVar()
xt_Var=tk.StringVar()
n_Var=tk.StringVar()
eq_Var=tk.StringVar()
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    meeting=y_Var.get()
    passkey=x_Var.get()
    time = xt_Var.get()
    duration= n_Var.get()
    equation= eq_Var.get()
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'y', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = y_Var, font=('calibre',10,'normal'))
  

passw_label = tk.Label(root, text = 'x', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = x_Var, font = ('calibre',10,'normal'))

time_label = tk.Label(root, text = 'xt', font = ('calibre',10,'bold'))
time_entry=tk.Entry(root, textvariable = xt_Var, font = ('calibre',10,'normal'))

dur_label = tk.Label(root, text = 'H', font = ('calibre',10,'bold'))
dur_entry=tk.Entry(root, textvariable = n_Var, font = ('calibre',10,'normal'))
eq_label = tk.Label(root, text = 'equation', font = ('calibre',10,'bold'))
eq_entry=tk.Entry(root, textvariable = eq_Var, font = ('calibre',10,'normal'))
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
time_label.grid(row=2,column=0)
time_entry.grid(row=2,column=1)
dur_label.grid(row=3,column=0)
dur_entry.grid(row=3,column=1)
eq_label.grid(row=4,column=0)
eq_entry.grid(row=4,column=1)
sub_btn.grid(row=5,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()
eq_val = eq_Var.get()
y_val = float(y_Var.get())
x_val =float(x_Var.get())
xt_val = float(xt_Var.get())
n_val = int(n_Var.get())


def euler(x,y,xt,n):
  xi = []
  yi = []
  xi.append(x)
  yi.append(y)
  h = (xt-x)/n
  for i in range (0,n):
    x= x+h
    def f(x,y):
      equation=eval(eq_val)
      return equation
    y = y + f(x,y)*h
    xi.append(x)
    yi.append(y)
  return xi,yi
def heun(x,y,xt,n):
  xi = []
  yi = []
  xi.append(x)
  yi.append(y)
  h = (xt-x)/n
  for i in range (0,n):
    def f(x,y):
      equation=eval(eq_val)
      return equation
    k1= f(x,y)
    k2 = f(x+h,y+k1*h)
    y = y + (k1+k2)*h/2
    xi.append(x+(i+1)*h)
    yi.append(y)
  return xi,yi
def midpoint(x,y,xt,n):
  xi = []
  yi = []
  xi.append(x)
  yi.append(y)
  h = (xt-x)/n
  for i in range (0,n):
    def f(x,y):
      equation=eval(eq_val)
      return equation
    k1= f(x,y)
    k2 = f(x+h/2,y+k1*h/2)
    y = y + k2*h
    xi.append(x+(i+1)*h)
    yi.append(y)
  return xi,yi
def ralston(x,y,xt,n):
  xi = []
  yi = []
  xi.append(x)
  yi.append(y)
  h = (xt-x)/n
  for i in range (0,n):
    def f(x,y):
      equation=eval(eq_val)
      return equation
    k1= f(x,y)
    k2 = f(x+3*h/4,y+3*k1*h/4)
    y = y + (k1/3+2*k2/3)*h
    xi.append(x+(i+1)*h)
    yi.append(y)
  return xi,yi
def runge_kutta4(x,y,xt,n):
  xi = []
  yi = []
  xi.append(x)
  yi.append(y)
  h = (xt-x)/n
  for i in range (0,n):
    def f(x,y):
      equation=eval(eq_val)
      return equation
    k1= f(x,y)
    k2 = f(x+h/2,y+k1*h/2)
    k3 = f(x+h/2,y+k2*h/2)
    k4 = f(x+h,y+k3*h)
    y = y + (k1+2*k2+2*k3+k4)*h/6
    xi.append(x+(i+1)*h)
    yi.append(y)
  return xi,yi
x= x_val
y=y_val
xt=xt_val
n= n_val

xi , ye = euler(x,y,xt,n)
xi , yh = heun(x,y,xt,n)
xi , ym = midpoint(x,y,xt,n)
xi , yr = ralston(x,y,xt,n)
xi , yr4 = runge_kutta4(x,y,xt,n)
print("Euler= ", ye[n])
print("Heun= ", yh[n])
print("Midpoint= ", ym[n])
print("Ralston= ", yr[n])
print("Runge-Kutta4= ", yr4[n])

plt.figure(figsize=(12,8))
plt.plot(xi , ye, "b", label="Euler")
plt.plot(xi , yh, "g", label="Heun")
plt.plot(xi , ym, "r", label="Midpoint")
plt.plot(xi , yr, "y", label="Ralston")
plt.plot(xi , yr4, "k", label="Runge-Kutta4")
plt.legend()
plt.show()