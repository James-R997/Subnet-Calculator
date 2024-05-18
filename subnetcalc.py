from networking_classes import Subnet, IPv4
import sys
from colorama import Fore, init

def main():

    init()

    helpMsg : str = f'''

        {Fore.LIGHTWHITE_EX}subnetcalc {Fore.WHITE}- your handy subnet calculator.
{Fore.LIGHTBLACK_EX}
    Usage    : 
        - python3 subnetcalc.py [ipaddress]/[prefix]

    Examples : 
        - python3 subnetcalc.py 192.168.0.1/27
        - python3 subnetcalc.py 110.111.69.223/19
        - python3 subnetcalc.py 13.194.89.93/10

    '''

    if len( sys.argv ) == 2 : # making sure the user didnt add more than one argument

        address : str = sys.argv[1] # getting the argument
    
        if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
            print(helpMsg)

        else:       # if the address provided by the user Valid
            IPPrefix   : list[ str ]      = address.split("/") # making sure it has two values seperated by the /
            
            print("") # adding new line to prettify the output

            subnetInfo : dict[ str, str ] = Subnet.getEverything(IPPrefix[0], int(IPPrefix[1])) # getting all of the information about the subnet based on the Ip address and Prefix (as a dictionary)
            
            for key, val in subnetInfo.items():
                print(f"{Fore.LIGHTBLACK_EX}  {key:-<25}----->   {Fore.WHITE}{val}") # to print out all of the information about the subnet in pretty format
            print("") # adding new line to prettify the output
    else:
        print(helpMsg)

if __name__ == "__main__" :
    main()