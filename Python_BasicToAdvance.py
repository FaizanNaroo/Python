'''
from math import sqrt    #import particular function
import math as mymath   #alias 

import os                                    #importing the external libraries
os.system("python -m pip install pandas")
import pandas as pd


print(dir(pd))           #give all the function names of the library

# numpy      used for mathematical operations e.g matrix multiplication
'''

'''
print("Hello, World!")
#input is in form of string so we have to convert its type
print("enter the value of x:")
x=int(input())

print(x)

first_name="hello"
print(first_name)

y=2 

shapes={
    "Rectangle":{
        "l":x,
        "h":y,
        "area":x*y,
    },
    "Circle":{
        "r":x,
        "area":3.14*x*x,
    },
}

for shape,properties in shapes.items():
    print(f"\nDetails for {shape}")
    for key,value in properties.items():
        print(f"{key.capitalize()}:{value}")


print("x+y=",x+y)
print("x/y=",x/y)         #it gives answer in complete way
print("x//y=",x//y)    #give only quotient
print("x**y=",x**y)    #x ki power y

fname='Faizan'
lname="naroo"
fullname=fname+" "+lname
print(fullname)
print(fname.upper())
print(lname.capitalize())
print('helloo ',lname*3)
initial=fname[0]+lname[0]
print(initial)
print("  helo  ".strip())   #remove spaces from start and end

print(type(x))
print(type(fullname))
print(type(lname))
print("\n")

message="hello {fname},welcome \n"
print(message)
message=f"hello {fname},welcome \n"
print(message)

list_quantities={
    "books":'0',
    "notes":'0'
}
item_init={
    "books":0,
    "notes":0
}
print("showing way of using list:\ninput: ")
list_quantities["books"]=input()
item_init["books"]=int(list_quantities["books"])

print(type(list_quantities["books"]),list_quantities["books"])
print(type(item_init["books"]),item_init["books"])

item_names={"books","laptop","notes"}
list=",".join(item_names)
print(f"items:\n{list}")
'''


'''
#functions
def func(name,pet='nothing'):
    print(f"hello,{name}, pet:{pet}")

     
func("rehan\n")
func("rehan","cat")
func(pet="hamster",name="brother")
'''

'''
def operation(x,y):
    product=x*y
    sum=x+y
    line="sum and product"
    return line,sum,product

result=operation(2,3)
print(result)

result1,result2,result3=operation(2,3)
print(result1,result2,result3)
'''

'''
i=1
while i<5:
     print(i)
     i+=1

print("for loop")
a=range(3,15,2)     # start=0,stop,step=1
skip={5,15}
i=1
for var in  a:
     print(var)
     if(var==9):
          break
     elif(var>=5):      #else if()
          break
          
'''

'''
#listing
list=["apple",'mango',123]
for a in list:
    print(a)

del list[1]
print(list)

l=["grapes"]
concatenate=list+l
print(concatenate)

list.append("abc")
print(list)

slicing=list[0:2]
print(slicing)

check="apple" in list
print(check)

lenght=len(list)
print(lenght)

list.insert(1,"banana")
print(list)
'''

'''
#tuples
t=(1,2,3,4)
concatenate=t+(7,8)
print(concatenate)
print(t*2)
print(concatenate[3])
print(concatenate[-1])    #print wrap around
print(t.index(2))
print(t.count(2))

try:
 t[2]=17              # this will give error for tuple
except TypeError as e:
 print("error")
print(t)

#sets
s1={1,2,3,4}
print("set 1:",s1)
s1.add(6)
s1.remove(2)
print("set 1:",s1)

s2={"a","b","c"}
U=s1.union(s2)
print(U)

s2={"a","b","c"}
A=s1.symmetric_difference(s2)    #either is 1 or 2 not in both
print(A)

s3={30,10,15,30,15}               #always print only unique elements
print(s3)

#dictionary
dic={'a':1,'b':2,'c':3}
print(dic)
for key,value in dic.items():
 print(f"key:{key}, value:{value}")
print(dic['a'])
dic['b']=5
print(dic.get('b'))
del dic['b']
print(dic)
rem=dic.pop('a')
print(rem)
print(dic)
dic.clear()
print(dic)

sqr={x:x*x for x in range(1,6)}
print("dictionary:",sqr)

#nested
nested_dic={
 'class1':{'stud1':'faizan','stud2':'khan'},
 'class2':{'stud1':'naroo','stud2':'rajput'}
}
print(nested_dic)
print(nested_dic['class1']['stud2'])
'''

