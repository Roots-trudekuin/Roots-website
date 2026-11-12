"""Bouwt de statische website in public/ uit de ontwerpbronnen.

Gebruik:  python3 bron/build.py
Instellingen (betaallink, prijs, formulieren, links): bron/config.json.
Lege waarden in config.json = dat onderdeel wordt niet getoond.
"""
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "public")
ASSETS = os.path.join(HERE, "assets")
cfg = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
PREVIEW = os.environ.get("PREVIEW") == "1"   # alleen voor previews: lege knoplinks tijdelijk zichtbaar maken
if PREVIEW:
    for k in ("challenge_betaallink", "individueel_betaallink", "havening_betaallink", "kennismaking_url"):
        cfg[k] = cfg[k] or "#"
    cfg["whatsapp_nummer"] = cfg["whatsapp_nummer"] or "31600000000"
_nr = re.sub(r"\D", "", cfg.get("whatsapp_nummer", ""))
if _nr.startswith("06"):
    _nr = "31" + _nr[1:]
cfg["_wa"] = f"https://wa.me/{_nr}" if _nr else ""

sys.path.insert(0, HERE)
os.chdir(tempfile.mkdtemp())          # de ontwerpbronnen schrijven hun canvasbestanden hierheen
os.makedirs("project", exist_ok=True)

import gen_common as gc  # noqa: E402

gc.ICON = "/img/roots-icoon.png"
gc.PORTRAIT = "/img/trude.jpg"
gc.COVER = "/img/omslag-handboek.jpg"


def tbc(label, text):
    """In het ontwerp waren dit gestippelde 'te bevestigen'-kaders. Live: verbergen."""
    if label == "Alleen met jouw akkoord":          # verhaal 2014: publiek (besluit Trude 9 nov)
        return f'<p class="p">{text}</p>'
    if label == "Prijs en start":
        parts = [p for p in (cfg["challenge_prijs"], cfg["challenge_startdatum"]) if p]
        return f'<p class="p" style="font-weight:600;margin:0" data-chal-date>{" &#183; ".join(parts)}</p>' if parts else ""
    return ""


gc.tbc = tbc

import gen_home  # noqa: E402
import gen_sales  # noqa: E402
import gen_pages  # noqa: E402
import gen_en  # noqa: E402
import gen_en_pages  # noqa: E402
import gen_prog  # noqa: E402

from gen_common import header, footer, hero, optin_card, CHECK  # noqa: E402

CHECKOUT = cfg["challenge_betaallink"]
OPTIN_ACTION = cfg["handboek_formulier_action"]
CONTACT_ACTION = cfg["contact_formulier_action"]

LINKS = [
    ("EN-Home.dc.html#handbook", "/en#handbook"), ("EN-Home.dc.html", "/en"),
    ("EN-Challenge.dc.html", "/en/challenge"), ("EN-Insights.dc.html", "/en/insights"),
    ("EN-About.dc.html", "/en/about-trude"), ("EN-Contact.dc.html", "/en/contact"),
    ("Main.dc.html#handboek", "/#handboek"), ("Main.dc.html", "/"),
    ("Optin.dc.html", "/#handboek"),
    ("Challenge.dc.html", "/challenge"),
    ("Inzicht.dc.html#artikelen", "/inzicht#artikelen"), ("Inzicht.dc.html", "/inzicht"),
    ("Over.dc.html", "/over-trude"), ("Contact.dc.html", "/contact"),
    ("Welkom.dc.html", "/welkom"),
    ("Programmas.dc.html", "/programmas"),
    ("Individueel.dc.html", "/programmas/individueel-programma"),
    ("Havening.dc.html", "/programmas/havening-en-hypnose"),
] + [(gen_prog.thema_href(t[0]), f"/programmas/havening-en-hypnose/{t[0]}") for t in gen_prog.THEMAS]

MARKERS = {"WA-DIRECT": "_wa", "PAY-IND": "individueel_betaallink", "PAY-HAV": "havening_betaallink", "BOOK-KM": "kennismaking_url"}


