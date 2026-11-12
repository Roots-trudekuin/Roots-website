from gen_common import *

def cta_band(title, text, href="Challenge.dc.html", label="Bekijk de Trigger Breakfree Challenge"):
    return f'''<section class="rose" style="padding:90px 0"><div class="wn" style="text-align:center">
<h2 class="h2">{title}</h2><p class="lead">{text}</p>
<a class="btn" href="{href}" style="background:#FFFFFF;color:#333333">{label}</a></div></section>'''

PROG = header("prog") + f'''
{hero("Programma&#8217;s", "Waar je ook begint, het gaat om hetzelfde: <span class=\"cam\">je patroon uitzetten bij de bron.</span>", ["Begin gratis met het handboek. Of stap direct in de Trigger Breakfree Challenge, en werk zeven dagen met &#233;&#233;n patroon van jezelf."], optin_card(), '<a class="btn2" href="Challenge.dc.html">Of bekijk direct de Trigger Breakfree Challenge &#8594;</a>')}
<section style="padding:30px 0 100px"><div class="w">
<div class="card" style="display:flex;gap:56px;align-items:center;flex-wrap:wrap;border:1px solid #BD9D60">
<div style="flex:0 0 360px;max-width:100%">{buycard().split('<p class="cap"')[0]}</div></div>
<div style="flex:1 1 420px;min-width:0">
<p class="kick">Hoofdprogramma &#183; 7 dagen</p>
<h2 class="h2">Trigger Breakfree Challenge</h2>
<p class="p">Je kiest &#233;&#233;n patroon dat je echt kwijt wilt. In zeven dagen ontdek je waartegen het je beschermt, wat het bij j&#243;u aanzet, en hoe het is als het niet meer automatisch aangaat. Elke dag een korte video, &#233;&#233;n ding om te doen, en de community. Ik kijk mee.</p>
<div style="display:flex;gap:24px;align-items:center;flex-wrap:wrap"><a class="btn" href="Challenge.dc.html">Bekijk de Challenge</a><span class="ps">[Prijs] &#183; [Startdatum]</span></div>
</div></div>
<div class="grid2" style="margin-top:40px">
<div class="card" style="display:flex;gap:30px;align-items:center;flex-wrap:wrap"><img src="{COVER}" alt="Omslag Handboek Patroon-Reset" style="width:150px;box-shadow:0 12px 30px rgba(120,95,60,.15)"><div style="flex:1 1 220px"><p class="cap">Gratis</p><h3 class="h3" style="font-size:24px;font-weight:400">Handboek Patroon-Reset</h3><p class="ps" style="margin-bottom:20px">Waarom je patroon terugkomt terwijl je het allang begrijpt. En waar echte verandering begint.</p><a class="btn" href="Optin.dc.html">Stuur mij het handboek</a></div></div>
<div class="card"><p class="cap" style="color:#8E7372">In ontwikkeling</p><h3 class="h3" style="font-size:24px;font-weight:400">ROOTS online programma</h3><p class="ps" style="margin-bottom:20px">In zeven stappen naar een reset. Het volledige programma, voor wie al haar patronen wil leren bijwerken.</p>{tbc("Binnenkort", "Nog niet te koop: geen koopknop. Naam, inhoud en startmoment volgen.")}</div>
</div>
</div></section>
''' + cta_band("Niet zeker waar je begint?", "Begin met het gratis handboek. Of stap direct in de challenge.", "Optin.dc.html", "Stuur mij het gratis handboek") + footer()

def vtile(title, text):
    return f'''<div><div class="vid" style="aspect-ratio:16/9;background:#E9DCCD"><img src="{PORTRAIT}" alt="" style="opacity:.55"><div style="position:absolute;left:0;right:0;bottom:0;padding:18px;background:rgba(250,241,232,.92)"><p class="ps" style="font-weight:600;font-size:15px">{title}</p></div><div class="play">{PLAY}</div></div>
<p class="ps" style="margin:16px 0 10px">{text}</p><a class="btn2" href="Challenge.dc.html">Doe dit met je eigen patroon &#8594;</a></div>'''

