"""Nieuwe inspiratiepagina met routes (bouwblokken). Patcht live/inspiracion (EN) en live/es/inspiracion (ES)."""
import re, sys, urllib.parse

WA = 'https://wa.me/573504186252?text='
def wa(t): return WA + urllib.parse.quote(t, safe='')

# (id, img, days, diff, price4, price2, {lang: (name, route, tag, note, [(label,title,line)...])})
R = [
 ('esencial','valle-cascada',4,3,'1.855.000','2.710.000',{
  'es':('Cocorná esencial','Medellín → Cascadia → Medellín','Lo mejor de Cocorná sin mochila pesada: cascadas, panela, masaje y rafting, con base en Cascadia.','',[
    ('Día 1','Llegada a Cascadia','Te instalas y te refrescas en una piscina natural en medio del bosque.'),
    ('Día 2','Valle de las Cascadas','Un día entero entre cascadas y pozas, con guía local.'),
    ('Día 3','Panela, cascadas y masaje','De la caña a la panela, un baño en la cascada y un masaje junto al agua.'),
    ('Día 4','Rafting en el Santo Domingo','Rápidos y aguas tranquilas para despedirte con adrenalina.')]),
  'en':('Cocorná essentials','Medellín → Cascadia → Medellín','The best of Cocorná without a heavy backpack: waterfalls, panela, a massage and rafting, based at Cascadia.','',[
    ('Day 1','Arrival at Cascadia','Settle in and cool off in a natural pool in the middle of the forest.'),
    ('Day 2','Valle de las Cascadas','A full day of waterfalls and pools with a local guide.'),
    ('Day 3','Panela, waterfalls and massage','From sugar cane to panela, a swim under the waterfall and a massage by the water.'),
    ('Day 4','Rafting the Santo Domingo','Rapids and calm water for an adrenaline-filled goodbye.')])}),
 ('carmen-cascadia','valle-caminantes-800',5,3,'1.605.000','2.210.000',{
  'es':('De El Carmen a Cascadia, a pie','El Carmen de Viboral → Valle de las Cascadas → Cascadia','Tres días caminando de un pueblo de cerámica a la selva, con dos noches en fincas campesinas.','',[
    ('Día 1','A caminar desde El Carmen','De Medellín a El Carmen de Viboral y a caminar. Primera noche en una finca del camino.'),
    ('Día 2','Bajada al Valle de las Cascadas','Bajas al valle. Noche en una finca campesina dentro del valle.'),
    ('Día 3','Del valle a Cascadia','Sales del valle a pie entre cascadas y pozas, hasta la piscina natural de Cascadia.'),
    ('Día 4','Tú eliges','Chocolate del grano a la barra o aguas bravas en el Calderas.'),
    ('Día 5','Sigue tu viaje','Bus a Medellín o Bogotá: nosotros compramos tu tiquete.')]),
  'en':('From El Carmen to Cascadia on foot','El Carmen de Viboral → Valle de las Cascadas → Cascadia','Three days walking from a ceramics town into the jungle, with two nights on rural farms.','',[
    ('Day 1','Start walking in El Carmen','From Medellín to El Carmen de Viboral and off you go. First night at a farm along the trail.'),
    ('Day 2','Down into the Valle de las Cascadas','Descend into the valley. Night at a family farm inside the valley.'),
    ('Day 3','From the valley to Cascadia','Walk out past waterfalls and pools to Cascadia\'s natural pool.'),
    ('Day 4','Your choice','Chocolate from bean to bar, or whitewater on the Calderas.'),
    ('Day 5','Onward','Bus to Medellín or Bogotá: we buy your ticket.')])}),
 ('melcocho','melcocho-nado',6,3,'1.645.000','2.425.000',{
  'es':('Cascadia y el río Melcocho','Cascadia → río Melcocho → Cascadia','Tres días río arriba por el cañón del Melcocho y vuelta a Cascadia para descansar con masaje o cacao.','Después de la caminata vuelves en 4x4 a Cascadia, una hora de camino.',[
    ('Día 1','Llegada a Cascadia','Bosque, aves y una piscina natural para empezar.'),
    ('Día 2','Al cañón del Melcocho','Pozas cristalinas y noche en finca junto al río.'),
    ('Día 3','Río arriba','Todo el día por el río: saltos desde rocas y caminos campesinos.'),
    ('Día 4','De vuelta a Cascadia','Último baño en el río y en 4x4 a Cascadia.'),
    ('Día 5','Masaje o cacao','Día libre: un masaje junto a la cascada o un tour de cacao, tú eliges.'),
    ('Día 6','Sigue tu viaje','Bus a Medellín o Bogotá: nosotros compramos tu tiquete.')]),
  'en':('Cascadia and the Melcocho river','Cascadia → Melcocho river → Cascadia','Three days upriver through the Melcocho canyon, then back to Cascadia to rest with a massage or cacao.','After the hike a 4x4 takes you back to Cascadia, about one hour.',[
    ('Day 1','Arrival at Cascadia','Forest, birds and a natural pool to start.'),
    ('Day 2','Into the Melcocho canyon','Crystal-clear pools and a night at a riverside farm.'),
    ('Day 3','Upriver','A full day along the river: rock jumps and farm trails.'),
    ('Day 4','Back to Cascadia','A last swim in the river, then a 4x4 to Cascadia.'),
    ('Day 5','Massage or cacao','Free day: a massage by the waterfall or a cacao tour, you choose.'),
    ('Day 6','Onward','Bus to Medellín or Bogotá: we buy your ticket.')])}),
 ('medellin-sonson','valle-cascadas-rio',4,4,'1.110.000','1.670.000',{
  'es':('De Medellín a Sonsón, a pie','El Carmen de Viboral → Valle de las Cascadas → Cascadia → río Melcocho → Guayaquil (Sonsón)','Cuatro días seguidos caminando: valle, selva y río, y de Sonsón en bus de vuelta a Medellín.','Cuatro días de caminata sin día de descanso: para caminantes en buena forma.',[
    ('Día 1','El Carmen al Valle','De Medellín a El Carmen de Viboral y a pie hasta el Valle de las Cascadas. Noche en finca.'),
    ('Día 2','Del valle a Cascadia','Cascadas y pozas hasta Cascadia, con piscina natural para las piernas cansadas.'),
    ('Día 3','Río Melcocho hasta Santa Rita','Al cañón del río Melcocho y río arriba hasta Santa Rita. Noche en finca.'),
    ('Día 4','De Santa Rita a Guayaquil (Sonsón)','De Santa Rita a la vereda Guayaquil en Sonsón, y bus de vuelta a Medellín.')]),
  'en':('From Medellín to Sonsón on foot','El Carmen de Viboral → Valle de las Cascadas → Cascadia → Melcocho river → Guayaquil (Sonsón)','Four days of walking in a row: valley, jungle and river, then a bus from Sonsón back to Medellín.','Four hiking days without a rest day: for fit walkers.',[
    ('Day 1','El Carmen to the valley','From Medellín to El Carmen de Viboral, then on foot into the Valle de las Cascadas. Night at a farm.'),
    ('Day 2','From the valley to Cascadia','Waterfalls and pools all the way to Cascadia, with a natural pool for tired legs.'),
    ('Day 3','Melcocho river to Santa Rita','Into the Melcocho canyon and upriver to Santa Rita. Night at a farm.'),
    ('Day 4','Santa Rita to Guayaquil (Sonsón)','From Santa Rita to the village of Guayaquil in Sonsón, and a bus back to Medellín.')])}),
 ('bogota-guayaquil','guayaquil-bosque',4,4,'1.260.000','1.765.000',{
  'es':('De Bogotá a Sonsón, ruta corta','Bogotá → Cascadia → río Melcocho → Guayaquil (Sonsón)','Llegas desde Bogotá, descansas en Cascadia y cruzas la selva hasta Sonsón en dos días.','Desde Bogotá son más de 8 horas en bus. Más rápido: vuelo a Rionegro y 4x4 hasta Cocorná.',[
    ('Día 1','De Bogotá a la selva','Llegas a Cascadia y te bajas el viaje en la piscina natural.'),
    ('Día 2','Día libre o aventura','Cacao o rafting en el Calderas.'),
    ('Día 3','Río Melcocho hasta Santa Rita','Al cañón del río Melcocho y río arriba hasta Santa Rita. Noche en finca.'),
    ('Día 4','De Santa Rita a Guayaquil (Sonsón)','De Santa Rita a la vereda Guayaquil en Sonsón, y bus a Medellín.')]),
  'en':('From Bogotá to Sonsón, short route','Bogotá → Cascadia → Melcocho river → Guayaquil (Sonsón)','Arrive from Bogotá, rest at Cascadia and cross the jungle to Sonsón in two days.','From Bogotá the bus takes over 8 hours. Faster: fly to Rionegro and take a 4x4 to Cocorná.',[
    ('Day 1','From Bogotá to the jungle','Arrive at Cascadia and unwind in the natural pool.'),
    ('Day 2','Free day or adventure','Cacao or rafting on the Calderas.'),
    ('Day 3','Melcocho river to Santa Rita','Into the Melcocho canyon and upriver to Santa Rita. Night at a farm.'),
    ('Day 4','Santa Rita to Guayaquil (Sonsón)','From Santa Rita to the village of Guayaquil in Sonsón, and a bus to Medellín.')])}),
 ('paramo','sonson-montana',6,5,'1.800.000','2.545.000',{
  'es':('La gran travesía: Melcocho y páramo de Sonsón','Bogotá → Cascadia → río Melcocho → páramo de Sonsón → Sonsón','Nuestra ruta más exigente: cuatro días del cañón del Melcocho al páramo, entre frailejones y niebla.','La ruta más dura, para caminantes con experiencia. Desde Bogotá: más de 8 horas en bus, o vuelo a Rionegro y 4x4.',[
    ('Día 1','De Bogotá a la selva','Llegas a Cascadia y te bajas el viaje en la piscina natural.'),
    ('Día 2','Día libre o aventura','Cacao o rafting en el Calderas.'),
    ('Día 3','Empieza la travesía','El cañón del río Melcocho y sus pozas cristalinas.'),
    ('Día 4','Río arriba','Por caminos campesinos hacia el nacimiento del Melcocho.'),
    ('Día 5','El páramo','Subida al páramo de Sonsón: frailejones, niebla y aire frío.'),
    ('Día 6','Hasta Sonsón','Último tramo hasta Sonsón y bus a Medellín, unas 3 horas.')]),
  'en':('The great crossing: Melcocho and the Sonsón páramo','Bogotá → Cascadia → Melcocho river → Sonsón páramo → Sonsón','Our toughest route: four days from the Melcocho canyon up to the páramo, among frailejones and mist.','Our hardest route, for experienced hikers. From Bogotá: over 8 hours by bus, or fly to Rionegro and take a 4x4.',[
    ('Day 1','From Bogotá to the jungle','Arrive at Cascadia and unwind in the natural pool.'),
    ('Day 2','Free day or adventure','Cacao or rafting on the Calderas.'),
    ('Day 3','The crossing begins','The Melcocho canyon and its crystal-clear pools.'),
    ('Day 4','Upriver','Along farm trails towards the source of the Melcocho.'),
    ('Day 5','The páramo','Climb to the Sonsón páramo: frailejones, mist and cold air.'),
    ('Day 6','To Sonsón','Last stretch to Sonsón and a bus to Medellín, about 3 hours.')])}),
]

