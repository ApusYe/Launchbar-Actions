#!/usr/local/bin/python3
# # -*- coding: utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
from PdfBookmark import PdfBookmark

def P_import(TOC, PDF_Without_TOC):
    PDF_Without_TOC0 = PdfBookmark(PDF_Without_TOC)
    PDF_Without_TOC0.importBookmark(TOC)


if len(sys.argv) == 3 and sys.argv[2][-3:] == 'pdf' and sys.argv[1][-2:] == 'bm': 
    P_import(sys.argv[1], sys.argv[2])       
    sp.run(['open', sys.argv[2].replace('.pdf', '_bookmark.pdf')])
    sp.run(['afplay', '/System/Library/Sounds/submarine.aiff'])
    print('Done! New PDF Opened!')

else:
    sp.run(['afplay', '/System/Library/Sounds/Tink.aiff'])
    print('Usage: [bm] [PDF without TOC]')
