import sys
import binascii

fout = open(sys.argv[1]+".bin", "wb")
fin = open(sys.argv[1], "r")
counter = 0
while True:
        buf1 = fin.readline()
        if not buf1:
            break
        print(buf1)
        if (buf1[:6] == "Block "):
                idx = buf1.find(":")
                buf2 = buf1[idx+2:]
                splitted = buf2.split(" ")
                print(splitted)
                for data in splitted:
                        try:
                                fout.write(binascii.unhexlify(data.strip()))
                        except:
                                print("Something went wrong")
fin.close()
fout.close()
input("Press Enter to continue...")
