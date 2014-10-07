#!/usr/bin/env python

# example of a constant time password check

def check_pass(real_passwd, given_passwd):
    success = 0

    # pad real password out of zeroes
    gp_len = len(given_passwd)
    rp_len = len(real_passwd)

    # assume  that real_passwd is mutable
    for i in given_passwd:
        if (i > rp_len):
            real_passwd += "\x00"
        else:
            pass
    

    for i in given_passwd:
            success += real_passwd[i] ^ given_passwd[i]
                

    # now if given_passwd is less than the real_passwd
    if (gp_len != rp_len):
        return False

    if (success==0):
        return True
    else:
        return False 
