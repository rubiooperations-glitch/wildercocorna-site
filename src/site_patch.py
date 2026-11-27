import glob,re,sys
root=sys.argv[1]
PTS={'valle-de-las-cascadas-1-dia':('La Piñuela','La Piñuela'),'valle-de-las-cascadas-2-dias':('La Piñuela','La Piñuela'),'valle-de-las-cascadas-3-dias':('La Piñuela','La Piñuela'),
 'jungle-trekking-melcocho':('El Retiro','El Retiro'),'melcocho-2-dias':('El Retiro','El Retiro'),'melcocho-sonson-paramo':('El Retiro','Sonsón')}
def tline(slug,lang):
    s,e=PTS[slug]; lab=('Empieza en','termina en') if lang=='es' else ('Starts in','ends in')
    return f'<span class="tline" aria-label="{lab[0]} {s}, {lab[1]} {e}"><span class="tl-s">{s}</span><span class="tl-d" aria-hidden="true"></span><span class="tl-e">{e}</span></span>'
HERO={'es':'<p class="hroute" aria-label="De Medellín a Cocorná, unas 2 horas"><span class="hr-s">Medellín</span><span class="hr-d" aria-hidden="true"><em>2 h</em></span><span class="hr-e">Cocorná</span></p>',
      'en':'<p class="hroute" aria-label="From Medellín to Cocorná, about 2 hours"><span class="hr-s">Medellín</span><span class="hr-d" aria-hidden="true"><em>2 h</em></span><span class="hr-e">Cocorná</span></p>'}
n=0
for f in glob.glob(root+'/**/*.html',recursive=True):
    s=open(f,encoding='utf-8').read(); o=s
    lang='es' if '/es/' in f.replace(root,'') else 'en'
    s=re.sub(r'<span class="tline".*?</span></span>','',s,flags=re.S)  # idempotent (inner spans close)
    s=re.sub(r'<p class="hroute".*?</p>','',s,flags=re.S)
    # tiles: <a class="tile" href=".../slug/">...<div class="price"> insert before price
    def tile(m):
        slug=m.group(2); body=m.group(3)
        if slug in PTS:
            new,k=re.subn(r'<span class="meta">Cocorn[^<]*</span>',tline(slug,lang),body,count=1)
            if not k: new=body.replace('<span class="price"',tline(slug,lang)+'<span class="price"',1)
            body=new
        return m.group(1)+body
    s=re.sub(r'(<a class="tile" href="[^"]*?/([a-z0-9-]+)/"[^>]*>)(.*?</a>)',tile,s,flags=re.S)
    # tcards: insert after lvl span closing in tbody, using h3 link slug
    def tc(m):
        slug=m.group(1); block=m.group(0)
        if slug in PTS:
            block=block.replace('<p class="muted tlead">',tline(slug,lang)+'<p class="muted tlead">',1)
        return block
    s=re.sub(r'<div class="tbody"><h3><a href="[^"]*?/([a-z0-9-]+)/">.*?<p class="muted tlead">',tc,s,flags=re.S)
    if 'class="hero"' in s:
        s=re.sub(r'(<section class="hero">.*?<p class="lead">.*?</p>)',lambda m:m.group(1)+HERO[lang],s,count=1,flags=re.S)
    if s!=o: open(f,'w',encoding='utf-8').write(s); n+=1
print('patched',n)
