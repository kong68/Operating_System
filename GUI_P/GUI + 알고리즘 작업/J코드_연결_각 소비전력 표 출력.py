
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

process_num = 0
processor_num = 0
p_core_num = 0
Ecore_Num_ = 0
time_quantum = 0
arrive_time = []
burst_time = []


def setting():
    global process_num
    global processor_num
    global p_core_num
    global Ecore_Num_
    global time_quantum
    global arrive_time
    global burst_time
    
    process_num = len(Time_table_list)
    processor_num = eval(Entry.get(processor_num_)) # 숫자
    p_core_num = eval(Entry.get(Pcore_)) # 숫자
    Ecore_Num_ = eval(Entry.get(Ecore_)) # 숫자
    time_quantum = eval(Entry.get(RR_time_quantum_)) # 숫자
    scheduling_method = scheduling_method_.get()
    for i in range(len(Time_table_list)):
        arrive_time.append(Time_table_list[i][1])
    for j in range(len(Time_table_list)):
        burst_time.append(Time_table_list[j][2])



    if scheduling_method == "RR":
        print("RR선택")
        # 스케줄링 객체 생성
        RR = Scheduling(process_num, processor_num, p_core_num, arrive_time, burst_time, time_quantum)
        # rr 스케줄링 실행.
        RR.Round_Robin()
        # 표에 데이터 삽입
        for i in range(len(RR.getPOWER())):
            Power_Consumption_table.insert('', 'end', text="", values=RR.getPOWER()[i], iid=i)

        # RR은 RoundRobin
        # 먼저 레디큐 호출법
        print(f"\nReadyQueue: {RR.getRQ()}")
        # WT 호출법
        print(f"\nWT: {RR.getWT()}")
        # BT 호출법
        print(f"\nBT: {RR.getBT()}")
        # TT 호출법
        print(f"\nTT: {RR.getTT()}")
        # NTT 호출법
        print(f"\nNTT: {RR.getNTT()}")
        # 각 코어당 전력 호출법
        print(f"\nPOWER: {RR.getPOWER()}")
        # 총 전력 호출법
        print(f"\nTOTAL POWER: {RR.getTOTALPOWER()}")
        # 스케줄링 종료시간 호출법
        print(f"\nTIME: {RR.getTIME()}")

    
  


Add_Button = Button(root, text="Add", command = add_click, fg ="blue")
Add_Button.place(x=100, y=270, width=70)

Add_Button = Button(root, text="Reset", command = remove, fg ="red")
Add_Button.place(x=200, y=270, width=70)

Add_Button = Button(root, text="Start", command = setting)
Add_Button.place(x=100, y=320, width=170)


##############################################################################



################################################################################





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

ttt = [['P1','P2','P3'],["P4"],['P1','P1','P1','P1']]

#for i in range(0,len(ttt)):
#    Ready_Queue = Label(root, text=ttt[i], background = "white", font = ("",30))
#    Ready_Queue.place(x=50,y=430)

# 레디큐 출력 ex
Ready_Queue = Label(root, text=ttt[0], background = "white", font = ("",30))
Ready_Queue.place(x=50,y=430)
Ready_Queue.destroy()  #이전 출력 내역 삭제
Ready_Queue = Label(root, text=ttt[1], background = "white", font = ("",30))
Ready_Queue.place(x=50,y=430)



    
################################# -알고리즘- ###########################################3    

    
class Process:
    def __init__(self, number, arrive_time, burst_time):
        self._number = number
        self.arrive_time = arrive_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.terminate_time = -1

    def __str__(self):
        TT = self.terminate_time - self.arrive_time
        return f"<process{self._number}>\nWT: {self.waiting_time}, TT: {TT}, NTT: {TT / self.burst_time:.1f}"


class Processor:
    def __init__(self, core="e"):
        self._core = core
        self.work = []
        self.power = 0
        self.time_quantum = None


