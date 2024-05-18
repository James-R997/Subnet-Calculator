from typing import NewType

BinaryString = NewType( 'BinaryString', str )


def isBinary( value: BinaryString ) -> bool :
    '''
    Checks if the given value is a string of base 2 number, returns True if it is, False if its not.
    '''
    try:
        return all( char in "01" for char in value ) 
    except TypeError : # if it wasn't a string
        return False


def binStrValidation( value: str ) -> None :
    '''
    Checks if the given value is a string of base 2 number, raises ValueError if its not.
    '''
    if not isBinary( value ) :
        raise ValueError( "THIS IS NOT A BINARY STRING TYPE" )
    