VIDEOS = header("vid") + f'''
{hero("Video&#8217;s", "Korte video&#8217;s over waarom je patroon terugkomt, <span class=\"cam\">en wat je eraan kunt doen.</span>", ["Kijk, herken, en ontdek hoe je anders naar je patroon kunt kijken."], optin_card(), '<div style="margin-top:8px">'+tbc("Voorstel", "Er zijn nog geen video&#8217;s. Hieronder voorgestelde onderwerpen; de pagina gaat pas live met echte video&#8217;s. Of: pagina weglaten tot die er zijn.")+'</div>')}
<section style="padding:40px 0 110px"><div class="w"><div class="grid2" style="gap:48px">
{vtile("Waarom je terugvalt terwijl je het allang begrijpt", "Je kent je patroon door en door. Waarom gaat het dan toch nog aan?")}
{vtile("Je verhaal en je neuro-biologie horen bij elkaar", "Wat je verhaal je vertelt, en wat je neuro-biologie ermee doet.")}
{vtile("Je patroon is een kwaliteit in automatische vorm", "Zorgzaamheid, scherpte, verantwoordelijkheid. Waarom je niets van jezelf hoeft af te leren.")}
{vtile("&#8216;Wat zette het d&#237;t keer aan?&#8217;", "De vraag die je na een terugval stelt, bepaalt wat je vindt.")}
</div></div></section>
''' + cta_band("Van kijken naar doen", "In de Trigger Breakfree Challenge werk je zeven dagen met &#233;&#233;n patroon van jezelf.") + footer()

