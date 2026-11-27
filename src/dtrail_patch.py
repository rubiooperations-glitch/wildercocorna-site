import re,sys,glob
ROOT=sys.argv[1]
PTS={'valle-de-las-cascadas-1-dia':('La Piñuela','La Piñuela'),'valle-de-las-cascadas-2-dias':('La Piñuela','La Piñuela'),'valle-de-las-cascadas-3-dias':('La Piñuela','La Piñuela'),
 'jungle-trekking-melcocho':('El Retiro','El Retiro'),'melcocho-2-dias':('El Retiro','El Retiro'),
 'melcocho-sonson-paramo':('El Retiro','Sonsón'),
 'basecamp-aventura':('Cascadia Lodge','Cascadia Lodge'),'basecamp-naturaleza':('Cascadia Lodge','Cascadia Lodge')}
L={'es':('Salida','Llegada'),'en':('Start','Finish')}
for f in glob.glob(ROOT+'/**/expediciones/*/index.html',recursive=True)+glob.glob(ROOT+'/expediciones/*/index.html'):
    slug=f.rstrip('/').split('/')[-2]; lang='es' if '/es/' in f else 'en'
    s=open(f).read(); o=s
    s=re.sub(r'<p class="tl-from">.*?</p>','',s); s=re.sub(r'<p class="tl-to">.*?</p>','',s)
    s=s.replace('<ol class="timeline trail">','<ol class="timeline">')
    if slug in PTS and '<ol class="timeline">' in s:
        a,b=PTS[slug]; x,y=L[lang]
        s=s.replace('<ol class="timeline">',f'<p class="tl-from"><span>{x}</span>{a}</p><ol class="timeline trail">',1)
        i=s.find('<ol class="timeline trail">'); j=s.find('</ol>',i)+5
        s=s[:j]+f'<p class="tl-to"><span>{y}</span>{b}</p>'+s[j:]
    if slug=='melcocho-sonson-paramo':
        s=s.replace('<span class="fk">Salida</span><b>Sonsón','<span class="fk">Ruta</span><b>El Retiro → Sonsón')
        s=s.replace('<span class="fk">Start</span><b>Sonsón','<span class="fk">Route</span><b>El Retiro → Sonsón')
    if s!=o: open(f,'w').write(s); print(f)