BLOCKS = {
 'es':[('Valle de las Cascadas','1 a 3 días','La Piñuela','La Piñuela o Cascadia'),
       ('El Carmen → Valle → Cascadia','3 días','El Carmen de Viboral','Cascadia'),
       ('Río Melcocho','2 o 3 días','Cascadia','Cascadia'),
       ('Melcocho → Guayaquil','2 días','Cascadia','Sonsón → bus a Medellín'),
       ('Melcocho → páramo de Sonsón','4 días','Cascadia','Sonsón → bus a Medellín'),
       ('Descanso en Cascadia','1 a 3 noches','Medellín, Bogotá o tras una caminata','Cualquier caminata')],
 'en':[('Valle de las Cascadas','1 to 3 days','La Piñuela','La Piñuela or Cascadia'),
       ('El Carmen → valley → Cascadia','3 days','El Carmen de Viboral','Cascadia'),
       ('Melcocho river','2 or 3 days','Cascadia','Cascadia'),
       ('Melcocho → Guayaquil','2 days','Cascadia','Sonsón → bus to Medellín'),
       ('Melcocho → Sonsón páramo','4 days','Cascadia','Sonsón → bus to Medellín'),
       ('Rest at Cascadia','1 to 3 nights','Medellín, Bogotá or after a hike','Any hike')],
}

