# build echo-trans/index.html from echo-report.html (adds config.js + copyright)
h=open('source/echo-report.html').read(); i=h.rfind('<script>')
h=h[:i]+'<script src="config.js"></script>\n'+h[i:]
h=h.replace('<head>','<head>\n<!-- © 2026 Dr. Md. Shayeekh Mahbub Setu. All rights reserved. Unauthorised copying or reuse prohibited. -->',1)
open('index.html','w').write(h)
