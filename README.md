# Port Scanner

## Overview
**Port Scanner** is a Python-based network reconnaissance tool that allows users to scan a target host for open TCP ports within the range of 1-1024 (well-known ports). This tool is designed for educational purposes, network diagnostics, and security assessments.

## Features

### Core Functionality
- **Host Resolution**: Automatically resolves domain names to IP addresses
- **Port Range Scanning**: Scans ports 1 through 1024 (configurable)
- **Timeout Management**: Configurable connection timeout (default: 0.5 seconds)
- **Error Handling**: Comprehensive error handling for network issues
- **Performance Metrics**: Measures and displays total scan duration

### User-Friendly Features
- **Simple Interface**: Easy-to-use command-line interface
- **Real-time Feedback**: Shows open ports as they're discovered
- **Graceful Exit**: Handles Ctrl+C interrupts properly
- **Detailed Logging**: Provides timestamps and scan progress information

## Requirements

### Prerequisites
- Python 3.6 or higher
- Network connectivity
- Appropriate permissions for socket operations

### Dependencies
The tool uses only Python standard libraries:
- `socket` - For network connections
- `sys` - For system-level operations
- `datetime` - For timing and timestamping

No additional packages need to be installed.

## Installation

### Method 1: Direct Download
```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

### Method 2: Manual Setup
1. Download the `port_scanner.py` file
2. Ensure Python is installed on your system
3. Verify installation:
   ```bash
   python --version
   ```

## Usage

### Basic Usage
Run the script from the command line:
```bash
python port_scanner.py
```

### Interactive Mode
1. Launch the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target when prompted:
   ```
   Enter a remote host to scan (IP or URL): example.com
   ```
   or
   ```
   Enter a remote host to scan (IP or URL): 192.168.1.1
   ```

### Example Output
```
------------------------------------------------------------
Enter a remote host to scan (IP or URL): example.com
------------------------------------------------------------
Scanning remote host: 93.184.216.34
Scanning started at: 2024-01-15 14:30:00.123456
------------------------------------------------------------
Port 80: Open
Port 443: Open
Scanning Complete in: 0:01:45.678901
```

## Configuration

### Modifying Scan Parameters
Edit the `port_scanner.py` file to customize:

1. **Port Range**: Change line 30
   ```python
   for port in range(1, 1025):  # Change to range(1, 100) for fewer ports
   ```

2. **Timeout Settings**: Change line 33
   ```python
   sock.settimeout(0.5)  # Increase for slower networks, decrease for faster scans
   ```

### Common Modifications

#### Scan Specific Ports
```python
# Replace line 30 with:
ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]
for port in ports_to_scan:
```

#### Faster Scanning (Reduced Timeout)
```python
# Change line 33 to:
sock.settimeout(0.1)  # More aggressive, may miss open ports on slow networks
```

## Technical Details

### How It Works
1. **Host Resolution**: Uses `socket.gethostbyname()` to convert domain names to IP addresses
2. **TCP Handshake**: Attempts a TCP three-way handshake on each port
3. **Result Interpretation**:
   - `connect_ex()` returns 0: Port is open and accepting connections
   - `connect_ex()` returns error code: Port is closed/filtered
4. **Timeout Handling**: Abandons connection attempts after specified timeout

### Port Range Explained
- **Ports 1-1024**: Well-known ports (standard services)
- Common ports scanned:
  - 21: FTP
  - 22: SSH
  - 23: Telnet
  - 25: SMTP
  - 53: DNS
  - 80: HTTP
  - 443: HTTPS

## Limitations

### Technical Constraints
- **Single-threaded**: Scans ports sequentially (can be slow for full range)
- **TCP Only**: Only scans TCP ports, not UDP
- **No Service Detection**: Identifies open ports but not services running
- **Basic Stealth**: Uses full TCP handshake (easily detectable by IDS)

### Performance Notes
- Scanning all 1024 ports takes approximately 8-10 minutes (with 0.5s timeout)
- Time increases linearly with more ports or longer timeouts
- Network latency significantly affects scan duration

## Security and Legal Considerations

### Important Disclaimer
**WARNING**

1. **Legal Use Only**: Only scan systems you own or have explicit permission to test
2. **Educational Purpose**: This tool is for learning and authorized security assessments
3. **Potential Consequences**: Unauthorized scanning may result in:
   - Legal action
   - Network blocking
   - Account termination by ISP
   - Civil or criminal penalties

### Common Issues

#### "Hostname could not be resolved"
- Check internet connectivity
- Verify the hostname/URL is correct
- Ensure DNS is working properly

#### "Couldn't connect to server"
- Target host may be offline
- Firewall may be blocking connections
- Network configuration issues

#### Slow Scanning
- Increase timeout value
- Reduce port range
- Check network speed and latency

#### Permission Errors
- On Linux/macOS, ports below 1024 may require sudo
- Run with appropriate privileges if needed

### Debug Mode
Add debug print statements to line 34:
```python
print(f"Testing port {port}...")  # Add this line for debugging
result = sock.connect_ex((remote_server_ip, port))
```

## Future Enhancements

### Planned Features
1. **Multi-threading**: Parallel scanning for faster results
2. **Service Detection**: Banner grabbing to identify running services
3. **UDP Scanning**: Support for UDP port scanning
4. **Save Results**: Export scan results to file (CSV, JSON, TXT)
5. **Custom Port Lists**: Import/export port lists for scanning

### Advanced Features Under Consideration
- Stealth scanning techniques (SYN, FIN, XMAS scans)
- OS fingerprinting
- Vulnerability correlation
- Graphical user interface (GUI)
- Scheduled scanning
- Comparison with previous scans

## Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Areas Needing Improvement
- Code optimization
- Additional scanning techniques
- Better error handling
- Enhanced reporting features
- Documentation improvements
- 
