import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress

def validate_ip(ip_address):
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ipaddress.AddressValueError:
        return False

def validate_cidr(cidr):
    try:
        cidr = int(cidr)
        return 0 <= cidr <= 32
    except ValueError:
        return False

def calculate_subnet():
    ip_address = entry_ip.get()
    cidr = entry_cidr.get()

    if not validate_ip(ip_address):
        messagebox.showerror("Error", "Invalid IP address.")
        return

    if not validate_cidr(cidr):
        messagebox.showerror("Error", "Invalid CIDR. It must be between 0 and 32.")
        return

    try:
        ip_network = ipaddress.IPv4Network(f"{ip_address}/{cidr}", strict=False)
        subnet_details = [
            f"Network Address:\t{ip_network.network_address}",
            f"Broadcast Address:\t{ip_network.broadcast_address}",
            f"First Usable IP:\t{ip_network.network_address + 1}",
            f"Last Usable IP:\t{ip_network.broadcast_address - 1}",
            f"Available Hosts:\t{ip_network.num_addresses - 2}",
            f"Mask:\t\t{ip_network.netmask}",
        ]

        # Update the label_subnet_details text
        result_text = "\n".join(subnet_details)
        label_subnet_details.config(text=result_text)

        # Resize the window to fit the content and add a small extension for binary IP display
        window.geometry(f"{window_width+50}x{300 + label_subnet_details.winfo_reqheight()}")

    except ipaddress.NetmaskValueError:
        messagebox.showerror("Error", "Invalid CIDR value. CIDR must be between 0 and 32.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
window = tk.Tk()
window.title("Simple Subnet Calculator")

# Small initial window size
window_width = 300
window_height = 150
window.geometry(f"{window_width}x{window_height}")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

frame = ttk.Frame(window, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

label_ip = ttk.Label(frame, text="IP Address:")
label_ip.grid(row=0, column=0, padx=5, pady=5)

entry_ip = ttk.Entry(frame)
entry_ip.grid(row=0, column=1, padx=5, pady=5)

label_cidr = ttk.Label(frame, text="CIDR:")
label_cidr.grid(row=1, column=0, padx=5, pady=5)

entry_cidr = ttk.Entry(frame)
entry_cidr.grid(row=1, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate_subnet)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Create a label to display the subnet details
label_subnet_details = ttk.Label(window, anchor=tk.W, justify=tk.LEFT, wraplength=window_width - 40)
label_subnet_details.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

window.mainloop()
