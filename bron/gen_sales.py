from gen_common import *

def pair(now, then):
    return f'''<div class="grid2" style="gap:48px;padding:26px 0;border-top:1px solid #E3D3BF">
<div style="display:flex;gap:16px">{DASH}<p class="p" style="margin:0">{now}</p></div>
<div style="display:flex;gap:16px">{CHECK}<p class="p" style="margin:0">{then}</p></div></div>'''

def flow(items, accent):
    out = []
    for i, t in enumerate(items):
        border = '1px solid #BD9D60' if accent else '1px solid #E0CFC0'
        bg = '#FFFFFF' if accent else '#F6EEE6'
        out.append(f'<div style="background:{bg};border:{border};padding:18px 22px;border-radius:2px;text-align:center"><p class="ps" style="font-size:16px">{t}</p></div>')
        if i < len(items) - 1:
            out.append(f'<div style="display:flex;justify-content:center;padding:6px 0">{ARROW}</div>')
    return ''.join(out)

def faq(q, a):
    return f'<div style="padding:28px 0;border-top:1px solid #E3D3BF"><h3 class="h3" style="font-weight:500">{q}</h3><p class="p" style="margin:0">{a}</p></div>'

FORK = '''<svg width="300" height="190" viewBox="0 0 300 190" fill="none" aria-hidden="true"><path d="M150 186 V110 C150 80 120 60 60 40 M150 110 C150 80 180 60 240 40" stroke="#BD9D60" stroke-width="2.2"></path><path d="M150 186 V110" stroke="#BD9D60" stroke-width="2.2"></path><circle cx="60" cy="40" r="7" fill="#BEA8A7"></circle><circle cx="240" cy="40" r="7" fill="#BD9D60"></circle><circle cx="150" cy="176" r="10" fill="#FFFFFF" stroke="#BD9D60" stroke-width="2"></circle></svg>'''

