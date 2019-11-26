
import tkinter as tk
from tkinter import *


#回调函数
def callRadiobutton():
    print('python is good!')

def callRadobuttonPrint(v):
    print(v)


# 弹窗
def create_window():
    # ans是一个list, 里面每一个值对应一个回答的对象, 对于每一个对象可以用get获取它的数值
    for an in ans:
        print(an.get())
    window = tk.Toplevel(root)
    window.geometry("300x200+120+100")
    window.title("ans")
    tk.Label(
        window,
        text="xxx",
    ).pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Radiobutton')
    root.geometry("900x600+120+100")         #设置窗口大小  并初始化桌面位置
    root.resizable(width =True,height =True)  #宽不可变 高可变 默认True
    ans = []
    questions = ["question1", "question2"] # 问题
    ans_list = ["aasdas", "b", "c", "d", "e"] # 答案的数组
    for i in range(len(questions)):
        ans.append(IntVar())
    for num_ques in range(len(questions)):

        frame = Frame(root)
        tk.Label(frame,
                 text=questions[num_ques],
                 justify=tk.LEFT,
                 padx=20).pack()
        for i in range(5):
            Radiobutton(frame, variable=ans[num_ques],
                        text=ans_list[i],
                        value=i,
                        command=callRadiobutton).pack(side=LEFT)
        frame.pack(side=TOP)
    button = tk.Button(root, text='Yes', width=25, command=create_window)
    button.pack(side=TOP)
    root.mainloop()

# df = pd.read_csv('try.csv',index_col=0,header=None)

# arrangement = []
#
# for row in df.iterrows():
#     row = list(row)
#     row[1] = row[1].as_matrix().reshape(6,5)
#     arrangement.append(row)
#
# q1 = int(input('Do you prefer popular game or minority game:'))
# q2 = int(input('How much time do you want to spend on a game:'))
# q3 = int(input('How much you\'d like to spend on video game:'))
# q4 = int(input('What difficulty would you like to choose:'))
# q5 = int(input('What system requirement would you like to choose:'))
# q6 = int(input('What rating would you like to choose:'))
#
# for i in range(len(arrangement)):
# 	print((arrangement[i])[0])
# 	print('合 = ',(((arrangement[i])[1])[0][q1-1])+(((arrangement[i])[1])[1][q2-1])+(((arrangement[i])[1])[2][q3-1])+(((arrangement[i])[1])[3][q4-1])+(((arrangement[i])[1])[4][q5-1])+(((arrangement[i])[1])[5][q6-1]))
# 	# print(row[0])
#     # (arrangement[i])[0][len((arrangement[i])[0]):len((arrangement[i])[0])] = ((arrangement[i])[1])[0][q1-1])+(((arrangement[i])[1])[1][q2-1])+(((arrangement[i])[1])[2][q3-1])+(((arrangement[i])[1])[3][q4-1])+(((arrangement[i])[1])[4][q5-1])+(((arrangement[i])[1])[5][q6-1])
# 	# print(row[0])