'''

import array
arr=array.array('i',[1,2,3,4,5])
print(arr)

arr.insert(3,17)
print(arr)

arr.remove(17)
print(arr)

arr.pop()
print(arr)

arrto_list=arr.tolist()
print(arrto_list)

'''

'''

stack=[]                       # dont forget the =
def push(stack,element):
    stack.append(element)

def pop(stack):
    if not is_empty(stack):
        element=stack.pop()
        return element
    else:
        print("stack is empty")

def top(stack):
    return stack[-1]

def is_empty(stack):
    return len(stack)==0


push(stack,1)
push(stack,2)
push(stack,3)
print(stack)
print(top(stack))
pop(stack)
print(stack)

from collections import deque
queue=deque([1,2,3,4,5,6])
print(queue)

def dequeue(queue):
    if not is_empty(queue):
        element=queue.popleft()
        return element
    else:
        print('queue is empty')

def peek(queue):
    return queue[0]

queue.rotate(2)               #move to the right direction (moving front to rear)and last will wrap around
print(queue)

queue.rotate(-2)               #move to the left direction (moving rear to front)and last will wrap around
print(queue)

queue.reverse()
print(queue)
'''

'''
#os
import os
def main():
    print(os.getcwd())
    print (type(os.getcwd()))
     
    print(os.getcwdb())
    print (type(os.getcwdb()))
    
   # os.mkdir("directory to delete")
    print(os.listdir())

    #os.chdir("")
   # os.rename("directory to delete","nothing")
    print(os.listdir())
   # os.rmdir("nothing")
    print(os.listdir())

    print(os.path.exists('C:\\Users\\hp\\OneDrive\\Desktop\\Summer\\python'))   #use the byte path
    print(os.path.isfile('C:\\Users\\hp\\OneDrive\\Desktop\\Summer\\python')) 
    print(os.path.isdir('C:\\Users\\hp\\OneDrive\\Desktop\\Summer\\python')) 
     
    path2=os.path.join(os.getcwd(),"nothing.txt")
    print(str(path2))
    print(os.path.basename(path2))
    print(os.path.dirname(path2))
main()
'''
'''
#file handling
import os
file=open("testing.txt",'w')     #also make file and open it
file.write("hello world\n")
file.write(str(123)+"\n")
file.close

file =open  ("testing.txt",'a')
file.write("this is appending")
file.close
file=open("testing.txt","r")
content=file.read()
print(content)
file.close

file=open("testing.txt",'r')
for line in file:
    print("line:",line.strip())
file.close

file=open("testing.txt","r")
lines=file.readlines()                  #it gives the list of line seperated with comma
print("line1:",lines)          
file.close()

lines[2]="line is changed"
file=open("testing.txt","w")
file.writelines(lines)
file.close()
file=open("testing.txt","r")
content=file.read()
print(content)
file.close()

lines.pop(2)
file=open("testing.txt","w")
file.writelines(lines)
file.close()
file=open("testing.txt","r")
content=file.read()
print(content)
file.close()

file=open("testing.txt",'r')
while True:
    line=file.readline()
    if not line:
        break
    print(line.strip())
file.close()

os.remove("testing.txt")

file=open("testing.txt","w")
file.close()
print(file.closed)


os.remove("testing.txt")

'''

'''
#exception handling 
try:
    file=open("testing.txt",'r')
except FileNotFoundError:      #ValueError,ZeroDivisionError
    print("file is not found")
else:
    print("file opened")
    file.close()
    print("file closed")
finally:
    print("exception is done") 
'''