# 각각 알고리즘 마다 처리해야하므로 각 알고리즘 클래스에 변수를 저장해야함
class Scheduling:
    def __init__(self, process_num, processor_num, p_core_num, arrive_time, burst_time, time_quantum=None):
        self.process_num = process_num
        self.processor_num = processor_num
        self.processors = {}
        self.processes = {}
        self.ready_q = []
        self.time = 0
        self.time_quantum = time_quantum
        self.power_consumption = 0
        self.readyqueue = []
        self.WT = []
        self.BT = []
        self.TT = []
        self.NTT = []
        self.POWER = []
        # 프로세서 객체 생성.

        for i in range(1, processor_num + 1):
            if p_core_num > 0:
                self.processors[i] = Processor("p")
                p_core_num -= 1

            else:
                self.processors[i] = Processor()

        # 프로세스 객체 생성.
        for i in range(process_num):
            self.processes[i + 1] = Process(i + 1, arrive_time[i], burst_time[i])

    # 도착시간이 가장 늦은 시간을 찾는 작업
    def _find_max_arrive_time(self):
        max_arr = -1
        for i in range(1, process_num + 1):
            max_arr = max(max_arr, self.processes[i].arrive_time)
        return max_arr

    # 모든 프로세서들을 살펴보아 하나의 프로세스라도 일하고 있다면 True를 리턴
    def _working(self):
        for i in range(1, self.processor_num + 1):
            if self.processors[i].work != []:
                return True
        return False

    # 작업수행이 가능한 프로세서, 즉 비어있는 프로세서를 찾는 작업
    def _find_empty_processor(self):
        for i in range(1, self.processor_num + 1):
            if not self.processors[i].work:
                return i

        return False

    def _calculate_waiting_time(self):
        for i in self.ready_q:
            tmp = i[1]
            self.processes[tmp].waiting_time += 1

    def _calculate_power_consumption(self):
        for i in range(1, self.processor_num + 1):
            self.power_consumption += self.processors[i].power

    # 프로세가 일하는 함수
    def _processor_running_for_SPN(self):
        # 프로세서를 하나씩 살핌
        for i in range(1, self.processor_num + 1):
            tmp_process = self.processors[i].work[:]
            # 일해야하는 프로세서 일 경우
            if tmp_process:
                tmp_process_num = tmp_process[1]
                # p코어라면
                if self.processors[i]._core == "p":
                    # 해당 프로세스의 실행시간 2개 빼줌
                    tmp_process[0] -= 2
                    # 해당 프로세서의 전력 3 증가
                    self.processors[i].power += 3
                # e코어라면
                else:
                    # 해당 프로세스의 실행 시간 1개 빼줌
                    tmp_process[0] -= 1
                    # 해당 프로세서의 전력 1 증가
                    self.processors[i].power += 1
                # 해당 프로세스가 모든 실행을 마쳤을 경우
                if tmp_process[0] <= 0:
                    # 빈 리스트를 해당 프로세서에게 저장하여 프로세스 종료를 알림.
                    self.processors[i].work = []
                    # 실행 종료시간 기록
                    self.processes[tmp_process_num].terminate_time = self.time + 1
                # 해당 프로세스의 잔여 실행시간이 있을 경우
                else:
                    # 다시 해당 프로세서에게 저장.
                    self.processors[i].work = tmp_process
            # 일할 프로세서가 아니라면 대기 전력 추가
            else:
                self.processors[i].power += 0.1

    def Shortest_Process_Next(self):
        visited = [False] * (self.process_num + 1)
        max_arr_time = self._find_max_arrive_time()
        # 도착할 프로세스들이 없고, 레디큐에도 프로세스가 없고 일하고 있는 프로세스가 없을 경우 while loop 종료! >> 스케줄링 종료
        while self.time <= max_arr_time or self.ready_q or self._working():

            # 레디큐에 도착한 프로세스 레디큐에 넣어주기
            self._fill_ready_q(visited)

            self.setRQ()
            # 레디 큐가 빌 때까지 반복 >> 프로세서들에게 프로세스를 뿌려줄 수 있는 만큼 모두 뿌려주기
            while self.ready_q:
                # 빈 프로세스를 찾고
                empty_processor = self._find_empty_processor()
                # 일을 안하고 있는 프로세서가 없다면 종료
                if not empty_processor:
                    break
                # 레디 큐에 있는 프로세스를 빈 프로세서에게 넣어준다.
                self.processors[empty_processor].work = heapq.heappop(self.ready_q)
            # 앞에서 이미 프로세서들에게 할당해줄 만큼 할당해 줬으므로 레디 큐에 남아 있는 프로세스들은 기다릴 수 밖에 없다 >> 대기시간 계산
            self._calculate_waiting_time()

            # 모두 프로세서들에게 프로세스를 배치 했으므로 프로세스 일하기
            self._processor_running_for_SPN()

            self.time += 1

        '''스케줄링 마친 후 총 전력 소비량 계산'''
        self._calculate_power_consumption()
        # print("\n\n----------SPN-----------")
        # for i in range(1, self.process_num + 1):
        #     print(self.processes[i])
        # print(f"\nPower_Consumption: {self.power_consumption:.1f}")

    def _processor_running_for_SRTN(self):
        # 프로세서를 하나씩 살핌
        for i in range(1, self.processor_num + 1):
            tmp_process = self.processors[i].work[:]
            # 일해야하는 프로세서 일 경우
            if tmp_process:
                tmp_process_num = tmp_process[1]
                # p코어라면
                if self.processors[i]._core == "p":
                    # 해당 프로세스의 실행시간 2개 빼줌
                    tmp_process[0] -= 2
                    # 해당 프로세서의 전력 3 증가
                    self.processors[i].power += 3
                # e코어라면
                else:
                    # 해당 프로세스의 실행 시간 1개 빼줌
                    tmp_process[0] -= 1
                    # 해당 프로세서의 전력 1 증가
                    self.processors[i].power += 1
                # 해당 프로세스가 모든 실행을 마쳤을 경우
                if tmp_process[0] <= 0:
                    # 빈 리스트를 해당 프로세서에게 저장하여 프로세스 종료를 알림.
                    self.processors[i].work = []
                    # 실행 종료시간 기록
                    self.processes[tmp_process_num].terminate_time = self.time + 1
                else:
                    self.processors[i].work = tmp_process
            # 일할 프로세서가 아니라면 대기 전력 추가
            else:
                self.processors[i].power += 0.1

    def Shortest_Remaining_Time_Next(self):

        visited = [False] * (self.process_num + 1)
        max_arr_time = self._find_max_arrive_time()
        # 도착할 프로세스들이 없고, 레디큐에도 프로세스가 없고 일하고 있는 프로세스가 없을 경우 while loop 종료! >> 스케줄링 종료
        while self.time <= max_arr_time or self.ready_q or self._working():

            # 레디큐에 도착한 프로세스 레디큐에 넣어주기
            self._fill_ready_q(visited)
            self.setRQ()
            '''남은 수행시간 기준 선점 스케줄링 임'''
            # 프로세서들 하나씩 확인
            for i in range(1, processor_num + 1):
                # 레디 큐가 비었으면 할당 종료
                if not self.ready_q:
                    break
                # tmp = 레디 큐 안의 최소 수행시간 프로세서
                tmp = heapq.heappop(self.ready_q)
                # 프로세서가 비었다면 바로 넣기
                if self.processors[i].work == []:
                    self.processors[i].work = tmp

                else:
                    # 레디큐에서 새로 꺼낸 프로세스가 i번째 프로세서에게 할당 된 프로세서보다 실행시간이 작을 경우 >> 선점
                    if tmp[0] < self.processors[i].work[0]:
                        # 둘이 위치 바꾸어주기
                        heapq.heappush(self.ready_q, self.processors[i].work)
                        self.processors[i].work = tmp
                    # 반대일 경우 >> 다시 레디큐에 넣기
                    else:
                        heapq.heappush(self.ready_q, tmp)


            # 앞에서 이미 프로세서들에게 할당해줄 만큼 할당해 줬으므로 레디 큐에 남아 있는 프로세스들은 기다릴 수 밖에 없다 >> 대기시간 계산
            self._calculate_waiting_time()

            # 모두 프로세서들에게 프로세스를 배치 했으므로 프로세스 일하기
            self._processor_running_for_SRTN()

            self.time += 1

        '''스케줄링 마친 후 총 전력 소비량 계산'''
        self._calculate_power_consumption()
        # print("\n\n----------SRTN-----------")
        # for i in range(1, self.process_num + 1):
        #     print(self.processes[i])
        # print(f"\nPower_Consumption: {self.power_consumption:.1f}")

    def _processor_running_for_RR(self):
        # 프로세서 하나씩 처리 >> 1초 처리하는 거임
        for i in range(1, self.processor_num + 1):
            # i 번째 프로세서의 프로세스
            tmp_process = self.processors[i].work[:]
            # i 번째 프로세서에게 할당 받은 프로세스가 있으면 작업 수행
            if tmp_process:
                # 프로세스 번호
                tmp_process_num = tmp_process[1]
                # 만약 i번째 프로세서가 p코어 일 경우
                if self.processors[i]._core == "p":
                    # 프로세스 실행시간 2 감소
                    tmp_process[0] -= 2
                    # i번째 프로세서의 전력 소비량 3 증가
                    self.processors[i].power += 3
                # i번째 프로세스가 e 코어 일 경우
                else:
                    # 프로세스 실행시간 1 감소
                    tmp_process[0] -= 1
                    # i번째 프로세서의 전력 소비량 1 증가
                    self.processors[i].power += 1
                # i번째 프로세서의 time_quantum 1 감소
                self.processors[i].time_quantum -= 1

                quantum = self.processors[i].time_quantum

                # 프로세스가 종료되었다면
                if tmp_process[0] <= 0:
                    # i번째 프로세서에서 제거
                    self.processors[i].work = []
                    # 종료된 프로세스의 종료시간 저장
                    self.processes[tmp_process_num].terminate_time = self.time + 1
                # 프로세스의 실행시간이 남아있다면
                else:
                    # time out이라면
                    if quantum <= 0:
                        # i번째 프로세서에서 프로세스 제거
                        self.processors[i].work = []
                        # 프로세스가 종료된 것은 아니고 time out 이므로 다시 레디큐에 삽입
                        self.ready_q.append(tmp_process)
                    # time_quantum이 남아 있다면
                    else:
                        # i번째 프로세서가 해당 프로세스 계속 작업 >> 1초뒤에 다시 작업하기위해 저장.
                        self.processors[i].work = tmp_process
            # i번째 프로세서에 할당된 프로세스가 없을 경우
            else:
                # i번째 프로세서의 전력 소비량 증가 >> 대기전력 소비량
                self.processors[i].power += 0.1

    # 레디큐에 도착한 프로세서를 레디큐로 옮겨주는 작업
    def _fill_ready_q_for_RR(self, visited):
        for i in range(1, self.process_num + 1):
            if not visited[i] and self.time >= self.processes[i].arrive_time:
                self.ready_q.append([self.processes[i].burst_time, self.processes[i]._number])
                visited[i] = True

    def _fill_ready_q(self, visited):
        for i in range(1, self.process_num + 1):
            if not visited[i] and self.time >= self.processes[i].arrive_time:
                heapq.heappush(self.ready_q, [self.processes[i].burst_time, self.processes[i]._number])
                visited[i] = True

    def Round_Robin(self):
        visited = [False] * (self.process_num + 1)
        # 도착하는 프로세스 중 도착시간이 제일 긴 시간을 찾는다.
        max_arr_time = self._find_max_arrive_time()
        # 현재시간이 최대 도착시간보다 크고, 레디큐가 비었으며, 모든 프로세스가 일을 안한다면 스케줄링 종료
        while self.time <= max_arr_time or self.ready_q or self._working():

            # 도착한 프로세스들 레디큐에 삽입
            self._fill_ready_q_for_RR(visited)
            self.setRQ()

            # 프로세서들에게 할당 >> 할당할 수 있을 만큼 레디 큐에서 모두 할당해준다. >>  프로세서가 여러개이므로 반드시 고려할 점
            while self.ready_q:
                # 빈 프로세서를 찾는다
                empty_processor = self._find_empty_processor()
                # 빈 프로세스가 없다면 프로세스 할당 중지
                if not empty_processor:
                    break
                # 찾은 빈 프로세서에게 레디 큐에서 프로세스 할당 >> 선입 선출 구조
                self.processors[empty_processor].work = self.ready_q.pop(0)
                # 할당 받은 즉시 그 프로세서에게 입력으로 받은 time_quantum을 copy해준다.
                self.processors[empty_processor].time_quantum = self.time_quantum
            # 레디 큐에 기다리는 프로세스를 찾아 그 프로세스의 대기시간을 증가시킨다.
            self._calculate_waiting_time()
            # 프로세서 작업 수행
            self._processor_running_for_RR()

            # 현재 시간 증가
            self.time += 1

        '''스케줄링 마친 후 총 전력 소비량 계산'''
        self._calculate_power_consumption()
        # print("\n\n----------RoundRobin-----------")
        # for i in range(1, self.process_num + 1):
        #     print(self.processes[i])
        # print(f"\nPower_Consumption: {self.power_consumption:.1f}")

    def setRQ(self):
        if len(self.ready_q) == 0:
            self.readyqueue.append([])
        else:
            tmp = []
            for i in self.ready_q:
                tmp.append("P" + str(i[1]))
            self.readyqueue.append(tmp)


    '''데이터 얻는 메서드'''

    def getRQ(self):
        # print(len(self.readyqueue))
        return self.readyqueue

    def getWT(self):
        for i in range(1, process_num + 1):
            self.WT.append(self.processes[i].waiting_time)
        return self.WT

    def getBT(self):
        for i in range(1, process_num + 1):
            self.BT.append(self.processes[i].burst_time)
        return self.BT

    def getTT(self):
        for i in range(1, process_num + 1):
            self.TT.append(self.processes[i].terminate_time - self.processes[i].arrive_time)
        return self.TT

    def getNTT(self):
        for i in range(process_num):
            self.NTT.append(round(self.TT[i] / self.BT[i], 2))
        return self.NTT

    def getPOWER(self):
        for i in range(1, processor_num + 1):
            self.POWER.append((self.processors[i]._core.upper() + "코어", round(self.processors[i].power, 2)))
        return self.POWER

    def getTOTALPOWER(self):
        TOTALPOWER = 0
        for i in self.POWER:
            TOTALPOWER += i[1]
        return round(TOTALPOWER, 2)

    def getTIME(self):
        return self.time


