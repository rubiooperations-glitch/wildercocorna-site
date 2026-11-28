import re,sys,urllib.parse
ROOT=sys.argv[1]
WA='https://wa.me/573504186252?text='
C={'es':dict(k='Grupos abiertos',h='Solo o en pareja, camina en grupo.',p='Nuestras expediciones son privadas, pero si viajas solo o en pareja te unimos con otros viajeros que van en las mismas fechas. Así se reparte el costo del guía y del transporte, y el precio por persona baja. No hay mínimo de personas: tú eliges si prefieres ir en privado o en grupo.',
 s=['Nos dices la expedición y tus fechas.','Buscamos viajeros con las mismas fechas.','Cuando todos confirman, el precio por persona baja.'],
 n='Ojo: un grupo abierto solo es seguro cuando todos los viajeros han confirmado. Te avisamos por WhatsApp en cuanto esté listo.',
 d=('Próxima salida abierta','Melcocho–Sonsón y páramo, 4 días','Salida entre el 19 y el 27 de diciembre · 1 viajero ya apuntado','Me uno a esta salida','Hola, me quiero unir a la salida abierta Melcocho–Sonsón y páramo (4 días) entre el 19 y el 27 de diciembre. Somos: '),
 b='Pregunta por un grupo abierto',m='Hola, viajo solo/a y me interesa un grupo abierto. Mis fechas son: '),
 'en':dict(k='Open groups',h='Travelling solo? Hike as a group.',p='Our expeditions are private, but if you travel solo or as a couple we can match you with other travellers on the same dates. That way the cost of the guide and transport is shared, and the price per person goes down. There is no minimum group size: you choose whether you go private or join a group.',
 s=['Tell us the expedition and your dates.','We look for travellers on the same dates.','Once everyone confirms, the price per person drops.'],
 n='Good to know: an open group is only certain once every traveller has confirmed. We let you know on WhatsApp as soon as it is set.',
 d=('Next open departure','Melcocho–Sonsón & páramo, 4 days','Departure between 19 and 27 December · 1 traveller already in','Join this departure','Hi, I would like to join the open departure Melcocho–Sonsón & páramo (4 days) between 19 and 27 December. We are: '),
 b='Ask about an open group',m='Hi, I am travelling solo and I am interested in an open group. My dates are: ')}
def block(l):
    c=C[l]; steps=''.join(f'<li><span>{i+1}</span>{t}</li>' for i,t in enumerate(c['s']))
    d=c['d']
    return (f'<div class="wrap section ogs" id="grupos-abiertos"><div class="og">'
            f'<div class="og-t stack"><p class="kicker">{c["k"]}</p><h2>{c["h"]}</h2><p>{c["p"]}</p>'
            f'<p class="og-n">{c["n"]}</p>'
            f'<div class="og-dep" data-until="2026-12-27"><span class="og-dk">{d[0]}</span><a class="og-dn" href="expediciones/melcocho-sonson-paramo/">{d[1]}</a><span class="og-dd">{d[2]}</span>'
            f'<a class="btn wa" href="{WA+urllib.parse.quote(d[4])}" target="_blank" rel="noopener">{d[3]}</a></div>'
            f'<a class="link og-ask" href="{WA+urllib.parse.quote(c["m"])}" target="_blank" rel="noopener">{c["b"]} →</a></div>'
            f'<ol class="og-s">{steps}</ol></div></div>\n')
for l,f in (('es',f'{ROOT}/es/index.html'),('en',f'{ROOT}/index.html')):
    h=open(f).read()
    h=re.sub(r'<div class="wrap section ogs".*?</ol></div></div>\n','',h,flags=re.S)
    a=h.find('<main'); m=h[a:]
    pos=[x.start() for x in re.finditer(r'<section\b',m)]
    p=a+pos[5]
    # put before any trail segment directly preceding? section 5 has no seg before it
    h=h[:p]+block(l)+h[p:]
    open(f,'w').write(h)
print('ok')
