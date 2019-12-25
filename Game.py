from tkinter import *
from tkinter import messagebox
a=0
l=[["Question 1. The average of first 50 natural numbers is (5 PTS) ", ["25.30", "25.5", "25", "12"], 2, 5],
       ["Question 2. The number of 3-digit numbers divisible by 6, is (5 PTS)",["149", "166", "150", "151"],3,5],
       ["Question 3. What is 1004 divided by 4?(3 PTS)",["52","20","2010","251"],4,3],
       ["Question 4. A clock strikes once at 1 o’clock, twice at 2 o’clock, thrice at \n3 o’clock and so on. How many times will it strike \nin 24 hours?(5 PTS)",["136","156","78","196"],2,5],
       ["Question 5. 106 × 106 – 94 × 94 =?(7 PTS) ",["2004","2400","1904","1906"],2,7],
       ["Question 6. Which of the following numbers gives 240 when added to its \n own square?(3 PTS)",["15","16","17","20"],1,3],
       ["Question 7. Evaluation of 8^3 × 8^2 × 8^(-5) is.(3 PTS)",["1","0","-1","2"],1,3],
       ["Question 7. A number is divisible by 3 if the sum of its digits is divisible \n by?(3 PTS)",["1","2","3","5"],2,3],
       ["Question 8. Subtract 457 from 832(5 PTS)",["375","57","379","380"],1,5],
       ["Question 9. 2% of 21 is equal to ?(5 PTS)",["0.42","0.24","0.69","0.14"],1,5],
       ["Question 10.  A car covers a distance of 200km in 2 hours 40 minutes, \nwhereas a jeep covers the same distance in 2 hours.\n What is the ratio of their speed?(7 PTS)",["3:4","4:3","4:5","5:4"],1,7]]

def main1():
    global root1
    global Username
    root1=Tk()
    root1.resizable(0,0)
    Username = IntVar()
    root1.geometry("400x220")
    root1.config(bg="#220047")
    root1.title("Welcome")
    label_1 = Label(root1,text="Maths Quiz",font=("roboto",30),bg="#220047",fg="#CE9141")
    label_1.place(x=100,y=10)
    label_2 = Label(root1,text="Enter the number of teams:",font=("roboto",19),bg="#220047",fg="#CE9141")
    label_2.place(x=10,y=90)
    entry1= Entry(root1,textvar=Username,width=5)
    entry1.place(x=335,y=100)
    button1 = Button(root1,text="Play",font=("roboto",20),bg="#CE9141",fg="#220047",activeforeground="#CE9141",activebackground="#220047")
    button1.bind("<Button-1>",startgame)
    button1.place(x=170,y=150)
    root1.mainloop()
def startgame(event):
    global root2
    global xdict
    xdict=teams()
    print(xdict)
    root1.destroy()
    root2 = Tk()
    root2.resizable(0, 0)
    root2.geometry("600x300")
    gamegui()
def gamegui():
    global a
    if a>10:
        print(xdict)
        dt = "Result: \n"
        for i in xdict:
            tmp2=str(xdict[i])
            tmp3="Team "+i+" points= "+tmp2
            dt += (tmp3+"\n")
        messagebox.showinfo("Game ended!!!",dt)
        root2.destroy()
        return None

    global answer
    global label1
    global label2
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global entry2
    global button2
    global tmpa
    global tmpp
    root2.config(bg="#220047")
    noq = l[a]
    tmpq = noq[0]
    tmpo = noq[1]
    tmpa = noq[2]
    tmpp = noq[3]
    answer=StringVar()
    label1 = Label(root2, text="Maths Quiz", font=("roboto", 30), bg="#220047", fg="#CE9141")
    label1.place(x=200, y=10)
    label2 = Label(root2, text=tmpq, font=("roboto", 12), bg="#220047", fg="#CE9141")
    label2.place(x=40, y=80)
    label3 = Label(root2, text="1) "+tmpo[0], font=("roboto", 15), bg="#220047", fg="#CE9141")
    label3.place(x=70, y=140)
    label4 = Label(root2, text="2) "+tmpo[1], font=("roboto", 15), bg="#220047", fg="#CE9141")
    label4.place(x=170, y=140)
    label5 = Label(root2, text="3) "+tmpo[2], font=("roboto", 15), bg="#220047", fg="#CE9141")
    label5.place(x=270, y=140)
    label6 = Label(root2, text="4) "+tmpo[3], font=("roboto", 15), bg="#220047", fg="#CE9141")
    label6.place(x=370, y=140)
    label7=Label(root2,text="Enter team name and answerhere(for eg:A1):", font=("roboto", 13), bg="#220047", fg="#CE9141")
    label7.place(x=40,y=200)
    entry2 = Entry(root2, textvar=answer, width=5)
    entry2.place(x=425, y=204)
    button2= Button(root2, text="Submit", font=("roboto", 20), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                    activebackground="#220047")
    button2.bind("<Button-1>", check)
    button2.place(x=240, y=240)
    root2.mainloop()

def teams():
    count=Username.get()
    print(count)
    tdict={}
    for i in range(65,65+count):
        tdict[chr(i)]=0
    return tdict


def check(event):
    global a
    l=answer.get()
    label1.place_forget()
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    label6.place_forget()
    label7.place_forget()
    entry2.place_forget()
    button2.place_forget()
    first=l[0]
    second=int(l[1])
    if second==tmpa:
        tmp1=xdict[first]
        tmp1+=tmpp
        xdict[first]=tmp1
    a+=1
    gamegui()
main1()