from gen_common import *
from gen_sales import faq

# Knop-markers. build.py vervangt ze door de links uit config.json, of haalt de knop weg als de link leeg is.
PAY_IND = "PAY-IND"      # betaallink individueel programma
PAY_HAV = "PAY-HAV"      # betaallink 3 sessies Havening & hypnose
BOOK = "BOOK-KM"         # boekingspagina gratis kennismaking 20 min

PRIJS_IND = "&#8364;1.335"
PRIJS_HAV = "&#8364;500"

def kennismaking(label="Plan een gratis kennismaking van 20 minuten"):
    return f'<a class="btn2" href="{BOOK}">{label} &#8594;</a>'

def offer(cap, title, items, prijs, prijs_sub, btn_label, btn_href):
    li = ''.join(f'<li style="font-size:16px">{CHECK}<span>{t}</span></li>' for t in items)
    return f'''<div class="buy">
<p class="cap">{cap}</p>
<h2 class="h2" style="font-size:28px;margin-bottom:18px">{title}</h2>
<ul class="list" style="margin-bottom:22px">{li}</ul>
<p style="font-size:34px;font-weight:300;margin:0;color:#333333">{prijs}</p>
<p class="ps" style="font-size:14px;margin:4px 0 0">{prijs_sub}</p>
<a class="btn" href="{btn_href}" style="display:block;margin-top:22px">{btn_label}</a>
<p class="ps" style="text-align:center;margin-top:16px">{kennismaking("Eerst kennismaken? Plan 20 minuten gratis")}</p>
<p class="ps" style="text-align:center;margin-top:12px"><a class="btn2" href="WA-LINK">Liever eerst een vraag? App me &#8594;</a></p>
</div>'''

IND_OFFER = offer("Individueel programma", "Jouw patroon, met mij &#233;&#233;n op &#233;&#233;n",
                  ["8 online sessies met mij", "Jouw patroon is het werkmateriaal", "Dezelfde stappen als de Challenge, in jouw tempo"],
                  PRIJS_IND, "Voor het hele programma van 8 sessies", "Ja, ik wil starten", PAY_IND)

HAV_OFFER = offer("Havening &amp; hypnose", "3 sessies voor &#233;&#233;n thema",
                  ["3 online sessies van 1,5 uur", "&#201;&#233;n thema dat jij kiest", "Havening en hypnose gecombineerd"],
                  PRIJS_HAV, "Voor 3 sessies samen", "Boek 3 sessies", PAY_HAV)

def sessie(n, titel, tekst):
    return f'<div class="step" style="padding:22px 0;border-top:1px solid #E3D3BF"><div class="num">{n}</div><div><h3 class="h3">{titel}</h3><p class="ps" style="font-size:16px">{tekst}</p></div></div>'

# ---------------------------------------------------------------- Programma's
def progcard(cap, title, text, href, label, extra=""):
    return f'''<div class="card" style="display:flex;flex-direction:column;background:#FAF1E8">
<p class="cap">{cap}</p><h3 class="h3" style="font-size:26px;font-weight:400">{title}</h3>
<p class="p" style="flex:1 1 auto">{text}</p>{extra}
<a class="btn" href="{href}" style="align-self:flex-start">{label}</a></div>'''