#GUI
'''
import tkinter as mytk

def on_button_click():
    print("button clicked")

def another_function():
    print("another function executed")

def button_click_with_param(param):
    print(f"button clicked with parameter: {pararm}")

root=mytk.Tk()
root.title("My GUI Application")
root.geometry("400x200")

kw={'bg':'yellow'}
label=mytk.Label(root,text="hello world",**kw)
label.pack()

button=mytk.Button(root,text="Click Me")
button.pack()

button1=mytk.Button(root,text="Click Me1",command=on_button_click,bg="blue",fg="red")
button1.pack(pady=40)

root.mainloop() 
'''
'''
import tkinter as mytk
from tkinter import ttk

def save_inputs():
    with open("inputs.txt",'w') as file:
        file.write(f"test entry:{entry_text.get()}\n")
        file.write(f"combo box:{combo_var.get()}\n")
        file.write(f"check button:{check_var.get()}\n")
        file.write(f"radio button:{radio_var.get()}\n")
    print("inputs saved to 'inputs.txt'")

root =mytk.Tk()
root.title("Tkinter Widgets Example")
root.geometry("500x500")

entry_label=mytk.Label(root,text="enter some text:")
entry_label.pack(pady=5)
entry_text=mytk.Entry(root)
entry_text.pack(pady=5)

combo_lable=mytk.Label(root,text="choose an option:")
combo_lable.pack(pady=5)
combo_var=mytk.StringVar()
combo_box=ttk.Combobox(root,textvariable=combo_var)
combo_box['values']=("option 1","option 2","option 3")
combo_box.current(0)
combo_box.pack(pady=5)

check_var=mytk.BooleanVar()
check_button=mytk.Checkbutton(root,text="check me",variable=check_var)
check_button.pack(pady=5)

radio_label=mytk.Label(root,text="choose an option:")
radio_label.pack(pady=5)
radio_var=mytk.StringVar()
radio_button1=mytk.Radiobutton(root,text="option A",variable=radio_var,value="A")
radio_button1.pack(pady=5)
radio_button2=mytk.Radiobutton(root,text="option B",variable=radio_var,value="B")
radio_button2.pack(pady=5)

save_button=mytk.Button(root,text="save input",command=save_inputs)
save_button.pack(pady=20)

root.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk,messagebox

def show_info_dialog():
    messagebox.showinfo("Dialog box","this is a dialog box")

def show_info_message():
    messagebox.showinfo("Message box","this is a message box")

def save_listbox_collection():
    selected_items=list_box.curselection()
    selected_text=[list_box.get(i)for i in selected_items]
    print(f"selected items:{selected_text}")  

root=tk.Tk()
root.title("Tkinter Widgets Example")

paned_window=ttk.PanedWindow(root,orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH,expand=True)

left_frame=ttk.Frame(paned_window,width=100,height=300,relief=tk.SUNKEN)
paned_window.add(left_frame,weight=4)


right_frame=ttk.Frame(paned_window,width=100,height=300,relief=tk.SUNKEN)
paned_window.add(right_frame,weight=4)

text_widget=tk.Text(left_frame,wrap='word',height=10)
scroll_bar1=ttk.Scrollbar(left_frame,orient='vertical',command=text_widget.yview)
text_widget.configure(yscrollcommand=scroll_bar1.set)
text_widget.grid(row=0,column=0,sticky='nsew')
scroll_bar1.grid(row=0,column=1,sticky='ns')

left_frame.grid_rowconfigure(0,weight=1)
left_frame.grid_columnconfigure(0,weight=1)


list_box=tk.Listbox(left_frame)
list_box.grid(row=1,column=0,sticky='ew',padx=2)
for item in ["Item1","Item2","Item3"]:
    list_box.insert(tk.END,item)

spin_box=tk.Spinbox(left_frame,from_=0,to=10) 
spin_box.grid(row=2,column=0,sticky='ew',pady=10)

menu_button=tk.Menubutton(right_frame,text="Menu Button",relief=tk.RAISED)
menu=tk.Menu(menu_button,tearoff=0)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")
menu.add_command(label="Option 4")
menu_button.config(menu=menu)
menu_button.pack(pady=20)

dialog_button=tk.Button(right_frame,text="Showing Dialog",command=show_info_dialog)
dialog_button.pack(pady=20)
message_button=tk.Button(right_frame,text="Showing Message",command=show_info_message)
message_button.pack(pady=20)

save_button=tk.Button(right_frame,text="Save listbox",command=save_listbox_collection)
save_button.pack(pady=20)

root.mainloop()

'''
'''
#canvas
import tkinter as tk 

root =tk.Tk()
root.title("canvas")

canvas=tk.Canvas(root,width=800,height=600,bg='black')
canvas.pack()

canvas.create_line(10,10,200,200,fill='red',dash=(4,2))
canvas.create_arc(10,250,350,2,start=0,extent=150,outline="pink")
canvas.create_text(450,250,text="hello",font=("Arial", 20), fill="blue")
root.mainloop()
'''
'''
#classed and objects
class Animal:
    legs = 4
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{sound}")

def main():
    dog = Animal("Supra", "Dog")
    print(dog.name)
    print(dog.species)
    dog.make_sound("aaa")
main()
'''
'''
import subprocess
import sys
import pip
import os
import pandas as pdVista
import numpy as numVista

def main():
    myseries=pdVista.Series()
    print(myseries)

    myseries=pdVista.Series(['a','b','c','d','e'])
    print(myseries)

    myseries=pdVista.Series(100*numVista.random.randn(5),index=['a','b','c','d','e'])
    print(myseries)

    prime_list=[23,45,5,33,24,5,34,4]
    prime_series=pdVista.Series(prime_list)
    print(prime_series)

    print(numVista.mean(prime_series))
    
    print(numVista.median(prime_series))
    
    print(numVista.sqrt(prime_series))

    
    print(prime_series[4:8])
    
    print(prime_series.iloc[7])
    
    print(prime_series.sort_values())
    
    print(prime_series.sort_index())

    #data frames

    data={
        'name':['ali','ahmend','akbar'],
        'age':[2,4,6],
        'city':['pindi','karachi','lahore']
    }

    myDf=pdVista.DataFrame(data)
    print(myDf,'\n')

    print(myDf.head(),'head\n')    #print first five rows
    
    print(myDf.tail(),'tail\n')    #pritn last five rows
    
    print(myDf.info(),'info\n')
    
    print(myDf.describe(),'describe\n')

    myDf_transpose=myDf.transpose()
    print(myDf_transpose)

    myDf_sort=myDf.sort_values(by='age')
    print(myDf_sort)

    myDf_sort_index=myDf.sort_index()
    print(myDf_sort_index)

    myDf_with_nan=myDf.copy()
    myDf_with_nan.loc[2,'age']=None
    print(myDf_with_nan)

    a=myDf_with_nan.dropna()
    print(a)

    a=myDf_with_nan.fillna(value={'age':23})
    print(a)
   
    myDf["age_plus_15"]=myDf['age'].apply(lambda x:x+14)
    print(myDf)
    
    applied=myDf.map(lambda x:str(x).upper() )
    print("applied;\n",applied)
    
    myDf['country']='pakistan'
    print(myDf)

    my_drop=myDf.drop('age',axis=1)    #axis=1 to drop column and axis=0 drop row
    print(my_drop)     


main()
'''

