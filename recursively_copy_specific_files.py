import os
import shutil
import sys

dst = r'E:\pios\123'
qqq = ['QRD7x27A', 'QRD7X27A-LA','QRD8x25','QRD8x25Q', 'QRD7225', 'QRD7227', 'QRD7227C', 'QRD8225C', 'QRD8625-DSDA']
for i in qqq:
    for root, dirs, files in os.walk(os.path.join(r'\\oaserver\oafile\GIGABYTE\C1\Software\Tools\Qualcomm_Doc\Libary', i)):
        #print root
        for f in files:
            if f.endswith('.pdf'):
                #print root
                if not os.path.exists(os.path.join(dst, root[2:])):
                    os.makedirs(os.path.join(dst, root[2:]))
                shutil.copy(os.path.join(root, f), os.path.join(dst, root[2:]))
                print os.path.join(root, f)
raw_input()
