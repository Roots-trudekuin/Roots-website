from gen_common import *

def scene(where, intent, what, after):
    return f'''<div class="row top" style="gap:44px;padding:34px 0;border-top:1px solid #E3D3BF">
<div style="flex:0 0 170px"><p class="cap" style="margin:6px 0 0">{where}</p></div>
<div class="c1"><p class="ps" style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#8E7372;margin-bottom:6px">Wat je je voornam</p><p class="p" style="margin:0">{intent}</p></div>
<div class="c1" style="flex:1.6 1 0"><p class="ps" style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#8E7372;margin-bottom:6px">Wat er gebeurde</p><p class="p" style="margin:0">{what}</p></div>
<div class="c1"><p class="ps" style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#8E7372;margin-bottom:6px">En daarna</p><p class="p" style="margin:0">{after}</p></div>
</div>'''

def wish(title, text):
    return f'''<div class="card" style="padding:36px"><p class="cap">{title}</p><p class="p" style="margin:0">{text}</p></div>'''

HOME = header("home") + f'''
<section id="handboek" style="padding:90px 0 100px;position:relative;overflow:hidden">
<div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div>
<div class="w"><div class="row" style="gap:72px">
<div class="c1" style="flex:1.25 1 0">
<p class="kick">ROOTS &#183; Zet je patroon uit bij de bron</p>
<h1 class="h1">Je kent je patroon door en door. <span class="cam">En toch neemt het je over,</span> nog voordat jij kunt kiezen.</h1>
<p class="lead">Je had je voorgenomen het deze keer anders te doen. Rustig blijven. Nee zeggen. Gewoon luisteren. En dan valt die stilte, klinkt die toon, komt die ene opmerking. Voor je het weet zeg je ja, word je fel of klap je dicht.</p>
<p class="lead" style="margin-bottom:36px">Pas daarna zie je het: daar ging het weer. Terwijl je precies weet waar het vandaan komt.</p>
<div style="display:flex;gap:28px;align-items:center;flex-wrap:wrap">
<a class="btn" href="Optin.dc.html">Ja, stuur mij het gratis handboek</a>
<a class="btn2" href="Programmas.dc.html">Of werk direct met mij &#8594;</a>
</div>
</div>
<div class="c1" style="flex:1 1 0">{optin_card()}</div>
</div></div>
</section>

<section class="rose" style="padding:80px 0"><div class="wn" style="text-align:center">
<p class="quote" style="margin:0;color:#FFFFFF">Het frustrerende is niet dat je niets begrijpt.<br>Het frustrerende is juist dat je z&#243;veel begrijpt, en het toch nog gebeurt.</p>
</div></section>

<section class="sec white"><div class="w">
<p class="kick">Herken je dit?</p>
<h2 class="h2" style="max-width:780px">Je wilde anders reageren. En toch nam het oude het over.</h2>
<div style="margin-top:30px">
{scene("Op je werk", "Deze week neem ik er niets meer bij.", "Je leidinggevende vraagt wie het project oppakt. Er valt een stilte. Je voelt onrust in je borst, je adem stokt even. &#8216;Ik doe het wel.&#8217; Je hoort het jezelf zeggen voordat je het besloten hebt.", "&#8217;s Avonds ben je boos op jezelf. En nu moet je het ook doen.")}
{scene("In je relatie", "Vanavond vertel ik rustig dat ik me alleen voelde.", "Je hebt de woorden klaar. Hij zucht en kijkt op zijn telefoon. En ineens hoor je jezelf scherp worden. Of je zegt &#8216;laat maar&#8217; en loopt de kamer uit.", "Je ligt wakker. Waarom lukt het me nou niet gewoon te zeggen wat ik voel?")}
{scene("In een gesprek", "Ik luister eerst, en reageer daarna.", "Een collega zegt: &#8216;Mag ik je iets meegeven?&#8217; Je wangen worden warm. Je gaat uitleggen, verklaren, verdedigen. Je hoort niet eens meer wat ze eigenlijk zei.", "Achteraf weet je precies wat je liever had gezegd.")}
{scene("Bij familie", "Ik laat me deze keer niet meeslepen.", "Op de verjaardag maakt je moeder die ene opmerking. Binnen een seconde voel je je weer twaalf. Je past je aan, en glimlacht.", "Je rijdt naar huis met een knoop in je maag.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div>
<p class="lead" style="max-width:820px;margin-top:44px">Je weet waar het vandaan komt. Je hebt het onderzocht, gevoeld, besproken. En toch gebeurt het. <span class="cam" style="font-weight:500">Dat is geen kwestie van te weinig inzicht.</span></p>
</div></section>

<section class="sec" style="position:relative;overflow:hidden"><div class="w">
<p class="kick">Stel je voor</p>
<h2 class="h2" style="max-width:820px">Datzelfde moment. <span class="cam">Maar nu loopt het anders.</span></h2>
<div class="grid3" style="margin-top:40px">
{wish("Bij jezelf blijven", "Hij zucht en pakt zijn telefoon. Je merkt het. En je blijft bij jezelf. &#8216;Ik wil je iets vertellen. Wil je even naar me kijken?&#8217; En dan zeg je wat je voelde.")}
{wish("Je grens aangeven", "De stilte valt na de vraag wie het oppakt. Je voelt hem, en je lijf blijft rustig. &#8216;Deze keer niet, mijn week zit vol.&#8217; Zonder uitleg. Zonder schuldgevoel achteraf.")}
{wish("Luisteren zonder verdedigen", "&#8216;Mag ik je iets meegeven?&#8217; Je bent nieuwsgierig in plaats van gespannen. &#8216;Wat bedoel je precies?&#8217; En je hoort het hele verhaal.")}
</div>
<p class="lead" style="max-width:820px;margin-top:48px">Niet omdat je jezelf beter in de hand hebt. Maar omdat het oude patroon niet meer als eerste beslist. Hoe zou dat voelen? En wat zou je doen met al die ruimte?</p>
</div></section>

<section class="sec white"><div class="w"><div class="row" style="gap:80px">
<div class="c1">
<p class="kick">Een andere kijk</p>
<h2 class="h2">Weten waar je patroon vandaan komt, is iets anders dan weten wat het <span class="cam">n&#250;</span> aanzet.</h2>
<p class="p">We zijn opgegroeid met &#233;&#233;n manier van kijken naar patronen: vanuit je geschiedenis. Die manier is niet fout. Ze kijkt alleen niet naar de plek waar het patroon wordt aangezet.</p>
<p class="p">Niet je verhaal zet je patroon aan. Je neuro-biologie doet dat, met een paar stukjes uit je verhaal. Je overlevingssysteem wil je beschermen. En het gebruikt daarvoor oude informatie die nog niet is bijgewerkt.</p>
<p class="p">Dat is geen fout van jou. En het is te veranderen. Bij de bron.</p>
</div>
<div class="c1" style="display:flex;flex-direction:column;gap:18px">
<div class="cardS"><p class="cap" style="color:#8E7372">De vraag die je altijd stelde</p><p class="quote" style="margin:0">&#8220;Waar komt dit vandaan?&#8221;</p></div>
<div style="display:flex;justify-content:center">{ARROW}</div>
<div class="cardS" style="border:1px solid #BD9D60"><p class="cap">De vraag die het verschil maakt</p><p class="quote" style="margin:0">&#8220;Wat zette het d&#237;t keer aan?&#8221;</p></div>
</div>
</div></div></section>

<section class="sec" style="position:relative;overflow:hidden"><div class="w"><div class="row" style="gap:90px">
<div style="flex:0 0 380px;position:relative" class="photo"><div class="dots" style="position:absolute;left:-40px;bottom:-40px;width:220px;height:220px;opacity:.6"></div><span class="tape"></span><img src="{COVER}" alt="Omslag Handboek Patroon-Reset" style="position:relative;box-shadow:0 24px 60px rgba(120,95,60,.18)"></div>
<div class="c1">
<p class="kick">Gratis &#183; Handboek Patroon-Reset</p>
<h2 class="h2">Van inzicht naar blijvende verandering</h2>
<p class="lead">Ontdek waarom je patroon terugkomt terwijl je het allang begrijpt. En waar echte verandering begint.</p>
<ul class="list">
<li>{CHECK}<span>Waarom begrijpen en het automatisch aangaan van je patroon twee verschillende dingen zijn</span></li>
<li>{CHECK}<span>De shift: kijken vanuit je neuro-biologie, niet alleen vanuit je verhaal</span></li>
<li>{CHECK}<span>De drie stappen van ROOTS, op hoofdlijnen</span></li>
<li>{CHECK}<span>Het verhaal van Sanne: dezelfde stilte, een andere uitkomst</span></li>
<li>{CHECK}<span>Met een link naar mijn gratis masterclass</span></li>
</ul>
<div style="display:flex;gap:24px;align-items:center;flex-wrap:wrap"><a class="btn" href="Optin.dc.html">Ja, stuur mij het handboek</a><span class="ps">Elf pagina&#8217;s. Direct in je mailbox.</span></div>
</div>
</div></div></section>

<section class="sec white"><div class="w"><div class="row" style="gap:80px">
<div style="flex:0 0 340px" class="photo"><span class="tape"></span><img src="{PORTRAIT}" alt="Portret Trude Kuin"></div>
<div class="c1">
<p class="kick">Wie ben ik</p>
<h2 class="h2">Ik ben Trude.</h2>
<p class="p">Sinds 1988 begeleid ik mensen bij persoonlijke veranderprocessen. Als consulent, coach, hypnotherapeut en Havening practitioner. Duizenden mensen.</p>
<p class="p">Al die jaren hield &#233;&#233;n vraag me bezig: hoe help ik mensen zo te veranderen dat ze daar blijvend zelf invloed op krijgen? Uit die vraag groeide ROOTS: de methode waarmee je je patroon uitzet bij de bron.</p>
<div style="display:flex;gap:26px;align-items:center;flex-wrap:wrap"><a class="btn" href="Programmas.dc.html">Werk met mij</a><a class="btn2" href="Over.dc.html">Lees mijn verhaal &#8594;</a></div>
</div>
</div></div></section>

<section class="sec"><div class="w">
<p class="kick" style="text-align:center">Waar wil je beginnen?</p>
<h2 class="h2" style="text-align:center;max-width:760px;margin-left:auto;margin-right:auto">Twee wegen. Dezelfde bron.</h2>
<div class="grid2" style="margin-top:50px">
<div class="card"><p class="cap">Eerst begrijpen &#183; gratis</p><h3 class="h3" style="font-size:26px;font-weight:400">Handboek Patroon-Reset</h3><p class="p">Lees waarom je patroon terugkomt, en kijk de masterclass via de link in het handboek. In je eigen tempo.</p><a class="btn" href="Optin.dc.html">Stuur mij het handboek</a></div>
<div class="card" style="border:1px solid #BD9D60"><p class="cap">Direct ervaren &#183; 7 dagen</p><h3 class="h3" style="font-size:26px;font-weight:400">Trigger Breakfree Challenge</h3><p class="p">Je kiest &#233;&#233;n patroon van jezelf. Je ontdekt wat het bij j&#243;u aanzet, en ervaart hoe het is als het niet meer automatisch aangaat. Met mij erbij.</p><a class="btn" href="Challenge.dc.html">Bekijk de Challenge</a></div>
</div>
</div></section>
''' + footer()

