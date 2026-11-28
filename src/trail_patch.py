import re,sys
ROOT=sys.argv[1]
X=[29,82,22,76,30,50]  # x% of start/end points
BG=['var(--cream)','#fff','var(--cream)','#fff','#fff']
L={'es':[('Cocorná · 1.300 m','Aquí empieza la aventura'),('La vereda','Fincas campesinas y guías de aquí'),('Las cascadas','Más de las que puedes contar'),('Tu reserva','Sin complicaciones'),('Fin del camino','Y el comienzo del tuyo')],
   'en':[('Cocorná · 1,300 m','Where the adventure starts'),('The vereda','Farm stays and guides from here'),('The waterfalls','More than you can count'),('Your booking','No hassle'),('End of the trail','And the start of yours')]}
INS=[1,2,3,4,7]
def seg(i,lang):
    a,b=X[i]*14.4,X[i+1]*14.4
    d=f'M{a:.0f} 0 C{a:.0f} 45 {b:.0f} 30 {b:.0f} 80 L{b:.0f} 140'
    # elevation silhouette
    ele='M0 140 L0 112 L120 96 L210 104 L330 78 L420 90 L540 64 L640 86 L760 70 L880 92 L990 74 L1100 98 L1210 82 L1320 100 L1440 88 L1440 140 Z'
    t,s=L[lang][i]; end=' ts-end' if i==4 else ''
    side='l' if X[i+1]<50 else 'r'
    return (f'<div class="trail-seg" style="--bg:{BG[i]}" aria-hidden="true"><svg viewBox="0 0 1440 140" preserveAspectRatio="none">'
      f'<defs><mask id="tsm{i}" maskUnits="userSpaceOnUse"><path class="ts-draw" d="{d}" pathLength="1" stroke="#fff" stroke-width="60" fill="none"/></mask></defs>'
      f'<path class="ts-ele" d="{ele}"/><path class="ts-path" d="{d}" mask="url(#tsm{i})"/></svg>'
      f'<span class="ts-pt ts-{side}{end}" style="left:{X[i+1]}%"><b>{t}</b><em>{s}</em></span></div>\n')
for lang,f in (('es',f'{ROOT}/es/index.html'),('en',f'{ROOT}/index.html')):
    h=open(f).read()
    h=re.sub(r'<div class="trail-seg".*?</div>\n','',h,flags=re.S)
    a=h.find('<main'); b=h.find('</main>'); m=h[a:b]
    pos=[x.start() for x in re.finditer(r'<section\b',m)]
    print(f,len(pos))
    for k in sorted(range(len(INS)),reverse=True):
        p=pos[INS[k]]; m=m[:p]+seg(k,lang)+m[p:]
    h=h[:a]+m+h[b:]; open(f,'w').write(h)
