# -*- coding: utf-8 -*-
import sys
from readfasta import readfasta
fileName = sys.argv[1]
resultList = readfasta(fileName)
sequnce = resultList[0][1]
print(sequnce)