def optin(mobile=False):
    return header("home") + f'''
<div style="position:relative;min-height:900px;background:#FAF1E8">
<div class="w hide-m" style="padding-top:90px;opacity:.35"><p class="kick">ROOTS &#183; Zet je patroon uit bij de bron</p><h1 class="h1" style="max-width:700px">Je kent je patroon door en door. En toch neemt het je over, nog voordat jij kunt kiezen.</h1></div>
<div style="position:absolute;inset:0;background:rgba(51,51,51,.42);display:flex;align-items:center;justify-content:center;padding:20px">
<div role="dialog" aria-label="Gratis handboek aanvragen" style="background:#FFFFFF;max-width:900px;width:100%;border-radius:2px;position:relative;display:flex;flex-wrap:wrap">
<button type="button" aria-label="Sluiten" style="position:absolute;right:14px;top:14px;background:transparent;border:0;font-size:26px;color:#333333;width:44px;height:44px;cursor:pointer">&#215;</button>
<div style="flex:1 1 300px;background:#FAF1E8;padding:40px;display:flex;align-items:center;justify-content:center"><img src="{COVER}" alt="Omslag Handboek Patroon-Reset" style="width:100%;max-width:260px;box-shadow:0 18px 40px rgba(120,95,60,.18)"></div>
<div style="flex:1.3 1 340px;padding:48px 44px">
<p class="kick">Gratis handboek</p>
<h2 class="h2" style="font-size:32px;margin-bottom:14px">Handboek Patroon-Reset</h2>
<p class="p" style="font-size:17px">Ontdek waarom je patroon terugkomt terwijl je het allang begrijpt. En waar echte verandering begint.</p>
<form>
<div class="field"><label for="vn">Voornaam</label><input id="vn" type="text" placeholder="Je voornaam"></div>
<div class="field"><label for="em">E-mailadres</label><input id="em" type="email" placeholder="jij@voorbeeld.nl"></div>
<a class="btn" href="Bedankt.dc.html" style="display:block;margin-top:8px">Stuur mij het handboek</a>
</form>
<p class="ps" style="font-size:13px;margin-top:14px">Je krijgt het handboek per e-mail. Af en toe stuur ik je iets waarvan ik denk dat het je verder helpt. Uitschrijven kan altijd. <a href="#">Privacyverklaring</a></p>
<div style="margin-top:16px">{tbc("Koppeling", "Formulier via Plug&amp;Pay of e-maildienst, met automatische mail + doorsturen naar de bedankpagina.")}</div>
</div>
</div></div></div>'''