T = {
 'es':dict(home='Inicio',crumb='Inspiración',h1='Rutas por Cocorná, de 4 a 6 días',
   lead='Caminatas de varios días, noches en fincas campesinas y descanso en Cascadia. Combina los bloques a tu gusto: nosotros compramos tus tiquetes de bus al siguiente destino.',
   days='días',diff='Dificultad',from_='Desde',pp='p.p. en grupo de 4',pair='Pareja',ppp='p.p.',excl='Precio indicativo. Tiquetes de bus aparte: nosotros los compramos por ti.',bus='Tiquetes de bus aparte: nosotros los compramos por ti.',
   want='Quiero esta ruta',msg='Hola, me interesa la ruta "{n}" ({d} días). Me pueden enviar una propuesta?',
   bh='Arma tu propia ruta con bloques',bl='Cada bloque tiene un inicio y un final fijo. Los unimos con bus o 4x4, y tú eliges el orden.',
   bcols=('Bloque','Duración','Empieza en','Termina en'),
   ctah='¿Otra combinación en mente?',ctal='Cuéntanos cuántos días tienes y qué te gusta. Armamos tu ruta.',ctab='Arma tu ruta por WhatsApp',ctam='Hola, quiero armar una ruta de varios días en Cocorná.',
   title='Rutas de 4 a 6 días por Cocorná · Wilder Cocorná',
   desc='Rutas de 4 a 6 días por Cocorná: Valle de las Cascadas, río Melcocho y páramo de Sonsón, con noches en fincas campesinas.',
   alt='Ruta {n}, Cocorná'),
 'en':dict(home='Home',crumb='Inspiration',h1='Routes through Cocorná, 4 to 6 days',
   lead='Multi-day hikes, nights on rural farms and time to rest at Cascadia. Combine the building blocks as you like: we buy your bus tickets to the next destination.',
   days='days',diff='Difficulty',from_='From',pp='p.p. in a group of 4',pair='Couple',ppp='p.p.',excl='Indicative price. Bus tickets extra: we buy them for you.',bus='Bus tickets extra: we buy them for you.',
   want='I want this route',msg='Hi, I\'m interested in the route "{n}" ({d} days). Can you send me a proposal?',
   bh='Build your own route from blocks',bl='Each block has a fixed start and end point. We link them by bus or 4x4, and you choose the order.',
   bcols=('Block','Duration','Starts in','Ends in'),
   ctah='Another combination in mind?',ctal='Tell us how many days you have and what you enjoy. We will build your route.',ctab='Plan your route on WhatsApp',ctam='Hi, I want to plan a multi-day route in Cocorná.',
   title='4- to 6-day routes through Cocorná · Wilder Cocorná',
   desc='4- to 6-day routes through Cocorná, Colombia: Valle de las Cascadas, the Melcocho river and the Sonsón páramo, with nights on rural farms.',
   alt='{n} route, Cocorná'),
}

