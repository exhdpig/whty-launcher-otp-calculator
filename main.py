import time, hmac, hashlib, struct

secret = b"12345678901234567890"#引号内填入密钥，此方法已失效，现直接填入密钥

def totp():
    counter = int(time.time() / 1800)  # 30分钟
    msg = struct.pack(">Q", counter)
    h = hmac.new(secret, msg, hashlib.sha1).digest()
    o = h[19] & 15
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return str(code).zfill(6)

print(totp())

