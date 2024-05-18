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
python3 subnetcalc.py <IP_ADDRESS>/<PREFIX>
```

### Example Output For 192.168.0.1/24
```bash

  Subnet Mask (base 2)---------->   11111111111111111111111111111000
  Subnet Mask (base 10)--------->   255.255.255.248
  Subnet Address---------------->   192.168.0.0
  First Host Address------------>   192.168.0.1
  Last Host Address------------->   192.168.0.6
  Broadcast Address------------->   192.168.0.7
  Next subnet Address----------->   192.168.0.8

```

## Requirements
Python 3.x

## Installation
clone the repo:
```bash
git clone https://github.com/James-R997/Subnet-Calculator.git
```