'''
#data loading and storage in various formats
import subprocess
import sys
import pip
import os
import pandas as pdVista
import openpyxl

def main():
    data={
        'name':['ali','ahmend','akbar'],
        'age':[2,4,6],
        'city':['pindi','karachi','lahore']
    }
    pd=pdVista.DataFrame(data)


    pd.to_csv('data.csv',index=False)
    a=pdVista.read_csv('data.csv')
    print(a)

    pd.to_json('data.json',orient='records')
    a=pdVista.read_json('data.json')
    print(a)

    pd.to_json(sys.stdout,orient='records')#stdout means directly output to the terminal, orient means the design of output
    a=pdVista.read_csv('data.csv')
    print(a)  

    pd.to_csv('data.tsv',sep='\t',index=False)#it is tsv, index=false means do not write index column
    tsv=pdVista.read_csv('data.tsv',sep='\t')
    print(tsv)

    print("Excel\n")
    file_path='sample_data.xlsx'
    with pdVista.ExcelWriter(file_path) as w:
        pd.to_excel(w,sheet_name='ss',index=False)
        print(f'{file_path}')
    r=pdVista.read_excel(file_path,sheet_name='ss')
    print(r)

main()
'''

'''
try:
   x = int(“Hello”)
 except ValueError:
  print(“Caught a ValueError”)
 else:
  print(“No error occurred”)
 finally:
  print(“This will always execute”)
  '''

'''
#data science and data analysis
import subprocess
import sys
import pip
import os
import pandas as pd
import numpy as np

data={
        'name':['ali','ahmend','akbar',np.nan],
        'age':[2,4,6,11],
        'city':['pindi','karachi',np.nan,'lahore']
}
pf=pd.DataFrame(data)

print(pf.isna())

print(pf.dropna())#drop rows with missing values

print(pf.dropna(axis=1))  #drop column

print("\n")
a=pf._append(pf.iloc[1],ignore_index=True)
print(a)

print(a.drop_duplicates())
 
print(pf.replace({'ali':'heroo'}))

print(pf.rename(columns={'name':'alpha'}))
print(pf.rename(index={0:'first'}))

print(pf[pf['age']<=4])#inner pf is filter the condition and outer is filter the true conditions
print("hello")
for i in [0,1,2,3]:
 print(pf.sample(n=2,random_state=i))
 i=i+1

print(pf.sample(frac=1).reset_index(drop=True))
'''

