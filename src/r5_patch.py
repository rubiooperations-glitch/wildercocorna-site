import re,sys,glob,collections
ROOT=sys.argv[1]
JS='<script id="r5js">(function(){var last;document.addEventListener("click",function(e){last=e.target.closest?e.target.closest("a"):null},true);addEventListener("pageswap",function(e){if(!e.viewTransition||!last)return;var c=last.closest(".tile,.tcard,.rcard,.teaser")||last;var i=c.querySelector("img");if(i){i.style.viewTransitionName="hero-img";e.viewTransition.finished.then(function(){i.style.viewTransitionName=""})}});var f=document.querySelectorAll("form,.cta,.site-footer,.og");if("IntersectionObserver"in window&&f.length){var on=new Set();var io=new IntersectionObserver(function(es){es.forEach(function(x){x.isIntersecting?on.add(x.target):on.delete(x.target)});document.body.classList.toggle("wa-hide",on.size>0)});f.forEach(function(el){io.observe(el)})}})()</script>'
n=0
for f in glob.glob(ROOT+'/**/*.html',recursive=True):
    s=open(f).read(); o=s
    s=re.sub(r'<script id="r5js">.*?</script>\n?','',s,flags=re.S)
    s=s.replace('</body>',JS+'\n</body>',1)
    # duplicate tile titles -> add duration
    tiles=list(re.finditer(r'<a class="tile[^"]*"[^>]*>(.*?)</a>',s,re.S))
    def parts(m):
        b=m.group(1); h=re.search(r'<h3>([^<]*)</h3>',b); me=re.search(r'class="meta">([^<·]*)',b)
        return h,me
    names=[]
    for m in tiles:
        h,me=parts(m)
        if h: names.append(h.group(1).split(' · ')[0])
    cnt=collections.Counter(names)
    for m in reversed(tiles):
        h,me=parts(m)
        if not h or not me: continue
        base=h.group(1).split(' · ')[0]
        if cnt[base]>1 and ' · ' not in h.group(1):
            dur=me.group(1).strip().split(' / ')[0]
            a=m.start(1)+h.start(1); b=m.start(1)+h.end(1)
            s=s[:a]+base+' · '+dur+s[b:]
    # first tile image eager + high priority (LCP)
    i=s.find('<a class="tile"')
    if i>0:
        j=s.find('loading="lazy"',i); k=s.find('</a>',i)
        if 0<j<k: s=s[:j]+'loading="eager" fetchpriority="high"'+s[j+len('loading="lazy"'):]
    if s!=o: open(f,'w').write(s); n+=1
# 404: bilingual, cream, trail, no active nav
f=ROOT+'/404.html'; s=open(f).read()
s=s.replace('<a href="/" class=on>Home</a>','<a href="/">Home</a>')
new=('<section class="nf"><div class="wrap section narrow nf-in"><p class="kicker">Error 404</p>'
 '<h1>Este sendero no existe.<span>This trail doesn\'t exist.</span></h1>'
 '<p class="lead muted">Pero en Cocorná hay muchos otros. · But there are plenty of others in Cocorná.</p>'
 '<p class="hroute nf-r"><span class="hr-s">Aquí · Here</span><span class="hr-d" aria-hidden="true"><em>?</em></span><span class="hr-e">Cocorná</span></p>'
 '<div class="row"><a class="btn" href="/es/expediciones/">Ver expediciones</a><a class="btn ghost" href="/expediciones/">See expeditions</a></div></div></section>')
s=re.sub(r'<section class="(?:wrap section narrow" style="min-height:50vh"|nf")>.*?</section>',new,s,count=1,flags=re.S)
open(f,'w').write(s)
print(n)
