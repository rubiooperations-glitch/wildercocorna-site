import re,sys
ROOT=sys.argv[1]
FINCA={'es':'<p>Duermes en fincas de familias campesinas que cocinan delicioso y te reciben con mucho cariño. Muchas veces en los cuartos de los hijos: ya se fueron de la casa y en la finca viven los abuelos. Camas sencillas, alojamiento rural y sin lujos. Eso es justo la experiencia, y tu visita les ayuda de verdad a estas familias.</p>\n<p>Para el camino te empacan <b>fiambre</b>: el almuerzo típico envuelto en hoja de plátano, que comes directo de la hoja.</p>\n',
 'en':"<p>You sleep on small farms run by country families who cook wonderfully and make you feel at home. Often in the children's rooms: the kids have moved out and the grandparents still live on the farm. Simple beds, rural and basic stays, and that is exactly the experience. Your stay also really helps these families.</p>\n<p>For the trail they pack you a <b>fiambre</b>: a traditional lunch wrapped in a banana leaf, which you eat straight from the leaf.</p>\n"}
H={'es':'Así es la ruta','en':"What it's like"}
WATER={'es':'<p>En el camino ves quebradas y cascadas, y hay pozas para nadar.</p>\n','en':'<p>Along the way you pass streams and waterfalls, with pools to swim in.</p>\n'}
SONSON={'es':'<p>En el camino ves quebradas y cascadas, y hay pozas para nadar. La ruta sube bastante, así que toca caminar con constancia. Arriba, hacia Sonsón, hace más frío.</p>\n','en':'<p>Along the way you pass streams and waterfalls, with pools to swim in. The route climbs a lot, so you need to keep a steady pace. Higher up, towards Sonsón, it gets colder.</p>\n'}
NOTE={'es':('<p class="exp-note"><b>Lleva:</b> un buen saco para el frío y vestido de baño.</p>','<p class="exp-note"><b>Lleva:</b> vestido de baño y ropa para cambiarte.</p>'),
      'en':('<p class="exp-note"><b>Bring:</b> a warm sweater and swimwear.</p>','<p class="exp-note"><b>Bring:</b> swimwear and a change of clothes.</p>')}
ITIN={'es':('Itinerario',[('Día 1','Salida desde El Retiro hacia el cañón del río Melcocho. Primeros baños en pozas naturales y noche en finca campesina.'),('Día 2','Río arriba entre quebradas, cascadas y pozas para nadar. Noche en otra finca, con comida casera.'),('Día 3','Subida hacia el nacimiento del río, con la opción de llegar al páramo. Más altura y más frío. Noche en finca.'),('Día 4','Último tramo hasta Manzanares Arriba, en Sonsón.')]),
      'en':('Itinerary',[('Day 1','Set off from El Retiro into the Melcocho river canyon. First swims in natural pools and a night on a country farm.'),('Day 2','Upriver past streams, waterfalls and pools to swim in. Night on another farm, with home cooking.'),('Day 3','Climb towards the source of the river, with the option to reach the páramo. Higher and colder. Night on a farm.'),('Day 4','Last stretch to Manzanares Arriba, in Sonsón.')])}
PAGES=['valle-de-las-cascadas-2-dias','valle-de-las-cascadas-3-dias','melcocho-2-dias','jungle-trekking-melcocho','melcocho-sonson-paramo']
for slug in PAGES:
  for lang,f in (('es',f'{ROOT}/es/expediciones/{slug}/index.html'),('en',f'{ROOT}/expediciones/{slug}/index.html')):
    s=open(f).read()
    s=re.sub(r'<section class="tsec exp">.*?</section>\n\s*','',s,flags=re.S)
    s=re.sub(r'<section class="tsec itin-x">.*?</section>\n\s*','',s,flags=re.S)
    son=slug=='melcocho-sonson-paramo'
    sec=f'<section class="tsec exp"><h2>{H[lang]}</h2>\n'+FINCA[lang]+(SONSON if son else WATER)[lang]+NOTE[lang][0 if son else 1]+'</section>\n   '
    s=s.replace('<section class="tsec two-cards">',sec+'<section class="tsec two-cards">',1)
    if son:
      t,days=ITIN[lang]
      li=''.join(f'<li><span class="tl-k">{a}</span><p>{b}</p></li>' for a,b in days)
      it=f'<section class="tsec itin-x"><h2>{t}</h2><ol class="timeline">{li}</ol></section>\n   '
      s=s.replace('<section class="tsec"><div class="gallery">',it+'<section class="tsec"><div class="gallery">',1)
    open(f,'w').write(s)
print('ok')