'''

import pandas as pd
import numpy as np

# First DataFrame
data = {
    'name': ['ali', 'ahmend', 'akbar', np.nan],
    'age': [2, 4, 6, 11],
    'city': ['pindi', 'karachi', np.nan, 'lahore']
}
pf = pd.DataFrame(data)
print(pf)

# One-hot encoding
print(pd.get_dummies(pf, columns=['name']))

# Marks DataFrame
marks = [1, 33, 88, 44, 2, 7, 8, 0]
pf = pd.DataFrame(marks, columns=['Marks'])
print(pf)
# Define bins and labels
bins = [0, 30, 60, 77, 100]
labels = ['F', 'C', 'A', 'A+']

# Cut into grades
print('\0')
pf['Grade'] = pd.cut(pf['Marks'], bins=bins, labels=labels)
print(pf)
print('\0')

pf.index={'s1','s2','s3','s4','s5','s6','s7','s8'}
print(pf)

pf['Marks']=pf['Marks'].astype(str)
print(pf.dtypes) 

print(pf['Grade'].str.split('F'))

print(pf['Grade'].str.replace('A','l'))
 
print(pf['Grade'].str.contains('F'))

print(pd.unique(pf['Grade']))

print(pf['Grade'].value_counts())

rng=np.random.default_rng()
random_ages=rng.integers(20,50,size=10)
print(random_ages)

pf=pd.DataFrame({'random_aGes':random_ages})

pf['randomAges']=pd.qcut(pf['random_aGes'],q=3,labels=['first','second','third'])
print(pf)

print("\0",rng.standard_normal(5))

print(pf['randomAges'].cat.add_categories(['Scientist']))

print(pf['randomAges'].cat.as_ordered())
print(pf['randomAges'].cat.ordered)

print(pf['randomAges'].cat.remove_categories(['first']))

print(pf['randomAges'].cat.remove_unused_categories())

print(pf['randomAges'].cat.rename_categories(['a','b','c']))

'''

'''
import pandas as pd
import numpy as np

data=pd.Series(np.random.uniform(size=8),index=[['x','x','x','y','y','z','z','w'],[1,2,3,4,2,3,2,5]])
print(data)

print(data.reorder_levels([1,0]).sort_index())

print(data["y"])

print(data.xs(2,level=1))    #seltecting values whith 2 in the index level 1

df=data.unstack()
print("\n",df)

df.index.names=["name_year"]
print(df)

print(df.index.nlevels)

arrays=[[1,1,2,2],['red','blue','pink','red']]
index=pd.MultiIndex.from_arrays(arrays,names=['number','color'])
frame=pd.DataFrame(np.random.randn(4,2),index=index,columns=['a','b'])
print(frame)

print(frame.groupby(level="color").sum())

print(frame.reset_index().set_index(["color",'number']))

'''

'''

#database

import sqlite3
import pandas as pd

def create(conn):
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute(
        # CREATE TABLE IF NOT EXISTS users (
        #     userid INTEGER PRIMARY KEY,
        #     name TEXT,
        #     age INTEGER
        #)
    )

    cursor.execute(
        # CREATE TABLE IF NOT EXISTS Orders (
        #     orderid INTEGER PRIMARY KEY AUTOINCREMENT,
        #     userid INTEGER,
        #     product TEXT,
        #     amount INTEGER,
        #     FOREIGN KEY(userid) REFERENCES users(userid)
        # )
    )

    # Insert into users if empty
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    if user_count == 0:
        cursor.executemany(
           #INSERT INTO users (name, age) VALUES (?, ?)
        , [
            ('Ali', 30),
            ('Boby', 24),
            ('Sheri', 10)
        ])
    
    # Insert into Orders if empty
    cursor.execute('SELECT COUNT(*) FROM Orders')
    order_count = cursor.fetchone()[0]
    if order_count == 0:
        cursor.executemany(
            #INSERT INTO Orders (userid, product, amount) VALUES (?, ?, ?)
        , [
            (1, 'laptop', 1222),
            (2, 'phone', 600)
        ])
    
    conn.commit()


def main():
    conn = sqlite3.connect("testing.db")  
    create(conn)
    
    # Show orders
    df = pd.read_sql_query('SELECT * FROM Orders', conn)
    print(df)
    df1 = pd.read_sql_query('SELECT * FROM users', conn)
    print(df1)
 
 
    print(pd.merge(df,df1,how='left',on='userid'))

    print(pd.concat([df,df1],axis=0,ignore_index=True))

    conn.close()

main()

'''
 