def cut(html, start, end, keep_end=False):
    i = html.find(start)
    if i < 0:
        return html
    j = html.find(end, i)
    if j < 0:
        return html
    return html[:i] + (html[j:] if keep_end else html[j + len(end):])


def fix(html, lang="nl"):
    for mk, key in MARKERS.items():
        if cfg[key]:
            html = html.replace(f'href="{mk}"', f'href="{cfg[key]}"')
        else:
            html = re.sub(r'<a [^>]*href="' + mk + r'"[^>]*>.*?</a>', "", html, flags=re.S)
            html = re.sub(r'<p class="ps"[^>]*>\s*</p>', "", html)
    html = html.replace('<a class="btn" href="Afrekenen.dc.html"', '<a class="btn" data-chal-buy href="Afrekenen.dc.html"')
    html = html.replace('<a class="btn" data-chal-buy href="Afrekenen.dc.html" style="display:block;margin-top:20px">', '<a class="btn" data-chal-buy href="Afrekenen.dc.html" style="display:block;margin-top:20px">')
    if cfg.get("challenge_betaallink_en"):
        html = html.replace('href="EN-Checkout"', f'href="{cfg["challenge_betaallink_en"]}"')
    else:
        html = re.sub(r'<a class="btn" href="EN-Checkout"[^>]*>.*?</a>', "", html, flags=re.S)
    # knoppen naar de betaalpagina
    if not CHECKOUT:
        html = cut(html, '<div class="c1">\n<p class="kick">Zo meld je je aan</p>', 'Ja, ik doe mee</a>\n</div>\n')
    if CHECKOUT:
        html = html.replace('href="Afrekenen.dc.html"', f'href="{CHECKOUT}"')
        html = html.replace(" &#183; [betaalmethoden bevestigen]", "")
    else:
        html = re.sub(r'<a class="btn" data-chal-buy href="Afrekenen\.dc\.html"[^>]*>.*?</a>', "", html, flags=re.S)
        html = re.sub(r'<p class="ps"[^>]*>Veilig afrekenen via Plug&amp;Pay[^<]*</p>', "", html)
        html = html.replace('<div class="c1">\n<p class="kick">Geen verrassingen</p>', '<div class="c1" style="max-width:820px">\n<p class="kick">Geen verrassingen</p>')
    if not cfg["challenge_startdatum"]:
        html = re.sub(r'<div class="step"><div class="num">4</div><p[^>]*>Op \[startdatum\] begint dag 1\.</p></div>', "", html)
    else:
        html = html.replace('<div class="step"><div class="num">4</div><p class="p" style="margin:8px 0 0">Op [startdatum]', '<div class="step" data-chal-hide><div class="num">4</div><p class="p" style="margin:8px 0 0">Op [startdatum]')
        html = html.replace("[startdatum]", cfg["challenge_startdatum"])

    # handboekformulier
    act = OPTIN_ACTION or ("/en/thank-you" if lang == "en" else "/bedankt")
    method = "post" if OPTIN_ACTION else "get"
    for btn_txt, href in (("Stuur mij het handboek", 'href="Bedankt.dc.html"'), ("Send me the handbook", 'href="#"')):
        html = re.sub(r'<form>(\s*<div class="field">.*?)<a class="btn" ' + re.escape(href) + r' style="display:block;margin-top:8px">' + btn_txt + r'</a>\s*</form>',
                      lambda m: f'<form action="{act}" method="{method}">{m.group(1)}<button class="btn" type="submit" style="display:block;width:100%;margin-top:8px">{btn_txt}</button></form>',
                      html, flags=re.S)
    html = html.replace('placeholder="Je voornaam" aria-label="Voornaam"', 'name="voornaam" autocomplete="given-name" placeholder="Je voornaam" aria-label="Voornaam" required')
    html = html.replace('placeholder="jij@voorbeeld.nl" aria-label="E-mailadres"', 'name="email" autocomplete="email" placeholder="jij@voorbeeld.nl" aria-label="E-mailadres" required')
    html = html.replace('placeholder="Your first name" aria-label="First name"', 'name="voornaam" autocomplete="given-name" placeholder="Your first name" aria-label="First name" required')
    html = html.replace('placeholder="you@example.com" aria-label="Email address"', 'name="email" autocomplete="email" placeholder="you@example.com" aria-label="Email address" required')
    html = html.replace('<label>Voornaam</label>', '<label>Voornaam</label>').replace('<label>E-mailadres</label>', '<label>E-mailadres</label>')

    # video-plekken zonder video
    html = re.sub(r'<div class="vid hide-m"[^>]*><div class="play">.*?</svg></div></div>', "", html, flags=re.S)
    html = re.sub(r'<div class="c1"><div class="vid"[^>]*>.*?</svg></div></div>\s*</div>', "", html, flags=re.S)

    # praktische FAQ met nog onbekende antwoorden
    html = cut(html, '<p class="kick" style="margin-top:60px">Praktisch</p>', '<div style="border-top:1px solid #E3D3BF"></div>\n</div></section>', keep_end=True)

    # footer en header
    html = html.replace('<li><a href="#">Instagram [@handle]</a></li>', f'<li><a href="{cfg["instagram_url"]}">Instagram</a></li>' if cfg["instagram_url"] else "")
    html = html.replace('<li><a href="#">Skool-community [naam en link]</a></li>', f'<li><a href="{cfg["skool_url"]}">Community</a></li>' if cfg["skool_url"] else "")
    html = html.replace('<li><a href="#">Skool community [name and link]</a></li>', f'<li><a href="{cfg["skool_url"]}">Community</a></li>' if cfg["skool_url"] else "")
    for nl, en, key in (("Privacyverklaring", "Privacy policy", "privacy_url"), ("Algemene voorwaarden", "Terms and conditions", "voorwaarden_url")):
        for label in (nl, en):
            html = html.replace(f'<li><a href="#">{label}</a></li>', f'<li><a href="{cfg[key]}">{label}</a></li>' if cfg[key] else "")
            html = html.replace(f'<a href="#">{label}</a>', f'<a href="{cfg[key]}">{label}</a>' if cfg[key] else "")
    html = html.replace('<li><a href="#">Cookies</a></li>', "")
    html = html.replace('| <a href="#">EN</a>', '| <a href="/en">EN</a>')
    html = html.replace('<a href="Main.dc.html">NL</a>', '<a href="/">NL</a>')

    for a, b in LINKS:
        html = html.replace(f'href="{a}"', f'href="{b}"')
    mlink = '<a class="mnav" href="/en#handbook">Free handbook</a>' if lang == "en" else '<a class="mnav" href="/#handboek">Gratis handboek</a>'
    html = html.replace('</nav>', mlink + '</nav>', 1)
    html = html.replace('<button class="burger" type="button" aria-label="Menu openen">', '<button class="burger" type="button" aria-label="Menu openen" aria-expanded="false">')
    html = html.replace('<button class="burger" type="button" aria-label="Open menu">', '<button class="burger" type="button" aria-label="Open menu" aria-expanded="false">')
    return html