OVER = header("over") + f'''
{hero("De vrouw achter ROOTS", "Hoi, ik ben <span class=\"cam\">Trude.</span>", ["Al meer dan vijfendertig jaar houdt &#233;&#233;n vraag me bezig: hoe help ik mensen zo te veranderen dat ze daar blijvend zelf invloed op krijgen?", "Die vraag bracht me bij ROOTS."], optin_card())}

<section class="sec white"><div class="w"><div class="row top" style="gap:80px">
<div style="flex:0 0 380px" class="photo"><span class="tape"></span><img src="{PORTRAIT}" alt="Portret Trude Kuin"></div>
<div class="c1">
<p class="kick">Waar het begon</p>
<h2 class="h2">Op straat verzon ik de spelletjes.</h2>
<p class="p">Als kind was ik op straat degene met de idee&#235;n. De andere kinderen kwamen erbij en volgden mijn voorstellen. Ik zorgde dat niemand werd gepest. Mensen verbinden en meenemen in iets nieuws: dat zat er al vroeg in.</p>
<p class="p">Later studeerde ik gezondheidskunde. Ik werd trainer van sollicitatieclubs, adviseur, recruiter, en begeleidde mensen bij beroepskeuze en studie. Daarna kwamen coaching, hypnotherapie en Havening erbij. Duizenden gesprekken, steeds dichter bij de kern. Wat speelt er in mensen? Wat houdt ze tegen? En hoe brengen ze hun potentieel in beweging?</p>
</div>
</div></div></section>

<section class="sec"><div class="wn">
<p class="kick">De vraag die ik niet meer losliet</p>
<h2 class="h2">Blij de deur uit. En twee weken later was alles terug.</h2>
<p class="p">In mijn werk zag ik iets wat me niet meer losliet. Mensen kwamen binnen met een rotgevoel en geen perspectief. Ze gingen blij de deur uit. En twee weken later, bij de volgende afspraak, waren alle oude patronen terug.</p>
<p class="quote" style="margin:34px 0">&#8220;Hoe help ik mensen zo te veranderen dat ze daar blijvend zelf invloed op krijgen?&#8221;</p>
<p class="p">Niet afhankelijk van mij. Niet tot de volgende afspraak. Maar zo dat ze het zelf kunnen, ook later.</p>
</div></section>

<section class="sec white"><div class="wn">
<p class="kick">Eerst op mezelf</p>
<h2 class="h2">Mijn eigen patronen waren mijn eerste onderzoeksmateriaal.</h2>
<p class="p">Drie vragen stelde ik altijd. Hoe werkt dit? Waar heb ik invloed op? En hoe gebruik ik die invloed voor wat ik wil bereiken? Die vragen stelde ik ook aan mijn eigen leven.</p>
<p class="p">Mijn eigen patronen waren daardoor niet alleen iets waar ik vanaf wilde. Ze werden onderzoeksmateriaal. Wat ik ontdekte, paste ik eerst op mezelf toe. Daardoor wist ik in mijn praktijk precies waarom ik iets deed, waarop ik werkte en welk resultaat ik wilde.</p>
<div style="margin:30px 0">{tbc("Alleen met jouw akkoord", "In 2014 zat ik op mijn laagste punt. Ziek van de stress na het faillissement van mijn bedrijf, alles kwijt, en geen arts of psycholoog die wist wat te doen. Daar besloot ik: liever alles verliezen dan zo doorgaan. Als niemand me kan helpen helen, dan ga ik het zelf doen. Daar begon wat later ROOTS zou heten.")}</div>
<p class="p">Zo heb ik mezelf bevrijd van patronen die me steeds dezelfde valkuilen lieten herhalen. En gecre&#235;erd wat ik het belangrijkste vond: mijn potentieel volledig gebruiken, voor meer bewustzijn, liefde en creatie.</p>
</div></section>

<section class="sec"><div class="w"><div class="row" style="gap:70px">
<div class="c1" style="flex:0 0 440px"><div class="photo"><span class="tape"></span><img src="/img/trude-2.jpg" alt="Trude Kuin"></div></div>
<div class="c1">
<p class="kick">Hoe ROOTS groeide</p>
<h2 class="h2">Van losse inzichten naar een methode.</h2>
<p class="p">Ik bleef onderzoeken. Mijn eigen ervaringen, en wat de wetenschap ontdekte over verandering. Mijn nieuwsgierigheid zit in het verbinden van invalshoeken. Als ik de samenhang begin te zien, gebeurt er iets waar ik enorm van geniet: wat eerst ingewikkeld leek, wordt behapbaar. En daardoor be&#239;nvloedbaar.</p>
<p class="p">Zo groeide ROOTS. Een methode die lichaam en geest niet scheidt, en je verhaal en je neuro-biologie bij elkaar houdt. Waarmee je je patroon uitzet bij de bron, en leert het daarna zelf bij te stellen.</p>
<p class="quote" style="margin-top:26px">Het meest intieme van jezelf, hoe je je voelt en hoe je denkt, hoort van jou te zijn.</p>
</div>
</div></div></section>

<section class="sec white"><div class="wn" style="text-align:center">
<p class="kick">Waarom ROOTS bestaat</p>
<h2 class="h2">Worden wie je had kunnen zijn. Voordat je over twintig jaar terugkijkt en denkt: had ik dit maar eerder geweten.</h2>
<p class="p">Geen guru. Geen levenslange begeleiding. Een gids die je het ambacht leert, zodat je je patronen zelf kunt bijstellen. Ook later. Zonder mij.</p>
<div style="display:flex;gap:24px;justify-content:center;flex-wrap:wrap;margin-top:34px"><a class="btn" href="Contact.dc.html">Werk met mij</a><a class="btn2" href="Contact.dc.html" style="align-self:center">Of laten we eerst praten &#8594;</a></div>
</div></section>
''' + footer()

def acard(cat, title, text):
    return f'<a href="Artikel.dc.html" class="card" style="padding:0;overflow:hidden;text-decoration:none;color:#333333;display:block"><div class="dots" style="height:150px;background-color:#F3E7DA;opacity:.9"></div><div style="padding:28px"><p class="cap" style="font-size:12px">{cat}</p><h3 class="h3" style="font-weight:400;font-size:21px">{title}</h3><p class="ps" style="margin-bottom:12px">{text}</p><p class="ps" style="color:#8E7372;font-size:13px">Voorbeeldtitel &#183; nog niet geschreven</p></div></a>'

