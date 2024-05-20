from typing import Union, Final
from custumeTypes import BinaryString, binStrValidation

# BinaryStrings are costume data type i created to use as type hint, cuz it's helpful
# example of BinaryString: '01101001'

class Subnet:

    @staticmethod
    def getSubnetAddr( IP : str, 
                       Prefix : int 
                     )       -> str :
        '''
        Returns the subnet address of the given ip address and its prefix.
        '''

        # Subnet Mask
        subnetmask :       BinaryString   = Subnet.getSubnetMask( Prefix )                    # this is a subnetmask as a BinaryString ip address
        subnetmask : list[ BinaryString ] = IPv4.getOctets( subnetmask )                      # this is the list of four BinaryString octets of the subnet mask

        # IP Address
        IP         : list[     str      ] = IP.split(".")                                 # returns list of four base 10 octets
        binIP      : list[ BinaryString ] = [ IPv4.octToBin( octet ) for octet in IP ]    # creating a list of BinaryStrings of the ip address octets

        # AND operation
        result     : list[ BinaryString ] = [ IPv4.ANDitOut( subnetmask[0], binIP[0] ), IPv4.ANDitOut( subnetmask[1], binIP[1] ), IPv4.ANDitOut( subnetmask[2], binIP[2] ), IPv4.ANDitOut( subnetmask[3], binIP[3] ) ]
        
        # Converting BinaryStrings octets into stings
        final      : list[     str      ] = [ IPv4.binToOct( result[0] ), IPv4.binToOct( result[1] ), IPv4.binToOct( result[2] ), IPv4.binToOct( result[3] ) ]

        # compining every octet into one address
        subnet     :       BinaryString   = ".".join( final )

        return subnet

    @staticmethod
    def getNextSubnet(   IP   : str,
                       Prefix : int 
                       ) ->     str :
        '''
        Returns the next subnet of a given Prefix.
        '''

        # initializing the blocksize variable
        blocksize = Subnet.getBlockSize( Prefix )
        
        # this variable is going to be used to manipulate the current octet and change it value
        currentOctet : int = 3

        while blocksize >= 256: # if the block size is greater than or equal to 256 then its divided by 256 and the current octet becomes the octet before the one we were in
            blocksize //= 256
            currentOctet -= 1
        
        # after reaching the octet we want, we're going to do the folowing
        currentsubnet :       str   = Subnet.getSubnetAddr( IP, Prefix ) # getting the subnet address
        currentsubnet : list[ str ] = currentsubnet.split(".")           # splitting it into octets

        currentsubnet[currentOctet] = str(int(currentsubnet[currentOctet]) + blocksize) # we're changing the octet value by adding the blocksize to it (which would give us the next subnet)

        if currentsubnet[currentOctet] == "256":    # if the value of the octet is 256
            currentsubnet[currentOctet] = "0"       # change the value of that octet to zero
            currentOctet -= 1                       # making the current octet the next one to the left
            
            currentsubnet[currentOctet] = str( int(currentsubnet[currentOctet]) + 1 ) # adding one to that octet.

        nextsubnet = ".".join( currentsubnet ) # joining the octets into an address

        return nextsubnet

    @staticmethod
    def getSubnetMask( Prefix : int ) -> BinaryString :
        '''
        Returns a BinaryString of the subnetmask of a given Prefix.
        '''

        # making sure the prefix is correct
        if Prefix > 32 or Prefix < 1 :
            raise ValueError("PREFIXES MUST BE >= 1 or <= 32 !")

        # the difference between the total number of bits in an IPv4 address minus the given prefix
        difference : int = 32 - Prefix

        maskbits   : list[ str ] = [ "1" for _ in range(Prefix) ]   # the network bits

        [ maskbits.append( "0" ) for _ in range(difference) ]       # appending the hosts bits

        subnetmask = "".join( maskbits )    # converting it to a BinaryString of the subnet mask

        binStrValidation( subnetmask )      # raising an error if it didnt work so i can debug it with ease lol

        return subnetmask
    
    @staticmethod
    def base2to10( IP : BinaryString ) -> str :
        '''
        Returns a base 10 ip address based on the given BinaryString.
        '''

        # splitting the address into octets
        splitted : list[ BinaryString ] = IPv4.getOctets( IP )

        base10   : list[ str ]          = []

        for octet in splitted:
            base10.append( IPv4.binToOct( octet ) ) # appending the base 10 string of the octet to the list
        
        base10   : str = ".".join( base10 ) # joining the octets into one address

        return base10

    @staticmethod
    def getFirstHost( IP : str ) -> str :
        '''
        Returns the first host in the subnet.
        takes the subnet address as a parameter IP
        '''

        # splitting the octets from
        octets    : list[ str ] = IP.split(".")

        # adding 1 to the last octet
        octets[3] = str( int(octets[3]) + 1 )

        # joining the octets into an address
        firsthost : str = ".".join(octets)

        return firsthost

    @staticmethod
    def getLastHost( IP : str, Prefix : int ) -> str :
        '''
        Returns the last host in the subnet.
        '''

        blocksize : int = Subnet.getBlockSize( Prefix ) - 2 # gets the total number of hosts (all addresses minus the subnet address and the broadcast address)
        
        currentOctet       : int = 3    # the current octet

        while blocksize >= 256: # check how big the blocksize is, the bigger it is the lower the octet we're going to manipulate
            blocksize //= 256
            currentOctet -= 1
        
        IP : list[ str ] = IP.split(".") # spliting the octets

        IP[currentOctet] = str( int(IP[currentOctet]) + blocksize ) # adding the blocksize to the current octet

        # the following lines are to deal with the rest of the octets on the right
        if currentOctet == 0:
            IP[1] = "255"
            IP[2] = "255"
            IP[3] = "254"

        elif currentOctet == 1:
            IP[2] = "255"
            IP[3] = "254"
        
        elif currentOctet == 2:
            IP[3] = "254"

        # joining the octets into an address
        lasthost = ".".join( IP )

        return lasthost

    @staticmethod
    def getBroadcast( subnet : str, Prefix : int ) -> str :
        '''
        Returns the broadcast address of the subnet.
        '''

        # using the last host as a starting point (since the broadcast address = the last host + 1)
        lasthost = Subnet.getLastHost(subnet, Prefix)
        lasthost = lasthost.split(".")
        
        # checking if the last octet of the lasthost is smaller than 255
        if int(lasthost[3]) < 255 :
            lasthost[3] = str( int( lasthost[3] ) + 1 ) # if it is then we're adding 1 to it (which makes the address the broadcast address)

        # compining the octets into an address
        broadcast : str = ".".join( lasthost )

        return broadcast
        
    getBlockSize = staticmethod( lambda Prefix : 2**(32-Prefix) ) # which is 2 to the power of the hosts bits, equals to the total number of possible addresses in this prefix.

    @staticmethod
    def getEverything( ipAddr: str, Prefix : int ) -> dict[ str, str ] :
        '''
        returns all of the possible info about the given ip address and with the prefix
        '''
        info    : dict[ str, str ] = {}

        sub     : str = Subnet.getSubnetAddr( ipAddr, Prefix )
        netmask : str = Subnet.getSubnetMask(         Prefix )

        info["Subnet Mask (base 2)"]    = netmask
        info["Subnet Mask (base 10)"]   = Subnet.base2to10     (   netmask   )
        info["Subnet Address"]          = sub
        info["First Host Address"]      = Subnet.getFirstHost  ( sub         )
        info["Last Host Address"]       = Subnet.getLastHost   ( sub, Prefix )
        info["Broadcast Address"]       = Subnet.getBroadcast  ( sub, Prefix )
        info["Next subnet Address"]     = Subnet.getNextSubnet ( sub, Prefix )

        return info
   

