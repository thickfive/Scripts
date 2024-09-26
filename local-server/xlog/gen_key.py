# 安装依赖
# pip3 install bloxroute-pyelliptic --break-system-packages
# pip3 install zstandard --break-system-packages

# python3 gen_key.py 
# python3 decode_mars_nocrypt_log_file.py temp.xlog
# python3 decode_mars_crypt_log_file.py temp.xlog

# save private key
# b'62ff5c2ff51eb469d2c0bfd736cd271da4f9c084b2a121b507f7275c9136317f'
# appender_open's parameter:
# b'22e47ed6923fb6f680ae35a5fb95f1f5bffe1febf6d976d5f58a37722ce6f807'b'b16804838e8e3bec41751094dbb11794a02c82adb7c7ad6157f9c8d24a725000'
# 结果去掉 b''
# private key = 62ff5c2ff51eb469d2c0bfd736cd271da4f9c084b2a121b507f7275c9136317f
# public key = 22e47ed6923fb6f680ae35a5fb95f1f5bffe1febf6d976d5f58a37722ce6f807b16804838e8e3bec41751094dbb11794a02c82adb7c7ad6157f9c8d24a725000

from binascii import hexlify, unhexlify

import pyelliptic

CURVE = 'secp256k1'

svr = pyelliptic.ECC(curve=CURVE)

svr_pubkey = svr.get_pubkey()
svr_privkey = svr.get_privkey()


print("save private key")

print(hexlify(svr_privkey))

print("\nappender_open's parameter:")
print("%s%s" %(hexlify(svr.pubkey_x),  hexlify(svr.pubkey_y)))