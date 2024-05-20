# Subnet Calcolator
Python script that calculate the subnet details based on the provided Ip Address and the Prefix.

## It Determines The Following:
- The subnet address
- The first and last host addresses
- The broadcast address
- The next subnet address

## Usage
To use the script, run the following command in your terminal inside the directory of the script:
```bash
python3 subnetcalc.py <IP_ADDRESS>/<PREFIX> <OPTION>
```
### Options (Optional):
- addr             - Display the network address of the subnet.
- netMask          - Display the subnet mask of the subnet.
- nextAddr         - Display the next subnet address.
- firstHost        - Display the first usable host address in the subnet.
- lastHost         - Display the last usable host address in the subnet.
- broadcast        - Display the broadcast address of the subnet.


### Example Output For 192.168.0.1/24
```bash

  =======================================
  |      Name      |      Address       |
  +----------------+--------------------+
  |     Subnet     |    192.168.0.0     |
  |  Subnet Mask   |   255.255.255.0    |
  |   First Host   |    192.168.0.1     |
  |   Last Host    |   192.168.0.254    |
  |   Broadcast    |   192.168.0.255    |
  |  Next subnet   |    192.168.1.0     |
  +----------------+--------------------+

```

## Requirements
Python 3.7 and above.

## Installation
clone the repo:
```bash
git clone https://github.com/James-R997/Subnet-Calculator.git
```