def page(path, title, desc, body, lang="nl", noindex=False):
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    wa_float = (f'''<div class="wabub" id="wabub" role="dialog" aria-label="App Trude via WhatsApp"><button class="wax" type="button" aria-label="Sluiten">&#215;</button><div class="wahd"><img src="/img/portret-rond.jpg" alt=""><div><b>Trude Kuin</b><span>ROOTS</span></div></div><p>Hoi, ik ben Trude. Een vraag? App me gerust.</p><a class="btn" href="{cfg["_wa"]}" target="_blank" rel="noopener">Appen</a></div>
<a class="wa" href="{cfg["_wa"]}" target="_blank" rel="noopener" aria-label="App Trude via WhatsApp"><svg width="22" height="22" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3 1 2.6 1.1 2.8.1.2 1.9 2.9 4.6 4 1.7.7 2.4.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3z"/></svg><span>Appen?</span></a>
<script>(function(){{var b=document.getElementById("wabub");if(!b)return;var k="wabub-dicht",s=false;try{{s=sessionStorage.getItem(k)==="1"}}catch(e){{}}if(s)return;var shown=false;function show(){{if(shown)return;shown=true;b.classList.add("open")}}setTimeout(show,6000);window.addEventListener("scroll",function(){{if(window.scrollY>window.innerHeight*.6)show()}},{{passive:true}});b.querySelector(".wax").addEventListener("click",function(){{b.classList.remove("open");try{{sessionStorage.setItem(k,"1")}}catch(e){{}}}});}})();</script>''') if cfg["_wa"] and lang == "nl" else ""
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="icon" href="/img/roots-icoon.png">
<link rel="stylesheet" href="/css/site.css">
</head>
<body>
{body}
{wa_float}
<script>(function(){{var d="{cfg['challenge_inschrijving_sluit']}";if(!d||new Date()<new Date(d+"T00:00:00"))return;var w="{cfg['challenge_wachtlijst_url'] or '/contact'}";document.querySelectorAll('[data-chal-buy]').forEach(function(a){{a.href=w;a.textContent="Zet me op de wachtlijst";}});document.querySelectorAll('[data-chal-date]').forEach(function(p){{p.textContent="Volgende ronde volgt. Zet je op de wachtlijst.";}});document.querySelectorAll('[data-chal-hide]').forEach(function(e){{e.style.display="none";}});}})();</script>
<script>(function(){{var b=document.querySelector('.burger');if(!b)return;b.addEventListener('click',function(){{var h=b.closest('.hdr');var o=h.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');}});document.querySelectorAll('.nav a').forEach(function(a){{a.addEventListener('click',function(){{var h=document.querySelector('.hdr');h.classList.remove('open');b.setAttribute('aria-expanded','false');}});}});}})();</script>
</body>
</html>
'''
    left = re.findall(r"\[[^\]\s][^\]]{0,60}\]", re.sub(r"<[^>]+>", " ", body))
    if left:
        print(f"  let op, placeholder in {path}: {left}")
    if "dc.html" in body:
        print(f"  let op, ontwerplink in {path}: {re.findall(r'[A-Za-z-]+\.dc\.html', body)}")
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)


MOBILE_CSS = """
html{scroll-behavior:smooth}
.wa{position:fixed;right:22px;bottom:22px;z-index:50;display:flex;align-items:center;gap:10px;background:#BD9D60;color:#FFFFFF;text-decoration:none;font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase;padding:14px 20px;border-radius:40px;box-shadow:0 10px 26px rgba(120,95,60,.28)}
.wa:hover{background:#A98A50;color:#FFFFFF}
.wabub{position:fixed;right:22px;bottom:92px;z-index:51;width:300px;background:#FFFFFF;border-radius:14px;padding:20px 20px 18px;box-shadow:0 18px 44px rgba(120,95,60,.25);opacity:0;transform:translateY(12px);pointer-events:none;transition:opacity .35s,transform .35s}
.wabub.open{opacity:1;transform:none;pointer-events:auto}
.wabub:after{content:"";position:absolute;right:34px;bottom:-8px;width:16px;height:16px;background:#FFFFFF;transform:rotate(45deg)}
.wahd{display:flex;gap:12px;align-items:center;margin-bottom:12px}
.wahd img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.wahd b{display:block;font-weight:600;font-size:15px;color:#333333}
.wahd span{font-size:12px;color:#8C7240}
.wabub p{font-size:15px;line-height:1.5;margin:0 0 14px;color:#333333}
.wabub .btn{display:block;text-align:center;padding:12px 18px}
.wax{position:absolute;right:10px;top:8px;background:none;border:0;font-size:22px;line-height:1;color:#8C7240;cursor:pointer;padding:4px}
@media (max-width:900px){.wa{padding:13px 16px;right:16px;bottom:16px}.wabub{right:16px;bottom:82px;width:min(300px,calc(100vw - 32px))}}
.mnav{display:none}
@media (max-width:900px){
 .hdr{position:relative}
 .hdr.open .nav{display:flex;position:absolute;top:100%;left:0;right:0;z-index:30;flex-direction:column;gap:0;background:#FAF1E8;padding:8px 22px 22px;border-bottom:1px solid #EADCC9;box-shadow:0 12px 24px rgba(120,95,60,.08)}
 .hdr.open .nav a{padding:13px 0;font-size:17px;border-bottom:1px solid #EFE3D3}
 .hdr.open .nav a.mnav{display:block;border:0;margin-top:14px;background:#BD9D60;color:#FFFFFF;text-align:center;font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:14px;padding:15px}
}
"""

# ---------- opbouw ----------
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "css"))
shutil.copytree(os.path.join(ASSETS, "img"), os.path.join(OUT, "img"))
shutil.copytree(os.path.join(ASSETS, "fonts"), os.path.join(OUT, "fonts"))

fonts = "".join(
    f"@font-face{{font-family:'Montserrat';font-style:normal;font-weight:{w};font-display:swap;src:url('/fonts/montserrat-latin-{w}-normal.woff2') format('woff2')}}"
    for w in (300, 400, 500, 600, 700))
fonts += "@font-face{font-family:'Montserrat';font-style:italic;font-weight:300;font-display:swap;src:url('/fonts/montserrat-latin-300-italic.woff2') format('woff2')}"
fonts += "@font-face{font-family:'Cinzel';font-style:normal;font-weight:400;font-display:swap;src:url('/fonts/cinzel-latin-400-normal.woff2') format('woff2')}"
open(os.path.join(OUT, "css", "site.css"), "w", encoding="utf-8").write(fonts + gc.CSS + MOBILE_CSS)

# Homepage: ronde portretfoto bij 'Wie ben ik' (besluit Trude 9 nov)
home = gen_home.HOME.replace(
    '<div style="flex:0 0 340px" class="photo"><span class="tape"></span><img src="/img/trude.jpg" alt="Portret Trude Kuin"></div>',
    '<div style="flex:0 0 340px" class="photo"><img src="/img/portret-rond.jpg" alt="Portret Trude Kuin"></div>')

page("index.html", "TrudeThecla | ROOTS · Zet je patroon uit bij de bron",
     "Je kent je patroon door en door, en toch neemt het je over. Ontdek met het gratis Handboek Patroon-Reset waarom je patroon terugkomt en waar echte verandering begint.",
     fix(home))

page("challenge.html", "Trigger Breakfree Challenge · TrudeThecla | ROOTS",
     "Zeven dagen, één patroon van jezelf, met Trude erbij. Ontdek wat je patroon aanzet en ervaar hoe het is als het niet meer automatisch aangaat.",
     fix(gen_sales.CHALLENGE))

page("programmas.html", "Programma's · TrudeThecla | ROOTS",
     "Werk met je patroon in het individuele programma, de Trigger Breakfree Challenge of drie sessies Havening en hypnose.",
     fix(gen_prog.PROGRAMMAS))
page("programmas/individueel-programma.html", "Individueel programma · TrudeThecla | ROOTS",
     "Acht online sessies met Trude Kuin, op jouw patroon en in jouw tempo. Zodat je oude patroon niet meer automatisch beslist hoe jij reageert.",
     fix(gen_prog.INDIVIDUEEL))
page("programmas/havening-en-hypnose.html", "Havening & hypnose · TrudeThecla | ROOTS",
     "Drie online sessies Havening en hypnose voor één thema: een reactie die terugkomt, spanning bij een moment, of een doel waar je op vastloopt.",
     fix(gen_prog.HAVENING))
for slug, (titel, sub, body) in gen_prog.THEMA_PAGES.items():
    page(f"programmas/havening-en-hypnose/{slug}.html", f"{re.sub('&[^;]+;', '', titel)} · Havening & hypnose · TrudeThecla | ROOTS", re.sub(r"&#8217;", "’", sub), fix(body))

inzicht = header("inz") + hero(
    "Inzicht", 'Waarom je patroon terugkomt, <span class="cam">en hoe je er anders naar kijkt.</span>',
    ["Artikelen en video&#8217;s over terugval, je verhaal en je neuro-biologie. Om te lezen, te kijken en te herkennen."],
    optin_card(),
    '<div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:10px"><a class="btn2" href="#artikelen">Artikelen</a><a class="btn2" href="#videos">Video&#8217;s</a></div>') + '''
<section id="artikelen" class="sec white"><div class="w"><p class="kick">Artikelen</p><h2 class="h2">Lees verder</h2><p class="p">De eerste artikelen volgen binnenkort.</p></div></section>
<section id="videos" class="sec"><div class="w"><p class="kick">Video&#8217;s</p><h2 class="h2">Kijk en herken</h2><p class="p">De eerste video&#8217;s volgen binnenkort.</p></div></section>
''' + gen_pages.cta_band("Van lezen en kijken naar doen", "In de Trigger Breakfree Challenge werk je zeven dagen met &#233;&#233;n patroon van jezelf.") + footer()
page("inzicht.html", "Inzicht · TrudeThecla | ROOTS",
     "Artikelen en video's van Trude Kuin over waarom oude patronen terugkomen, en hoe je er anders naar kijkt.", fix(inzicht))

page("over-trude.html", "Over Trude · TrudeThecla | ROOTS",
     "Trude Kuin begeleidt sinds 1988 mensen bij persoonlijke verandering en ontwikkelde ROOTS: de methode waarmee je je patroon uitzet bij de bron.",
     fix(gen_pages.OVER))

contact = gen_pages.CONTACT
c_act = CONTACT_ACTION or (f"mailto:{cfg['contact_email']}" if cfg["contact_email"] else "")
if c_act:
    contact = contact.replace("FORM-ATTR", f'action="{c_act}" method="post"' + (' enctype="text/plain"' if c_act.startswith("mailto:") else ""))
elif PREVIEW:
    contact = contact.replace(" FORM-ATTR", "")
else:
    print("  let op: contactformulier verborgen, vul contact_formulier_action of contact_email in")
    contact = re.sub(r'<form class="buy" id="cform".*?</form>', optin_card(), contact, flags=re.S)
page("contact.html", "Contact · TrudeThecla | ROOTS", "Een vraag over de Trigger Breakfree Challenge, je aanmelding of je toegang? Stuur Trude een bericht.", fix(contact))

bedankt = cut(gen_home.BEDANKT, '<section style="padding:70px 0"><div class="wn" style="text-align:center">\n<p class="cap">Gratis community</p>', "</div></section>")
page("bedankt.html", "Je handboek is onderweg · TrudeThecla | ROOTS", "Je Handboek Patroon-Reset is onderweg naar je mailbox.", fix(bedankt), noindex=True)

steps = ['<div class="card"><div class="step"><div class="num">1</div><div><h3 class="h3">Check je mail</h3><p class="ps">Met je toegang en alle praktische informatie.</p></div></div></div>']
if cfg["skool_url"]:
    steps.append(f'<div class="card"><div class="step"><div class="num">{len(steps)+1}</div><div><h3 class="h3">Kom in de community</h3><p class="ps">Stel jezelf voor. <a href="{cfg["skool_url"]}">Naar de community</a></p></div></div></div>')
if cfg["challenge_startdatum"]:
    steps.append(f'<div class="card"><div class="step"><div class="num">{len(steps)+1}</div><div><h3 class="h3">Zet de start in je agenda</h3><p class="ps">Dag 1 begint op {cfg["challenge_startdatum"]}.</p></div></div></div>')
welkom = header(minimal=True) + f'''
<section class="sec"><div class="wn" style="text-align:center">
<p class="kick">Je doet mee</p>
<h1 class="h1">Welkom in de Trigger Breakfree Challenge!</h1>
<p class="lead">Wat fijn dat je erbij bent. Je bevestigingsmail is onderweg.</p>
</div>
<div class="w" style="margin-top:40px"><div class="grid{3 if len(steps) == 3 else 2 if len(steps) == 2 else 2}" style="max-width:{'100%' if len(steps) > 1 else '520px'};margin:0 auto">{"".join(steps)}</div>
<div class="wn" style="margin-top:56px;text-align:center"><p class="lead">Kies alvast je patroon. Denk aan een moment van de afgelopen weken waarop je dacht: nu doe ik het w&#233;&#233;r.</p><p class="lead cam" style="font-weight:500">Liefs, Trude</p></div>
</div></section>
'''
page("welkom.html", "Welkom · TrudeThecla | ROOTS", "Welkom in de Trigger Breakfree Challenge.", fix(welkom), noindex=True)

if cfg["masterclass_video_url"] or PREVIEW:
    mc = gen_sales.MASTERCLASS if not cfg["masterclass_video_url"] else re.sub(r'<div class="vid" style="aspect-ratio:16/9;margin-top:10px">.*?</svg></div></div>',
                f'<div class="vid" style="aspect-ratio:16/9;margin-top:10px"><iframe src="{cfg["masterclass_video_url"]}" title="Masterclass Zet je patroon uit bij de bron" style="width:100%;height:100%;border:0" allow="autoplay; fullscreen" allowfullscreen></iframe></div>',
                gen_sales.MASTERCLASS, flags=re.S)
    page("masterclass-zet-je-patroon-uit.html", "Masterclass Zet je patroon uit bij de bron · TrudeThecla | ROOTS",
         "Gratis masterclass van Trude Kuin.", fix(mc), noindex=True)

# Engels
EN_IMG = [("/_blob/9c771f73242de6925af332c753654877", "/img/omslag-handbook-en.jpg"), ("/_blob/b75005e3606297823a6d47a9e3562265", "/img/portret-rond-en.jpg")]
def en_img(h):
    for x, y in EN_IMG:
        h = h.replace(x, y)
    return h
en = en_img(gen_en.EN)
page("en/index.html", "TrudeThecla | ROOTS · Switch off your pattern at the source",
     "You know your pattern inside out, and yet it takes over. Discover with the free Pattern Reset Handbook why your pattern keeps coming back and where real change begins.",
     fix(en, "en"), lang="en")

page("en/challenge.html", "Trigger Breakfree Challenge · TrudeThecla | ROOTS",
     "Seven days, one pattern of your own, with Trude alongside you. Discover what sets your pattern off and experience what it is like when it no longer starts automatically.",
     fix(en_img(gen_en_pages.EN_CHALLENGE), "en"), lang="en")
page("en/insights.html", "Insights · TrudeThecla | ROOTS",
     "Articles and videos by Trude Kuin about why old patterns keep coming back, and how to look at them differently.",
     fix(en_img(gen_en_pages.EN_INSIGHTS), "en"), lang="en")
page("en/about-trude.html", "About Trude · TrudeThecla | ROOTS",
     "Since 1988 Trude Kuin has guided people through personal change. She developed ROOTS: the method that lets you switch off your pattern at the source.",
     fix(en_img(gen_en_pages.EN_ABOUT), "en"), lang="en")
en_contact = en_img(gen_en_pages.EN_CONTACT)
if c_act:
    en_contact = en_contact.replace('<form class="card" style="margin-top:20px">', f'<form class="card" style="margin-top:20px" action="{c_act}" method="post"' + (' enctype="text/plain"' if c_act.startswith("mailto:") else "") + ">")
    en_contact = en_contact.replace('<input id="c1" type="text">', '<input id="c1" name="naam" type="text" required>').replace('<input id="c2" type="email">', '<input id="c2" name="email" type="email" required>').replace('<textarea id="c3" rows="6"></textarea>', '<textarea id="c3" name="bericht" rows="6" required></textarea>').replace('<button class="btn" type="button">Send</button>', '<button class="btn" type="submit">Send</button>')
else:
    en_contact = cut(en_contact, '<form class="card" style="margin-top:20px">', "</form>")
page("en/contact.html", "Contact · TrudeThecla | ROOTS", "A question about the Trigger Breakfree Challenge, signing up or your access? Send Trude a message.", fix(en_contact, "en"), lang="en")
page("en/thank-you.html", "Your handbook is on its way · TrudeThecla | ROOTS", "Your Pattern Reset Handbook is on its way to your inbox.", fix(en_img(gen_en_pages.EN_THANKS), "en"), lang="en", noindex=True)
page("en/welcome.html", "Welcome · TrudeThecla | ROOTS", "Welcome to the Trigger Breakfree Challenge.", fix(en_img(gen_en_pages.EN_WELCOME), "en"), lang="en", noindex=True)

print("klaar:", sorted(os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs if f.endswith(".html")))
