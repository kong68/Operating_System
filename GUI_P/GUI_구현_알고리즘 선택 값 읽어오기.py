import tkinter
import tkinter.ttk
from tkinter import *



import heapq








root=tkinter.Tk()
root.title("운영체제 프로세스 스케줄링 7조")
root.geometry("1290x950+50+30")
root.resizable(False, False)
root.configure(background = "white")

canvas = Canvas(root, width = 300, height =150, bg="white")  #bd = 2
canvas.pack(fill="both",expand=True)


############################# -이미지- #################################

photo=PhotoImage(file="C:/Users/user/Desktop/GUI 구현/school_logo.png") #PhotoImage를 통한 이미지 지정
label=Label(root, image=photo,background = "white") #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
label.place(x=900,y= 14)



############################# -라인- #################################

canvas.create_line(20, 3, 20, 917,fill="black", width = 3)
canvas.create_line(20, 3, 1272, 3,fill="black", width = 3)

canvas.create_line(22, 375, 1272, 375,fill="gray", width = 1.5)
canvas.create_line(390, 5, 390, 375,fill="gray", width = 1.5)

canvas.create_line(20, 917, 1272, 917,fill="black", width = 3)
canvas.create_line(1272, 3, 1272, 917,fill="black", width = 3)

canvas.create_line(22, 540, 1272, 540,fill="gray", width = 1.5)

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

Pcore = Label(root, text="P코어 수",background = "white")
Pcore.place(x=50,y=190)

Ecore = Label(root, text="E코어 수",background = "white")
Ecore.place(x=50,y=210)

excution_speed = Label(root, text="실행 속도       1000ms",background = "white")
excution_speed.place(x=50,y=230)

Ready_Queue = Label(root, text="[ Ready Queue ]",background = "white")
Ready_Queue.place(x=50,y=380)


count = -1 #버튼 누를 때 마다 증가
Time_table_list = [] #표에 들어갈 내용 튜플 형태로 저장



def add_click():
    global count
    global Time_table_list
    count += 1
    print(count)


    name = Entry.get(process_name_)  # 문자
    AT = eval(Entry.get(Arrival_Time_)) # 숫자
    BT = eval(Entry.get(Burst_Time_)) # 숫자
    Time_table_list.append((name,AT,BT))

    print(Time_table_list)

    # 표에 삽입될 데이터
    #treelist=[(name,AT, BT), ("P2","Boni", 90), ("P3","Boni", 90), ("P4","Dannel", 78), ("P5","Minho", 93)]

    # 표에 데이터 삽입
    # for i in range(len(treelist)):
    Time_table.insert('', 'end', text="", values=Time_table_list[count], iid=count)
    Proces_State.insert('', 'end', text="", values=Time_table_list[count], iid=count)


def remove():  # 맨뒤에 추가한 항목 삭제
    global count
    global Time_table_list
    Time_table.delete(count)
    Proces_State.delete(count)
    Time_table_list.pop(count)
    count = count - 1
    


method = ["FCFS", "RR", "SPN","SRTN", "HRRN","own algorithm"]
scheduling_method_ = ttk.Combobox(root, height = 6, values = method)
scheduling_method_.place(x=150,y=40)

RR_time_quantum_ = Entry(root, width=20, borderwidth = 2)
RR_time_quantum_.place(x=150,y=70)

process_name_ = Entry(root, width=20, borderwidth = 2)
process_name_.place(x=150,y=100)
Arrival_Time_ = Entry(root, width=20, borderwidth = 2)
Arrival_Time_.place(x=150,y=120)
Burst_Time_ = Entry(root, width=20, borderwidth = 2)
Burst_Time_.place(x=150,y=140)
processor_num_ = Entry(root, width=20, borderwidth = 2)
processor_num_.place(x=150,y=170)
Pcore_ = Entry(root, width=20, borderwidth = 2)
Pcore_.place(x=150,y=190)
Ecore_ = Entry(root, width=20, borderwidth = 2)
Ecore_.place(x=150,y=210)

processer_num__ = 0
Pcore_Num_ = 0
Ecore_NUm_ = 0

def setting():
    global processer_num__ 
    global Pcore_Num_
    global Ecore_NUm_

    
    processer_num__ = eval(Entry.get(processor_num_)) # 숫자
    Pcore_Num_ = eval(Entry.get(Pcore_)) # 숫자
    Ecore_NUm_ = eval(Entry.get(Ecore_)) # 숫자
    print(scheduling_method_.get())
    
    
    print(processer_num__) 
    print(Pcore_Num_)
    print(Ecore_NUm_)

Add_Button = Button(root, text="Add", command = add_click, fg ="blue")
Add_Button.place(x=100, y=270, width=70)

Add_Button = Button(root, text="Reset", command = remove, fg ="red")
Add_Button.place(x=200, y=270, width=70)

