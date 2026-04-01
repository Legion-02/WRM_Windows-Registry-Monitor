import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

import config
from baseline import create_baseline
from monitor import monitor


class RegistryMonitorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Registry Monitor GUI")
        self.root.geometry("980x680")
        self.root.minsize(900, 620)

        self.monitor_thread = None
        self.stop_event = threading.Event()

        self.status_var = tk.StringVar(value="Ready")
        self.interval_var = tk.StringVar(value=str(config.POLL_INTERVAL))

        self.build_ui()

    def build_ui(self):
        top_frame = ttk.Frame(self.root, padding=12)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Polling Interval (seconds):").grid(row=0, column=0, sticky="w", padx=(0, 8))
        ttk.Entry(top_frame, width=10, textvariable=self.interval_var).grid(row=0, column=1, sticky="w")

        ttk.Button(top_frame, text="Create Baseline", command=self.create_baseline_action).grid(row=0, column=2, padx=8)
        ttk.Button(top_frame, text="Start Monitoring", command=self.start_monitoring).grid(row=0, column=3, padx=8)
        ttk.Button(top_frame, text="Stop Monitoring", command=self.stop_monitoring).grid(row=0, column=4, padx=8)
        ttk.Button(top_frame, text="Open Logs", command=self.open_logs).grid(row=0, column=5, padx=8)
        ttk.Button(top_frame, text="Clear Screen", command=self.clear_output).grid(row=0, column=6, padx=8)

        info_frame = ttk.LabelFrame(self.root, text="Monitored Registry Paths", padding=12)
        info_frame.pack(fill="x", padx=12, pady=(0, 10))

        monitored_text = "\n".join([f"• {path}" for path in config.MONITORED_KEYS])
        ttk.Label(info_frame, text=monitored_text, justify="left").pack(anchor="w")

        output_frame = ttk.LabelFrame(self.root, text="Live Output", padding=12)
        output_frame.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        self.output_box = scrolledtext.ScrolledText(output_frame, wrap="word", font=("Consolas", 10))
        self.output_box.pack(fill="both", expand=True)

        status_bar = ttk.Label(self.root, textvariable=self.status_var, anchor="w", relief="sunken", padding=(10, 6))
        status_bar.pack(fill="x", side="bottom")

    def append_output(self, message):
        self.output_box.insert("end", message + ("" if message.endswith("\n") else "\n"))
        self.output_box.see("end")

    def safe_append_output(self, message):
        self.root.after(0, lambda: self.append_output(message))

    def safe_set_status(self, message):
        self.root.after(0, lambda: self.status_var.set(message))
        self.root.after(0, lambda: self.append_output(message))

    def create_baseline_action(self):
        try:
            value = int(self.interval_var.get().strip())
            if value < 1:
                raise ValueError
            config.POLL_INTERVAL = value
        except ValueError:
            messagebox.showerror("Invalid Input", "Polling interval must be a positive number.")
            return

        try:
            create_baseline(config)
            self.status_var.set("Baseline created successfully.")
            self.append_output("Baseline created successfully.")
            messagebox.showinfo("Success", "baseline.json created successfully.")
        except PermissionError:
            messagebox.showerror("Permission Error", "Run this application as Administrator.")
        except Exception as exc:
            messagebox.showerror("Error", f"Failed to create baseline: {exc}")

    def start_monitoring(self):
        if self.monitor_thread and self.monitor_thread.is_alive():
            messagebox.showinfo("Already Running", "Monitoring is already running.")
            return

        if not os.path.exists("baseline.json"):
            messagebox.showwarning("Missing Baseline", "Please create baseline first.")
            return

        try:
            value = int(self.interval_var.get().strip())
            if value < 1:
                raise ValueError
            config.POLL_INTERVAL = value
        except ValueError:
            messagebox.showerror("Invalid Input", "Polling interval must be a positive number.")
            return

        self.stop_event = threading.Event()
        self.monitor_thread = threading.Thread(
            target=monitor,
            kwargs={
                "status_callback": self.safe_set_status,
                "log_callback": self.safe_append_output,
                "stop_event": self.stop_event,
            },
            daemon=True,
        )
        self.monitor_thread.start()
        self.status_var.set("Monitoring started.")

    def stop_monitoring(self):
        if self.monitor_thread and self.monitor_thread.is_alive():
            self.stop_event.set()
            self.status_var.set("Stopping monitor...")
        else:
            self.status_var.set("Monitor is not running.")

    def open_logs(self):
        log_path = os.path.abspath("logs.txt")
        if not os.path.exists(log_path):
            messagebox.showinfo("Logs", "logs.txt not found yet.")
            return
        filedialog.askopenfilename(initialdir=os.path.dirname(log_path), initialfile="logs.txt")
        os.startfile(log_path)

    def clear_output(self):
        self.output_box.delete("1.0", "end")


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    try:
        style.theme_use("vista")
    except Exception:
        pass
    app = RegistryMonitorGUI(root)
    root.mainloop()