INZICHT = header("inz") + f'''
{hero("Inzicht", "Waarom je patroon terugkomt, <span class=\"cam\">en hoe je er anders naar kijkt.</span>", ["Artikelen en video&#8217;s over terugval, je verhaal en je neuro-biologie. Om te lezen, te kijken en te herkennen."], optin_card(), '<div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:10px"><a class="btn2" href="#artikelen">Artikelen</a><a class="btn2" href="#videos">Video&#8217;s</a></div>')}

<section id="artikelen" class="sec white"><div class="w">
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:30px;flex-wrap:wrap">
<div><p class="kick">Artikelen</p><h2 class="h2" style="margin:0">Lees verder</h2></div>
<div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn2" href="#">Alles</a><a class="btn2" href="#">Terugval in oude patronen</a><a class="btn2" href="#">Je verhaal en je neuro-biologie</a><a class="btn2" href="#">Patronen als kwaliteit</a></div>
</div>
<div style="margin:30px 0">{tbc("Voorstel", "Nog geen artikelen. Categorie&#235;n en titels zijn een voorstel. Elk artikel krijgt een eigen pagina (zie de voorbeeldpagina Artikel), met eigen titel en beschrijving voor zoekmachines.")}</div>
<div class="grid3">
{acard("Terugval in oude patronen", "&#8216;Alweer?! Ik dacht dat ik dit had opgelost.&#8217;", "Waarom een patroon terugkomt terwijl je het allang begrijpt.")}
{acard("Je verhaal en je neuro-biologie", "Waarom nog dieper graven in je verhaal je patroon niet uitzet", "Over het verschil tussen weten waar het vandaan komt en wat het nu aanzet.")}
{acard("Patronen als kwaliteit", "Je overleeft met je kwaliteiten", "Zorgzaamheid, scherpte, verantwoordelijkheid. En wat er gebeurt als ze automatisch worden.")}
</div>
</div></section>

<section id="videos" class="sec"><div class="w">
<p class="kick">Video&#8217;s</p><h2 class="h2">Kijk en herken</h2>
<div style="margin:0 0 30px">{tbc("Voorstel", "Er zijn nog geen video&#8217;s. Onderwerpen hieronder zijn een voorstel. Belangrijke video&#8217;s kunnen een eigen pagina krijgen met begeleidende tekst of transcript.")}</div>
<div class="grid2" style="gap:48px">
{vtile("Waarom je terugvalt terwijl je het allang begrijpt", "Je kent je patroon door en door. Waarom gaat het dan toch nog aan?")}
{vtile("Je verhaal en je neuro-biologie horen bij elkaar", "Wat je verhaal je vertelt, en wat je neuro-biologie ermee doet.")}
{vtile("Je patroon is een kwaliteit in automatische vorm", "Waarom je niets van jezelf hoeft af te leren.")}
{vtile("&#8216;Wat zette het d&#237;t keer aan?&#8217;", "De vraag die je na een terugval stelt, bepaalt wat je vindt.")}
</div>
</div></section>
''' + cta_band("Van lezen en kijken naar doen", "In de Trigger Breakfree Challenge werk je zeven dagen met &#233;&#233;n patroon van jezelf.") + footer()