PROGRAMMAS = header("prog") + hero(
    "Programma&#8217;s",
    'Kies hoe je met je patroon aan de slag gaat. <span class="cam">Alleen, in een groep of met mij.</span>',
    ["Alle programma&#8217;s gaan over hetzelfde: je oude patroon beslist niet langer automatisch hoe jij reageert. Je kiest zelf hoe je dat doet en in welk tempo.",
     "Nog niet zeker? Begin met het gratis handboek."],
    optin_card()) + f'''
<section class="sec white"><div class="w">
<p class="kick" style="text-align:center">Het aanbod</p>
<h2 class="h2" style="text-align:center">Drie manieren om te beginnen</h2>
<div class="grid3" style="margin-top:46px">
{progcard("&#201;&#233;n op &#233;&#233;n &#183; 8 sessies", "Individueel programma", "Je werkt met &#233;&#233;n patroon van jezelf, samen met mij. Dezelfde stappen als in de Challenge, maar dan helemaal afgestemd op jou en in jouw tempo. Online.", "Individueel.dc.html", "Bekijk het programma", f'<p class="ps" style="margin-bottom:20px;font-weight:600">{PRIJS_IND} &#183; 8 online sessies</p>')}
{progcard("In een groep &#183; 7 dagen", "Trigger Breakfree Challenge", "Zeven dagen, &#233;&#233;n patroon van jezelf. Elke dag een korte video en &#233;&#233;n ding om te doen, met de community erbij. Ik kijk mee.", "Challenge.dc.html", "Bekijk de Challenge", '<p class="ps" style="margin-bottom:20px;font-weight:600" data-chal-date>Start 14 december</p>')}
{progcard("Kort traject &#183; 3 sessies", "Havening &amp; hypnose", "Voor &#233;&#233;n duidelijk thema: een reactie die steeds terugkomt, spanning bij een bepaald moment, of een doel waar je op vastloopt.", "Havening.dc.html", "Bekijk de thema&#8217;s", f'<p class="ps" style="margin-bottom:20px;font-weight:600">{PRIJS_HAV} &#183; 3 online sessies van 1,5 uur</p>')}
</div>
</div></section>
<section class="sec"><div class="wn" style="text-align:center">
<p class="kick">Twijfel je wat bij je past?</p>
<h2 class="h2">Laten we 20 minuten praten.</h2>
<p class="p">Je vertelt waar je tegenaan loopt. Ik vertel eerlijk welk programma daarbij past, of dat geen van allemaal past. Gratis en online.</p>
<div style="display:flex;gap:26px;justify-content:center;align-items:center;flex-wrap:wrap"><a class="btn" href="{BOOK}">Plan een gratis kennismaking</a><a class="btn2" href="WA-LINK">Of app me &#8594;</a></div>
</div></section>
''' + footer()

