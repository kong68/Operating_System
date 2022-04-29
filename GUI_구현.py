import tkinter
import tkinter.ttk
from tkinter import *


root=tkinter.Tk()
root.title("운영체제 프로세서 스케줄링 7조")
root.geometry("1200x900+100+100")
root.configure(background = "white")

canvas = Canvas(root, width = 300, height =150, bg="white", bd=2)
canvas.pack(fill="both",expand=True)

############################# -라인- #################################

canvas.create_line(0, 360, 400, 360,fill="black")
canvas.create_line(400, 0, 400, 360,fill="black")

############################# -버튼- #################################


scheduling_method = Label(root, text="스케줄링 기법",background = "white")
scheduling_method.place(x=50,y=40)

RR_time_quantum = Label(root, text="RR 타임퀀텀",background = "white")
RR_time_quantum.place(x=50,y=70)

process_name_print = Label(root, text="프로세스 이름",background = "white")
process_name_print.place(x=50,y=100)
Arrival_Time = Label(root, text="도착시간 (AT)",background = "white")
Arrival_Time.place(x=50,y=120)
Burst_Time = Label(root, text="실행시간 (BT)",background = "white")
Burst_Time.place(x=50,y=140)


processor_num = Label(root, text="프로세서 수",background = "white")
processor_num.place(x=50,y=170)

execution_speed = Label(root, text="실행 속도",background = "white")
execution_speed.place(x=50,y=190)

count = -1 #버튼 누를 때 마다 증가
treelist = [] #표에 들어갈 내용 튜플 형태로 저장

def click():
    global count
    global treelist
    count += 1
    print(count)


    name = Entry.get(process_name_)  #문자
    AT = eval(Entry.get(Arrival_Time_)) # 숫자
    BT = eval(Entry.get(Burst_Time_)) # 숫자
    treelist.append((name,AT,BT))

    print(treelist)

    # 표에 삽입될 데이터
    #treelist=[(name,AT, BT), ("P2","Boni", 90), ("P3","Boni", 90), ("P4","Dannel", 78), ("P5","Minho", 93)]

    # 표에 데이터 삽입
   # for i in range(len(treelist)):
    treeview.insert('', 'end', text="", values=treelist[count], iid=count)


def remove():  # 맨뒤에 추가한 항목 삭제
    global count
    global treelist
    treeview.delete(count)
    treelist.pop(count)
    count = count - 1
    


method = ["FCFS", "RR", "SPN","SRTN", "HRRN","own algorithm"]
scheduling_method_ = ttk.Combobox(root, height = 4, values = method)
scheduling_method_.place(x=150,y=40)

RR_time_quantum_ = Entry(root, width=20)
RR_time_quantum_.place(x=150,y=70)

process_name_ = Entry(root, width=20)
process_name_.place(x=150,y=100)
Arrival_Time_ = Entry(root, width=20)
Arrival_Time_.place(x=150,y=120)
Burst_Time_ = Entry(root, width=20)
Burst_Time_.place(x=150,y=140)
processor_num_ = Entry(root, width=20)
processor_num_.place(x=150,y=170)
execution_speed_ = Entry(root, width=20)
execution_speed_.place(x=150,y=190)




Add_Button = Button(root, text="Add", command = click)
Add_Button.place(x=100, y=230, width=70)

Add_Button = Button(root, text="Reset", command = remove)
Add_Button.place(x=200, y=230, width=70)

Add_Button = Button(root, text="Start")
Add_Button.place(x=105, y=280, width=140)


############################# -표 1- #################################

lbl = tkinter.Label(root, text="[ Time table ]",background = "white")
lbl.place(x=685,y=30)


# ﻿표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
treeview=tkinter.ttk.Treeview(root, columns=["Process Name", "Arrival Time","Burst Time"], displaycolumns=["Process Name", "Arrival Time","Burst Time"])
treeview.place(x=500,y=60)

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("Process Name", width=150, anchor="center")
treeview.heading("Process Name", text="Process Name", anchor="center")

treeview.column("Arrival Time", width=150, anchor="center")
treeview.heading("Arrival Time", text="Arrival Time(AT)", anchor="center")

treeview.column("Burst Time", width=150, anchor="center")
treeview.heading("Burst Time", text="Burst Time(BT)", anchor="center")

treeview["show"] = "headings"

# 표에 삽입될 데이터
#treelist=[("P1","Tom", 80), ("P2","Bani", 71), ("P3","Boni", 90), ("P4","Dannel", 78), ("P5","Minho", 93)]

# 표에 데이터 삽입
#for i in range(len(treelist)):
#    treeview.insert('', 'end', text="", values=treelist[i], iid=i)



############################# -표 2- #################################

lbl = tkinter.Label(root, text="[ Proces State ]",background = "white")
lbl.place(x=685,y=500)


# ﻿표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
treeview2=tkinter.ttk.Treeview(root, columns=["Process Name", "Arrival Time","Burst Time"], displaycolumns=["Process Name", "Arrival Time","Burst Time"])
treeview2.place(x=500,y=530)

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview2.column("Process Name", width=150, anchor="center")
treeview2.heading("Process Name", text="Process Name", anchor="center")

treeview2.column("Arrival Time", width=150, anchor="center")
treeview2.heading("Arrival Time", text="Arrival Time(AT)", anchor="center")

treeview2.column("Burst Time", width=150, anchor="center")
treeview2.heading("Burst Time", text="Burst Time(BT)", anchor="center")

treeview2["show"] = "headings"
# 표에 삽입될 데이터
treelist2=[("P1","Tom", 80), ("P2","Bani", 71), ("P3","Boni", 90), ("P4","Dannel", 78), ("P5","Minho", 93)]

# 표에 데이터 삽입
for i in range(len(treelist2)):
    treeview2.insert('', 'end', text="", values=treelist2[i], iid=i)

# GUI 실행
root.mainloop()