ARTIKEL = header("inz") + f'''
<section style="padding:70px 0 40px"><div class="w">
<p class="ps" style="font-size:14px"><a href="Inzicht.dc.html">Inzicht</a> &#8250; <a href="Inzicht.dc.html#artikelen">Artikelen</a> &#8250; Terugval in oude patronen</p>
<div style="max-width:900px;margin-top:20px">{tbc("Voorbeeldpagina", "Zo ziet elk artikel eruit. De titel en tekst schrijf jij; hieronder staan alleen opbouw en plekken.")}</div>
</div></section>
<section style="padding:0 0 100px"><div class="w"><div class="row top" style="gap:72px">
<article class="c1" style="flex:1.6 1 0">
<p class="kick">Terugval in oude patronen</p>
<h1 class="h1">&#8216;Alweer?! Ik dacht dat ik dit had opgelost.&#8217;</h1>
<p class="ps" style="color:#8E7372;margin-bottom:34px">Trude Kuin &#183; [datum] &#183; [leestijd]</p>
{tbc("Opening", "Een herkenbare situatie, in de taal van de lezer.")}
<h2 class="h2" style="font-size:28px;margin-top:40px">[Tussenkop die vertelt wat er komt]</h2>
{tbc("Uitleg", "Het inzicht op begripsniveau. Geen stappen uit de methode.")}
<h2 class="h2" style="font-size:28px;margin-top:40px">[Tussenkop]</h2>
{tbc("Voorbeeld", "Een praktijkvoorbeeld of beeld dat het inzicht laat landen.")}
<div class="cardS" style="margin-top:44px;border:1px solid #BD9D60"><p class="cap">Doe dit met je eigen patroon</p><p class="p">In de Trigger Breakfree Challenge werk je zeven dagen met &#233;&#233;n patroon van jezelf.</p><a class="btn" href="Challenge.dc.html">Bekijk de Challenge</a></div>
<div style="margin-top:24px">{tbc("Zoekmachines", "Per artikel: eigen webadres, paginatitel en korte beschrijving.")}</div>
</article>
<aside class="c1" style="flex:1 1 0;position:sticky;top:24px">{optin_card()}
<div style="margin-top:36px"><p class="cap">Lees ook</p>
<p class="p" style="margin:0 0 10px"><a href="Artikel.dc.html">Waarom nog dieper graven in je verhaal je patroon niet uitzet</a></p>
<p class="p" style="margin:0"><a href="Artikel.dc.html">Je overleeft met je kwaliteiten</a></p></div>
</aside>
</div></div></section>
''' + footer()

def bcard(cat, title):
    return f'<div class="card" style="padding:0;overflow:hidden"><div class="dots" style="height:170px;background-color:#F3E7DA;opacity:.9"></div><div style="padding:28px"><p class="cap" style="font-size:12px">{cat}</p><h3 class="h3" style="font-weight:400;font-size:21px">{title}</h3><p class="ps" style="color:#8E7372">Voorbeeldtitel &#183; nog niet geschreven</p></div></div>'

BLOG = header("blog") + f'''
{hero("Blog", "Over terugval, <span class=\"cam\">je verhaal en je neuro-biologie.</span>", ["Artikelen over waarom oude patronen terugkomen, en hoe je er anders naar kijkt."], optin_card())}
<section style="padding:0 0 20px"><div class="wn" style="text-align:center">
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:10px">
<a class="btn2" href="#">Alles</a><a class="btn2" href="#">Terugval in oude patronen</a><a class="btn2" href="#">Je verhaal en je neuro-biologie</a><a class="btn2" href="#">Patronen als kwaliteit</a><a class="btn2" href="#">Ervaringen</a>
</div></div></section>
<section style="padding:40px 0 100px"><div class="w">
<div style="max-width:820px;margin:0 auto 40px">{tbc("Leeg", "Nog geen artikelen. Categorie&#235;n en titels hieronder zijn een voorstel; tot de eerste artikelen er zijn toont de pagina: &#8216;De eerste artikelen volgen binnenkort.&#8217;")}</div>
<div class="grid3">
{bcard("Terugval in oude patronen", "&#8216;Alweer?! Ik dacht dat ik dit had opgelost.&#8217;")}
{bcard("Je verhaal en je neuro-biologie", "Waarom nog dieper graven in je verhaal je patroon niet uitzet")}
{bcard("Patronen als kwaliteit", "Je overleeft met je kwaliteiten")}
</div>
<div class="card" style="margin-top:60px;display:flex;gap:40px;align-items:center;flex-wrap:wrap"><img src="{COVER}" alt="Omslag Handboek Patroon-Reset" style="width:130px"><div style="flex:1 1 300px"><h3 class="h3" style="font-size:24px;font-weight:400">Gratis: Handboek Patroon-Reset</h3><p class="ps">Ontdek waarom je patroon terugkomt terwijl je het allang begrijpt.</p></div><a class="btn" href="Optin.dc.html">Stuur mij het handboek</a></div>
</div></section>
''' + footer()