CHALLENGE = header("prog") + f'''
<section style="padding:90px 0 110px;position:relative;overflow:hidden"><div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div><div class="w"><div class="row top" style="gap:72px">
<div class="c1" style="flex:1.25 1 0">
<p class="kick">Trigger Breakfree Challenge &#183; 7 dagen</p>
<h1 class="h1">Stel je voor dat je oude patroon <span class="cam">niet meer automatisch beslist</span> hoe jij reageert.</h1>
<p class="lead" style="margin-bottom:56px">Dat je in die vergadering, in dat gesprek, op die verjaardag gewoon zelf kiest. Zeven dagen, &#233;&#233;n patroon van jezelf, met mij erbij.</p>
<p class="kick">Wat is het?</p>
<h2 class="h2">Wat is de Trigger Breakfree Challenge?</h2>
<p class="p">Een week waarin je niet n&#243;g meer over je patroon gaat begrijpen. Je gaat het bij jezelf doen.</p>
<p class="p">Je kiest &#233;&#233;n patroon dat je echt kwijt wilt. Het ja zeggen terwijl je nee bedoelt. Het fel worden. Het dichtklappen. Het harder werken. Het uitleggen. En in zeven dagen ontdek je waartegen het je beschermt, wat het bij j&#243;u aanzet, en hoe het is als het niet meer automatisch aangaat.</p>
<p class="p">Elke dag een korte video van mij. Elke dag &#233;&#233;n ding om te doen, in je eigen week, in je eigen leven. En een community met mensen die dit herkennen, waarin je deelt wat je merkt. Ik kijk mee.</p>
</div>
<div class="c1" style="flex:1 1 0;position:sticky;top:24px">{buycard()}</div>
</div></div></section>

<section class="sec white"><div class="wn">
<p class="kick">Je kent dit</p>
<h2 class="h2">Je wist het. Je had het je voorgenomen. En toch.</h2>
<p class="p">Een opmerking. Een bepaalde toon. Iemand die afstand neemt. Een stilte die net te lang duurt. En voor je het goed en wel doorhebt, gebeurt precies datgene waarvan je dacht dat je er inmiddels voorbij was. Je past je aan. Je trekt je terug. Je gaat pleasen. Je wordt fel. Je werkt harder. Of je begint jezelf uit te leggen.</p>
<p class="p">En pas daarna denk je: verdorie. Nu doe ik het w&#233;&#233;r.</p>
<p class="p">Dan begint het zoeken opnieuw. Wat heb ik nog niet gezien? Moet ik nog verder terug? Heb ik het nog niet goed genoeg gevoeld?</p>
<p class="lead cam" style="font-weight:500;margin-top:30px">Je kunt precies vertellen waar je patroon vandaan komt. Maar dat voorkomt niet dat het opnieuw gebeurt.</p>
</div></section>

<section class="sec"><div class="w">
<div class="grid2" style="gap:48px;margin-bottom:10px"><div><p class="kick">Nu</p><h2 class="h2" style="font-size:32px">Wat er nu gebeurt</h2></div><div><p class="kick">Stel je voor</p><h2 class="h2" style="font-size:32px">Hetzelfde moment, een andere ervaring</h2></div></div>
{pair("In de vergadering valt een stilte. &#8216;Ik doe het wel.&#8217; Het is eruit voordat je het besloten hebt.", "Dezelfde stilte. Je lijf blijft rustig. Je kiest zelf of je iets oppakt.")}
{pair("Je partner zegt iets op die ene toon. Je wordt fel, of je trekt je terug.", "Je hoort de toon. Je blijft bij jezelf, en zegt wat je eigenlijk bedoelde.")}
{pair("Een collega geeft feedback. Je gaat uitleggen, verdedigen, verklaren.", "Je hoort wat er gezegd wordt, zonder dat de oude reactie het gesprek overneemt.")}
{pair("Achteraf weet je precies wat je liever had gedaan. Maar op het moment zelf leek die keuze er niet te zijn.", "De keuze is er gewoon. Niet spectaculair. Vaak heel gewoon.")}
{pair("Na een terugval begint het zelfverwijt. &#8216;Zie je wel. Het ligt aan mij.&#8217;", "Terugval is informatie. &#8216;H&#233;. Interessant. Mijn systeem beschermt me nog ergens tegen.&#8217;")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>

<section class="sec white"><div class="w">
<div class="wn" style="padding:0;text-align:center;max-width:820px;margin:0 auto">
<p class="kick">Waarom inzicht niet genoeg is</p>
<h2 class="h2">Weten waar het vandaan komt, verandert nog niet wat het <span class="cam">n&#250;</span> aanzet.</h2>
<p class="p">Je verhaal helpt je begrijpen wat er in je leven is gebeurd. Je neuro-biologie bepaalt hoe oude informatie nu nog automatisch meespeelt. Je overlevingssysteem gebruikt een paar stukjes uit je verhaal om je te beschermen. Sneller dan jij kunt denken. Daarom helpt al je begrip je op het moment zelf niet.</p>
</div>
<div class="grid2" style="margin-top:56px;gap:56px;max-width:980px;margin-left:auto;margin-right:auto">
<div><p class="cap" style="text-align:center;color:#8E7372">De oude kijk</p>
{flow(["Er gebeurt iets kleins: een stilte, een toon, een blik", "De oude reactie neemt het over", "Achteraf: &#8216;Waar komt dit vandaan?&#8217;", "Nog een laag, nog verder terug, nog een verklaring", "Volgende keer: precies hetzelfde &#8635;"], False)}</div>
<div><p class="cap" style="text-align:center">De nieuwe kijk</p>
{flow(["Er gebeurt iets kleins: een stilte, een toon, een blik", "Je vraagt: &#8216;Wat zette het d&#237;t keer aan?&#8217;", "Je ziet hoe je neuro-biologie een paar stukjes uit je verhaal gebruikt om je te beschermen", "Precies daar werk je mee, met &#233;&#233;n patroon", "Dezelfde situatie. Je keuze is er nog."], True)}</div>
</div>
<div class="cardS" style="max-width:980px;margin:60px auto 0;display:flex;gap:40px;align-items:center;flex-wrap:wrap">
<div style="flex:1 1 420px"><h3 class="h3" style="font-size:24px;font-weight:400">Je patroon is niet het probleem. Het automatisme is het probleem.</h3><p class="p" style="margin:0">Je patroon is een kwaliteit in zijn automatische vorm. Zorgzaamheid, scherpte, aanvoelen, verantwoordelijkheid nemen. Je hoeft niets van jezelf af te leren. Je krijgt iets terug: de keuze.</p></div>
<a class="btn" href="Afrekenen.dc.html">Ja, ik doe mee</a>
</div>
</div></section>

<section class="sec"><div class="w"><div class="row top" style="gap:80px">
<div style="flex:0 0 420px">
<div class="photo"><span class="tape"></span><img src="{PORTRAIT}" alt="Portret Trude Kuin"></div>
<div class="vid hide-m" style="margin-top:28px;aspect-ratio:16/9;background:#E9DCCD"><div class="play">{PLAY}</div></div>
<div style="margin-top:12px">{tbc("Video", "Persoonlijke video: Trude over waarom ROOTS bestaat &#8212; nog op te nemen.")}</div>
</div>
<div class="c1">
<p class="kick">Hoe ROOTS ontstond</p>
<h2 class="h2">E&#233;n vraag die ik niet meer losliet.</h2>
<p class="p">In mijn eerste jaren in dit werk zag ik iets wat me bleef dwarszitten. Mensen kwamen binnen met een rotgevoel en geen perspectief. Ze gingen blij de deur uit. En twee weken later, bij de volgende afspraak, waren alle oude patronen terug.</p>
<p class="quote" style="margin:30px 0">&#8220;Hoe help ik mensen zo te veranderen dat ze daar blijvend zelf invloed op krijgen?&#8221;</p>
<p class="p">Sinds 1988 begeleid, train en adviseer ik mensen bij persoonlijke veranderprocessen. Als consulent, coach, hypnotherapeut en Havening practitioner. Duizenden mensen. En steeds stelde ik dezelfde drie vragen. Hoe werkt dit? Waar heb ik invloed op? En hoe gebruik ik die invloed voor wat ik wil bereiken?</p>
<p class="p">Die vragen stelde ik ook aan mijn eigen leven. Mijn eigen patronen werden mijn eerste onderzoeksmateriaal. Wat ik ontdekte, paste ik eerst op mezelf toe.</p>
<div style="margin:6px 0 24px">{tbc("Alleen met jouw akkoord", "In 2014 zat ik op mijn laagste punt. Ziek, alles kwijt, geen arts die wist wat te doen. Daar besloot ik: als niemand me kan helpen helen, dan ga ik het zelf doen. Daar begon wat later ROOTS zou heten.")}</div>
<p class="p">Het antwoord zat niet in nog een laag van het verhaal. Het zat in hoe de neuro-biologie dat verhaal gebruikt. Toen ik die samenhang zag, werd wat eerst ingewikkeld leek behapbaar. En daardoor be&#239;nvloedbaar. Zo groeide ROOTS.</p>
</div>
</div></div></section>

<section class="sec white"><div class="wn">
<p class="kick">De volgende stap</p>
<h2 class="h2">Begrijpen is niet hetzelfde als ervaren.</h2>
<p class="p">In het handboek en de masterclass laat ik je zien d&#225;t het zo werkt. E&#233;n ding laat ik daar niet zien: hoe je het stukje vindt dat bij j&#243;u het alarm aanzet, en hoe die koppeling wordt verbroken.</p>
<p class="p">Niet omdat het geheim is. Omdat het pas werkt als je het doet. Met &#233;&#233;n patroon van jezelf. En met iemand erbij die ziet wat jij op dat moment niet ziet.</p>
<p class="lead cam" style="font-weight:500">Daarom is er de Trigger Breakfree Challenge.</p>
</div></section>

<section class="sec"><div class="w">
<p class="kick">Uit de praktijk</p>
<h2 class="h2" style="max-width:760px">Hoe dat er in het echte leven uitziet</h2>
<div class="row top" style="gap:56px;margin-top:20px">
<div class="c1 card">
<p class="cap">Sanne, 46, HR-manager</p>
<p class="p">Sanne kent haar patroon door en door. Ze pakt alles op. Jaren therapie, stapels boeken. Ze weet precies waar het vandaan komt. Na haar burn-out pakt ze het echt anders aan: minder uren, grenzen, nee zeggen. Het gaat maanden goed.</p>
<p class="p">Dan valt in een vergadering een stilte na de vraag wie het project oppakt. &#8216;Ik doe het wel.&#8217; Ze hoort het zichzelf zeggen voordat ze het besloten heeft.</p>
<p class="p">Een paar weken later valt weer die stilte. Sanne merkt het op, maar haar lijf blijft rustig. Ze denkt: ik hoef niets. Een collega zegt: &#8216;Ik doe het wel.&#8217;</p>
<p class="p" style="margin:0"><span class="cam" style="font-weight:600">Ze is nog steeds iemand die dingen oppakt. Nu als ze het kiest.</span></p>
<p class="ps" style="margin-top:18px;font-size:13px;color:#7A6A5A">Praktijkvoorbeeld uit het Handboek Patroon-Reset.</p>
</div>
<div class="c1">
<h3 class="h3" style="font-size:24px;font-weight:400">Hoe dat voelt</h3>
<p class="p">Niet spectaculair. Vaak heel gewoon. Je zit in een situatie die je vroeger meteen meenam, en je merkt dat je keuze er nog is. Je voelt wat je voelt, je denkt wat je denkt, en het oude patroon neemt het niet over.</p>
<p class="quote" style="margin:30px 0">Dat is waar vrijheid begint. Niet doordat je jezelf beter beheerst, maar doordat je overlevingsprogramma niet meer aan het stuur zit.</p>
</div>
</div>
<div class="grid3" style="margin-top:56px">
{tbc("Ervaring deelnemer", "Echte ervaring uit de eerste groep, met naam en toestemming. Volgt na de try-out.")}
{tbc("Ervaring deelnemer", "Echte ervaring uit de eerste groep, met naam en toestemming. Volgt na de try-out.")}
{tbc("Ervaring deelnemer", "Echte ervaring uit de eerste groep, met naam en toestemming. Volgt na de try-out.")}
</div>
</div></section>

<section class="sec white"><div class="w"><div class="row top" style="gap:72px">
<div class="c1">
<p class="kick">Het aanbod</p>
<h2 class="h2">Dit krijg je in de Trigger Breakfree Challenge</h2>
<ul class="list">
<li>{CHECK}<span><b style="font-weight:600">Zeven korte video&#8217;s van mij.</b> Elke dag &#233;&#233;n, zodat je weet wat je doet en waarom.</span></li>
<li>{CHECK}<span><b style="font-weight:600">Elke dag &#233;&#233;n ding om te doen.</b> In je eigen week, in je eigen leven.</span></li>
<li>{CHECK}<span><b style="font-weight:600">E&#233;n patroon van jezelf.</b> Geen theorie over patronen in het algemeen. Jouw patroon is het werkmateriaal.</span></li>
<li>{CHECK}<span><b style="font-weight:600">De community.</b> Met anderen die dit herkennen. Je deelt wat je merkt, en ik kijk mee.</span></li>
</ul>
<h3 class="h3" style="margin-top:44px;font-size:24px;font-weight:400">Zo ziet de week eruit</h3>
<div class="grid2" style="gap:16px;margin-top:20px">
<div class="cardS" style="padding:26px"><p class="cap" style="margin-bottom:6px">Dag 1&#8211;2 &#183; In kaart</p><p class="ps">Je patroon, de vicieuze cirkel, en waartegen het je beschermt.</p></div>
<div class="cardS" style="padding:26px"><p class="cap" style="margin-bottom:6px">Dag 3&#8211;4 &#183; Opsporen</p><p class="ps">Wat het bij jou aanzet.</p></div>
<div class="cardS" style="padding:26px"><p class="cap" style="margin-bottom:6px">Dag 5&#8211;6 &#183; Verbreken</p><p class="ps">De koppeling, zodat het alarm niet meer afgaat.</p></div>
<div class="cardS" style="padding:26px"><p class="cap" style="margin-bottom:6px">Dag 7 &#183; Versterken</p><p class="ps">Wat je w&#233;l wilt automatiseren.</p></div>
</div>
<div style="margin-top:16px">{tbc("Dagindeling", "Overgenomen uit masterclass v4.2 (&#8216;aanpassen zodra de challenge af is&#8217;). Plus: tijd per dag, platform van de community, terugkijken.")}</div>
<div class="grid2" style="margin-top:50px;gap:36px">
<div><h3 class="h3">Voor jou als</h3><ul class="list"><li style="font-size:16px">{CHECK}<span>je je patroon allang begrijpt, en het je toch nog overneemt</span></li><li style="font-size:16px">{CHECK}<span>je &#233;&#233;n patroon echt kwijt wilt</span></li><li style="font-size:16px">{CHECK}<span>je het bij jezelf wilt ervaren, niet alleen begrijpen</span></li></ul></div>
<div><h3 class="h3">Niet voor jou als</h3><ul class="list"><li style="font-size:16px">{DASH}<span>je nog meer inzicht zoekt. Daar heb je genoeg van.</span></li></ul></div>
</div>
</div>
<div style="flex:0 0 400px">{buycard()}</div>
</div></div></section>

<section class="sec"><div class="wn">
<p class="kick">&#8220;Maar&#8230;&#8221;</p>
<h2 class="h2">Misschien denk je nu&#8230;</h2>
{faq("&#8220;Ik heb al zoveel gedaan.&#8221;", "Precies daarom. Alles wat je deed, werkte op je verhaal, je begrip of je gedrag. Dit werkt op de laag eronder.")}
{faq("&#8220;Moet ik weer terug naar vroeger?&#8221;", "Nee. We zoeken geen nieuwe verklaring. We zoeken het stukje dat je overlevingssysteem gebruikt. Dat is iets anders dan je geschiedenis opnieuw vertellen.")}
{faq("&#8220;Ik ben te gevoelig, te complex.&#8221;", "Een gevoelig systeem reageert sneller, ja. Het werkt ook sneller bij. Dat je veel voelt, is hier geen nadeel.")}
{faq("&#8220;Is dit weer zo&#8217;n snelle belofte?&#8221;", "Eerlijk: het is &#233;&#233;n week, met &#233;&#233;n patroon. Je gaat niet al je patronen tegelijk te lijf. Je ervaart bij &#233;&#233;n patroon wat er verandert als je op deze laag werkt.")}
<p class="kick" style="margin-top:60px">Praktisch</p>
{faq("Hoeveel tijd kost het per dag?", "[Tijd per dag &#8212; bevestigen]")}
{faq("Start iedereen tegelijk?", "[Bevestigen &#8212; je overweegt de eerste keer online met een groep tegelijk te starten]")}
{faq("Wat gebeurt er na betaling?", "Je krijgt direct een bevestigingsmail met je toegang en de startdatum. [Toegangsroute bevestigen]")}
{faq("Kan ik later terugkijken?", "[Bevestigen]")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>

<section class="sec white"><div class="w"><div class="row top" style="gap:64px">
<div class="c1">
<p class="kick">Geen verrassingen</p>
<h2 class="h2">Je weet vooraf precies wat je koopt.</h2>
<p class="p">Zeven dagen met &#233;&#233;n patroon van jezelf. Elke dag een korte video en &#233;&#233;n ding om te doen. De community, waarin ik meekijk. Een vraag vooraf? Stuur me een bericht. Ik antwoord zelf.</p>
<a class="btn2" href="Contact.dc.html">Stel je vraag &#8594;</a>
<div style="margin-top:26px">{tbc("Garantie of annulering", "Nog niets vastgesteld, dus de pagina belooft niets. Wil je een geld-terug- of annuleringsregeling? Jouw besluit.")}</div>
</div>
<div class="c1">
<p class="kick">Zo meld je je aan</p>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:10px">
<div class="step"><div class="num">1</div><p class="p" style="margin:8px 0 0">Klik op &#8216;Ja, ik doe mee&#8217;.</p></div>
<div class="step"><div class="num">2</div><p class="p" style="margin:8px 0 0">Reken veilig af via Plug&amp;Pay.</p></div>
<div class="step"><div class="num">3</div><p class="p" style="margin:8px 0 0">Je krijgt direct een mail met je toegang tot de community.</p></div>
<div class="step"><div class="num">4</div><p class="p" style="margin:8px 0 0">Op [startdatum] begint dag 1.</p></div>
</div>
<a class="btn" href="Afrekenen.dc.html" style="margin-top:30px">Ja, ik doe mee</a>
</div>
</div></div></section>

<section class="sec"><div class="wn" style="text-align:center">
<h2 class="h2">Wanneer je tot hier hebt gelezen, vraag jezelf dan dit af&#8230;</h2>
<div style="display:flex;justify-content:center;margin:20px 0 30px">{FORK}</div>
</div>
<div class="wn">
<p class="lead">Stel je voor dat er een splitsing in de weg is.</p>
<p class="p">Links ga je verder zoals je gewend bent. Bij de volgende terugval zoek je opnieuw in je verhaal. Nog een laag, nog verder terug, nog een verklaring. Dat is niet fout. Het heeft je veel gegeven. Alleen zet het je patroon niet uit.</p>
<p class="p">Rechts kijk je de volgende keer niet terug, maar naar wat het n&#250; aanzet. Met &#233;&#233;n patroon van jezelf. Zeven dagen. Met mij erbij.</p>
<div class="card" style="margin:36px 0"><p class="p" style="margin:0"><span class="cam" style="font-weight:600">Even dromen.</span> Stel dat het patroon er straks gewoon niet meer is. Niet onderdrukt, niet gemanaged. Je zit in dat gesprek, die vergadering, dat familiediner. En er gebeurt niks. Wat doe je dan met al die ruimte?</p></div>
<p class="lead">Je hoeft niet opnieuw te beginnen. Alles wat je deed telt. Het miste &#233;&#233;n laag. Die laag doen we in de challenge.</p>
<p class="lead">En het gaat je zeker lukken!</p>
<p class="lead cam" style="font-weight:500">Liefs, Trude</p>
<div style="text-align:center;margin-top:40px"><a class="btn" href="Afrekenen.dc.html">Ja, ik doe mee met de Trigger Breakfree Challenge</a></div>
</div></section>

<section class="sec white"><div class="wn">
<div class="cardS" style="border:1px solid #BD9D60">
<p class="cap">PS &#8212; voor wie snel naar beneden scrolde</p>
<ul class="list">
<li>{CHECK}<span>Voor wie haar patroon allang begrijpt, en merkt dat het haar toch nog overneemt</span></li>
<li>{CHECK}<span>7 dagen, &#233;&#233;n patroon van jezelf, elke dag een korte video en &#233;&#233;n ding om te doen</span></li>
<li>{CHECK}<span>Samen in de community, en ik kijk mee</span></li>
<li>{CHECK}<span>Je ontdekt wat het bij jou aanzet, en ervaart hoe het is als het niet meer automatisch aangaat</span></li>
</ul>
{tbc("Prijs en start", "[Prijs] &#183; [Startdatum] &#183; [garantie/annulering indien besloten]")}
<a class="btn" href="Afrekenen.dc.html" style="display:block;margin-top:22px">Ja, ik doe mee</a>
</div>
</div></section>
''' + footer()