SHOW_PRICES = False
def price_html(t,p4,p2):
    if SHOW_PRICES:
        return f'<div class="rprice"><p><strong>{t["from_"]} COP {p4}</strong> {t["pp"]} · {t["pair"]}: COP {p2} {t["ppp"]}</p><p class="small muted">{t["excl"]}</p></div>'
    return f'<p class="small muted">{t["bus"]}</p>'

def dots(n):
    return ''.join(f'<span class="d{" on" if i<n else ""}"></span>' for i in range(5))

def main_html(lang, A):
    t = T[lang]
    out = [f'''
<section class="insp-hero"><img src="{A}img/cascada-alta.webp" alt="{'Cascada alta entre la selva de Cocorná' if lang=='es' else 'Tall waterfall in the Cocorná jungle'}" fetchpriority="high">
<div class="th-in wrap"><p class="crumbs light"><a href="../">{t['home']}</a> / {t['crumb']}</p><h1>{t['h1']}</h1>
<p class="insp-lead">{t['lead']}</p></div></section>
<section class="wrap section" style="padding-bottom:0"><nav class="chips">''' + ''.join(f'<a href="#{rid}">{d[lang][0]} · {days} {t["days"]}</a>' for rid,_,days,_,_,_,d in R) + '</nav></section>']
    for k,(rid,img,days,diff,p4,p2,d) in enumerate(R):
        name,route,tag,note,ds = d[lang]
        lis = ''.join(f'<li><span class="rd-day">{a}</span><span class="rd-t">{b}</span><span class="rd-l">{c}</span></li>' for a,b,c in ds)
        out.append(f'''<section class="plan route" id="{rid}"><div class="wrap section">
<div class="rgrid"><div class="rpic"><img src="{A}img/{img}.webp" alt="{t['alt'].format(n=name)}" loading="lazy"></div>
<div class="stack rinfo"><p class="kicker">{days} {t['days']} · <span class="diff" aria-label="{t['diff']} {diff}/5">{dots(diff)}</span> {t['diff']} {diff}/5</p>
<h2>{name}</h2><p class="rroute">{route}</p><p class="muted">{tag}</p>
{f'<p class="rnote">{note}</p>' if note else ''}
<ol class="rdays">{lis}</ol>
{price_html(t,p4,p2)}
<a class="btn wa" href="{wa(t['msg'].format(n=name,d=days))}" target="_blank" rel="noopener">{t['want']}</a></div></div></div></section>''')
    rows = ''.join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{e}</td></tr>' for a,b,c,e in BLOCKS[lang])
    out.append(f'''<section class="wrap section"><div class="stack" style="gap:10px"><h2>{t['bh']}</h2><p class="muted">{t['bl']}</p></div>
<div class="btable"><table><thead><tr>{''.join(f'<th>{c}</th>' for c in t['bcols'])}</tr></thead><tbody>{rows}</tbody></table></div></section>
<section class="wrap section"><div class="cta">
 <div class="stack" style="gap:10px"><h2>{t['ctah']}</h2><p class="muted">{t['ctal']}</p></div>
 <a class="btn wa big" href="{wa(t['ctam'])}" target="_blank" rel="noopener">{t['ctab']}</a>
</div></section>
''')
    return '\n'.join(out)

