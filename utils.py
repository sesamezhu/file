import hmac, base64, struct, hashlib, time
import os, re
import pyperclip

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack('>Q', intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack('>I', h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    return str(
            get_hotp_token(secret, intervals_no=int(time.time())//30)
        ).zfill(6)


if __name__ == '__main__':
    token = get_totp_token('IAYRQWOHHGDFVN7B')
    # raw_input('Press any key to continue')
    pyperclip.copy(token)
    print token
