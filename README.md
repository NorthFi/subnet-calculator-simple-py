# 🌐 Simple Subnet Calculator

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

*A sleek, intuitive GUI application for network subnet calculations*

[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Screenshots](#-screenshots) •
[Contributing](#-contributing)

</div>

---

## 🚀 Features

- **🎯 Precise Calculations**: Instantly calculate network address, broadcast address, and usable IP ranges
- **✨ Clean Interface**: Modern tkinter GUI with intuitive design
- **⚡ Real-time Validation**: Input validation with helpful error messages
- **🔢 Complete Network Info**: Shows subnet mask, host count, and all essential network details
- **📱 Responsive Design**: Auto-resizing window that adapts to content
- **🛡️ Error Handling**: Robust validation for IP addresses and CIDR notation

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/NorthFi/subnet-calculator-simple-py.git

# Navigate to the project directory
cd subnet-calculator-simple-py

# Run the application
python subnet_calculator.py
```

No additional dependencies required! The application uses only Python standard library modules.

## 🎮 Usage

1. **Launch the application**
   ```bash
   python subnet_calculator.py
   ```

2. **Enter network details**
   - Input any valid IPv4 address (e.g., `192.168.1.100`)
   - Enter CIDR notation (e.g., `24` for /24 subnet)

3. **Calculate and view results**
   - Click "Calculate" to see comprehensive subnet information
   - View network address, broadcast address, usable IP range, and more

### Example Calculations

| Input | CIDR | Network Address | Broadcast Address | Usable IPs | Hosts |
|-------|------|----------------|-------------------|------------|-------|
| 192.168.1.100 | 24 | 192.168.1.0 | 192.168.1.255 | 192.168.1.1 - 192.168.1.254 | 254 |
| 10.0.0.50 | 16 | 10.0.0.0 | 10.0.255.255 | 10.0.0.1 - 10.0.255.254 | 65534 |
| 172.16.5.10 | 28 | 172.16.5.0 | 172.16.5.15 | 172.16.5.1 - 172.16.5.14 | 14 |

## 🖼️ Screenshots

*Add your screenshots here showing the application in action*

## 🏗️ Technical Details

### Architecture
- **GUI Framework**: tkinter with ttk styling
- **Network Calculations**: Python's `ipaddress` module
- **Input Validation**: Custom validation functions for IP and CIDR
- **Error Handling**: Comprehensive exception handling with user-friendly messages

### Key Components
- `validate_ip()`: IPv4 address validation
- `validate_cidr()`: CIDR notation validation (0-32)
- `calculate_subnet()`: Core subnet calculation logic
- Dynamic window resizing for optimal user experience

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Ideas for Contributions
- 🌟 Add IPv6 support
- 🎨 Implement dark mode theme
- 📊 Add subnet visualization
- 💾 Save/load subnet configurations
- 🔄 Subnet splitting/merging tools
- 📱 Mobile-responsive design

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's powerful `ipaddress` module
- Inspired by the need for quick network calculations
- Thanks to all contributors and users

---

<div align="center">

**Made with ❤️ for network engineers and IT professionals**

*Star ⭐ this repository if you find it helpful!*

</div>