CSS = '''
/* routes inspiración */
.route .section{gap:0}
.rgrid{display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:start}
.route:nth-of-type(odd) .rpic{order:2}
.rpic{border-radius:14px;overflow:hidden;aspect-ratio:4/3}
.rpic img{width:100%;height:100%;object-fit:cover}
.rinfo{gap:12px}
.rinfo .kicker{color:var(--accent);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.diff{display:inline-flex;gap:3px}
.diff .d{width:9px;height:9px;border-radius:50%;border:1.5px solid var(--accent)}
.diff .d.on{background:var(--accent)}
.rroute{font-weight:600;color:var(--green)}
.rnote{background:#fff;border-left:3px solid var(--accent);padding:10px 14px;font-size:15px;line-height:22px}
.rdays{list-style:none;margin:6px 0 4px;padding:0;border-left:2px solid var(--line)}
.rdays li{display:grid;grid-template-columns:70px 1fr;column-gap:12px;padding:8px 0 8px 16px;position:relative}
.rdays li:before{content:"";position:absolute;left:-6px;top:15px;width:10px;height:10px;border-radius:50%;background:var(--green)}
.rd-day{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);padding-top:3px}
.rd-t{font-family:"Source Serif 4",Georgia,serif;font-weight:600;color:var(--green);font-size:18px;line-height:24px}
.rd-l{grid-column:2;font-size:15px;line-height:22px;color:var(--muted)}
.rprice p{margin:0}
.rprice .small{font-size:13px;margin-top:2px}
.route .btn.wa{border-radius:999px;align-self:flex-start}
.btable{overflow-x:auto;margin-top:20px}
.btable table{width:100%;border-collapse:collapse;font-size:15px}
.btable th{text-align:left;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);padding:10px 12px}
.btable td{border-bottom:1px solid var(--line);padding:12px;vertical-align:top}
@media (max-width:820px){.rgrid{grid-template-columns:1fr;gap:20px}.route:nth-of-type(odd) .rpic{order:0}.rdays li{grid-template-columns:58px 1fr}}
'''