MASTERCLASS = header(minimal=True) + f'''
<section style="padding:90px 0 60px;position:relative;overflow:hidden"><div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div><div class="w"><div class="row top" style="gap:72px">
<div class="c1" style="flex:1.25 1 0">
<p class="kick">Gratis masterclass</p>
<h1 class="h1">Zet je patroon uit <span class="cam">bij de bron</span></h1>
<p class="lead">Waarom je patroon terugkomt terwijl je het allang begrijpt. En wat er w&#233;l nodig is om het bij te werken.</p>
<div class="vid" style="aspect-ratio:16/9;margin-top:10px"><img src="{PORTRAIT}" alt="Still uit de masterclass"><div class="play">{PLAY}</div></div>
<div style="margin-top:14px">{tbc("Video", "Masterclassvideo (&#177; [duur] minuten) &#8212; Trude neemt hem nu op. Geluid start pas na klik; ondertiteling als die er is.")}</div>
</div>
<div class="c1" style="flex:1 1 0;position:sticky;top:24px"><div class="buy">
<p class="cap">Je volgende stap</p>
<h2 class="h2" style="font-size:26px;margin-bottom:22px">Doe het met &#233;&#233;n patroon van jezelf</h2>
<div style="border:1px solid #BD9D60;padding:22px;border-radius:2px">
<p class="cap" style="margin-bottom:6px">1 &#183; Nu starten</p>
<h3 class="h3">Individueel programma</h3>
<p class="ps" style="font-size:15px;margin-bottom:16px">8 online sessies met mij, op jouw patroon. &#8364;1.335</p>
<a class="btn" href="Individueel.dc.html" style="display:block">Ja, ik wil nu starten</a></div>
<div style="border:1px solid #E0CFC0;padding:22px;border-radius:2px;margin-top:16px">
<p class="cap" style="margin-bottom:6px">2 &#183; In een groep</p>
<h3 class="h3">Trigger Breakfree Challenge</h3>
<p class="ps" style="font-size:15px;margin-bottom:16px">7 dagen, met de community erbij. Start 14 december.</p>
<a class="btn" href="Challenge.dc.html" style="display:block" data-chal-info>Bekijk de Challenge</a></div>
</div></div>
</div></div></section>

<section style="padding:20px 0 90px"><div class="w"><div style="max-width:740px">
<h2 class="h2" style="font-size:30px">In deze masterclass vertel ik:</h2>
<ul class="list">
<li>{CHECK}<span>waarom inzicht en het aangaan van je patroon twee verschillende processen zijn, en waarom al je begrip je op het moment zelf niet helpt</span></li>
<li>{CHECK}<span>wat je patroon werkelijk aanzet, en waarom dat niet je verhaal is</span></li>
<li>{CHECK}<span>waarom je het daar niet met begrip of oefenen bereikt, en wat er w&#233;l nodig is om het bij te werken</span></li>
</ul>
</div></div></section>

<section class="sec white"><div class="w">
<div class="wn" style="padding:0;text-align:center;max-width:820px;margin:0 auto">
<p class="kick">En nu?</p>
<h2 class="h2">Begrijpen is niet hetzelfde als ervaren.</h2>
<p class="p">In de masterclass laat ik zien d&#225;t het zo werkt. Je patroon verandert pas als je het bij jezelf doet, met &#233;&#233;n patroon van jezelf en met iemand erbij die ziet wat jij op dat moment niet ziet. Je kunt kiezen hoe.</p>
</div>
<div class="grid2" style="margin-top:46px;max-width:980px;margin-left:auto;margin-right:auto">
<div class="card" style="border:1px solid #BD9D60;background:#FAF1E8"><p class="cap">1 &#183; Nu starten &#183; &#233;&#233;n op &#233;&#233;n</p><h3 class="h3" style="font-size:26px;font-weight:400">Individueel programma</h3><p class="p">Acht online sessies met mij. Dezelfde stappen als in de Challenge, volledig afgestemd op jouw patroon en jouw tempo. Je kunt meteen beginnen.</p><p class="ps" style="font-weight:600;margin-bottom:20px">&#8364;1.335 &#183; 8 online sessies</p><a class="btn" href="Individueel.dc.html">Ja, ik wil nu starten</a></div>
<div class="card" style="background:#FAF1E8"><p class="cap">2 &#183; In een groep &#183; 7 dagen</p><h3 class="h3" style="font-size:26px;font-weight:400">Trigger Breakfree Challenge</h3><p class="p">Zeven dagen, &#233;&#233;n patroon van jezelf. Elke dag een korte video en &#233;&#233;n ding om te doen, samen met anderen die dit herkennen. Ik kijk mee.</p><p class="ps" style="font-weight:600;margin-bottom:20px" data-chal-date>Start 14 december</p><a class="btn" href="Challenge.dc.html" data-chal-info>Bekijk de Challenge</a></div>
</div>
</div></section>
<section style="padding:40px 0"><div class="w" style="text-align:center"><p class="ps">&#169; TrudeThecla &#183; <a href="#">Privacyverklaring</a></p></div></section>
'''

