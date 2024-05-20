from networking_classes import Subnet, IPv4
from sys import argv

def main():

    helpMsg : str = f'''
        subnetcalc - Your Handy Subnet Calculator.

    Usage: python3 subnetcalc.py [ipaddress/prefix] [option]

    Options (optional):
        addr             - Display the network address of the subnet.
        netMask          - Display the subnet mask of the subnet.
        nextAddr         - Display the next subnet address.
        firstHost        - Display the first usable host address in the subnet.
        lastHost         - Display the last usable host address in the subnet.
        broadcast        - Display the broadcast address of the subnet.

    Note: If none of these options were used then it will returns the entire information of the subnet.

    Examples : 
        - python3 subnetcalc.py 192.168.0.1/27 addr
        - python3 subnetcalc.py 110.111.69.223/19
        - python3 subnetcalc.py 13.194.89.93/10 lastHostAddr

    '''
    if len( argv ) == 2 : # checking if the user used one argument

        address : str = argv[1] # assign the argument to the variable address
    
        if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
            print(helpMsg)

        else:       # if the address provided by the user Valid
            IP, Prefix = address.split("/") # assinging the IP and the Prefix value

            Prefix : str = int( Prefix )   # making it integer
            
            subnetInfo : dict[ str, str ] = Subnet.getEverything( IP, Prefix ) # getting all of the information about the subnet based on the Ip address and Prefix (as a dictionary)

            # print("") # adding new line to prettify the output
            # for index, (key, val) in enumerate( subnetInfo.items() ) :
            #     if index == 0 :
            #         print("\t\t\tSubnet Mask")

            #     print(f"  {key:-<25}----->   {val}") # to print out all of the information about the subnet in pretty format
            #     if index == 1:
            #         print("\n\t\t  Subnet Informations")
            # this format is harder to read, im gonna print it as a table

            # printing out the table of the subnet informations
            
            print(f'''
  {"":=>39}
  |{"Name":^16}|{"Address":^20}|
  +{"":->16}+{"":->20}+
  |{"Subnet":^16}|{subnetInfo["Subnet Address"]:^20}|
  |{"Subnet Mask":^16}|{subnetInfo["Subnet Mask (base 10)"]:^20}|
  |{"First Host":^16}|{subnetInfo["First Host Address"]:^20}|
  |{"Last Host":^16}|{subnetInfo["Last Host Address"]:^20}|
  |{"Broadcast":^16}|{subnetInfo["Broadcast Address"]:^20}|
  |{"Next subnet":^16}|{subnetInfo["Next subnet Address"]:^20}|
  +{"":->16}+{"":->20}+
''')

            # print("") # adding new line to prettify the output

    elif len(argv) == 3 :

        keyword : str = argv[2] # assigning the argument to the variable keyword.

        if keyword == "addr" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid
                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer
                
                address: str = Subnet.getSubnetAddr(IP, Prefix) # getting the subnet address
                
                print(address)

        elif keyword == "netMask" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid

                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer

                address: str = Subnet.base2to10( Subnet.getSubnetMask( Prefix ) ) # getting the subnet mask
                
                print(address)
        
        elif keyword == "nextAddr" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid
                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer
                
                address: str = Subnet.getNextSubnet(IP, Prefix) # getting the next subnet address
                
                print(address)

        elif keyword == "firstHost" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid
                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer
                
                address: str = Subnet.getFirstHost(Subnet.getSubnetAddr(IP, Prefix)) # getting the subnet address
                
                print(address)
        
        elif keyword == "lastHost" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid
                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer

                address = Subnet.getLastHost(IP, Prefix) # getting the next subnet address
                
                print(address)

        elif keyword == "broadcast" :
            address : str = argv[1] # assign the argument to the variable address

            if IPv4.addressValidation( address ) == False : # if the address provieded by the user Invalid
                print(helpMsg)

            else:       # if the address provided by the user Valid
                IP, Prefix = address.split("/") # assinging the IP and the Prefix value

                Prefix : str = int( Prefix )   # making it integer

                address = Subnet.getBroadcast(IP, Prefix) # getting the next subnet address
                
                print(address)

        else: # means the keyword is invalid
            print(helpMsg)

    else:   # means the user wrote too much arguments
        print(helpMsg)
if __name__ == "__main__" :
    main()