import time, hmac, hashlib, struct

secret = b""#引号内填入密钥，想知道是什么自己解包去吧

def totp():
    counter = int(time.time() / 1800)  # 30分钟
    msg = struct.pack(">Q", counter)
    h = hmac.new(secret, msg, hashlib.sha1).digest()
    o = h[19] & 15
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return str(code).zfill(6)

print(totp())

