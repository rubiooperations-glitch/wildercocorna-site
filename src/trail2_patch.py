import re,sys,html
ROOT=sys.argv[1]
ELE='M0 140 L0 112 L120 96 L210 104 L330 78 L420 90 L540 64 L640 86 L760 70 L880 92 L990 74 L1100 98 L1210 82 L1320 100 L1440 88 L1440 140 Z'
def seg(uid,x0,x1,bg,t,s,end=False):
    a,b=x0*14.4,x1*14.4
    d=f'M{a:.0f} 0 C{a:.0f} 45 {b:.0f} 30 {b:.0f} 80 L{b:.0f} 140'
    side='l' if x1<50 else 'r'
    em=f'<em>{s}</em>' if s else ''
    return (f'<div class="trail-seg tsx" style="--bg:{bg}" aria-hidden="true"><svg viewBox="0 0 1440 140" preserveAspectRatio="none">'
      f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse"><path class="ts-draw" d="{d}" pathLength="1" stroke="#fff" stroke-width="60" fill="none"/></mask></defs>'
      f'<path class="ts-ele" d="{ELE}"/><path class="ts-path" d="{d}" mask="url(#{uid})"/></svg>'
      f'<span class="ts-pt ts-{side}{" ts-end" if end else ""}" style="left:{x1}%">'+(f'<b>{t}</b>' if t else '')+f'{em}</span></div>\n')
def clean(h): return re.sub(r'<div class="trail-seg tsx".*?</div>\n','',h,flags=re.S)
XS=[18,78,24,72,30,70,26,74]
# expediciones listing: a segment before every category after the first
for f in (ROOT+'/es/expediciones/index.html',ROOT+'/expediciones/index.html'):
    h=clean(open(f).read())
    secs=list(re.finditer(r'<section id="(\w+)" class="(band)?">',h))
    for k in range(len(secs)-1,0,-1):
        m=secs[k]; h2=re.search(r'<h2>([^<]*)</h2>',h[m.end():]).group(1)
        bg='var(--cream)' if m.group(2) else '#fff'
        h=h[:m.start()]+seg(f'tsx{k}',XS[k-1],XS[k],bg,'','',k==len(secs)-1)+h[m.start():]
    open(f,'w').write(h)
# agencias + contacto: one segment between the page head and the content
L={'agencias':{'es':('Para agencias','Rutas a medida para tus grupos'),'en':('For agencies','Tailor-made routes for your groups')},
   'contacto':{'es':('Tu reserva','Empieza aquí'),'en':('Your booking','Starts here')}}
for page,lab in L.items():
    for lang,f in (('es',f'{ROOT}/es/{page}/index.html'),('en',f'{ROOT}/{page}/index.html')):
        h=clean(open(f).read())
        i=h.find('</section>',h.find('<section class="page-head">'))+len('</section>')
        h=h[:i]+'\n'+seg('tsx0',22,14,'#fff',*lab[lang])+h[i:]
        open(f,'w').write(h)
print('ok')