# ---------------------------------------------------------------- Individueel programma
INDIVIDUEEL = header("prog") + hero(
    "Individueel programma &#183; 8 online sessies",
    'Stel je voor dat je oude patroon <span class="cam">niet meer automatisch beslist</span> hoe jij reageert. Met mij naast je.',
    ["Je kiest &#233;&#233;n patroon dat je echt kwijt wilt. In acht sessies ontdekken we samen waartegen het je beschermt, wat het bij j&#243;u aanzet, en hoe het is als het niet meer automatisch aangaat.",
     "Dezelfde stappen als in de Trigger Breakfree Challenge. Alleen nu volledig op jou afgestemd, in jouw tempo."],
    IND_OFFER) + f'''
<section class="sec white"><div class="wn">
<p class="kick">Je kent dit</p>
<h2 class="h2">Je weet waar het vandaan komt. En toch gebeurt het weer.</h2>
<p class="p">Een stilte in de vergadering. Die ene toon van je partner. Feedback van een collega. En voor je het doorhebt zeg je ja, word je fel, trek je je terug of ga je uitleggen. Achteraf weet je precies wat je liever had gedaan.</p>
<p class="p">Je hebt al veel gedaan. Gesprekken, boeken, cursussen. Je begrijpt je patroon door en door. Alleen op het moment zelf helpt dat begrip je niet.</p>
<p class="lead cam" style="font-weight:500;margin-top:30px">Dat ligt niet aan jou. Je werkte op een andere laag dan de laag waar je patroon wordt aangezet.</p>
</div></section>

<section class="sec"><div class="w"><div class="row top" style="gap:72px">
<div class="c1">
<p class="kick">Waarom &#233;&#233;n op &#233;&#233;n</p>
<h2 class="h2">Soms wil je dit niet in een groep doen.</h2>
<p class="p">Omdat je patroon taai is. Omdat je liever niet deelt in een community. Omdat je wilt dat iemand precies ziet wat er bij j&#243;u gebeurt, en meteen bijstuurt.</p>
<p class="p">In het individuele programma heb je mij voor jou alleen. We nemen de tijd die jouw patroon nodig heeft. En ik zie wat jij op dat moment zelf niet ziet.</p>
</div>
<div class="c1">
<div class="cardS" style="background:#FFFFFF">
<p class="cap">Challenge of individueel?</p>
<ul class="list" style="margin:0">
<li style="font-size:16px">{CHECK}<span><b style="font-weight:600">Challenge:</b> zeven dagen, in een groep, met video&#8217;s en de community.</span></li>
<li style="font-size:16px">{CHECK}<span><b style="font-weight:600">Individueel:</b> acht sessies met mij, op jouw patroon en in jouw tempo.</span></li>
</ul>
</div>
</div>
</div></div></section>

<section class="sec white"><div class="wn">
<p class="kick">Zo ziet het programma eruit</p>
<h2 class="h2">Acht sessies, &#233;&#233;n patroon</h2>
{sessie(1, "Kennismaken en je patroon kiezen", "Welk patroon wil je kwijt? Wanneer neemt het je over, en wat kost het je?")}
{sessie(2, "Je patroon in kaart", "De cirkel waarin het steeds terugkomt, en waartegen het je beschermt.")}
{sessie(3, "Opsporen", "Wat zet het bij j&#243;u aan? We zoeken het stukje dat je systeem gebruikt.")}
{sessie(4, "Verder opsporen", "Het moment, het lijf, de kleine details die het alarm laten afgaan.")}
{sessie(5, "De koppeling verbreken", "Zodat het alarm bij dat stukje niet meer afgaat.")}
{sessie(6, "Je patroon doorbreken", "Het oude patroondeel niet meer doen, in je eigen leven.")}
{sessie(7, "Versterken", "Wat wil je w&#233;l automatisch laten gaan? Daar bouwen we aan.")}
{sessie(8, "Zelf verder", "Je weet hoe je terugval kunt lezen en wat je dan doet. Je hebt zelf invloed.")}
<div style="border-top:1px solid #E3D3BF"></div>
<p class="ps" style="margin-top:22px">Alle sessies zijn online. We plannen ze samen in.</p>
</div></section>

<section class="sec"><div class="w"><div class="row" style="gap:72px">
<div style="flex:0 0 360px" class="photo"><img src="{PORTRAIT}" alt="Portret Trude Kuin"></div>
<div class="c1">
<p class="kick">Met wie werk je?</p>
<h2 class="h2">Ik ben Trude.</h2>
<p class="p">Sinds 1988 begeleid ik mensen bij persoonlijke verandering. Als consulent, coach, hypnotherapeut en Havening practitioner. Steeds met dezelfde vraag: hoe help ik mensen zo te veranderen dat ze daar blijvend zelf invloed op krijgen?</p>
<p class="p">Mijn antwoord daarop is ROOTS. In het individuele programma werk ik ermee op jouw patroon, samen met jou.</p>
<a class="btn2" href="Over.dc.html">Meer over mij &#8594;</a>
</div>
</div></div></section>

<section class="sec white"><div class="w"><div class="grid2" style="gap:56px">
<div><h3 class="h3">Voor jou als</h3><ul class="list">
<li>{CHECK}<span>je je patroon allang begrijpt, en het je toch nog overneemt</span></li>
<li>{CHECK}<span>je &#233;&#233;n patroon echt kwijt wilt</span></li>
<li>{CHECK}<span>je liever &#233;&#233;n op &#233;&#233;n werkt dan in een groep</span></li>
</ul></div>
<div><h3 class="h3">Niet voor jou als</h3><ul class="list">
<li>{DASH}<span>je nog meer inzicht zoekt. Daar heb je genoeg van.</span></li>
<li>{DASH}<span>je liever eerst in een groep proeft. Kijk dan naar de <a href="Challenge.dc.html">Challenge</a>.</span></li>
</ul></div>
</div></div></section>

<section class="sec"><div class="wn">
<p class="kick">&#8220;Maar&#8230;&#8221;</p>
<h2 class="h2">Misschien denk je nu&#8230;</h2>
{faq("&#8220;Ik heb al zoveel gedaan.&#8221;", "Precies daarom. Alles wat je deed werkte op je verhaal, je begrip of je gedrag. Dit werkt op de laag eronder.")}
{faq("&#8220;Moet ik weer terug naar vroeger?&#8221;", "Nee. We zoeken geen nieuwe verklaring. We zoeken het stukje dat je overlevingssysteem nu gebruikt.")}
{faq("&#8220;Werkt dit ook online?&#8221;", "Ja. Alle sessies zijn online, vanuit je eigen huis.")}
{faq("&#8220;Ik weet niet of dit bij me past.&#8221;", "Plan dan eerst een gratis kennismaking van 20 minuten. Dan kijken we samen of het past.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>

<section class="rose" style="padding:90px 0"><div class="wn" style="text-align:center">
<h2 class="h2">Klaar om te beginnen?</h2>
<p class="lead">Acht online sessies met mij, op jouw patroon. {PRIJS_IND} voor het hele programma.</p>
<a class="btn" href="{PAY_IND}" style="background:#FFFFFF;color:#333333">Ja, ik wil starten</a>
<p class="ps" style="margin-top:20px"><a href="{BOOK}" style="color:#FFFFFF">Of plan eerst een gratis kennismaking van 20 minuten &#8594;</a></p>
<p class="lead" style="margin-top:36px">En het gaat je zeker lukken!</p>
<p class="lead" style="font-weight:500">Liefs, Trude</p>
</div></section>
''' + footer()

