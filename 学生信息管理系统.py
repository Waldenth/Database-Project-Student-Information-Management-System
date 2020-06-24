import pymysql
from tkinter import ttk  # py自带图形界面库
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox
import hashlib
import os
import time
# 组成
# 欢迎页类
# 管理员登录界面类
# 管理员操作界面类
# 学生登录界面类
# 学生信息查看界面类
# 关于界面类
# __main__()入口


# 欢迎页
class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面(返回的是主界面)
        self.window = tk.Tk()  # 初始框声明
        self.window.title('武汉大学学生信息管理系统')  # 窗口左上角属性信息
        self.window.geometry('500x650')  # 设置窗口大小,x

        label = Label(self.window, text="武汉大学学生信息管理系统", font=("微软雅黑", 20))
        label.pack(pady=100)  # Label宽度(上下),使用了pack()布局
        '''
        1、pack函数布局的时候，默认先使用的放到上面，然后依次向下排列，默认方式它会给我们的组件一个自认为合适的位置和大小。
        2、pack函数也可以接受几个参数，side参数，指定了它停靠在哪个方向，可以为LEFT,TOP,RIGHT,BOTTOM,分别代表左，上，右，下，
           它的fill参数可以是X,Y,BOTH,NONE即在水平方向填充，竖直方向填充，水平和竖直方向填充和不填充。
        3、它的expand参数可以是YES 和 NO,它的anchor参数可以是N,E,S,W(这里的NESW分别表示北东南西，这里分别表示上右下左)以及他们的组合或者是CENTER(表示中间)
        4、它的ipadx表示的是内边距的x方向，它的ipady表示的是内边距的y的方向，padx表示的是外边距的x方向，pady表示的是外边距的y方向。
        '''
        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        # 按钮command响应函数调用与传参
        Button(self.window, text="管理员登陆", font=("微软雅黑", 14), command=lambda: AdminPage(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="教师登陆", font=("微软雅黑", 14), command=lambda: TeacherPage(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="学生登陆", font=("微软雅黑", 14), command=lambda: StudentPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="关于", font=("微软雅黑", 14), command=lambda: AboutPage(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=("微软雅黑", 14), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.mainloop()  # 主消息循环


# 管理员登录界面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎您,管理员")
        self.window.geometry('500x550')

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='管理员登录口', bg='SkyBlue',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='管理员账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        self.admin_username = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        # self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='管理员密码：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员密码输入栏,密码用*显示
        self.admin_pass = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        # 登录确定按钮,响应函数调用self.login
        Button(self.window, text="登录", width=8, font=(
            "微软雅黑", 12), command=self.login).pack(side=LEFT,padx=60)
        Button(self.window, text="修改密码", width=8, font=(
            "微软雅黑", 12), command=self.ChangePass).pack(side=RIGHT,padx=60)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack(side=BOTTOM,pady=40)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def login(self):
        admin_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        args=(self.admin_username.get())
        sql = "SELECT * FROM admin_login_k WHERE admin_id=%s" 
        '''
        admin'or 'a'='a
        cursor.execute(sql,args)
        results = cursor.fetchall()
        print(results)
        '''
        try:
            # 执行SQL语句
            cursor.execute(sql,args)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.admin_pass.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == admin_pass:
            print("Log:User log success!")
            AdminSelect(self.window)  # 密码正确,调用管理员界面类,进入管理员操作界面
        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def ChangePass(self):
        AdminPassword(self.window)

class AdminPassword:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎您,管理员")
        self.window.geometry('500x650')

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='修改密码', bg='SkyBlue',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='管理员账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        self.admin_username = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        # self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='原始密码：', font=("微软雅黑", 14)).pack(pady=10)
        # 管理员密码输入栏,密码用*显示
        self.admin_pass_old = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass_old.pack()

        Label(self.window, text='修改密码：', font=("微软雅黑", 14)).pack(pady=10)
        self.admin_pass_new1 = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass_new1.pack()

        Label(self.window, text='确认修改密码：', font=("微软雅黑", 14)).pack(pady=10)
        self.admin_pass_new2 = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass_new2.pack()

        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        # 修改确定按钮,响应函数调用self.changepass
        Button(self.window, text="确定修改", width=8, font=(
            "微软雅黑", 12), command=self.changepass).pack(pady=20)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def changepass(self):
        if(self.admin_pass_new1.get()!=self.admin_pass_new2.get()):
            messagebox.showinfo('对不起!', '您的修改密码不一致')
            return
        admin_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        args=(self.admin_username.get())
        sql = "SELECT * FROM admin_login_k WHERE admin_id=%s" 
           
        try:
            # 执行SQL语句
            cursor.execute(sql,args)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.admin_pass_old.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == admin_pass:
            print("Log:User log success!")
            #AdminSelect(self.window)  # 密码正确,调用管理员界面类,进入管理员操作界面
            password_new=self.admin_pass_new1.get()
            new_pass=hashlib.md5()
            new_pass.update(password_new.encode('utf-8'))
            new_pass=str(new_pass.hexdigest())
            args=(new_pass,self.admin_username.get())
            sql="UPDATE admin_login_k SET admin_pass = %s WHERE admin_id = %s"
            #print(sql)
            db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
            cursor = db.cursor()  # 获取操作游标
            try:
                cursor.execute(sql,args)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '密码更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')

        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


class AdminSelect:  #管理员选择进入的操作界面
    def __init__(self,parent_window):
        parent_window.destroy() #销毁上一级界面
        self.window=tk.Tk()
        self.window.title("管理员选项")
        self.window.geometry('500x550')

        label = tk.Label(self.window, text='管理员操作选项', bg='SkyBlue',font=('微软雅黑', 20), width=50, height=3)
        label.pack()
        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        Button(self.window, text="修改学生信息和成绩", font=("微软雅黑", 14), command=lambda: AdminManage(self.window), width=30,fg='white', bg='gray', height=2,activebackground='black', activeforeground='white').pack()
        label_empty2=tk.Label(self.window,text='').pack(pady=5)
        Button(self.window, text="学生所属学院变动", font=("微软雅黑", 14), command=lambda: AdminManageMajor(self.window), width=30, fg='white', bg='gray', height=2,activebackground='black', activeforeground='white').pack()
        label_empty3=tk.Label(self.window,text='').pack(pady=5)
        Button(self.window, text="修改课程信息", font=("微软雅黑", 14), command=lambda: AdminManageCourse(self.window), width=30,fg='white', bg='gray',height=2, activebackground='black', activeforeground='white').pack()

        Button(self.window,width=10,text="数据库备份",font=("微软雅黑",12),command=lambda: AdminBackup(self.window)).pack(side=LEFT,padx=65,pady=5)
        Button(self.window,width=10,text="返回主界面",font=("微软雅黑",12),command=self.back).pack(side=RIGHT,padx=65)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()  # 主消息循环
    
    def back(self):
        StartPage(self.window)



class AdminBackup:
    def __init__(self,parent_window):
        parent_window.destroy()
        self.window=tk.Tk()
        self.window.title("数据库备份(管理员)")

        self.frame_left_top=tk.Frame(width=300,height=200)
        self.frame_right_top = tk.Frame(width=200, height=240)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        self.columns=("备份时间","备份文件路径")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)

        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        self.tree.column("备份时间", width=200, anchor='center')
        self.tree.column("备份文件路径", width=300, anchor='center')

         # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.Backup_number=0

        self.time=[]
        self.path=[]

        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql="SELECT Backup_time,filepath_and_name FROM Backup_info"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                self.time.append(row[0])
                self.path.append(row[1])
                self.Backup_number=self.Backup_number+1
        except:
            messagebox.showinfo('警告！', '数据库连接失败！')    
            return
        db.close()

        for i in range (min(len(self.time),len(self.path))):
            self.tree.insert('',i,values=(self.time[i],self.path[i]))

        for col in self.columns:
            self.tree.heading(col, text=col)

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top,text="数据库备份信息:", font=('微软雅黑', 20))

         # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)

        self.var_time=StringVar()
        self.var_path=StringVar()

        # 左上方消息区
        # 备份时间
        self.right_top_id_label = Label(
            self.frame_left_top, text="备份时间：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_time, font=('微软雅黑', 8))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 备份路径
        self.right_top_name_label = Label(
            self.frame_left_top, text="备份文件路径：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_path, font=('微软雅黑', 8))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='新建数据库备份', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='删除选中的备份', width=20, command=self.del_row)
        self.right_top_button3 = ttk.Button(
            self.frame_right_top, text='使用本备份恢复数据库', width=20, command=self.rollback)
        
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        AdminSelect(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            # print(self.col)
            # print(self.row)

            self.row_info = self.tree.item(self.row, "values")

            self.var_time.set(self.row_info[0])
            self.var_path.set(self.row_info[1])

            self.right_top_id_entry = Entry(
                self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        except:
            return

    def new_row(self):
        string_path=os.getcwd()
        self.Backup_number=self.Backup_number+1
        filename="Backup_file_"+str(self.Backup_number)+".sql"
        #print(filename)
        string_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        string_time=str(string_time)
        instruction="mysqldump -u root  -p123456 --databases school_database > ./"+filename
        #print(instruction)
        
        os.system(instruction)
        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql="INSERT INTO Backup_info(Backup_time,filepath_and_name) VALUES(%s,%s)"
        #print(filename)
        args=(string_time,filename)
        #print(args)
        cursor.execute(sql,args)
        db.commit()
        messagebox.showinfo('提示！', '数据库备份成功！')
     
        db.close()

        self.time.append(str(string_time))
        self.path.append(filename)
        self.tree.insert('',len(self.time)-1,values=(string_time,filename))
        self.tree.update()
        return

    def del_row(self):
        string_path=os.getcwd()
        res = messagebox.askyesnocancel('警告！', '是否删除所选备份?')
        if res == True:
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            args=self.row_info[0]
            sql="DELETE FROM Backup_info WHERE Backup_time=%s"
            try:
                cursor.execute(sql,args)
                db.commit()
                target_file=string_path+'\\'+self.row_info[1]
                os.remove(target_file)
                self.Backup_number=self.Backup_number-1
                messagebox.showinfo('提示！', '删除成功!')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败!')
                return
            db.close()  # 关闭数据库连接
            id_index = self.time.index(self.row_info[0])
            del self.time[id_index]
            del self.path[id_index]
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
        return
    def rollback(self):
        string_path=os.getcwd()
        res = messagebox.askyesnocancel('警告！', '是否选择本备份恢复数据库?')
        if res==True:
            try:
                intrcution="mysql -u root -p123456 TEST_SCHOOL < ./"+self.row_info[1]
                os.system(intrcution)
                #time.sleep(3)
                messagebox.showinfo('提示', '恢复成功!')
            except:
                messagebox.showinfo('警告', '恢复失败!')

# 老师登录界面
class TeacherPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎您,老师")
        self.window.geometry('500x550')

        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标

        sql="SELECT teacher_id FROM teacher_k"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取获得的行信息,本表两列
        teacher_id_list = cursor.fetchall()

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='教师登录口', bg='Lime',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='教师账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        self.admin_username = tk.StringVar()
        numberChosen = ttk.Combobox(self.window, width=28, textvariable=self.admin_username,font=tkFont.Font(size=14),state="readonly")
        numberChosen['values'] = teacher_id_list     # 设置下拉列表的值
        numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        numberChosen.pack()

        Label(self.window, text='教师密码：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员密码输入栏,密码用*显示
        self.admin_pass = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        # 登录确定按钮,响应函数调用self.login
        Button(self.window, text="登录", width=8, font=(
            "微软雅黑", 12), command=self.login).pack(side=LEFT,padx=60)
        Button(self.window, text="修改密码", width=8, font=(
            "微软雅黑", 12), command=self.ChangePass).pack(side=RIGHT,padx=60)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack(side=BOTTOM,pady=40)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def login(self):
        admin_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        args=(self.admin_username.get())
        sql = "SELECT * FROM teacher_login_k WHERE teacher_id=%s"

        try:
            # 执行SQL语句
            cursor.execute(sql,args)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.admin_pass.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == admin_pass:
            print("Log:User log success!")
            TeacherSelect(self.window,admin_id)  # 密码正确,调用管理员界面类,进入管理员操作界面
        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def ChangePass(self):
        TeacherPassword(self.window)

class TeacherPassword:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎您,老师")
        self.window.geometry('500x550')

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='修改密码', bg='Lime',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='教师账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        self.admin_username = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        # self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='原始密码：', font=("微软雅黑", 14)).pack(pady=10)
        # 管理员密码输入栏,密码用*显示
        self.admin_pass_old = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass_old.pack()

        Label(self.window, text='修改密码：', font=("微软雅黑", 14)).pack(pady=10)
        self.admin_pass_new = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass_new.pack()


        # 修改确定按钮,响应函数调用self.changepass
        Button(self.window, text="确定修改", width=8, font=(
            "微软雅黑", 12), command=self.changepass).pack(pady=20)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def changepass(self):
        admin_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        args=( self.admin_username.get())
        sql = "SELECT * FROM teacher_login_k WHERE teacher_id=%s" 

        try:
            # 执行SQL语句
            cursor.execute(sql,args)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.admin_pass_old.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == admin_pass:
            print("Log:User log success!")
            #AdminSelect(self.window)  # 密码正确,调用管理员界面类,进入管理员操作界面
            password_new=self.admin_pass_new.get()
            new_pass=hashlib.md5()
            new_pass.update(password_new.encode('utf-8'))
            new_pass=str(new_pass.hexdigest())
            args=(new_pass,self.admin_username.get())
            sql="UPDATE teacher_login_k SET teacher_pass = %s WHERE teacher_id = %s"  # SQL 语句
            #print(sql)
            db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
            cursor = db.cursor()  # 获取操作游标
            try:
                cursor.execute(sql,args)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '密码更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')

        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


class TeacherSelect:  #管理员选择进入的操作界面
    def __init__(self,parent_window,id):
        parent_window.destroy() #销毁上一级界面
        self.window=tk.Tk()
        self.window.title("教师选项")
        self.window.geometry('500x550')
        self.target_id=id

        label = tk.Label(self.window, text='教师操作选项', bg='Lime',font=('微软雅黑', 20), width=50, height=3)
        label.pack()
        label_empty2=tk.Label(self.window,text='').pack(pady=30)
        Button(self.window, text="查看课程信息", font=("微软雅黑", 14), command=lambda: TeacherCourseInfo(self.window,self.target_id), width=30, fg='white', bg='gray', height=2,activebackground='black', activeforeground='white').pack()
        label_empty3=tk.Label(self.window,text='').pack(pady=20)
        Button(self.window, text="查看修改个人信息", font=("微软雅黑", 14), command=lambda: TeacherInfo(self.window,self.target_id), width=30,fg='white', bg='gray',height=2, activebackground='black', activeforeground='white').pack()

        Button(self.window,width=10,text="返回主界面",font=("微软雅黑",12),command=self.back).pack(pady=55)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()  # 主消息循环
    
    def back(self):
        StartPage(self.window)


class TeacherInfo:
    def __init__(self, parent_window, teacher_id):
        parent_window.destroy() # 销毁主界面
        id=teacher_id
        self.target_teacher_id=id
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师个人信息')
        self.window.geometry('500x650')  # 这里的乘是小x
        label = tk.Label(self.window, text='教师个人信息', bg='LIME', font=('微软雅黑', 20), width=50, height=4)
        label.pack()
        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_tel=StringVar()
        self.var_qq=StringVar()
        self.var_dept=StringVar()
        self.var_id.set(id)
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        args=(id)
        sql="SELECT teacher_name,teacher_tel,teacher_qq,teacher_dept FROM teacher_k WHERE teacher_id=%s"
        cursor.execute(sql,args)
        results = cursor.fetchall()
        db.close()
        for row in results:
            self.var_name.set(row[0])
            self.var_tel.set(row[1])
            self.var_qq.set(row[2])
            self.var_dept.set(row[3])

        L1=tk.Label(self.window,text="工号",font=('微软雅黑', 15))
        L1.pack()
        E1=tk.Entry(self.window,textvariable=self.var_id, font=('微软雅黑', 15))
        E1.pack()
 
        L2=tk.Label(self.window,text="姓名",font=('微软雅黑', 15))
        L2.pack()
        E2=tk.Entry(self.window,textvariable=self.var_name, font=('微软雅黑', 15))
        E2.pack()

        L3=tk.Label(self.window,text="电话",font=('微软雅黑', 15))
        L3.pack()
        E3=tk.Entry(self.window,textvariable=self.var_tel, font=('微软雅黑', 15))
        E3.pack()

        L4=tk.Label(self.window,text="QQ",font=('微软雅黑', 15))
        L4.pack()
        E4=tk.Entry(self.window,textvariable=self.var_qq, font=('微软雅黑', 15))
        E4.pack()

        L5=tk.Label(self.window,text="学院",font=('微软雅黑', 15))
        L5.pack()
        E5=tk.Entry(self.window,textvariable=self.var_dept, font=('微软雅黑', 15))
        E5.pack()

        Button(self.window,text="修改信息",width=8, font=("微软雅黑", 12), command=self.update).pack(pady=15)

        Button(self.window, text="返回", width=8, font=("微软雅黑", 12), command=self.back).pack(pady=15)

    def back(self):
        TeacherSelect(self.window,self.target_teacher_id)  # 显示主窗口 销毁本窗口
    def update(self):
        #print(self.var_tel.get())
        #print(self.var_qq.get())
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        args=(self.var_tel.get(),self.var_qq.get(),self.target_teacher_id)
        sql="UPDATE teacher_k SET teacher_tel=%s,teacher_qq=%s WHERE teacher_id=%s"
        try:
            cursor.execute(sql,args)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '更新成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            return
        db.close()  # 关闭数据库连接
       
class TeacherCourseInfo:
    def __init__(self, parent_window, teacher_id):
        parent_window.destroy() # 销毁主界面
        self.target_teacher_id=teacher_id
        self.window = Tk()
        self.window.title('执教课程')
      
        self.frame_left_top = tk.Frame(width=300, height=220)
        self.frame_right_top = tk.Frame(width=200, height=220)
        self.frame_center = tk.Frame(width=550, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

         # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "学院","成绩")
        self.tree = ttk.Treeview(
            self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(
            self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("学院", width=200, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')

        for col in self.columns:  # 绑定函数
            self.tree.heading(col, text=col)

         # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id=[]
        self.name=[]
        self.dept=[]
        self.grade=[]
        

        # 创建一个下拉列表
        self.left_top_id_label = Label(
            self.frame_left_top, text="请选择课程：", font=('微软雅黑', 15))
        left_top_empty_label=Label(self.frame_left_top, text="", font=('微软雅黑', 15))
        self.number = tk.StringVar()
        numberChosen = ttk.Combobox(self.frame_left_top, width=35, textvariable=self.number)
        args=(self.target_teacher_id)
        sql="SELECT course FROM course_info WHERE teacher_id=%s"
        #print(sql)
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        cursor.execute(sql,args)
        results = cursor.fetchall()
        db.close()
        numberChosen['values'] = results     # 设置下拉列表的值
        self.left_top_id_label.grid(row=1, column=0)
        left_top_empty_label.grid(row=2,column=0)
        numberChosen.grid(row=3, column=0)      # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

        

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='查询', width=20, command=self.check)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='更新选中学生成绩', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(
            self.frame_right_top, text='返回上一级', width=20, command=self.back)

        #位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)


        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(
            row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        TeacherSelect(self.window,self.target_teacher_id)  # 显示主窗口 销毁本窗口
    def check(self):
        items=self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        self.select_course=self.number.get()
        
        self.id=[]
        self.name=[]
        self.dept=[]
        self.grade=[]
        
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        args=(self.select_course,self.target_teacher_id)
        sql="SELECT stu_id,stu_name,stu_dept,grade FROM student_k NATURAL JOIN stu_grade NATURAL JOIN course_info WHERE course=%s AND teacher_id=%s"
        #print(sql)
        try:
            cursor.execute(sql,args)
            results=cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.dept.append(row[2])
                self.grade.append(row[3])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')    
            return
        db.close()  # 关闭数据库连接   

        for i in range(len(self.id)):
            self.tree.insert('',i,values=(self.id[i],self.name[i],self.dept[i],self.grade[i]))



        return
    def updata_row(self):
        return


#修改学生学院信息类
class AdminManageMajor:
    def __init__(self,parent_window):
        parent_window.destroy()
        self.window=tk.Tk()
        self.window.title("管理员操作界面")

        self.frame_left_top=tk.Frame(width=300,height=200)
        self.frame_right_top = tk.Frame(width=200, height=240)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        self.columns=("学号","姓名","年龄","学院")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)

        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

         # 表格标题
        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("学院", width=150, anchor='center')

        
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

         # 定义存放每个学生各种信息的不同数组
        self.id = []
        self.name = []
        self.age = []
        self.dept = []

        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql = "SELECT stu_id,stu_name,stu_age,stu_dept FROM student_k"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.age.append(row[2])
                self.dept.append(row[3])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')    
            return
        db.close()  # 关闭数据库连接

        # 写入数据,这里只展示所有信息都完整的学生
        for i in range(min(len(self.id), len(self.name), len(self.age), len(self.dept))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.age[i], self.dept[i]))

          # 绑定函数，使表头可排序
        for col in self.columns:
            self.tree.heading(col, text=col)

         # 定义顶部区域
        self.top_title = Label(self.frame_left_top,text="学生专业信息:", font=('微软雅黑', 20))

        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()   # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_age = StringVar()   # 声明年龄
        self.var_dept = StringVar()  # 声明学院

        # 左上方消息区
        # 学号
        self.right_top_id_label = Label(
            self.frame_left_top, text="学号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 姓名
        self.right_top_name_label = Label(
            self.frame_left_top, text="姓名：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_name, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 年龄
        self.right_top_gender_label = Label(
            self.frame_left_top, text="年龄：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 专业
        self.right_top_gender_label = Label(
            self.frame_left_top, text="学院：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_dept,
                                            font=('微软雅黑', 15))

        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='更新选中学生信息', width=20, command=self.updata_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        AdminSelect(self.window)  # 返回父窗口 销毁本窗口

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            # print(self.col)
            # print(self.row)

            self.row_info = self.tree.item(self.row, "values")

            self.var_id.set(self.row_info[0])

            self.target_stu_id = self.row_info[0]

            self.var_name.set(self.row_info[1])
            self.var_age.set(self.row_info[2])
            self.var_dept.set(self.row_info[3])
            self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        except:
            print("Log:Invalid operation")
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE student_k SET stu_name = '%s', stu_age = '%s', stu_dept = '%s' \
				 WHERE stu_id = '%s'" % (self.var_name.get(), self.var_age.get(), self.var_dept.get(), self.var_id.get())  # SQL 语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                    return
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.age[id_index] = self.var_age.get()
                self.dept[id_index]=self.var_dept.get()

                self.tree.item(self.tree.selection()[0], values=(self.var_id.get(), self.var_name.get(),self.var_age.get(),self.var_dept.get()))  # 修改对对应行信息
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')


# 管理员填录学生成绩，修改非学院信息类
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = Tk()
        self.window.title('管理员操作界面')

        # 定义各个区域块的大小
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=240)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "年龄")
        self.tree = ttk.Treeview(
            self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(
            self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格标题
        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("姓名", width=150, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义存放每个学生各种信息的不同数组
        self.id = []
        self.name = []
        self.gender = []
        self.age = []

        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql = "SELECT stu_id,stu_name,stu_gender,stu_age FROM student_k"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取查询结果列表
            results = cursor.fetchall()
            for row in results:  # 对
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            return
        db.close()  # 关闭数据库连接

        # 写入数据,这里只展示所有信息都完整的学生
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):
            self.tree.insert('', i, values=(
                self.id[i], self.name[i], self.gender[i], self.age[i]))

        # 绑定函数，使表头可排序
        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(
                self.tree, _col, False))

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top,
                               text="学生信息:", font=('微软雅黑', 20))
        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,
                            sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()   # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()   # 声明性别
        self.var_age = StringVar()  # 声明年龄

        # 左上方消息区
        # 学号
        self.right_top_id_label = Label(
            self.frame_left_top, text="学号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 姓名
        self.right_top_name_label = Label(
            self.frame_left_top, text="姓名：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_name, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(
            self.frame_left_top, text="性别：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_gender_label = Label(
            self.frame_left_top, text="年龄：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('微软雅黑', 15))

        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='更新选中学生信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(
            self.frame_right_top, text='删除选中学生信息', width=20, command=self.del_row)
        self.right_top_button4 = ttk.Button(
            self.frame_right_top, text="更新学生课程成绩", width=20, command=self.updata_student)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminSelect(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            # print(self.col)
            # print(self.row)

            self.row_info = self.tree.item(self.row, "values")

            self.var_id.set(self.row_info[0])

            self.target_stu_id = self.row_info[0]
            
            self.var_name.set(self.row_info[1])
            self.var_gender.set(self.row_info[2])
            self.var_age.set(self.row_info[3])
            self.right_top_id_entry = Entry(
                self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        except:
            return

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):    # 根据排序后索引移动
            tv.move(k, '', index)
        # 重写标题，使之成为再点倒序的标题
        tv.heading(col, command=lambda: self.tree_sort_column(
            tv, col, not reverse))

    def new_row(self):
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该学生已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != '':
                # 连接数据库
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()
                sql = "INSERT INTO student_k(stu_id, stu_name, stu_gender, stu_age,stu_dept) \
				       VALUES ('%s', '%s', '%s', '%s','NULL')" % \
                    (self.var_id.get(), self.var_name.get(),
                     self.var_gender.get(), self.var_age.get())  # SQL 插入语句
                sql2="INSERT INTO stu_grade(stu_id,course_id,grade) VALUES('%s','NULL','NULL')"%\
                    (self.var_id.get())
                Newpassword=self.var_id.get()
                new_pass_md5=hashlib.md5()
                new_pass_md5.update(Newpassword.encode('utf-8'))
                NewpassMd5=new_pass_md5.hexdigest()
                sql3="INSERT INTO stu_login_k(stu_id,stu_pass) VALUES ('%s','%s')"%(self.var_id.get(),NewpassMd5)
                try:
                    cursor.execute(sql)
                    cursor.execute(sql2)
                    cursor.execute(sql3)
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告!', '提交失败!')
                    return
                db.close()

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) -1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功!请注意及时补全学生专业和课程信息')
            else:
                messagebox('警告!', '请填写学生数据!')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE student_k SET stu_name = '%s', stu_gender = '%s', stu_age = '%s' \
				 WHERE stu_id = '%s'" % (self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get())  # SQL 语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                    return
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.gender[id_index] = self.var_gender.get()
                self.age[id_index] = self.var_age.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                    self.var_age.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            #print(self.row_info[0])  # 鼠标选中的学号
            #print(self.tree.selection()[0])  # 行号
            #print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM student_k WHERE stu_id = '%s'" % (
                self.row_info[0])  # SQL 插入语句
            sql2="DELETE FROM stu_grade WHERE stu_id='%s'"%(self.row_info[0])
            sql3="DELETE FROM stu_login_k WHERE stu_id='%s'"%(self.row_info[0])
            try:
                cursor.execute(sql)  # 执行sql语句
                cursor.execute(sql2)
                cursor.execute(sql3)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                return
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            self.tree.delete(self.tree.selection()[0])  # 删除所选行

    def updata_student(self):
        AdminManageStudent(self.window, self.target_stu_id)

#三级界面，查看某个学生的课程信息
class AdminManageStudent:
    def __init__(self, parent_window, target_stu_id):
        id = target_stu_id
        id = str(id)
        parent_window.destroy()
        self.window = Tk()
        self.window.title('学生课程成绩填录')

        self.frame_left_top = tk.Frame(width=300, height=220)
        self.frame_right_top = tk.Frame(width=200, height=220)
        self.frame_center = tk.Frame(width=550, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "课程号", "课程","学分","成绩")
        self.tree = ttk.Treeview(
            self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(
            self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格标题
        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("课程号", width=100, anchor='center')
        self.tree.column("课程", width=150, anchor='center')
        self.tree.column("学分", width=50, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.course_id=[]
        self.course = []
        self.credit = []
        self.grade = []

        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()

        sql = "SELECT stu_id,course_id,course,credit,grade FROM stu_grade NATURAL JOIN course_info WHERE stu_id = '%s'" % (id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取查询结果列表
            results = cursor.fetchall()
            for row in results:  # 对
                self.id.append(row[0])
                self.course_id.append(row[1])
                self.course.append(row[2])
                self.credit.append(row[3])
                self.grade.append(row[4])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            return
        db.close()  # 关闭数据库连接
        # 写入数据,这里只展示所有信息都完整的学生
        for i in range(min(len(self.id), len(self.credit), len(self.course), len(self.grade),len(self.course_id))):
            self.tree.insert('', i, values=(
                self.id[i], self.course_id[i],self.course[i] ,self.credit[i],self.grade[i]))
        
        if min(len(self.id), len(self.credit), len(self.course), len(self.grade),len(self.course_id))==0:
            self.tree.insert('', 0, values=(id,'','','',''))
        
        for col in self.columns:  # 绑定函数
            self.tree.heading(col, text=col)

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top,
                               text="学生成绩信息:", font=('微软雅黑', 20))
        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,
                            sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()   # 声明学号
        self.var_course_id=StringVar()  #声明课程号
        self.var_course = StringVar()   # 声明课程名
        self.var_credit = StringVar()  # 声明学分
        self.var_grade = StringVar()  # 声明年龄

        # 左上方消息区
        # 学号
        self.right_top_id_label = Label(
            self.frame_left_top, text="学号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 课程号
        self.right_top_name_label = Label(
            self.frame_left_top, text="课程号：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_course_id, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 课程
        self.right_top_gender_label = Label(
            self.frame_left_top, text="课程：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_course,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学分
        self.right_top_gender_label = Label(
            self.frame_left_top, text="学分：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(
            self.frame_left_top, textvariable=self.var_credit, font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        #成绩
        self.right_top_gender_label = Label(
            self.frame_left_top, text="成绩：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(
            self.frame_left_top, textvariable=self.var_grade, font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=5, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='新建学生课程成绩', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='更新选中学生成绩', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(
            self.frame_right_top, text='删除选中学生成绩', width=20, command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(
            row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    # 返回调用

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            self.row_info = self.tree.item(self.row, "values")
            self.var_id.set(self.row_info[0])
            self.var_course_id.set(self.row_info[1])
            self.var_course.set(self.row_info[2])
            self.var_credit.set(self.row_info[3])
            self.var_grade.set(self.row_info[4])
            self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        except:
            print("Log:Invalid operation")

    def new_row(self):
        #print(self.course)
        if(self.var_course_id.get()) in self.course_id:
            messagebox.showinfo('警告！', '该学生本课程已存在!')
        else:
            if self.var_id.get() != '' and self.var_course_id.get() != '' and self.var_grade.get() != '':
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                args=(self.var_course_id.get())
                sql="SELECT course,credit FROM course_info WHERE course_id=%s"
                cursor.execute(sql,args)
                db.commit()
                results=cursor.fetchall()
                #print(len(results))
                if len(results)==0:
                    messagebox.showinfo('警告！', '课程号没有对应课程')
                    return
                
                for row in results:
                    COURSE=row[0]
                    CREDIT=row[1]
                #print(CREDIT)
                if self.var_course.get()!='' and self.var_course.get()!=COURSE:
                    messagebox.showinfo('警告！', '课程名与课程号不匹配')
                elif self.var_credit.get()!='' and self.var_credit.get()!=CREDIT:
                    messagebox.showinfo('警告！', '课程学分不匹配')
                elif self.var_id.get()!=self.row_info[0]:
                    messagebox.showinfo('警告！', '不能修改学生学号!')
                else:
                    sql = "INSERT INTO stu_grade(stu_id,course_id,grade)\
                    VALUES ('%s','%s','%s')" % (self.var_id.get(), self.var_course_id.get(),self.var_grade.get())
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                        messagebox.showinfo('警告!', '数据库连接失败!')
                        return
                    db.close()

                    self.id.append(self.var_id.get())
                    self.course_id.append(self.var_course_id.get())
                    self.course.append(self.var_course.get())
                    self.credit.append(self.var_credit.get())
                    self.grade.append(self.var_grade.get())
                    self.tree.insert('', len(self.id) - 1, values=(self.id[len(self.id) - 1],self.course_id[len(self.id) - 1],self.course[len(self.id) - 1], self.credit[len(self.id) - 1],self.grade[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写学生数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告!', '是否确定更新学生成绩?')
        if res == True:
            # 保证学号和课程名称与原先一致
            if self.var_id.get() == self.row_info[0] and str(self.var_course.get()) == str(self.row_info[2]) and str(self.var_course_id.get())==str(self.row_info[1]) and str(self.var_credit.get())==str(self.row_info[3]):
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()

                sql = "UPDATE stu_grade SET grade='%s' WHERE stu_id='%s' AND course_id='%s'" % (
                    self.var_grade.get(), self.var_id.get(), self.var_course_id.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    messagebox.showinfo('提示!', '课程成绩 更新成功!')
                except:
                    db.rollback()
                    messagebox.showinfo('提示!', '更新失败!请联系技术人员')
                    return

                db.close()
                id_index = self.id.index(self.row_info[0])
                self.grade[id_index] = self.var_grade.get()

                self.tree.item(self.tree.selection()[0], values=(self.var_id.get(
                ), self.var_course_id.get(), self.var_course.get(),self.var_credit.get(),self.var_grade.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告!', '只能修改成绩项')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选成绩数据?')
        if res == True:
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM stu_grade WHERE course_id = '%s' AND stu_id='%s'" % (
                self.row_info[1],self.row_info[0])  # SQL 语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                return
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.course_id[id_index]
            del self.course[id_index]
            del self.credit[id_index]
            del self.grade[id_index]

            self.tree.delete(self.tree.selection()[0])  # 删除所选行

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口



#课程信息修改类
class AdminManageCourse:
    def __init__(self,parent_window):
        parent_window.destroy()
        self.window=tk.Tk()
        self.window.title("管理员操作界面")

        self.frame_left_top=tk.Frame(width=300,height=240)
        self.frame_right_top = tk.Frame(width=200, height=240)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        self.columns=("课程号","课程名","学分","授课老师","老师工号")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)

        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

         # 表格标题
        self.tree.column("课程号", width=100, anchor='center')
        self.tree.column("课程名", width=150, anchor='center')
        self.tree.column("学分", width=50, anchor='center')
        self.tree.column("授课老师", width=100, anchor='center')
        self.tree.column("老师工号", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

         # 定义存放每个课程各种信息的不同数组
        self.course_id = []
        self.course = []
        self.credit = []
        self.teacher_name = []
        self.teacher_id=[]
         # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql = "SELECT course_id,course,credit,teacher_name,teacher_id FROM course_info NATURAL JOIN teacher_k"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                self.course_id.append(row[0])
                self.course.append(row[1])
                self.credit.append(row[2])
                self.teacher_name.append(row[3])
                self.teacher_id.append(row[4])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')    
            return
        db.close()  # 关闭数据库连接
        #print(self.teacher_id)
        # 写入数据,这里只展示所有信息都完整的课程
        for i in range(min(len(self.course_id), len(self.course), len(self.credit), len(self.teacher_name),len(self.teacher_id))):
            self.tree.insert('', i, values=(self.course_id[i], self.course[i], self.credit[i],self.teacher_name[i],self.teacher_id[i]))

          # 绑定函数，使表头可排序
        for col in self.columns:
            self.tree.heading(col, text=col)

         # 定义顶部区域
        self.top_title = Label(self.frame_left_top,text="课程信息:", font=('微软雅黑', 20))

        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        
        self.var_course_id = StringVar()   # 声明课程号
        self.var_course = StringVar()  # 声明课程名
        self.var_credit = StringVar()   # 声明学分
        self.var_teacher_name = StringVar()  # 声明老师
        self.var_teacher_id = StringVar() #声明工号
        
        # 左上方消息区
        # 课程号
        self.right_top_id_label = Label(
            self.frame_left_top, text="课程号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_course_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 课程名
        self.right_top_name_label = Label(
            self.frame_left_top, text="课程名：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_course, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_gender_label = Label(
            self.frame_left_top, text="学分：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_credit,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 老师工号
        self.right_top_gender_label = Label(
            self.frame_left_top, text="老师工号：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_teacher_id,
                                            font=('微软雅黑', 15))

        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)


        


        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='更新选中的课程信息', width=20, command=self.updata_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='删除选中课程信息', width=20, command=self.del_row)
        self.right_top_button3 = ttk.Button(
            self.frame_right_top, text='新建选中课程信息', width=20, command=self.new_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        AdminSelect(self.window)  # 返回父窗口 销毁本窗口

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            # print(self.col)
            # print(self.row)

            self.row_info = self.tree.item(self.row, "values")

            self.var_course_id.set(self.row_info[0])
            self.var_course.set(self.row_info[1])
            self.var_credit.set(self.row_info[2])
            self.var_teacher_id.set(self.row_info[4])
            self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_course_id, font=('Verdana', 15))
        except:
            print("Log:Invalid operation")
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_course_id.get() == self.row_info[0]:  # 如果所填课程号 与 所选课程号一致
                # 打开数据库连接
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE course_info SET course = '%s', credit = '%s', teacher_id = '%s' \
				 WHERE course_id = '%s'" % (self.var_course.get(), self.var_credit.get(), self.var_teacher_id.get(), self.var_course_id.get())  # SQL 语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                    return
                db.close()  # 关闭数据库连接

                try:
                    db = pymysql.connect("localhost", "root", "123456", "school_database")
                    cursor = db.cursor() 
                    args=(self.var_teacher_id.get())
                    sql="SELECT teacher_name FROM teacher_k WHERE teacher_id=%s"
                    cursor.execute(sql,args)
                    results=cursor.fetchall()
                    db.close() 
                    if(len(results)==0):
                        messagebox.showinfo('警告!', '没有指定定工号的老师!')
                        return
                    
                    id_index = self.course_id.index(self.row_info[0])
                    self.course[id_index] = self.var_course.get()
                    self.credit[id_index] = self.var_credit.get()
                    self.teacher_id[id_index]=self.var_teacher_id.get()
                    self.teacher_name[id_index]=results[0]

                    self.tree.item(self.tree.selection()[0], values=(self.var_course_id.get(), self.var_course.get(),self.var_credit.get(),results[0],self.var_teacher_id.get()))  # 修改对对应行信息
                except:
                    print("error")
                    messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            else:
                messagebox.showinfo('警告！', '不能修改课程号！')
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选课程数据?\n此操作将影响学生课程单.')
        if res == True:
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM course_info WHERE course_id = '%s'" % (
                self.row_info[0])  # SQL 语句
            sql2= "DELETE FROM stu_grade WHERE course_id='%s'"%(self.row_info[0])
            try:
                cursor.execute(sql)  # 执行sql语句
                cursor.execute(sql2)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                return 
            db.close()  # 关闭数据库连接

            id_index = self.course_id.index(self.row_info[0])
            del self.course_id[id_index]
            del self.course[id_index]
            del self.credit[id_index]
            del self.teacher_id[id_index]
            del self.teacher_name[id_index]
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
    def new_row(self):
        if str(self.var_course_id.get()) in self.course_id:
            messagebox.showinfo('警告！', '该课程已存在！')
        else:
            if(self.var_course_id.get()!=''and self.var_course.get()!=''and self.var_credit.get()!=''and self.var_teacher_id.get()!=''):
                db = pymysql.connect("localhost", "root", "123456", "school_database")
                cursor = db.cursor()
                args=(self.var_teacher_id.get())
                sql="SELECT teacher_name FROM teacher_k WHERE teacher_id=%s"
                #print(sql)
                cursor.execute(sql,args)
                results=cursor.fetchall()
                #print(results)
                if(len(results)==0):
                    messagebox.showinfo('警告!', '没有指定定工号的老师!')
                    return
                sql = "INSERT INTO course_info(course_id, course, credit, teacher_id) \
				       VALUES ('%s', '%s', '%s', '%s')" % \
                    (self.var_course_id.get(), self.var_course.get(),
                     self.var_credit.get(), self.var_teacher_id.get())  # SQL 插入语句  
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                    messagebox.showinfo('警告!', '提交失败!')
                    return
                db.close()
                self.course_id.append(self.var_course_id.get())
                self.course.append(self.var_course.get())
                self.credit.append(self.var_credit.get())
                self.teacher_name.append(self.var_teacher_name.get())
                self.teacher_id.append(self.var_teacher_id.get())

                self.tree.insert('', len(self.course_id) - 1, values=(
                        self.course_id[len(self.course_id) - 1], self.course[len(self.course_id) -1], self.credit[len(self.course_id) - 1],
                        results[0],self.teacher_id[len(self.course_id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '新建课程成功!')
            else:
                messagebox.showinfo('警告!','课程信息不全!')
        



# 学生登录界面
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎同学")
        self.window.geometry('500x550')

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='学生登录口', bg='Seashell',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='学生账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        sql="SELECT stu_id FROM student_k"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取获得的行信息,本表两列
        student_id_list = cursor.fetchall()

        # 创建一个下拉列表
        self.student_username = tk.StringVar()
        numberChosen = ttk.Combobox(self.window, width=28, textvariable=self.student_username,font=tkFont.Font(size=14),state="readonly")
        numberChosen['values'] = student_id_list    # 设置下拉列表的值
        numberChosen.pack()# 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值


        Label(self.window, text='学生密码：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员密码输入栏,密码用*显示
        self.student_pass = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass.pack()

        # 登录确定按钮,响应函数调用self.login
        Button(self.window, text="登录", width=8, font=(
            "微软雅黑", 12), command=self.login).pack(side=LEFT,padx=60)
        Button(self.window, text="修改密码", width=8, font=(
            "微软雅黑", 12), command=self.ChangePass).pack(side=RIGHT,padx=60)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack(side=BOTTOM,pady=40)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def login(self):
        student_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        sql = "SELECT * FROM stu_login_k WHERE stu_id='%s'" % (
            self.student_username.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                student_id = row[0]
                student_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.student_pass.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == student_pass:
            print("Log:User log success!")
            StudentSelect(self.window,self.student_username.get())  # 密码正确,调用管理员界面类,进入管理员操作界面
        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def ChangePass(self):
        StudentPassword(self.window)






class StudentPassword:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁父界面

        self.window = tk.Tk()
        self.window.title("欢迎学生")
        self.window.geometry('500x550')

        # 界面仍然使用pack()布局
        label = tk.Label(self.window, text='修改密码', bg='Seashell',
                         font=('微软雅黑', 20), width=50, height=4)
        label.pack()

        Label(self.window, text='学生账号：', font=("微软雅黑", 14)).pack(pady=20)
        # 管理员用户名输入栏
        self.student_username = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        # self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_username.pack()

        Label(self.window, text='原始密码：', font=("微软雅黑", 14)).pack(pady=10)
        # 管理员密码输入栏,密码用*显示
        self.student_pass_old = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass_old.pack()

        Label(self.window, text='修改密码：', font=("微软雅黑", 14)).pack(pady=10)
        self.student_pass_new = tk.Entry(
            self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass_new.pack()


        # 修改确定按钮,响应函数调用self.changepass
        Button(self.window, text="确定修改", width=8, font=(
            "微软雅黑", 12), command=self.changepass).pack(pady=20)
        # 返回按钮,调用self.back
        Button(self.window, text="返回首页", width=8, font=(
            "微软雅黑", 12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    # 登录调用
    def changepass(self):
        student_pass = None

        # 与Mysql数据库建立连接,准备查询管理员账户表
        db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
        cursor = db.cursor()  # 获取操作游标
        '''
        游标（cursor）是系统为用户开设的一个数据缓冲区,
        存放SQL语句的执行结果。每个游标区都有一个名字,
        用户可以用SQL语句逐一从游标中获取记录,并赋给主变量,
        交由主语言进一步处理。
        '''
        # 嵌入SQL语句,从管理员账户信息表中找到和输入框的用户一致的数据
        # self.admin_username.get(),得到username框输入字符串
        sql = "SELECT * FROM stu_login_k WHERE stu_id='%s'" % (
            self.student_username.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取获得的行信息,本表两列
            results = cursor.fetchall()
            for row in results:
                student_id = row[0]
                student_pass = row[1]
        except:
            print("Log:Error: unable to fecth data")
            messagebox.showinfo('对不起!', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')
        db.close()  # 关闭数据库连接

        print("Log:Logging in to administrator Oper interface....")

        # 验证密码哈希值
        password = self.student_pass_old.get()
        new_md5 = hashlib.md5()
        new_md5.update(password.encode('utf-8'))
        if str(new_md5.hexdigest()) == student_pass:
            print("Log:User log success!")
            #AdminSelect(self.window)  # 密码正确,调用管理员界面类,进入管理员操作界面
            password_new=self.student_pass_new.get()
            new_pass=hashlib.md5()
            new_pass.update(password_new.encode('utf-8'))
            new_pass=str(new_pass.hexdigest())
            args=(new_pass,self.student_username.get()) 
            sql="UPDATE stu_login_k SET stu_pass = %s WHERE stu_id = %s"  # SQL 语句
            #print(sql)
            db = pymysql.connect("localhost", "root",
                             "123456", "school_database")  # 打开数据库连接
            cursor = db.cursor()  # 获取操作游标
            try:
                cursor.execute(sql,args)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '密码更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')

        else:
            messagebox.showinfo('对不起', '您的用户名或密码不正确！\n若遗忘请联系技术人员.')

    # 返回调用
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口




class StudentSelect:  #学生选择进入的操作界面
    def __init__(self,parent_window,student_id):
        parent_window.destroy() #销毁上一级界面
        self.window=tk.Tk()
        self.window.title("学生选项")
        self.window.geometry('500x550')
        #print(student_id)

        label = tk.Label(self.window, text='学生操作选项', bg='Seashell',font=('微软雅黑', 20), width=50, height=3)
        label.pack()
        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        Button(self.window, text="查看个人信息", font=("微软雅黑", 14), command=lambda: StudentInfo(self.window,student_id), width=30,fg='white', bg='gray', height=2,activebackground='black', activeforeground='white').pack()
        label_empty2=tk.Label(self.window,text='').pack(pady=5)
        Button(self.window, text="已选课程信息或撤课", font=("微软雅黑", 14), command=lambda: StudentGrade(self.window,student_id), width=30, fg='white', bg='gray', height=2,activebackground='black', activeforeground='white').pack()
        label_empty3=tk.Label(self.window,text='').pack(pady=5)
        Button(self.window, text="在线选课", font=("微软雅黑", 14), command=lambda: StudentSelectCourse(self.window,student_id), width=30,fg='white', bg='gray',height=2, activebackground='black', activeforeground='white').pack()

        Button(self.window,width=10,text="返回主界面",font=("微软雅黑",12),command=self.back).pack(padx=65,pady=40)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()  # 主消息循环
    
    def back(self):
        StartPage(self.window)


class StudentInfo:
    def __init__(self, parent_window, student_id):
        parent_window.destroy() # 销毁主界面
        id=student_id
        self.target_stu_id=id
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生个人信息查看')
        self.window.geometry('500x550')  # 这里的乘是小x
        label = tk.Label(self.window, text='学生信息查看', bg='Seashell', font=('微软雅黑', 20), width=50, height=4)
        label.pack()
        label_empty1=tk.Label(self.window,text='').pack(pady=10)
        self.id = ''
        self.name = ''
        self.gender = ''
        self.age = ''
        self.dept=''
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()# 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_k WHERE stu_id = '%s'" % (student_id) # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '学号:  ' + row[0]
                self.name = '姓名:  ' + row[1]
                self.gender = '性别:  ' + row[2]
                self.age = '年龄:  ' + row[3]
                self.dept='学院:  '+row[4]
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            return
        db.close()		# 关闭数据库连接
 
        Label(self.window, text=self.id, font=('微软雅黑', 18)).pack(pady=5)
        Label(self.window, text=self.name, font=('微软雅黑', 18)).pack(pady=5)
        Label(self.window, text=self.gender, font=('微软雅黑', 18)).pack(pady=5)
        Label(self.window, text=self.age, font=('微软雅黑', 18)).pack(pady=5)
        Label(self.window, text=self.dept, font=('微软雅黑', 18)).pack(pady=5)

        Button(self.window, text="返回上一级", width=8, font=('微软雅黑', 12), command=self.back).pack(pady=40)
 
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
 
    def back(self):
        StudentSelect(self.window,self.target_stu_id)  # 显示主窗口 销毁本窗口




#学生查看个人成绩
class StudentGrade:
    def __init__(self,parent_window,target_stu_id):
        id = target_stu_id
        id = str(id)
        #print(id)
        self.target_stu_id=id
        parent_window.destroy()
        self.window = Tk()
        self.window.title('学生课程成绩')

        self.frame_left_top = tk.Frame(width=300, height=220)
        self.frame_right_top = tk.Frame(width=200, height=220)
        self.frame_center = tk.Frame(width=550, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "课程号", "课程","学分","成绩")
        self.tree = ttk.Treeview(
            self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(
            self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格标题
        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("课程号", width=100, anchor='center')
        self.tree.column("课程", width=150, anchor='center')
        self.tree.column("学分", width=50, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.course_id=[]
        self.course = []
        self.credit = []
        self.grade = []

        # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()

        sql = "SELECT stu_id,course_id,course,credit,grade FROM stu_grade NATURAL JOIN course_info WHERE stu_id = '%s'" % (id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取查询结果列表
            results = cursor.fetchall()
            for row in results:  # 对
                self.id.append(row[0])
                self.course_id.append(row[1])
                self.course.append(row[2])
                self.credit.append(row[3])
                self.grade.append(row[4])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            return
        db.close()  # 关闭数据库连接
        # 写入数据,这里只展示所有信息都完整的学生
        for i in range(min(len(self.id), len(self.credit), len(self.course), len(self.grade),len(self.course_id))):
            self.tree.insert('', i, values=(
                self.id[i], self.course_id[i],self.course[i] ,self.credit[i],self.grade[i]))
        
        if min(len(self.id), len(self.credit), len(self.course), len(self.grade),len(self.course_id))==0:
            self.tree.insert('', 0, values=(id,'','','',''))
        
        for col in self.columns:  # 绑定函数
            self.tree.heading(col, text=col)

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top,
                               text="学生成绩信息:", font=('微软雅黑', 20))
        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,
                            sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()   # 声明学号
        self.var_course_id=StringVar()  #声明课程号
        self.var_course = StringVar()   # 声明课程名
        self.var_credit = StringVar()  # 声明学分
        self.var_grade = StringVar()  # 声明年龄

        # 左上方消息区
        # 学号
        self.right_top_id_label = Label(
            self.frame_left_top, text="学号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 课程号
        self.right_top_name_label = Label(
            self.frame_left_top, text="课程号：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_course_id, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 课程
        self.right_top_gender_label = Label(
            self.frame_left_top, text="课程：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_course,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学分
        self.right_top_gender_label = Label(
            self.frame_left_top, text="学分：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(
            self.frame_left_top, textvariable=self.var_credit, font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        #成绩
        self.right_top_gender_label = Label(
            self.frame_left_top, text="成绩：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(
            self.frame_left_top, textvariable=self.var_grade, font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=5, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='撤课', width=20, command=self.del_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='返回上一级', width=20, command=self.back)
        

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(
            row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    # 返回调用

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            self.row_info = self.tree.item(self.row, "values")
            self.var_id.set(self.row_info[0])
            self.var_course_id.set(self.row_info[1])
            self.var_course.set(self.row_info[2])
            self.var_credit.set(self.row_info[3])
            self.var_grade.set(self.row_info[4])
            self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        except:
            print("Log:Invalid operation")
    def back(self):
        #print(self.target_stu_id)
        StudentSelect(self.window,self.target_stu_id)
        

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否确定撤课?')
        if res == True:
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            args=(self.row_info[1],str(self.target_stu_id))
            sql= "DELETE FROM stu_grade WHERE course_id=%s AND stu_id=%s"
            #print(sql)
            if len(str(self.row_info[4]))<=3 and len(str(self.row_info[4]))>=1:
                messagebox.showinfo('警告！', '撤课失败,已出成绩的课程无法撤课!')
                return
            try:
                cursor.execute(sql,args)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '撤课成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '撤课失败,数据库连接失败！')
                return
            db.close()  # 关闭数据库连接
            id_index = self.course_id.index(self.row_info[1])
            del self.id[id_index]
            del self.course_id[id_index]
            del self.course[id_index]
            del self.credit[id_index]
            del self.grade[id_index]
            #del self.teacher[id_index]
            self.tree.delete(self.tree.selection()[0])  # 删除所选行




#课程信息修改类
class StudentSelectCourse:
    def __init__(self,parent_window,target_stu_id):
        id=str(target_stu_id)
        self.target_stu_id=id
        parent_window.destroy()
        self.window=tk.Tk()
        self.window.title("学生选课界面")

        self.frame_left_top=tk.Frame(width=300,height=200)
        self.frame_right_top = tk.Frame(width=200, height=240)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        self.columns=("课程号","课程名","学分","授课老师")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)

        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

         # 表格标题
        self.tree.column("课程号", width=100, anchor='center')
        self.tree.column("课程名", width=150, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("授课老师", width=150, anchor='center')

        
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

         # 定义存放每个课程各种信息的不同数组
        self.course_id = []
        self.course = []
        self.credit = []
        self.teacher = []

         # 连接数据库
        db = pymysql.connect("localhost", "root", "123456", "school_database")
        cursor = db.cursor()
        sql = "SELECT course_id,course,credit,teacher_name FROM course_info NATURAL JOIN teacher_k"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                self.course_id.append(row[0])
                self.course.append(row[1])
                self.credit.append(row[2])
                self.teacher.append(row[3])
        except:
            print("Log:Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！') 
            return   
        db.close()  # 关闭数据库连接

        # 写入数据,这里只展示所有信息都完整的课程
        for i in range(min(len(self.course_id), len(self.course), len(self.credit), len(self.teacher))):
            self.tree.insert('', i, values=(self.course_id[i], self.course[i], self.credit[i], self.teacher[i]))

          # 绑定函数，使表头可排序
        for col in self.columns:
            self.tree.heading(col, text=col)

         # 定义顶部区域
        self.top_title = Label(self.frame_left_top,text="课程信息:", font=('微软雅黑', 20))

        # 定义左上方区域单个学生具体信息显示
        self.top_title.grid(row=0, column=0, columnspan=2,sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_course_id = StringVar()   # 声明课程号
        self.var_course = StringVar()  # 声明课程名
        self.var_credit = StringVar()   # 声明学分
        self.var_teacher = StringVar()  # 声明老师

        # 左上方消息区
        # 课程号
        self.right_top_id_label = Label(
            self.frame_left_top, text="课程号：", font=('微软雅黑', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_course_id, font=('微软雅黑', 15))
        self.right_top_id_label.grid(row=1, column=0)   # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)  # 可输入栏在1号列
        # 课程名
        self.right_top_name_label = Label(
            self.frame_left_top, text="课程名：", font=('微软雅黑', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_course, font=('微软雅黑', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_gender_label = Label(
            self.frame_left_top, text="学分：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_credit,
                                            font=('微软雅黑', 15))
        self.right_top_gender_label.grid(row=3, column=0)   # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 老师
        self.right_top_gender_label = Label(
            self.frame_left_top, text="授课老师：", font=('微软雅黑', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_teacher,
                                            font=('微软雅黑', 15))

        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

         # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('微软雅黑', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='选课', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(
            self.frame_right_top, text='返回上一级', width=20, command=self.back)
        
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        AdminSelect(self.window)  # 返回父窗口 销毁本窗口

    def click(self, event):
        try:
            self.col = self.tree.identify_column(event.x)  # 列
            self.row = self.tree.identify_row(event.y)  # 行
            # print(self.col)
            # print(self.row)

            self.row_info = self.tree.item(self.row, "values")

            self.var_course_id.set(self.row_info[0])
            self.var_course.set(self.row_info[1])
            self.var_credit.set(self.row_info[2])
            self.var_teacher.set(self.row_info[3])
            self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_course_id, font=('Verdana', 15))
        except:
            print("Log:Invalid operation")
    
    def new_row(self):
        res = messagebox.askyesnocancel('警告！', '是否确定选课?')
        if res==True:
            self.course_selected=[]
            db = pymysql.connect("localhost", "root", "123456", "school_database")
            cursor = db.cursor()
            args=(self.target_stu_id)
            sql="SELECT course_id FROM stu_grade WHERE stu_id=%s"
            try:
                cursor.execute(sql,args)
                results=cursor.fetchall()
                for row in results:
                    self.course_selected.append(row[0])
            except:
                print("Log:Error: unable to fetch data")
                messagebox.showinfo('警告！', '数据库连接失败！')  
                return
            if str(self.var_course_id.get()) in self.course_selected:
                messagebox.showinfo('警告！', '该课程已选！')
            else:
                if(self.var_course_id!=''):
                    sql = "INSERT INTO stu_grade(stu_id, course_id, grade) \
                        VALUES ('%s', '%s', '%s')" % \
                        (self.target_stu_id,self.var_course_id.get(), 'NULL')  # SQL 插入语句  
                    #print(sql)
                    try:
                        cursor.execute(sql)
                        db.commit()
                        messagebox.showinfo('提示！', '选课成功!')
                    except:
                        db.rollback()
                        messagebox.showinfo('警告!', '选课失败!')
                        return
                    db.close()
                else:
                    messagebox('警告!','课程信息不全!')
    def back(self):
        StudentSelect(self.window,self.target_stu_id)

# About页面
class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy() # 销毁主界面
 
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        self.window.geometry('500x550')  # 这里的乘是小x
 
        label = tk.Label(self.window, text='武汉大学学生信息管理系统', bg='AliceBlue', font=("微软雅黑", 20), width=50, height=4)
        label.pack()
        img_gif = PhotoImage(file = 'author.gif')
        img=Label(self.window, image = img_gif)
        img.pack(pady=20)
        Label(self.window, text='作者：Aaron-沈思源', font=("微软雅黑", 18)).pack(pady=15)
		
		
        Label(self.window, text='(。・∀・)ノ', font=("微软雅黑", 18)).pack(pady=20)
		
 
        Button(self.window, text="返回首页", width=8, font=("微软雅黑", 12), command=self.back).pack(pady=20)
		
		
		
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口





if __name__ == '__main__':
    try:
        # 打开数据库连接 连接测试
        db = pymysql.connect("localhost", "root", "123456", "students")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 如果数据表不存在则创建表 若存在则跳过
        # 设置主键唯一
        sql = """CREATE TABLE IF NOT EXISTS student_k(
                    id char(20) NOT NULL,
                    name char(20) default NULL,
                    gender char(5) default NULL,  
                    age char(5) default NULL,
                    PRIMARY KEY (id)

                    ) ENGINE = InnoDB 
                    DEFAULT	CHARSET = utf8
                    """
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS admin_login_k(
                            admin_id char(20) NOT NULL,
                            admin_pass char(35) default NULL,
                            PRIMARY KEY (admin_id)
                            ) ENGINE = InnoDB 
                            DEFAULT	CHARSET = utf8
                            """
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS stu_login_k(
                            stu_id char(20) NOT NULL,
                            stu_pass char(35) default NULL,
                            PRIMARY KEY (stu_id)
                            ) ENGINE = InnoDB 
                            DEFAULT	CHARSET = utf8
                            """
        cursor.execute(sql)

        # 关闭数据库连接
        db.close()

        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！！')
