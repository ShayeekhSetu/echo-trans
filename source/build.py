import re
html=open('/home/claude/echo-report.html').read()
css=open('/home/claude/base.css').read()+open('/home/claude/echo_extra.css').read()
# enlarge every font-size inside report-page (.pg) rules by 7%
def scale_rule(m):
    sel, body = m.group(1), m.group(2)
    if '.pg' in sel:
        body = re.sub(r'font-size:\s*([\d.]+)px', lambda f: 'font-size:%spx' % round(float(f.group(1))*1.07,2), body)
        body = re.sub(r'font:\s*(\d+)\s+([\d.]+)px', lambda f: 'font:%s %spx' % (f.group(1), round(float(f.group(2))*1.07,2)), body)
        body = re.sub(r'font:\s*([\d.]+)px', lambda f: 'font:%spx' % round(float(f.group(1))*1.07,2), body)
    return sel + '{' + body + '}'
css = re.sub(r'([^{}]+)\{([^{}]*)\}', scale_rule, css)
js=open('/home/claude/echo.js').read()
a=html.index('<style>')+7; b=html.index('</style>'); html=html[:a]+'\n'+css+'\n'+html[b:]
a=html.index('<script>')+8; b=html.rindex('</script>'); html=html[:a]+'\n'+js+'\n'+html[b:]
open('/home/claude/echo-report.html','w').write(html)