# ---------------------------------------------------------------- Havening & hypnose
THEMAS = [
    ("reactie-die-terugkomt", "Een reactie die steeds terugkomt",
     "Je weet hoe je wilt reageren. En toch neemt die ene reactie het steeds over.",
     ["Je wordt fel, terwijl je rustig wilde blijven", "Je zegt ja, terwijl je nee bedoelt", "Je klapt dicht in een gesprek dat ertoe doet", "Achteraf denk je: nu doe ik het w&#233;&#233;r"],
     "We kiezen &#233;&#233;n reactie die steeds terugkomt. We kijken naar het moment waarop hij aangaat, en werken met wat er dan in je lijf gebeurt. Het doel: dat die reactie niet meer automatisch aangaat, zodat je zelf kunt kiezen."),
    ("spanning-bij-een-moment", "Spanning bij een specifiek moment",
     "Een presentatie, een lastig gesprek, een afspraak die eraan komt. Je lijf zet zich al schrap voordat het zover is.",
     ["Je slaapt slecht voor een belangrijk gesprek", "Je lijf spant zich aan zodra je eraan denkt", "Je stelt dingen uit omdat het moment zo zwaar voelt", "Je wilt het goed doen, en juist daardoor lukt het minder"],
     "We nemen dat ene moment als uitgangspunt. We werken met de spanning die erbij hoort, en met hoe je het moment w&#233;l wilt beleven. Zodat je er rustiger in kunt staan."),
    ("herinnering-met-spanning", "Een herinnering die nog steeds spanning geeft",
     "Het is lang geleden. Je weet dat het voorbij is. En toch voel je het nog als je eraan denkt.",
     ["Een herinnering komt steeds terug, ook als je dat niet wilt", "Je voelt de spanning weer als je eraan denkt", "Je vermijdt plekken, mensen of onderwerpen die eraan raken", "Je wilt het een plek geven, zonder er steeds over te hoeven praten"],
     "We werken met het alarm dat nog aan die herinnering vastzit. Je hoeft er niet alles over te vertellen. Het doel: dat je eraan kunt denken zonder dat je lijf meteen alarm slaat."),
    ("vastlopen-op-je-doel", "Vastlopen op weg naar je doel",
     "Je weet wat je wilt. Je hebt een plan. En toch kom je steeds niet in beweging, of je haakt halverwege af.",
     ["Je stelt uit wat je echt belangrijk vindt", "Je begint vol energie en stopt halverwege", "Een stemmetje zegt dat het toch niks wordt", "Je ziet anderen doen wat jij ook wilt"],
     "We kijken naar het moment waarop je vastloopt. Wat gaat er dan aan, en waartegen beschermt het je? Daar werken we mee. En we versterken hoe het voelt om w&#233;l in beweging te komen."),
    ("verlangen-en-zingeving", "Verlangen en zingeving",
     "Er is iets wat je wilt, maar je weet niet precies wat. Of je weet het wel, en het voelt nog ver weg.",
     ["Je voelt een verlangen naar meer, zonder dat je het kunt benoemen", "Je leven loopt, maar het raakt je niet echt", "Je zoekt richting voor de komende jaren", "Je wilt dichter bij wat jij echt belangrijk vindt"],
     "We maken ruimte voor wat je echt wilt. In hypnose kun je dat verlangen voelen en verkennen. Met Havening werken we met wat je tegenhoudt. Zodat je richting kunt kiezen vanuit jezelf."),
]

