import re,sys,glob,os
from PIL import Image
ROOT=sys.argv[1]
# 1 contact: replace filler photo with a "how to get here" card
CARD={'es':'<div class="box getthere"><p class="kicker">Cómo llegar</p><p class="hroute"><span class="hr-s">Medellín</span><span class="hr-d" aria-hidden="true"><em>2 h</em></span><span class="hr-e">Cascadia Lodge</span></p><p class="small">Por la autopista Medellín–Bogotá. Te ayudamos con el transporte: bus, van privada desde Medellín o 4x4 desde el aeropuerto de Rionegro.</p><a class="link" href="../expediciones/#transporte">Ver opciones de transporte →</a></div>',
      'en':'<div class="box getthere"><p class="kicker">Getting here</p><p class="hroute"><span class="hr-s">Medellín</span><span class="hr-d" aria-hidden="true"><em>2 h</em></span><span class="hr-e">Cascadia Lodge</span></p><p class="small">Along the Medellín–Bogotá highway. We help with transport: bus, a private van from Medellín or a 4x4 from Rionegro airport.</p><a class="link" href="../expediciones/#transporte">See transport options →</a></div>'}
for lang,f in (('es',ROOT+'/es/contacto/index.html'),('en',ROOT+'/contacto/index.html')):
    s=open(f).read()
    s=re.sub(r'<div class="pic"><img src="[^"]*cocorna-valle\.webp"[^>]*></div>',CARD[lang],s)
    s=re.sub(r'<div class="box getthere">.*?</a></div>',CARD[lang],s,flags=re.S)
    open(f,'w').write(s)
# 2 meta description Melcocho–Sonsón
D={'es':'4 días desde El Retiro por el cañón del río Melcocho hasta Manzanares Arriba (Sonsón), con opción de páramo. Para caminantes en forma.',
   'en':'4 days from El Retiro through the Melcocho river canyon to Manzanares Arriba (Sonsón), with a páramo option. For fit hikers.'}
for lang,f in (('es',ROOT+'/es/expediciones/melcocho-sonson-paramo/index.html'),('en',ROOT+'/expediciones/melcocho-sonson-paramo/index.html')):
    s=open(f).read()
    s=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*"',lambda m:m.group(1)+D[lang]+'"',s)
    open(f,'w').write(s)
# 3 width/height on every <img> that lacks them
cache={}; n=0
for f in glob.glob(ROOT+'/**/*.html',recursive=True):
    s=open(f).read(); o=s; d=os.path.dirname(f)
    def fix(m):
        global n
        tag=m.group(0)
        if ' width=' in tag: return tag
        src=re.search(r'src="([^"]+)"',tag)
        if not src or src.group(1).startswith('http') or src.group(1).startswith('data:'): return tag
        p=src.group(1)
        path=os.path.normpath(os.path.join(ROOT,p.lstrip('/')) if p.startswith('/') else os.path.join(d,p))
        if path not in cache:
            try: cache[path]=Image.open(path).size
            except Exception: cache[path]=None
        if not cache[path]: return tag
        w,h=cache[path]; n+=1
        return tag[:-1].rstrip('/').rstrip()+f' width="{w}" height="{h}">'
    s=re.sub(r'<img\b[^>]*>',fix,s)
    if s!=o: open(f,'w').write(s)
print('imgs fixed',n)
