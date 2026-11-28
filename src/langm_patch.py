import re,sys,glob
ROOT=sys.argv[1]; n=0
PART=r'(?:<a [^>]*>[^<]*</a>|<span class="lang on">[^<]*</span>)'
for f in glob.glob(ROOT+'/**/*.html',recursive=True):
    s=open(f).read(); o=s
    s=re.sub(r'<span class="langsw lang-m">'+PART+'+</span>','',s)
    m=re.search(r'<span class="langsw">('+PART+'+)</span>',s)
    if m and '<button class="menu-btn"' in s:
        s=s.replace('<button class="menu-btn"','<span class="langsw lang-m">'+m.group(1)+'</span><button class="menu-btn"',1)
    if s!=o: open(f,'w').write(s); n+=1
print(n)
