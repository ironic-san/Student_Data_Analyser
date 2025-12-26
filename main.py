import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
#data cleaning
df=pd.read_csv("student_data.csv")
m,n=df.shape
c=0
for i in range(n):
    if df.iloc[:,i].isnull().any():
        count=df.iloc[:,i].isnull().sum()
        print(count,"Null Values Found in Column",i)
        c+=count
print("Total null values found:",c)
df.fillna(df.mean(numeric_only=True).round(), inplace=True)
print("Filled null Values with corresponding means")
ma=df["Math"].mean()
pa=df["Physics"].mean()
ca=df["CS"].mean()
df["TotalMarks"]=df["Math"]+df["CS"]+df["Physics"]
print("_________CLEAN DATAFRAME__________")
print(df)
#lineplot
plt.figure()
plt.plot(df["Roll"],df["TotalMarks"],marker=".",markersize=20,mfc="#e307f2",mec="lightgray",linestyle="solid",linewidth=5,color="#07f217")
plt.title("Roll No Vs Total Marks",fontsize=25,fontfamily="Times New Roman",color="#1d0af0")
plt.xlabel("Roll no",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
plt.ylabel("Total Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
plt.xticks(range(0,41,5))
plt.tick_params(axis="both",color="#f00a38")
plt.grid()
#barchart
plt.figure()
x=np.array(["Math","CS","Physics"])
y=np.array([ma,pa,ca])
plt.bar(x,y,color='#f00a38')
plt.yticks(range(0,100,5))
plt.title("Average Marks",fontsize=25,fontfamily="Times New Roman",color="#1d0af0")
plt.xlabel("Subject",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
plt.ylabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
#scatterplots
figure,axes=plt.subplots(2,2)
axes[0,0].scatter(df["Attendance"],df["Math"],color="#08fc49",alpha=0.5,s=20,label="Math")
axes[0,1].scatter(df["Attendance"],df["Physics"],color="#fc08f8",alpha=0.5,s=20,label="Physics")
axes[1,0].scatter(df["Attendance"],df["CS"],color="#fcfc08",alpha=0.5,s=20,label="CS")
axes[1,1].scatter(df["Attendance"],df["TotalMarks"],color="#00fcfc",alpha=0.5,s=20,label="TotalMarks")
axes[0,0].set_xticks(range(50,100,5))
axes[0,0].set_yticks(range(50,100,5))
axes[0,0].set_xlabel("Attendance",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[0,0].set_ylabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[0,0].legend()
axes[0,1].set_xticks(range(50,100,5))
axes[0,1].set_yticks(range(50,100,5))
axes[0,1].set_xlabel("Attendance",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[0,1].set_ylabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[0,1].legend()
axes[1,0].set_xticks(range(50,100,5))
axes[1,0].set_yticks(range(50,100,5))
axes[1,0].set_xlabel("Attendance",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[1,0].set_ylabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[1,0].legend()
axes[1,1].set_xticks(range(50,100,5))
axes[1,1].set_yticks(range(150,300,10))
axes[1,1].set_xlabel("Attendance",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[1,1].set_ylabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
axes[1,1].legend()
figure.suptitle("Attendance vs Marks",fontsize=25,fontfamily="Times New Roman",color="#1d0af0")
#histogram
plt.figure()
plt.hist(df["TotalMarks"],bins=10,color="#1408fc",edgecolor="Black")
plt.title("Marks Distribution",fontsize=25,fontfamily="Times New Roman",color="#1d0af0")
plt.xlabel("Marks",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
plt.ylabel("Students",fontsize=20,fontfamily="Times New Roman",color="#1d0af0")
plt.xticks(range(150,300,10))

plt.show()