# ---- awwwards-versie (25 nov): filter op begin/eind, routelijn, rustige motion ----
EXTRA = {
 'esencial': {'es':(['Medellín','Aeropuerto de Rionegro (MDE)','Bogotá'],['Medellín','Aeropuerto de Rionegro (MDE)','Bogotá'],'Antes o después de cualquier caminata'),
              'en':(['Medellín','Rionegro airport (MDE)','Bogotá'],['Medellín','Rionegro airport (MDE)','Bogotá'],'Before or after any hike')},
 'carmen-cascadia': {'es':(['El Carmen de Viboral'],['Medellín','Aeropuerto de Rionegro (MDE)','Bogotá'],'Llegada a El Carmen desde Medellín o el aeropuerto de Rionegro. Sigue con el río Melcocho o la ruta a Sonsón'),
              'en':(['El Carmen de Viboral'],['Medellín','Rionegro airport (MDE)','Bogotá'],'Reach El Carmen from Medellín or Rionegro airport. Continue with the Melcocho river or the route to Sonsón')},
 'melcocho': {'es':(['Medellín','Aeropuerto de Rionegro (MDE)','Bogotá'],['Medellín','Aeropuerto de Rionegro (MDE)','Bogotá'],'Empieza con la caminata desde El Carmen'),
              'en':(['Medellín','Rionegro airport (MDE)','Bogotá'],['Medellín','Rionegro airport (MDE)','Bogotá'],'Start with the hike from El Carmen')},
 'medellin-sonson': {'es':(['El Carmen de Viboral'],['Sonsón → bus a Medellín (3 h)'],'Llegada a El Carmen desde Medellín o el aeropuerto de Rionegro. Termina en otra región: ideal para seguir hacia el sur'),
              'en':(['El Carmen de Viboral'],['Sonsón → bus to Medellín (3 h)'],'Reach El Carmen from Medellín or Rionegro airport. Ends in another region: ideal to continue south')},
 'bogota-guayaquil': {'es':(['Bogotá','Medellín','Aeropuerto de Rionegro (MDE)'],['Sonsón → bus a Medellín (3 h)'],'Llega desde Bogotá y sal por Medellín'),
              'en':(['Bogotá','Medellín','Rionegro airport (MDE)'],['Sonsón → bus to Medellín (3 h)'],'Arrive from Bogotá, leave via Medellín')},
 'paramo': {'es':(['Bogotá','Medellín','Aeropuerto de Rionegro (MDE)'],['Sonsón → bus a Medellín (3 h)'],'Llega desde Bogotá y sal por Medellín'),
              'en':(['Bogotá','Medellín','Rionegro airport (MDE)'],['Sonsón → bus to Medellín (3 h)'],'Arrive from Bogotá, leave via Medellín')},
}
TAGS = {'esencial':'loop bogota','carmen-cascadia':'carmen','melcocho':'loop bogota','medellin-sonson':'carmen sonson','bogota-guayaquil':'bogota sonson','paramo':'bogota sonson'}
FILTERS = {'es':[('all','Todas'),('bogota','Sale de Bogotá'),('carmen','Sale de El Carmen'),('loop','Ida y vuelta'),('sonson','Termina en Sonsón')],
           'en':[('all','All'),('bogota','From Bogotá'),('carmen','From El Carmen'),('loop','Round trip'),('sonson','Ends in Sonsón')]}