AFREKENEN = header(minimal=True) + f'''
<section style="padding:70px 0 100px"><div class="w">
<div style="max-width:900px;margin-bottom:24px">{tbc("Voorbeeld", "Zo kan de Plug&amp;Pay-checkout worden ingericht. Het echte afrekenen gebeurt in Plug&amp;Pay; alle bedragen en betaalmethoden daar bevestigen.")}</div>
<p class="kick">Je bent er bijna</p>
<h1 class="h1" style="font-size:42px;max-width:900px">Start met de Trigger Breakfree Challenge</h1>
<div class="row top" style="gap:56px;margin-top:20px">
<div class="c1 card">
<p class="cap">1 &#183; Je gegevens</p>
<div class="grid2" style="gap:16px"><div class="field"><label for="f1">Voornaam</label><input id="f1" type="text"></div><div class="field"><label for="f2">Achternaam</label><input id="f2" type="text"></div></div>
<div class="field"><label for="f3">E-mailadres</label><input id="f3" type="email"></div>
<p class="cap" style="margin-top:26px">2 &#183; Betaalmethode</p>
<div style="display:flex;flex-direction:column;gap:10px">
<label style="display:flex;gap:12px;align-items:center;border:1px solid #D9C7B0;padding:14px 16px;font-size:16px"><input type="radio" name="pm" checked> iDEAL</label>
<label style="display:flex;gap:12px;align-items:center;border:1px solid #D9C7B0;padding:14px 16px;font-size:16px"><input type="radio" name="pm"> Creditcard</label>
<label style="display:flex;gap:12px;align-items:center;border:1px solid #D9C7B0;padding:14px 16px;font-size:16px"><input type="radio" name="pm"> Bancontact</label>
</div>
<div style="margin-top:22px">{tbc("Orderbump", "Er is nu geen extra product, dus geen aanvinkvak. Alleen toevoegen als je een bestaand product kiest.")}</div>
<hr class="line" style="margin:28px 0">
<div style="display:flex;justify-content:space-between;font-size:18px"><span>Trigger Breakfree Challenge</span><span>[prijs]</span></div>
<div style="display:flex;justify-content:space-between;font-size:20px;font-weight:600;margin-top:12px"><span>Totaal</span><span>[prijs incl. btw]</span></div>
<a class="btn" href="Welkom.dc.html" style="display:block;margin-top:26px">Betaal en doe mee</a>
<p class="ps" style="text-align:center;font-size:13px;margin-top:12px">Door te betalen ga je akkoord met de <a href="#">algemene voorwaarden</a>.</p>
</div>
<div style="flex:0 0 380px;display:flex;flex-direction:column;gap:24px">
<div class="buy" style="padding:24px"><div class="mock" style="padding:22px 0 18px"><div class="phone" style="width:140px;height:250px"><img src="{PORTRAIT}" alt="" style="height:120px"><div class="t">Dag 1 van 7</div><div class="n">Trigger Breakfree Challenge</div></div></div>
<ul class="list" style="margin:20px 0 0"><li style="font-size:15px">{CHECK}<span>7 dagen, elke dag een korte video</span></li><li style="font-size:15px">{CHECK}<span>1 patroon van jezelf</span></li><li style="font-size:15px">{CHECK}<span>Community, en ik kijk mee</span></li></ul></div>
<div class="cardS" style="background:#FFFFFF"><p class="cap">Na betaling</p><p class="ps">Je krijgt direct een mail met je toegang en de startdatum. Op dag 1 staat je eerste video klaar.</p></div>
<p class="quote" style="font-size:20px;margin:0">&#8220;Ik zie je in de challenge. En het gaat je zeker lukken!&#8221;</p><p class="ps cam" style="font-weight:600;margin-top:-10px">Liefs, Trude</p>
</div>
</div></div></section>
'''

