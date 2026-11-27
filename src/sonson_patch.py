import re,sys
ROOT=sys.argv[1]
C={'es':('''<section class="tsec exp"><h2>Así es la ruta</h2>
<p>Duermes en fincas de familias campesinas que cocinan delicioso y te reciben con mucho cariño. Muchas veces en los cuartos de los hijos: ya se fueron de la casa y en la finca viven los abuelos. Camas sencillas, alojamiento rural y sin lujos. Eso es justo la experiencia, y tu visita les ayuda de verdad a estas familias.</p>
<p>Para el camino te empacan <b>fiambre</b>: el almuerzo típico envuelto en hoja de plátano, que comes directo de la hoja.</p>
<p>En el camino ves quebradas y cascadas, y hay pozas para nadar. La ruta sube bastante, así que toca caminar con constancia. Arriba, hacia Sonsón, hace más frío.</p>
<p class="exp-note"><b>Lleva:</b> un buen saco para el frío y vestido de baño.</p></section>
''','es'),
'en':('''<section class="tsec exp"><h2>What it's like</h2>
<p>You sleep on small farms run by country families who cook wonderfully and make you feel at home. Often in the children's rooms: the kids have moved out and the grandparents still live on the farm. Simple beds, rural and basic stays, and that is exactly the experience. Your stay also really helps these families.</p>
<p>For the trail they pack you a <b>fiambre</b>: a traditional lunch wrapped in a banana leaf, which you eat straight from the leaf.</p>
<p>Along the way you pass streams and waterfalls, with pools to swim in. The route climbs a lot, so you need to keep a steady pace. Higher up, towards Sonsón, it gets colder.</p>
<p class="exp-note"><b>Bring:</b> a warm sweater and swimwear.</p></section>
''','en')}
for lang,f in (('es',ROOT+'/es/expediciones/melcocho-sonson-paramo/index.html'),('en',ROOT+'/expediciones/melcocho-sonson-paramo/index.html')):
    s=open(f).read()
    s=re.sub(r'<section class="tsec exp">.*?</section>\n','',s,flags=re.S)
    s=s.replace('<section class="tsec two-cards">',C[lang][0]+'   <section class="tsec two-cards">',1)
    open(f,'w').write(s)
print('ok')
