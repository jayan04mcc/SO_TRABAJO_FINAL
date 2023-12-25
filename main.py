import psutil
import tkinter as tk
from tkinter import ttk


def get_process_info():
    process_info = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent','create_time']):
        try:
            process_info.append({
                'pid': process.info['pid'],
                'name': process.info['name'],
                'cpu_percent': process.info['cpu_percent'],
                'memory_percent': process.info['memory_percent'],
                'create_time':process.info['create_time'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_info

def update_process_info():
    process_info = get_process_info()
    tree.delete(*tree.get_children())
    for process in process_info:
        tree.insert('', 'end', values=(process['pid'], process['name'], process['cpu_percent'], process['memory_percent'],process['create_time']))

    root.after(1000, update_process_info)

root = tk.Tk()
root.title("Proceso Monitor")

tree = ttk.Treeview(root, columns=('PID', 'Name', 'CPU %', 'Memory %','time'))
tree.heading('#0', text='PID')
tree.heading('#1', text='Name')
tree.heading('#2', text='CPU %')
tree.heading('#3', text='Memory %')
tree.heading('#4', text='time %')
tree.pack(expand=True, fill='both')

root.after(1000, update_process_info)

root.mainloop()