class IPv4:

    @staticmethod
    def getOctets(   IP     : BinaryString,
                   Octet    : Union[ None, int ] = None,
                 ) -> Union[ BinaryString, list[ BinaryString ] ]:
        '''
        Splits a 32 bit BinaryString Ip address into four 8 bits octets in binary, returns list of BinaryString's if Octet arg left to default
        You can also specify the octet you want get from this method, where the octets are like this : 1.2.3.4
        '''

        binStrValidation( IP ) # making sure the bin_ip is a binary value of the ip address

        first  : str = IP[:8]
        second : str = IP[8:16]
        third  : str = IP[16:24]
        last   : str = IP[24:]

        if Octet == None : # if there wasnt any specified octet to return
            OCTETS : Final = [ first, second, third, last ]
            return OCTETS
        
        else:
            if Octet > 4 or Octet < 1 :
                raise ValueError( "Octet number is not correct, must be one of these [ 1, 2, 3, 4 ]")
            
            else:
                if   Octet == 1 :
                    return first
                elif Octet == 2 :
                    return second
                elif Octet == 3 :
                    return third
                else            :
                    return last

    @staticmethod
    def ANDitOut( oct1 : BinaryString,
                  oct2 : BinaryString 
                  )   -> BinaryString :
        '''
        uses AND operator on oct1 and oct2 and returns output of these two.
        the main use of this method is to calculate the subnet address.
        '''

        # making sure the octets are BinaryStrings
        binStrValidation( oct1 )
        binStrValidation( oct2 )

        oct1   : int = int( oct1, 2 )
        oct2   : int = int( oct2, 2 )

        result : int = oct1 & oct2

        return IPv4.octToBin( result ) # returns a BinaryString of the result of using the AND operators on the provided octets.
    
    @staticmethod
    def addressValidation( address: str ) -> bool :
        '''
        returns True if the address is valid and false if its not
        checks the addrss and its prefix to determine if its valid or not.
        '''

        # initializing these variables to set it to True later if conditions are met
        validPrefix : bool = False
        validIP     : bool = False

        # checking if the address is not a string ---> return False ( not valid )
        if type( address ) != str:
            return False
        
        # after making sure it's a string, then spliting it to extract the ip and the prefix
        address = address.split("/")
    
        if len( address ) == 2: # meaning if there are an ip address and a prefix

            IP     : str =      address[0]
            Prefix : int = int( address[1] )

            try: # just to make sure the user didnt write Inalid inputs
                if Prefix > 32 or Prefix < 1: # if the prefix is invalid
                    return False
                else:
                    validPrefix = True # if it's valid then set validPrefix to True

            except ValueError: 
                return False
            
            # these below are just to enhance the readablility
            IPstring : list[str] = IP.split(".")    # splitting the ip address into octets (strings)

            IP       : list[int] = [ int( octet ) for octet in IPstring ]   # converting each octet into integer and adding it to this new list

            FIRST_OCTET  : int = 0
            SECOND_OCTET : int = 1
            THIRD_OCTET  : int = 2
            FOURTH_OCTET : int = 3

            # the code below is to check if the ip address is valid
            if len( IP ) == 4 :        # checks if the length of the splitted ip address if it has 4 elements
                if ( IP[FIRST_OCTET]  >= 1 and IP[FIRST_OCTET]  < 256 and       # if the first octet has value between 1 and 255
                     IP[SECOND_OCTET] >= 0 and IP[SECOND_OCTET] < 256 and       # if the second octet has value between 0 and 255
                     IP[THIRD_OCTET]  >= 0 and IP[THIRD_OCTET]  < 256 and       # if the third octet has value between 0 and 255
                     IP[FOURTH_OCTET] >= 0 and IP[FOURTH_OCTET] < 256  ):       # if the fourth octet has value between 0 and 255
                    validIP = True      # since the 4 octets have valid values then the ip address is valid. 
                else:
                    return False
            else:
                return False
        else:
            return False

        if validIP and validPrefix: # checks if both the ip address and the prefix are valid
            return True  # it's valid
        else:
            return False # it's invalid

    octToBin = staticmethod( lambda octet : format( int( octet ), "08b" ) ) # convets base 10 octets into BinaryStrings.
    
    binToOct = staticmethod( lambda octet : str( int( octet, 2 ) ) )          # converts BinaryStrings into base 10 octet string.