CONTACT = header("contact") + f'''
<section style="padding:90px 0 110px;position:relative;overflow:hidden"><div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div><div class="w"><div class="row top" style="gap:72px">
<div class="c1" style="flex:1 1 0">
<p class="kick">Contact</p><h1 class="h1">Laten we <span class="cam">praten.</span></h1>
<p class="lead">Een vraag, een idee, of alleen een gevoel dat het tijd is voor iets anders? Vertel het me. Het hoeft nog niet helemaal helder te zijn. Ik lees alles zelf.</p>
<div style="display:flex;flex-direction:column;gap:14px;margin:34px 0 0;max-width:420px">
<a class="btn" href="WA-DIRECT">App me via WhatsApp</a>
<a class="btn2" href="BOOK-KM" style="align-self:flex-start">Gratis kennismaking (20 min) &#8594;</a>
</div>
<p class="kick" style="margin-top:64px">Wat gebeurt er daarna?</p>
<div style="display:flex;flex-direction:column;gap:22px">
<div class="step"><div class="num">1</div><div><h3 class="h3">Ik lees je bericht</h3><p class="ps">Zelf, en met aandacht.</p></div></div>
<div class="step"><div class="num">2</div><div><h3 class="h3">Ik neem contact met je op</h3><p class="ps">Met een antwoord, een vraag terug, of een voorstel voor een kennismaking.</p></div></div>
<div class="step"><div class="num">3</div><div><h3 class="h3">We kijken samen wat past</h3><p class="ps">Eerlijk. Ook als dat betekent dat iets anders beter bij je past.</p></div></div>
</div>
</div>
<div class="c1" style="flex:1.1 1 0">
<form class="buy" id="cform" FORM-ATTR style="padding:40px;position:relative;z-index:1">
<p class="kick" style="margin-bottom:8px">Stuur een bericht</p>
<div class="grid2" style="gap:16px"><div class="field"><label for="c1">Naam *</label><input id="c1" name="naam" type="text" autocomplete="name" required></div>
<div class="field"><label for="c2">E-mailadres *</label><input id="c2" name="email" type="email" autocomplete="email" required></div></div>
<p class="field" style="margin-bottom:10px"><label>Kies hier je thema</label><span class="ps" style="font-size:13px">Meerdere mogelijk</span></p>
<div class="chips"><label class="chip"><input type="checkbox" name="thema" value="Patronen doorbreken"><span>Patronen doorbreken</span></label><label class="chip"><input type="checkbox" name="thema" value="Energieboost"><span>Energieboost</span></label><label class="chip"><input type="checkbox" name="thema" value="Gewoontes veranderen"><span>Gewoontes veranderen</span></label><label class="chip"><input type="checkbox" name="thema" value="Rust in je systeem"><span>Rust in je systeem</span></label><label class="chip"><input type="checkbox" name="thema" value="Relaties"><span>Relaties</span></label><label class="chip"><input type="checkbox" name="thema" value="Je doel bereiken"><span>Je doel bereiken</span></label><label class="chip"><input type="checkbox" name="thema" value="Richting en zingeving"><span>Richting en zingeving</span></label><label class="chip"><input type="checkbox" name="thema" value="Iets anders"><span>Iets anders</span></label></div>
<div class="field" style="margin-top:22px"><label for="c3">Vertel me meer</label><textarea id="c3" name="bericht" rows="7" placeholder="Waar loop je tegenaan, of wat wil je bereiken?"></textarea></div>
<label style="display:flex;gap:10px;font-size:14px;line-height:1.5;margin:4px 0 20px"><input type="checkbox" required> Ik ga akkoord met de <a href="#">privacyverklaring</a>.</label>
<button class="btn" type="submit" style="width:100%">Verstuur &#8594;</button>
</form>
</div>
</div></div></section>
''' + footer()

for name, body, w, h, t in [
    ("Inzicht.dc.html", INZICHT, 1440, 3300, "Inzicht"),
    ("Artikel.dc.html", ARTIKEL, 1440, 1900, "Voorbeeld artikelpagina"),
    ("Over.dc.html", OVER, 1440, 5000, "Over Trude"),
    ("Contact.dc.html", CONTACT, 1440, 1700, "Contact"),
]:
    open('project/' + name, 'w').write(page(t, body, w, h))
print('ok')
