ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET += ALPHABET.upper() + ' .,!?'


def encrypt(msg, shift):
    """
    Takes string msg and an integer shift
    returns new string which is an encrypted version
    of the message
    str, int -> str
    print(encrypt('John', 15)) -> 'YDwC'
    print(encrypt(' ', 6)) -> 'b'
    """
    # the body of function
    encrypted_msg=''
    new_index=0
    for i in msg:
        
            index=ALPHABET.find(i)

            alpha_index=index+shift     
       
            if abs(alpha_index)>=len(ALPHABET):
                new_index = alpha_index%len(ALPHABET)
            else:
                new_index = alpha_index
                
            encrypted_msg+=ALPHABET[new_index]
          
    return encrypted_msg



def decrypt(encrypted_msg, shift):
    """
    Takes string encrypted_msg and an integer shift
    returns new string which is a decrypted version
    of the message
    str, int -> str
    print(decrypt('eDUHM', 25)) -> Kevin
    print(decrypt('j.GT', -10000)) -> Ivan
    """
    # the body of function
    decrypted_msg=''
    new_index=0
    
    for i in encrypted_msg:
        
        index=ALPHABET.find(i)
                       
        alpha_index=index-shift
              
        if abs(alpha_index)>=len(ALPHABET):
                new_index = alpha_index%len(ALPHABET)
        else:
                new_index = alpha_index
                
           
        decrypted_msg+=ALPHABET[new_index]
        
    return decrypted_msg