T2 = {'es':dict(start='Empieza en',end='Termina en',combo='Combina',daybyday='Ver día a día',kick='6 rutas · 4 a 6 días · Cocorná, Antioquia',
          h1='Rutas por Cocorná',sub='de 4 a 6 días',filt='Filtrar rutas',
          lead='Bloques de varios días con inicio y final claros, fáciles de encajar en tu viaje. Nosotros compramos los tiquetes de bus al siguiente destino.'),
      'en':dict(start='Starts in',end='Ends in',combo='Combine',daybyday='Day by day',kick='6 routes · 4 to 6 days · Cocorná, Colombia',
          h1='Routes through Cocorná',sub='4 to 6 days',filt='Filter routes',
          lead='Multi-day blocks with clear start and end points, easy to fit into your trip. We buy the bus tickets to the next destination.')}

MTN='<svg viewBox="0 0 24 16" aria-hidden="true"><path d="M1 15 L8 4 L11 8 L15 1 L23 15 Z"/></svg>'
def lvl(n,lang):
    w='Aventura' if lang=='es' else 'Adventure'
    tt=('Nivel de aventura %d de 5' if lang=='es' else 'Adventure level %d of 5')%n
    ic=''.join(f'<i class="{"on" if i<n else ""}">{MTN}</i>' for i in range(5))
    return f'<span class="lvl" title="{tt}"><span class="lvl-i">{ic}</span><span class="lvl-t">{w} {n}/5</span></span>'

