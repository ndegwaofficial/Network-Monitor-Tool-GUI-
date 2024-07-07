import tkinter as tk
from tkinter import scrolledtext
from network_monitor import NetworkMonitor

class NetworkMonitorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor Tool")
        
        self.text_area = scrolledtext.ScrolledText(root, width=100, height=30)
        self.text_area.pack()
        
        self.monitor = NetworkMonitor()
        
        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack()
        
    def start_monitoring(self):
        self.monitor.discover_devices()
        self.monitor.start_monitoring()

if __name__ == "__main__":
    root = tk.Tk()
    gui = NetworkMonitorGUI(root)
    root.mainloop()
