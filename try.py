import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd


#回调函数
def callRadiobutton():
    print('python is good!')

def callRadobuttonPrint(v):
    print(v)



# 弹窗
def create_window():
    # ans是一个list, 里面每一个值对应一个回答的对象, 对于每一个对象可以用get获取它的数值
    final_list = []
    return_list = []
    # print(E1.get())####控制台打印
    for an, weight in zip(ans, Weights):
        final_list.append(weight.get())
        return_list.append(an.get())
    # print(return_list)
    rate = getScore(return_list)
    final_result = getResult(rate)
    window = tk.Toplevel(root)
    window.geometry("300x200+500+300")
    window.title("TOP recommend")
    tk.Label(
        window,
        text=final_result,#E1.get()#
    ).pack()


def getScore(return_list):
    rate = []
    for i in range(len(arrangement)):
        temp = []
        temp.append((arrangement[i])[0])
        temp.append((((arrangement[i])[1])[0][return_list[0]])+(((arrangement[i])[1])[1][return_list[1]]) + (((arrangement[i])[1])[2][return_list[2]])+(((arrangement[i])[1])[3][return_list[3]])+(((arrangement[i])[1])[4][return_list[4]])+(((arrangement[i])[1])[5][return_list[5]]))
        rate.append(temp)
    return rate

def takeSecond(elem):
    return elem[1]
def getResult(rate):
    rate.sort(key=takeSecond,reverse=True)
    result = ''
    for x in range(5):
        rate[x][:2]#把最高的5个推荐出来
        result += (rate[x][:2])[0]+'(score): '+str("%.5f" %rate[x][:2][1]) +'\n'
    return result

df = pd.read_csv('SYS660final_data.csv',index_col=0,header=1)

arrangement = []

for row in df.iterrows():
    row = list(row)
    row[1] = row[1].as_matrix().reshape(6,5)
    arrangement.append(row)


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('DSS-RadioGame')
    root.geometry("1000x800+200+10")#设置窗口大小  并初始化桌面位置
    root.resizable(width =True,height =True)  #宽不可变 高可变 默认True
    ans = []
    questions = ['How much you\'d like to spend on video game?($)',"Do you prefer popular game or minority game?(Sales Million)", "How much time do you want to spend on game?(H)",'What difficulty would you like to choose?','Which picture quality game do you want to choose?','What rating would you like to choose?'] # 问题
    ans_list = [["<19.99", "19.99-29.99","29.99-39.99", "39.99-49.99", "> 49.99"],['<8','9-15','16-24','25-30','>30'],['<50','50-150','150-250','250-350','>350'],['Heaven','Easy','Medium','Hard','Hell'],['Mosaic','Low','Medium','High','Optimal'],['<7','7-8','8-8.5','8.5-9','>9']] # 答案选项的数组
    weight = [0.196078431,0.18627451,0.166666667,0.162745098,0.160784314,0.12745098]#问题权重



    for i in range(len(questions)):
        ans.append(IntVar())#问题答案
    for num_ques in range(len(questions)):

        frame = Frame(root)
        tk.Label(frame,
                 text=questions[num_ques],
                 justify=tk.LEFT,
                 padx=20).pack()
        for i in range(5):
            Radiobutton(frame, variable=ans[num_ques],
                        text=ans_list[num_ques][i],
                        value=i,
                        command=callRadiobutton).pack(side=LEFT)
        frame.pack(side=TOP)
#权重选项
    # com = Frame(root)
    # tk.Label(com,
    #              text='caonima[num_ques]',
    #              justify=tk.LEFT,
    #              padx=20).pack()
    Weights = []

    for num_ques in range(len(questions)):
        fr = Frame(root)
        l = Label(fr,
                 text='What do you think is the '+str(num_ques+1)+' important factor')
        l.pack(side=TOP)# #将下拉菜单绑定到窗体
        xVariable = tk.StringVar()     # #创建变量，便于取值
        Weights.append(xVariable)

        com = ttk.Combobox(root, textvariable=xVariable)     # #创建下拉菜单
        com["value"] = ('Money Spend', 'Popularity', 'Time Cost', 'Difficulty', 'Picture Quality', 'Rating')    # #给下拉菜单设定值
        com.pack(side=TOP)
        fr.pack(side=TOP)
#呼出按钮
    button = tk.Button(root, text='Yes', width=25, command=create_window)
    button.pack(side=TOP)

    root.mainloop()