# process_num = int(input("# of Processes: "))
# processor_num = int(input("# of Processors: "))
# p_core_num = int(input("# of P core: "))
# arrive_time = list(map(int, input("Arrival time: ").split()))
# burst_time = list(map(int, input("Burst time: ").split()))
# time_quantum = int(input("Time quantum for RR: "))

# # 스케줄링 객체 생성
# SPN = Scheduling(process_num, processor_num, p_core_num, arrive_time, burst_time)
# # spn 스케줄링 실행
# SPN.Shortest_Process_Next()
# # 스케줄링 객체 생성
# SRTN = Scheduling(process_num, processor_num, p_core_num, arrive_time, burst_time)
# # srtn 스케줄링 실행
# SRTN.Shortest_Remaining_Time_Next()
# # 스케줄링 객체 생성
# RR = Scheduling(process_num, processor_num, p_core_num, arrive_time, burst_time, time_quantum)
# # rr 스케줄링 실행.
# RR.Round_Robin()

# '''여기서부터는 데이터를 얻는 매서드 호출법 입니다. >> print문 안의 중괄호만 보시면 돼요!'''
# # 일단 모든 데이터는 리스트로 묶어놨습니다 따로 필요한 데이터 형태나 수정사항 있으면 알려주세요
# # RR은 RoundRobin
# # 먼저 레디큐 호출법
# print(f"\nReadyQueue: {RR.getRQ()}")
# # WT 호출법
# print(f"\nWT: {RR.getWT()}")
# # BT 호출법
# print(f"\nBT: {RR.getBT()}")
# # TT 호출법
# print(f"\nTT: {RR.getTT()}")
# # NTT 호출법
# print(f"\nNTT: {RR.getNTT()}")
# # 각 코어당 전력 호출법
# print(f"\nPOWER: {RR.getPOWER()}")
# # 총 전력 호출법
# print(f"\nTOTAL POWER: {RR.getTOTALPOWER()}")
# # 스케줄링 종료시간 호출법
# print(f"\nTIME: {RR.getTIME()}")

'''
추가로 레디큐는 0초부터 시작이고 마지막 시간은 없어요
만약 스케줄링 시간이 총 20 초면 0~19초까지의 레디큐 상태만 볼 수 있어요 20초는 그냥 빈 리스트라고 생각하셔도 돼요
그리고 레디 큐의 데이터 기준, 즉 레디 큐의 각 인덱스(시간)는 각 시간마다 레디큐에 도착한 프로세스 받아주고 프로세서들에게 할당까지 한 상태예요 
'''



#print(SRTN.getRQ())
#print(SPN.getRQ())    
    
    
    
    
# GUI 실행
root.mainloop()