def thema_href(slug):
    return f"Thema-{slug}.dc.html"

HAV_UITLEG = '''<div class="grid2" style="gap:48px;margin-top:30px">
<div class="card"><p class="cap">Havening</p><p class="p" style="margin:0">Een methode met zachte aanraking van je armen, handen en gezicht, terwijl je aandacht bij een bepaald gevoel of moment is. Online doe je de aanraking zelf, en ik begeleid je stap voor stap.</p></div>
<div class="card"><p class="cap">Hypnose</p><p class="p" style="margin:0">Een rustige, gefocuste staat waarin je makkelijker voelt wat je w&#233;l wilt. Daarin versterken we de reactie die je wilt hebben, zodat die vanzelfsprekender wordt.</p></div>
</div>'''

def drie_sessies():
    return f'''<section class="sec white"><div class="wn">
<p class="kick">Zo verlopen de 3 sessies</p>
<h2 class="h2">Drie keer 1,5 uur, online</h2>
{sessie(1, "Je thema helder", "Waar loop je tegenaan, en hoe wil je het w&#233;l? We kiezen waar we mee werken en beginnen meteen.")}
{sessie(2, "Werken met Havening en hypnose", "We werken met de spanning die bij je thema hoort, en versterken wat je w&#233;l wilt.")}
{sessie(3, "Verankeren", "Wat merk je in je dagelijks leven? We werken verder waar dat nodig is, en sluiten af met wat je zelf kunt doen.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>'''

IND_VERSCHIL = 'De 3 sessies zijn voor &#233;&#233;n duidelijk thema. In het <a href="Individueel.dc.html">individuele programma</a> werk je in 8 sessies met de volledige ROOTS-stappen aan een patroon.'

HAV_FAQ = f'''<section class="sec"><div class="wn">
<p class="kick">Vragen</p>
<h2 class="h2">Goed om te weten</h2>
{faq("Werkt Havening ook online?", "Ja. Je doet de aanraking zelf, ik begeleid je. Je hebt alleen een rustige plek en een laptop of tablet met camera nodig.")}
{faq("Moet ik alles vertellen?", "Nee. Je vertelt wat jij wilt vertellen. Voor Havening is het niet nodig om alles uit te leggen.")}
{faq("Wat is het verschil met het individuele programma?", IND_VERSCHIL)}
{faq("Weet je niet welk thema bij je past?", "Plan een gratis kennismaking van 20 minuten. Dan kijken we samen.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>'''

