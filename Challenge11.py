#!/usr/bin/python3

import psutil

# Fetch the required system information
user_time = psutil.cpu_times().user
kernel_time = psutil.cpu_times().system
idle_time = psutil.cpu_times().idle
priority_user_time = psutil.cpu_times().nice
io_wait_time = psutil.cpu_times().iowait
hardware_interrupt_time = psutil.cpu_times().irq
software_interrupt_time = psutil.cpu_times().softirq
virtual_system_time = psutil.cpu_times().steal
guest_time = psutil.cpu_times().guest

# Save the information to a text file
with open("system_info.txt", "w") as f:
    f.write(f"Time spent by normal processes executing in user mode: {user_time}\n")
    f.write(f"Time spent by processes executing in kernel mode: {kernel_time}\n")
    f.write(f"Time when system was idle: {idle_time}\n")
    f.write(f"Time spent by priority processes executing in user mode: {priority_user_time}\n")
    f.write(f"Time spent waiting for I/O to complete: {io_wait_time}\n")
    f.write(f"Time spent for servicing hardware interrupts: {hardware_interrupt_time}\n")
    f.write(f"Time spent for servicing software interrupts: {software_interrupt_time}\n")
    f.write(f"Time spent by other operating systems running in a virtualized environment: {virtual_system_time}\n")
    f.write(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {guest_time}\n")

