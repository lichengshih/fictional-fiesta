import tkinter as tk
win=tk.Tk()
win.geometry('800x800')
win.title('體重控制小幫手')
win.config(background='white')

def calculate_bmi():
    height=float(height_entry.get())
    weight=float(weight_entry.get())
    bmi_value=round((weight/(height/100)**2),1)
    result='BMI 指數為：{} {}'.format(bmi_value, bmi_index(bmi_value))
    result_label.configure(text=result)
    
def bmi_index(bmi_value):
    if bmi_value <= 18:
        return '體重過輕可以多吃點！'
    elif  bmi_value <= 24:
        return '體重正常請繼續保持！'
    elif bmi_value > 24 :
        return '體重異常請少吃多動！'

header_label=tk.Label(win,text='BMI 計算器')
header_label.pack()
height_frame=tk.Frame(win)
height_frame.pack(side=tk.TOP)
height_label=tk.Label(height_frame,text='身高(cm)')
height_label.pack(side=tk.LEFT)
height_entry=tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)
weight_frame=tk.Frame(win)
weight_frame.pack(side=tk.TOP)
weight_label=tk.Label(weight_frame,text='體重(kg)')
weight_label.pack(side=tk.LEFT)
weight_entry=tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)
result_label=tk.Label(win)
result_label.pack()
calculate_btn=tk.Button(win, text='計算 BMI',command=calculate_bmi)
calculate_btn.pack()
win.mainloop()