def main_html(lang, A):
    t = T[lang]; t2 = T2[lang]
    radios = ''.join(f'<input type="radio" name="rf" id="rf-{k}" class="rf-in"{" checked" if k=="all" else ""}><label for="rf-{k}" class="rf-chip">{v}</label>' for k,v in FILTERS[lang])
    cards=[]
    for n,(rid,img,days,diff,p4,p2,d) in enumerate(R):
        name,route,tag,note,ds = d[lang]
        st,en,combo = EXTRA[rid][lang]
        pills=lambda xs,c: ''.join(f'<span class="rp {c}">{x}</span>' for x in xs)
        lis=''.join(f'<li><b>{a}</b> {b}</li>' for a,b,c in ds)
        notehtml = f'<p class="rc-note">{note}</p>' if note else ''
        cards.append(
          f'<article class="rcard" id="{rid}" data-tags="{TAGS[rid]}">'
          f'<div class="rc-pic"><img src="{A}img/{img}.webp" alt="{t["alt"].format(n=name)}" loading="lazy" width="800" height="450"><span class="rc-days">{days} {t["days"]}</span></div>'
          f'<div class="rc-body"><p class="rc-meta">{lvl(diff,lang)}</p>'
          f'<h2 class="rc-h">{name}</h2><p class="rc-route">{route}</p>'
          f'<div class="rc-line"><span class="rc-trail" aria-hidden="true"></span><div class="rc-pt s"><span class="rc-lab">{t2["start"]}</span><span class="rc-pills">{pills(st,"s")}</span></div>'
          f'<div class="rc-pt e"><span class="rc-lab">{t2["end"]}</span><span class="rc-pills">{pills(en,"e")}</span></div></div>'
          f'<p class="rc-combo"><span class="rc-lab">{t2["combo"]}</span> {combo}</p>{notehtml}'
          f'<details class="rc-det"><summary>{t2["daybyday"]}</summary><ol>{lis}</ol></details>'
          f'<a class="btn wa rc-btn" href="{wa(t["msg"].format(n=name,d=days))}" target="_blank" rel="noopener">{t["want"]}</a></div></article>')
    L=t['bcols']
    rows = ''.join(f'<tr><td data-l="{L[0]}"><strong>{a}</strong></td><td data-l="{L[1]}">{b}</td><td data-l="{L[2]}">{c}</td><td data-l="{L[3]}">{e}</td></tr>' for a,b,c,e in BLOCKS[lang])
    heroalt = 'Cascada alta entre la selva de Cocorná' if lang=='es' else 'Tall waterfall in the Cocorná jungle'
    ths = ''.join(f'<th>{c}</th>' for c in t['bcols'])
    return (f'\n<section class="insp-hero insp-hero-s"><img src="{A}img/cascada-alta.webp" alt="{heroalt}" fetchpriority="high">'
      f'<div class="th-in wrap"><p class="crumbs light"><a href="../">{t["home"]}</a> / {t["crumb"]}</p><p class="rx-kick">{t2["kick"]}</p>'
      f'<h1 class="rx-h1">{t2["h1"]} <em>{t2["sub"]}</em></h1><p class="insp-lead">{t2["lead"]}</p></div></section>\n'
      f'<section class="wrap section rx-routes"><div class="rfilter" role="group" aria-label="{t2["filt"]}">{radios}'
      f'<div class="rcards">{"".join(cards)}</div></div><p class="small muted" style="margin-top:14px">{t["bus"]}</p></section>\n'
      f'<section class="rx-band"><div class="wrap section"><div class="stack" style="gap:8px"><h2>{t["bh"]}</h2><p>{t["bl"]}</p></div>'
      f'<div class="btable"><table><thead><tr>{ths}</tr></thead><tbody>{rows}</tbody></table></div></div></section>\n'
      f'<section class="wrap section"><div class="cta"><div class="stack" style="gap:10px"><h2>{t["ctah"]}</h2><p class="muted">{t["ctal"]}</p></div>'
      f'<a class="btn wa big" href="{wa(t["ctam"])}" target="_blank" rel="noopener">{t["ctab"]}</a></div></section>\n')

CSS = open('/home/claude/insp_routes.css',encoding='utf-8').read()

def patch(path, lang, A):
    s = open(path, encoding='utf-8').read()
    i = s.index('<main id="main">') + len('<main id="main">'); j = s.index('</main>')
    s = s[:i] + main_html(lang, A) + s[j:]
    t = T[lang]
    s = re.sub(r'<title>.*?</title>', f'<title>{t["title"]}</title>', s, count=1)
    for pat,val in [(r'(<meta name="description" content=")[^"]*', t['desc']),(r'(<meta property="og:title" content=")[^"]*', t['title']),(r'(<meta property="og:description" content=")[^"]*', t['desc'])]:
        s = re.sub(pat, lambda m: m.group(1)+val, s, count=1)
    open(path,'w',encoding='utf-8').write(s)

if __name__ == '__main__':
    root = sys.argv[1]
    patch(f'{root}/es/inspiracion/index.html','es','../../')
    patch(f'{root}/inspiracion/index.html','en','../')
    css = open(f'{root}/style.css',encoding='utf-8').read()
    k=css.find('\n/* routes inspiración */')
    if k>=0: css=css[:k]
    open(f'{root}/style.css','w',encoding='utf-8').write(css+CSS)
    print('ok')