'''
import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(0,10,50)
y1=3*(np.sin(x1))
x2=np.linspace(-10,10,50)
y2=x2*x2

fig=plt.figure('GRAPH')

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

ax1.plot(x1,y1,color='blue',marker='o',linestyle='-',label='nothing')
ax1.set_title('Sine Wave')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperatur')
ax1.legend()
ax1.grid(True)

ax2.plot(x2,y2,color='red',marker='x',linestyle='-',label='hello')
ax2.set_title('Paraboa')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.legend()
ax2.grid(True)

ax1.set_xticks(np.arange(0,11,1))
ax1.set_yticks(np.arange(-3,3.5,0.5))

ax2.set_xticks(np.arange(-10,11,2))
ax2.set_yticks(np.arange(0,100,10))

plt.savefig('plot_example.png')

plt.show()

'''


'''
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

data=pd.DataFrame({
    'x':[1,2,3,4,5],
    'y':[2,3,4,5,6],
    'z':['a','b','c','d','e']
})


# plt.figure(figsize=(8,5))
# plt.scatter(data['x'],data['y'],color='blue')
# plt.title('matplot')
# plt.xlabel('X')
# plt.ylabel("Y")
# plt.show()

# plt.figure(figsize=(8,5))
# sns.scatterplot(x='x',y='y',data=data)
# plt.title('seaborn matplot')
# plt.show()


# plt.figure(figsize=(8,5))
# plt.plot(data['x'],data['y'],marker='o',linestyle='-',color='red')
# plt.title('matplot')
# plt.xlabel('X')
# plt.ylabel("Y")
# plt.show()


# plt.figure(figsize=(8,5))
# sns.lineplot(x='x',y='y',data=data)
# plt.title('seaborn matplot')
# plt.show()

# plt.figure(figsize=(8,5))
# plt.bar(data['x'],data['y'],color='purple')
# plt.title('matplot')
# plt.xlabel('X')
# plt.ylabel("Y")
# plt.show()

# plt.figure(figsize=(8,5))
# sns.barplot(x='x',y='y',data=data)
# plt.title('seaborn matplot')
# plt.show()

# plt.figure(figsize=(5,5))
# bar_width=0.35
# index=range(len(data))
# plt.bar(index,data['x'],bar_width,label='x',color='cyan')
# plt.bar([i+bar_width for i in index],data['y'],bar_width,label='y',color='orange')
# plt.xlabel('X')
# plt.ylabel("Y")
# plt.title('nothing')
# plt.xticks([i+bar_width/2 for i in index],data['z'])
# plt.show()


# plt.figure(figsize=(8,5))
# sns.boxplot(data['x'])
# plt.title(' matplot')
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(data['x'],bins=4,color='green')
# plt.title(' matplot')
# plt.show()

# plt.figure(figsize=(8,5))
# sns.histplot(data['x'],bins=4,kde=True,color='green')
# plt.title(' matplot')
# plt.show()

'''

'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

np.random.seed(42)

dates=pd.date_range(start='2024-5-1',periods=100,freq='D')
sales=np.random.randint(100,500,size=len(dates))
customers=np.random.randint(20,100,size=len(dates))
traffic=np.random.randint(200,800,size=len(dates))
ad_spend=np.random.randint(50,300,size=len(dates))

data=pd.DataFrame({
    'Date':dates,
    'Sales':sales,
    'Customers':customers,
    'Traffic':traffic,
    'Ad_spend':ad_spend
})

data.set_index('Date',inplace=True)

window_size=10
data['MA_Sales']=data['Sales'].rolling(window=window_size).mean()
data['EWMA_Sales']=data['Sales'].ewm(span=window_size).mean()
data['MA_Customers']=data['Customers'].rolling(window=window_size).mean()
data['EWMA_Customers']=data['Customers'].ewm(span=window_size).mean()
data['MA_Traffic']=data['Traffic'].rolling(window=window_size).mean()
data['EWMA_Traffic']=data['Traffic'].ewm(span=window_size).mean()


print(data.head(20))

input()

fig,ax=plt.subplots(figsize=(10,6))

