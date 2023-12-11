## README.md

**Simple Port Scanner**

This script scans a given host for open ports using Python's `socket` library.

**Features:**

* Scans a range of ports (default: 1-65000, customizable)
* Checks for TCP connections
* Identifies open ports and displays their numbers
* Easy-to-use and understand

**Requirements:**

* Python 3.x
* `socket` library (included in the standard library)

**Usage:**

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:

```
python port_scanner.py
```

**Options:**

* You can specify the host IP address or hostname as an argument:

```
python port_scanner.py 192.168.1.10
```

* You can customize the port range by modifying the `range(1, 65000)` line in the script.

**Output:**

The script will print a list of open ports, with the following format:

```
<port number> is open!
```

For example:

```
22 is open!
80 is open!
443 is open!
```

**Disclaimer:**

Please use this script responsibly and only on machines you have permission to scan. Port scanning without authorization may be illegal in some jurisdictions.

**Additional notes:**

* This script is a basic example and can be further improved by adding features like service identification and banner grabbing.
* You can adjust the port range to focus on specific services or applications.

**Please feel free to contribute to this script by reporting bugs or suggesting improvements.**