Add_Button = Button(root, text="Start", command = setting)
Add_Button.place(x=100, y=320, width=170)



############################# -표 1- #################################

lbl = tkinter.Label(root, text="[ Time table ]",background = "white")
lbl.place(x=605,y=10)


# 표 생성. colums 이름, displaycolum 보여지는 순서
Time_table=tkinter.ttk.Treeview(root, columns=["Process Name", "Arrival Time","Burst Time"], displaycolumns=["Process Name", "Arrival Time","Burst Time"], height=15)
Time_table.place(x=420,y=40)

#이름, 넓이, 정렬 위치
Time_table.column("Process Name", width=150, anchor="center")
Time_table.heading("Process Name", text="Process Name", anchor="center")

Time_table.column("Arrival Time", width=150, anchor="center")
Time_table.heading("Arrival Time", text="Arrival Time(AT)", anchor="center")

Time_table.column("Burst Time", width=150, anchor="center")
Time_table.heading("Burst Time", text="Burst Time(BT)", anchor="center")

Time_table["show"] = "headings"

# 표에 삽입될 데이터
#treelist=[("P1","Tom", 80), ("P2","Bani", 71), ("P3","Boni", 90), ("P4","Dannel", 78), ("P5","Minho", 93)]

# 표에 데이터 삽입
#for i in range(len(treelist)):
#    treeview.insert('', 'end', text="", values=treelist[i], iid=i)



############################# -표 2- #################################

lbl = tkinter.Label(root, text="[ Proces State ]",background = "white")
lbl.place(x=380,y=550)


# 표 생성. colums 이름, displaycolum 보여지는 순서
Proces_State=tkinter.ttk.Treeview(root, columns=["Process Name", "Arrival Time","Burst Time","Wating Time","Turnaround Time","Normalized TT"], displaycolumns=["Process Name", "Arrival Time","Burst Time","Wating Time","Turnaround Time","Normalized TT"], height=15)
Proces_State.place(x=30,y=580)

#이름, 넓이, 정렬 위치
Proces_State.column("Process Name", width=120, anchor="center")
Proces_State.heading("Process Name", text="Process Name", anchor="center")

Proces_State.column("Arrival Time", width=120, anchor="center")
Proces_State.heading("Arrival Time", text="Arrival Time(AT)", anchor="center")

Proces_State.column("Burst Time", width=120, anchor="center")
Proces_State.heading("Burst Time", text="Burst Time(BT)", anchor="center")

Proces_State.column("Wating Time", width=120, anchor="center")
Proces_State.heading("Wating Time", text="Wating Time(WT)", anchor="center")

Proces_State.column("Turnaround Time", width=150, anchor="center")
Proces_State.heading("Turnaround Time", text="Turnaround Time(TT)", anchor="center")

Proces_State.column("Normalized TT", width=150, anchor="center")
Proces_State.heading("Normalized TT", text="Normalized TT(NTT)", anchor="center")

Proces_State["show"] = "headings"


# WT, TT, NTT 넣기 위한 리스트
Proces_State_list = []

# 지정해서 넣기 예시
#Proces_State.insert('', index = 0, iid = 0, text="", values = Proces_State_list[0])




############################# -표 3- #################################

lbl = tkinter.Label(root, text="[ Power Consumption ]",background = "white")
lbl.place(x=1000,y=550)


# 표 생성. colums 이름, displaycolum 보여지는 순서
Power_Consumption_table=tkinter.ttk.Treeview(root, columns=["Core", "Power Consumption","Total Power Consumption"], displaycolumns=["Core", "Power Consumption","Total Power Consumption"])
Power_Consumption_table.place(x=850,y=580)

#이름, 넓이, 정렬 위치
Power_Consumption_table.column("Core", width=80, anchor="center")
Power_Consumption_table.heading("Core", text="Core", anchor="center")

Power_Consumption_table.column("Power Consumption", width=150, anchor="center")
Power_Consumption_table.heading("Power Consumption", text="Power Consumption", anchor="center")

Power_Consumption_table.column("Total Power Consumption", width=180, anchor="center")
Power_Consumption_table.heading("Total Power Consumption", text="Total Power Consumption", anchor="center")

Power_Consumption_table["show"] = "headings"


############################# -레디큐- #################################

ttt = [['P1','P2','P3'],['P4'],['P1','P1','P1','P1']]

#for i in range(0,len(ttt)):
#    Ready_Queue = Label(root, text=ttt[i], background = "white", font = ("",30))
#    Ready_Queue.place(x=50,y=430)

# 레디큐 출력 ex
Ready_Queue = Label(root, text=ttt[0], background = "white", font = ("",30))
Ready_Queue.place(x=50,y=430)
Ready_Queue.destroy()  #이전 출력 내역 삭제
Ready_Queue = Label(root, text=ttt[1], background = "white", font = ("",30))
Ready_Queue.place(x=50,y=430)


# GUI 실행
root.mainloop()