def update(num):
    ax.clear()
    ax.set_title(f"Time series data and moving average (Day {num+1})")
    ax.plot(data.index[:num+1],data['Sales'][:num+1],label='Sales',color='blue',alpha=0.5)
    ax.plot(data.index[:num+1],data['MA_Sales'][:num+1],label='MA Sales',color='blue',linestyle='--')
    ax.plot(data.index[:num+1],data['EWMA_Sales'][:num+1],label='EWMA Sales',color='blue',linestyle=':')

    ax.plot(data.index[:num+1],data['Customers'][:num+1],label='Customer',color='green',alpha=0.5)
    ax.plot(data.index[:num+1],data['MA_Customers'][:num+1],label='MA Customers',color='green',linestyle='--')
    ax.plot(data.index[:num+1],data['EWMA_Customers'][:num+1],label='EWMA Customers',color='green',linestyle=':')

    
    ax.set_xlabel('Date')
    ax.set_ylabel('Values')
    ax.legend(loc='upper left')
    ax.grid(True)
    
ani = animation.FuncAnimation(fig, update, frames=len(data), repeat=False)
plt.tight_layout()
plt.show()

   '''


'''
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_,to_,subject,body,smtp_server,smtp_port,login,password):
    msg=MIMEMultipart()
    msg['From']=from_
    msg['To']=to_
    msg['Subject']=subject

    msg.attach(MIMEText(body,'plain'))

    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()

        server.login(login,'rdqf gigg loer adfk')

        server.send_message(msg)
        print("successful")

    except Exception as e:
        print(f'fail  {e}')
    
    finally:
        server.quit()

from_="faizan@gmail.com"
to_="naim@sparrow.com"
subject='Testing'
body="so jao araam se or kuch bhi na kro aj"
smtp_server="smtp.gamil.com"
smtp_port=587
login="hello@nassli.com"
password=os.getenv('EMAIL_PASS')
send_email(from_,to_,subject,body,smtp_server,smtp_port,login,password)

'''

'''
import os
import subprocess
import sys

def install_pip():
    try:
        import pip
        print("pip already installed")
    except ImportError:
        print("pip not installed")
        subprocess.check_call([sys.executable,'-m','ensurepip'])
        print("pip installed")

def install_requests():
    try:
        import requests
        print('requests is already installed') 
    except ImportError:
        print("request not found,installing")
        subprocess.check_call([sys.executable,"-m",'pip','install','requests'])
        print("installed successfully")       

def get_google_location(api_key):
    import requests
    url=f''
    payload={
        "considerId":True
    }
    try:
        response=requests.post(url,json=payload)
        response.raise_for_status()
        data=response.json()

        print("Response Json: ",data)
        location=data.get('location',None)
        if location:
            latitude=location.get('lat',None)
            longitude=location.get('lng',None)
            return latitude,longitude
        else:
            return None
    except requests.exceptions.HTTPError as e:
        print(f'HTTP: {e}')
        print('response Text:',response.txt)
        return None
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")

        print("error ")
        return None

def main():
    install_pip()
    import pip
    print('pip version is ',pip.__version__)
    install_requests()
    import requests
    print("requests is installed",requests.__version__)


    api_key=""
    location=get_google_location(api_key)
    if location:
        latitude,lingitude=location
        print(f"{latitude}, {longitude}")
    else
        print("location not")


'''

'''
def main():
    import os
    import subprocess
    import sys

    # Fix 1: Use subprocess.run instead of check_call, and pass '-m' correctly
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'pymeteosource'],
                            capture_output=True, text=True)

    if result.returncode == 0:
        print("installation successful")
    else:
        print("installation failed")
        print(result.stderr)
        return  # Exit if installation failed

    # Fix 2: Import after successful installation
    try:
        from pymeteosource.api import Meteosource
        from pymeteosource.types import tiers, sections, langs, units
    except ImportError as e:
        print("Import failed:", e)
        return

    api_key = 'xtb8kygg5gpjzmsw051i0ptbpkq42b46h227sheq'
    my_tier = tiers.FREE

    meteosource = Meteosource(api_key, my_tier)

    # Fix 3: Make the request with exception handling
    try:
        forecast = meteosource.get_point_forecast(
            lat=32.1476,
            lon=74.1914,
            place_id=None,
            sections=[sections.CURRENT, sections.HOURLY],
            tz='UTC',
            lang=langs.ENGLISH,
            units=units.METRIC
        )
    except Exception as e:
        print("Error fetching forecast:", e)
        return

    print("\nFaizan Naroo1")
    print(forecast)

    print("\nFaizan Naroo2")
    print(forecast.current)

    print("\nFaizan Naroo3")
    print(forecast.hourly[0])

    print("\nFaizan Naroo4")
    print("hourly temperature in degree C is: ", forecast.hourly)
    
    # Fix 4: Add safety check for 24th hour access
    if len(forecast.hourly) > 23:
        print("hourly weather is: ", forecast.hourly[23]['weather'])
    else:
        print("Less than 24 hourly entries available")