WELKOM = header(minimal=True) + f'''
<section class="sec"><div class="wn" style="text-align:center">
<p class="kick">Je doet mee</p>
<h1 class="h1">Welkom in de Trigger Breakfree Challenge!</h1>
<p class="lead">Wat fijn dat je erbij bent. Je bevestigingsmail is onderweg.</p>
</div>
<div class="w" style="margin-top:40px"><div class="grid3">
<div class="card"><div class="step"><div class="num">1</div><div><h3 class="h3">Check je mail</h3><p class="ps">Met je toegang en alle praktische informatie.</p></div></div></div>
<div class="card"><div class="step"><div class="num">2</div><div><h3 class="h3">Kom in de community</h3><p class="ps">Stel jezelf voor. [link community]</p></div></div></div>
<div class="card"><div class="step"><div class="num">3</div><div><h3 class="h3">Zet de start in je agenda</h3><p class="ps">Dag 1 begint op [startdatum].</p></div></div></div>
</div>
<div class="wn" style="margin-top:56px;text-align:center"><p class="lead">Kies alvast je patroon. Denk aan een moment van de afgelopen weken waarop je dacht: nu doe ik het w&#233;&#233;r.</p><p class="lead cam" style="font-weight:500">Liefs, Trude</p></div>
</div></section>
'''

for name, body, w, h, t in [
    ("Challenge.dc.html", CHALLENGE, 1440, 14000, "Salespagina Trigger Breakfree Challenge"),
    ("M-Challenge.dc.html", CHALLENGE, 390, 27000, "Salespagina mobiel"),
    ("Masterclass.dc.html", MASTERCLASS, 1440, 2900, "Masterclass-kijkpagina (alleen via handboek)"),
    ("M-Masterclass.dc.html", MASTERCLASS, 390, 4600, "Masterclass mobiel"),
    ("Afrekenen.dc.html", AFREKENEN, 1440, 1600, "Afrekenen (Plug&amp;Pay-voorbeeld)"),
    ("Welkom.dc.html", WELKOM, 1440, 1200, "Welkom na aankoop"),
]:
    open('project/' + name, 'w').write(page(t, body, w, h))
print('ok')