def slot_band(title):
    return f'''<section class="rose" style="padding:90px 0"><div class="wn" style="text-align:center">
<h2 class="h2">{title}</h2>
<p class="lead">3 online sessies van 1,5 uur. {PRIJS_HAV} samen.</p>
<a class="btn" href="{PAY_HAV}" style="background:#FFFFFF;color:#333333">Boek 3 sessies</a>
<p class="ps" style="margin-top:20px"><a href="{BOOK}" style="color:#FFFFFF">Of plan eerst een gratis kennismaking van 20 minuten &#8594;</a></p>
<p class="lead" style="margin-top:36px;font-weight:500">Liefs, Trude</p>
</div></section>'''

def themacard(slug, titel, sub):
    return f'''<a href="{thema_href(slug)}" class="card" style="text-decoration:none;color:#333333;display:flex;flex-direction:column;background:#FAF1E8">
<h3 class="h3" style="font-size:22px;font-weight:400">{titel}</h3><p class="ps" style="font-size:16px;flex:1 1 auto">{sub}</p>
<span class="btn2" style="align-self:flex-start;margin-top:18px">Lees meer &#8594;</span></a>'''

HAVENING = header("prog") + hero(
    "Havening &amp; hypnose &#183; 3 sessies",
    'E&#233;n thema. Drie sessies. <span class="cam">Zodat het je niet meer automatisch overneemt.</span>',
    ["Soms wil je niet een heel programma. Je hebt &#233;&#233;n ding dat steeds terugkomt, &#233;&#233;n moment dat spanning geeft, of &#233;&#233;n doel waar je op vastloopt.",
     "In drie online sessies werken we daar gericht aan, met Havening en hypnose."],
    HAV_OFFER) + f'''
<section class="sec white"><div class="w">
<p class="kick" style="text-align:center">Waar kan ik je mee helpen?</p>
<h2 class="h2" style="text-align:center">Kies je thema</h2>
<div class="grid3" style="margin-top:46px">
{''.join(themacard(s, t, sub) for s, t, sub, *_ in THEMAS)}
<div class="card" style="background:#FFFFFF;border:1px solid #BD9D60;display:flex;flex-direction:column"><h3 class="h3" style="font-size:22px;font-weight:400">Staat je thema er niet tussen?</h3><p class="ps" style="font-size:16px;flex:1 1 auto">Vertel me waar je tegenaan loopt. Dan kijken we samen of dit past.</p><a class="btn2" href="{BOOK}" style="align-self:flex-start;margin-top:18px">Plan een gratis kennismaking &#8594;</a></div>
</div>
</div></section>
<section class="sec"><div class="wn">
<p class="kick">Wat het inhoudt</p>
<h2 class="h2">Havening en hypnose</h2>
<p class="p">Ik werk al jaren met allebei. Samen zijn ze sterk: Havening werkt met het alarm dat aan een moment of herinnering vastzit, hypnose versterkt hoe je het w&#233;l wilt.</p>
{HAV_UITLEG}
</div></section>
{drie_sessies()}
{HAV_FAQ}
''' + slot_band("Klaar om aan je thema te werken?") + footer()

def thema_page(slug, titel, sub, herken, aanpak):
    li = ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in herken)
    return header("prog") + hero(
        "Havening &amp; hypnose &#183; thema", titel, [sub],
        HAV_OFFER, '<a class="btn2" href="Havening.dc.html">&#8592; Alle thema&#8217;s</a>') + f'''
<section class="sec white"><div class="w"><div class="row top" style="gap:72px">
<div class="c1"><p class="kick">Herken je dit?</p><h2 class="h2">{titel}</h2><ul class="list">{li}</ul></div>
<div class="c1"><p class="kick">Wat we doen</p><h2 class="h2">Zo werken we eraan</h2><p class="p">{aanpak}</p></div>
</div></div></section>
<section class="sec"><div class="wn"><p class="kick">Wat het inhoudt</p><h2 class="h2">Havening en hypnose</h2>{HAV_UITLEG}</div></section>
{drie_sessies()}
{HAV_FAQ}
''' + slot_band("Wil je hieraan werken?") + footer()

THEMA_PAGES = {slug: (titel, sub, thema_page(slug, titel, sub, herken, aanpak)) for slug, titel, sub, herken, aanpak in THEMAS}