main()

'''



'''

import requests
import csv
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

cryptocurrencies = ['bitcoin', 'ethereum', 'dogecoin']

url = 'https://api.coingecko.com/api/v3/simple/price'

params = {
    'ids': ','.join(cryptocurrencies),
    'vs_currencies': 'usd'
}

def fetch_crypto_prices():
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Error", str(e))  # Fix: use str(e), not "e"
        return {}

def save_to_csv(data):
    # Fix: Correct strftime call and add file extension
    filename = f"crypto_prices_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Cryptocurrency', 'Price(USD)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for crypto, price in data.items():
            writer.writerow({"Cryptocurrency": crypto, "Price(USD)": price['usd']})  # Fix key name and structure

def update_gui(data):
    for crypto, price in data.items():
        # Fix: correct dictionary access
        tree.insert("", "end", values=(crypto.capitalize(), price['usd']))

def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    data = fetch_crypto_prices()
    if data:
        update_gui(data)
        save_to_csv(data)

# GUI setup
root = tk.Tk()
root.title("Cryptocurrency Prices")

# Fix: Correct column names
tree = ttk.Treeview(root, columns=("Cryptocurrency", "Price(USD)"), show='headings')
tree.heading("Cryptocurrency", text="Cryptocurrency")
tree.heading("Price(USD)", text="Price (USD)")
tree.pack(fill=tk.BOTH, expand=True)

# Fix: Correct button callback and parameter
refresh_button = tk.Button(root, text="Refresh Data", command=refresh_data)
refresh_button.pack(pady=10)

# Fix: Call the function (add parentheses)
initial_data = fetch_crypto_prices()
if initial_data:
    update_gui(initial_data)
    save_to_csv(initial_data)

root.mainloop()

'''


'''
############## webscraping
import os
import subprocess
import sys

# Try to import or install required libraries
try:
    import requests
except ImportError:
    os.system("python -m pip install requests")
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system("python -m pip install beautifulsoup4")
    from bs4 import BeautifulSoup

try:
    import lxml
except ImportError:
    os.system("python -m pip install lxml")
    import lxml

# Now perform the scraping
import requests
from lxml import html

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    tree = html.fromstring(response.content)

    # Fix: Quote and author extraction
    quotes = tree.xpath('//div[@class="quote"]/span[@class="text"]/text()')
    authors = tree.xpath('//div[@class="quote"]/span/small[@class="author"]/text()')

    for quote, author in zip(quotes, authors):
        print(f'"{quote}" — {author}')
else:
    print("Failed to retrieve the page")

    '''


'''
########  scan and generte qrcode
import os
import subprocess
import sys

try:
    import cv2
except ImportError:
    os.system("python -m pip install opencv-python")

try:
    import qrcode
except ImportError:
    os.system("python -m pip install qrcode")

try:
    from PIL import Image, ImageTk
except ImportError:
    os.system("python -m pip install pillow")

import tkinter as tk
from tkinter import filedialog, messagebox


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator and Scanner")
        self.root.geometry("600x500")

        self.label1 = tk.Label(root, text="Enter data for QR code")
        self.label1.pack(pady=10)

        self.data_entry = tk.Entry(root, width=40)
        self.data_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save", command=self.save_qr, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=10)

        self.scan_button = tk.Button(root, text="Scan", command=self.scan_qr)
        self.scan_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.qr_code_image = None

    def generate_qr(self):
        data = self.data_entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)

            self.qr_code_image = qr.make_image(fill_color="black", back_color="white")
            qr_img = ImageTk.PhotoImage(self.qr_code_image)

            self.qr_label.config(image=qr_img)
            self.qr_label.image = qr_img
            self.save_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Input Error", "Please enter data.")

    def save_qr(self):
        if self.qr_code_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png")])
            if file_path:
                self.qr_code_image.save(file_path)
        else:
            messagebox.showwarning("Save Error", "No QR code to save.")

    def scan_qr(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file_path:
            image = cv2.imread(file_path)
            qr_detector = cv2.QRCodeDetector()
            data, bbox, _ = qr_detector.detectAndDecode(image)
            if bbox is not None and data:
                self.result_label.config(text=f"Scanned Data: {data}")
            else:
                self.result_label.config(text="No QR code found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()

    '''