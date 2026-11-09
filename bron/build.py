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
        return f'<p class="p" style="font-weight:600;margin:0">{" &#183; ".join(parts)}</p>' if parts else ""
    return ""


gc.tbc = tbc

import gen_home  # noqa: E402
import gen_sales  # noqa: E402
import gen_pages  # noqa: E402
import gen_en  # noqa: E402
import gen_en_pages  # noqa: E402

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
]


def cut(html, start, end, keep_end=False):
    i = html.find(start)
    if i < 0:
        return html
    j = html.find(end, i)
    if j < 0:
        return html
    return html[:i] + (html[j:] if keep_end else html[j + len(end):])


def fix(html, lang="nl"):
    html = re.sub(r'<a class="btn" href="EN-Checkout"[^>]*>.*?</a>', "", html, flags=re.S)
    # knoppen naar de betaalpagina
    if not CHECKOUT:
        html = cut(html, '<div class="c1">\n<p class="kick">Zo meld je je aan</p>', 'Ja, ik doe mee</a>\n</div>\n')
    if CHECKOUT:
        html = html.replace('href="Afrekenen.dc.html"', f'href="{CHECKOUT}"')
        html = html.replace(" &#183; [betaalmethoden bevestigen]", "")
    else:
        html = re.sub(r'<a class="btn" href="Afrekenen\.dc\.html"[^>]*>.*?</a>', "", html, flags=re.S)
        html = re.sub(r'<p class="ps"[^>]*>Veilig afrekenen via Plug&amp;Pay[^<]*</p>', "", html)
        html = html.replace('<div class="c1">\n<p class="kick">Geen verrassingen</p>', '<div class="c1" style="max-width:820px">\n<p class="kick">Geen verrassingen</p>')
    if not cfg["challenge_startdatum"]:
        html = re.sub(r'<div class="step"><div class="num">4</div><p[^>]*>Op \[startdatum\] begint dag 1\.</p></div>', "", html)
    else:
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

contact = gen_pages.CONTACT.replace(" Ik lees alles zelf en antwoord binnen [termijn].", " Ik lees alles zelf.")
c_act = CONTACT_ACTION or (f"mailto:{cfg['contact_email']}" if cfg["contact_email"] else "")
if c_act:
    contact = contact.replace('<form class="card" style="margin-top:20px">', f'<form class="card" style="margin-top:20px" action="{c_act}" method="post"' + (' enctype="text/plain"' if c_act.startswith("mailto:") else "") + ">")
    contact = contact.replace('<input id="c1" type="text">', '<input id="c1" name="naam" type="text" required>')
    contact = contact.replace('<input id="c2" type="email">', '<input id="c2" name="email" type="email" required>')
    contact = contact.replace('<textarea id="c3" rows="6"></textarea>', '<textarea id="c3" name="bericht" rows="6" required></textarea>')
    contact = contact.replace('<button class="btn" type="button">Verstuur</button>', '<button class="btn" type="submit">Verstuur</button>')
else:
    contact = cut(contact, '<form class="card" style="margin-top:20px">', "</form>")
    contact = contact.replace("Stuur me een bericht.</h1>", "Stuur me een bericht.</h1>")
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

if cfg["masterclass_video_url"]:
    mc = re.sub(r'<div class="vid" style="aspect-ratio:16/9;margin-top:10px">.*?</svg></div></div>',
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