BEDANKT = header("home") + f'''
<section style="padding:90px 0 100px;position:relative;overflow:hidden"><div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div><div class="w"><div class="row top" style="gap:72px">
<div class="c1" style="flex:1.25 1 0">
<p class="kick">Gelukt</p>
<h1 class="h1">Je handboek is onderweg <span class="cam">naar je mailbox.</span></h1>
<p class="lead">Kijk over een paar minuten in je inbox. Niets gezien? Kijk dan even in je spam- of promotiemap, en zet mijn adres in je contacten.</p>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:36px">
<div class="step"><div class="num">1</div><div><h3 class="h3">Open de mail</h3><p class="ps">Met de link naar je Handboek Patroon-Reset.</p></div></div>
<div class="step"><div class="num">2</div><div><h3 class="h3">Lees het in &#233;&#233;n keer</h3><p class="ps">Elf pagina&#8217;s. Neem er een kop thee bij.</p></div></div>
<div class="step"><div class="num">3</div><div><h3 class="h3">Kijk de masterclass</h3><p class="ps">De link staat in het handboek.</p></div></div>
</div>
</div>
<div class="c1" style="flex:1 1 0">{buycard("Challenge.dc.html")}</div>
</div></div></section>

<section class="sec white"><div class="w"><div class="row" style="gap:70px">
<div class="c1">
<p class="kick">Wil je niet wachten?</p>
<h2 class="h2">In het handboek lees je d&#225;t het zo werkt. In de challenge ga je het doen.</h2>
<p class="p">Begrijpen hoe je patroon aangaat, is waardevol. Maar je patroon verandert niet door een handboek te lezen. Het verandert als je het bij jezelf doet. Met &#233;&#233;n patroon van jezelf. Zeven dagen. Met mij erbij.</p>
<a class="btn" href="Challenge.dc.html">Bekijk de Trigger Breakfree Challenge</a>
</div>
</div></div></section>

<section style="padding:70px 0"><div class="wn" style="text-align:center">
<p class="cap">Gratis community</p>
<p class="p">Wil je delen wat je ontdekt, en lezen hoe anderen met hun patronen aan de slag gaan? Kom in mijn gratis Skool-community.</p>
<a class="btn2" href="#">Naar de community &#8594;</a>
<div style="margin-top:20px">{tbc("Community", "Naam en link van de nieuwe Skool-community nog niet besloten.")}</div>
</div></section>
''' + footer()

import os
os.makedirs('project', exist_ok=True)
for name, body, w, h, t in [
    ("Main.dc.html", HOME, 1440, 5600, "Homepage – Start hier"),
    ("M-Home.dc.html", HOME, 390, 9800, "Homepage mobiel"),
    ("Optin.dc.html", optin(), 1440, 1000, "Opt-in handboek"),
    ("M-Optin.dc.html", optin(True), 390, 1100, "Opt-in mobiel"),
    ("Bedankt.dc.html", BEDANKT, 1440, 2500, "Bedankt handboek"),
]:
    open('project/' + name, 'w').write(page(t, body, w, h))
print('ok')
