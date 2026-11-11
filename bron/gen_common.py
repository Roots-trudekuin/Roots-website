ICON = "/_blob/2719836f879621fc432b251d905338f6"
PORTRAIT = "/_blob/dcd6077de198ea2008003a9181ea7678"
COVER = "/_blob/497be7824129ba9536b1c56ab65e6df4"

CSS = """
body{margin:0;background:#FAF1E8;color:#333333;font-family:'Montserrat',Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:#8C7240}a:hover{color:#333333}
*{box-sizing:border-box}
.w{max-width:1200px;margin:0 auto;padding:0 40px}
.wn{max-width:820px;margin:0 auto;padding:0 40px}
.kick{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#BD9D60;font-weight:600;margin:0 0 18px}
.h1{font-weight:300;font-size:50px;line-height:1.2;margin:0 0 28px;color:#333333;letter-spacing:-.01em}
.h2{font-weight:300;font-size:38px;line-height:1.28;margin:0 0 26px;color:#333333}
.h3{font-weight:500;font-size:21px;line-height:1.4;margin:0 0 10px;color:#333333}
.cap{font-weight:500;font-size:15px;letter-spacing:.2em;text-transform:uppercase;color:#BD9D60;margin:0 0 14px}
.cam{color:#BD9D60}
.p{font-size:18px;line-height:1.75;margin:0 0 20px}
.ps{font-size:15px;line-height:1.65;margin:0}
.lead{font-size:21px;line-height:1.7;margin:0 0 24px}
.btn{display:inline-block;background:#BD9D60;color:#FFFFFF;text-decoration:none;font-weight:600;letter-spacing:.09em;text-transform:uppercase;font-size:15px;line-height:1.3;padding:19px 32px;border-radius:2px;text-align:center;border:0;font-family:inherit;cursor:pointer}
.btn:hover{background:#A98A50;color:#FFFFFF}
.btn2{display:inline-block;color:#333333;text-decoration:none;font-weight:500;font-size:16px;border-bottom:1px solid #BD9D60;padding-bottom:3px}
.btn2:hover{color:#8C7240}
.sec{padding:110px 0}
.white{background:#FFFFFF}
.rose{background:#BEA8A7;color:#FFFFFF}
.rose .h1,.rose .h2,.rose .p,.rose .lead{color:#FFFFFF}
.rose .kick{color:#FFFFFF;opacity:.9}
.row{display:flex;gap:64px;align-items:center}
.row.top{align-items:flex-start}
.c1{flex:1 1 0;min-width:0}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:40px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:32px}
.card{background:#FFFFFF;padding:40px;border-radius:2px}
.cardS{background:#FAF1E8;padding:36px;border-radius:2px}
.dots{background-image:radial-gradient(#BEA8A7 1.6px,transparent 1.8px);background-size:20px 20px}
.dotsC{background-image:radial-gradient(#BD9D60 1.5px,transparent 1.7px);background-size:20px 20px;opacity:.55}
.photo{position:relative}
.photo img{display:block;width:100%;height:auto;border-radius:2px}
.tape{position:absolute;width:120px;height:30px;background:rgba(190,168,167,.6);top:-14px;left:50%;margin-left:-60px;transform:rotate(-4deg)}
.tbc{border:2px dashed #BEA8A7;background:rgba(190,168,167,.13);padding:14px 18px;border-radius:2px;font-size:14px;line-height:1.55;color:#333333}
.tbc b{display:block;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#8E7372;margin-bottom:4px;font-weight:700}
.list{list-style:none;padding:0;margin:0 0 24px}
.list li{display:flex;gap:14px;font-size:18px;line-height:1.65;margin:0 0 14px}
.list svg{flex:0 0 22px;margin-top:4px}
.line{height:1px;background:#E3D3BF;border:0;margin:0}
/* header */
.hdr{background:#FAF1E8;border-bottom:1px solid #EADCC9}
.hdr .in{max-width:1320px;margin:0 auto;padding:18px 40px;display:flex;align-items:center;gap:28px}
.logo{display:flex;align-items:center;gap:14px;text-decoration:none;color:#333333}
.logo img{height:46px;width:auto}
.logo .wm{font-family:'Cinzel',serif;font-size:26px;letter-spacing:.14em;color:#BD9D60;line-height:1}
.logo .sub{display:block;font-family:'Montserrat',sans-serif;font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:#333333;margin-top:5px}
.nav{display:flex;gap:26px;margin-left:auto;align-items:center}
.nav a{text-decoration:none;color:#333333;font-size:15px;font-weight:500}
.nav a:hover,.nav a.on{color:#BD9D60}
.lang{font-size:13px;letter-spacing:.1em;color:#333333}
.lang a{text-decoration:none;color:#333333}
.lang .on{color:#BD9D60;font-weight:600}
.hbtn{background:#BD9D60;color:#FFFFFF;text-decoration:none;font-weight:600;font-size:13px;letter-spacing:.08em;text-transform:uppercase;padding:13px 18px;border-radius:2px}
.hbtn:hover{background:#A98A50;color:#FFFFFF}
.burger{display:none;background:transparent;border:1px solid #BD9D60;width:46px;height:46px;border-radius:2px;margin-left:auto;align-items:center;justify-content:center}
/* footer */
.ftr{background:#BEA8A7;color:#FFFFFF;padding:72px 0 40px}
.ftr a{color:#FFFFFF;text-decoration:none}
.ftr a:hover{text-decoration:underline}
.ftr .cols{display:flex;gap:64px;flex-wrap:wrap}
.ftr .h{font-size:12px;letter-spacing:.2em;text-transform:uppercase;font-weight:600;margin:0 0 16px}
.ftr ul{list-style:none;padding:0;margin:0}
.ftr li{font-size:15px;line-height:2}
.ftr .wm{font-family:'Cinzel',serif;font-size:30px;letter-spacing:.14em}
/* product card */
.buy{background:#FFFFFF;border-radius:2px;padding:32px;box-shadow:0 18px 50px rgba(120,95,60,.12)}
.mock{background:#FAF1E8;border-radius:2px;padding:28px 0 22px;display:flex;justify-content:center;position:relative;overflow:hidden}
.phone{width:168px;height:300px;border:7px solid #333333;border-radius:28px;background:#FFFFFF;overflow:hidden;display:flex;flex-direction:column;position:relative;z-index:1}
.phone img{width:100%;height:150px;object-fit:cover;display:block}
.phone .t{padding:12px 12px 0;font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:#BD9D60;font-weight:700}
.phone .n{padding:4px 12px 0;font-size:13px;line-height:1.3;font-weight:500;color:#333333}
.phone .d{display:flex;gap:5px;padding:12px}
.phone .d i{display:block;width:14px;height:14px;border-radius:50%;background:#EADCC9}
.phone .d i.f{background:#BD9D60}
.play{position:absolute;width:74px;height:74px;border-radius:50%;background:rgba(255,255,255,.92);left:50%;top:50%;margin:-37px 0 0 -37px;display:flex;align-items:center;justify-content:center}
.vid{position:relative;background:#333333;border-radius:2px;overflow:hidden}
.vid img{display:block;width:100%;height:100%;object-fit:cover;opacity:.88}
.step{display:flex;gap:20px;align-items:flex-start}
.num{flex:0 0 46px;height:46px;border-radius:50%;border:1px solid #BD9D60;color:#BD9D60;display:flex;align-items:center;justify-content:center;font-weight:500;font-size:18px}
.field{display:flex;flex-direction:column;gap:6px;margin:0 0 16px}
.field label{font-size:13px;font-weight:600;letter-spacing:.06em}
.field input,.field textarea,.field select{font-family:inherit;font-size:16px;padding:15px 16px;border:1px solid #D9C7B0;border-radius:2px;background:#FFFFFF;color:#333333}
.quote{font-size:24px;line-height:1.55;font-weight:300;font-style:italic}
@media (max-width:900px){
 .w,.wn{padding:0 22px}
 .sec{padding:68px 0}
 .row{flex-direction:column;gap:36px;align-items:stretch}
 .row>*{flex:1 1 auto !important;width:100%;position:static !important}
 .grid2,.grid3{grid-template-columns:repeat(1,minmax(0,1fr));gap:22px}
 .h1{font-size:33px;line-height:1.25}
 .h2{font-size:27px}
 .lead{font-size:18px}
 .p,.list li{font-size:17px}
 .nav,.lang.dsk,.hbtn.dsk{display:none}
 .burger{display:flex}
 .hdr .in{padding:12px 18px;gap:12px}
 .logo img{height:34px}
 .logo .wm{font-size:21px}
 .card,.buy{padding:24px}
 .ftr .cols{gap:32px}
 .hide-m{display:none}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&amp;display=swap" rel="stylesheet">'

CHECK = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#BD9D60" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10.5"></circle><path d="M7.5 12.3l3 3 6-6.3"></path></svg>'
DASH = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#BEA8A7" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10.5"></circle><path d="M8 12h8"></path></svg>'
PLAY = '<svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="#BD9D60"></path></svg>'
ARROW = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#BD9D60" stroke-width="1.6" aria-hidden="true"><path d="M12 4v16M6 14l6 6 6-6"></path></svg>'
BURGER = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#333333" stroke-width="1.6" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"></path></svg>'

def tbc(label, text):
    return f'<div class="tbc"><b>{label}</b>{text}</div>'

def header(active="", minimal=False):
    def a(href, label, key):
        cls = ' class="on"' if key == active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    logo = f'<a class="logo" href="Main.dc.html"><img src="{ICON}" alt=""><span><span class="wm">ROOTS</span><span class="sub">door TrudeThecla</span></span></a>'
    if minimal:
        return f'<header class="hdr"><div class="in">{logo}</div></header>'
    nav = ''.join([
        a("Main.dc.html#handboek", "Start hier", "home"),
        a("Programmas.dc.html", "Programma&#8217;s", "prog"),
        a("Inzicht.dc.html", "Inzicht", "inz"),
        a("Over.dc.html", "Over Trude", "over"),
        a("Contact.dc.html", "Contact", "contact"),
    ])
    return (f'<header class="hdr"><div class="in">{logo}<nav class="nav" aria-label="Hoofdmenu">{nav}</nav>'
            f'<div class="lang dsk"><span class="on">NL</span> | <a href="#">EN</a></div>'
            f'<a class="hbtn dsk" href="Main.dc.html#handboek">Gratis handboek</a>'
            f'<button class="burger" type="button" aria-label="Menu openen">{BURGER}</button></div></header>')

def footer():
    return f'''<footer class="ftr"><div class="w"><div class="cols">
<div style="flex:1 1 260px"><div class="wm">ROOTS</div><p class="ps" style="margin-top:10px;color:#FFFFFF">Zet je patroon uit bij de bron.</p><p class="ps" style="margin-top:22px;color:#FFFFFF">Een methode van TrudeThecla.</p></div>
<div><p class="h">Website</p><ul><li><a href="Main.dc.html#handboek">Start hier</a></li><li><a href="Programmas.dc.html">Programma&#8217;s</a></li><li><a href="Challenge.dc.html">Trigger Breakfree Challenge</a></li><li><a href="Inzicht.dc.html">Inzicht</a></li><li><a href="Main.dc.html#handboek">Gratis handboek</a></li><li><a href="Over.dc.html">Over Trude</a></li></ul></div>
<div><p class="h">Contact</p><ul><li><a href="Contact.dc.html">Stuur een bericht</a></li><li><a href="#">Instagram [@handle]</a></li><li><a href="#">Skool-community [naam en link]</a></li></ul></div>
<div><p class="h">Info</p><ul><li><a href="#">Privacyverklaring</a></li><li><a href="#">Algemene voorwaarden</a></li><li><a href="#">Cookies</a></li></ul></div>
</div><hr class="line" style="background:rgba(255,255,255,.4);margin:48px 0 20px"><p class="ps" style="color:#FFFFFF">&#169; TrudeThecla</p></div></footer>'''

def page(title, body, w=1440, h=4000):
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{CSS}</style>
</helmet>
<div style="width: 100%; font-family: Montserrat, Arial, sans-serif; color: #333333; background: #FAF1E8">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

def buycard(btn_href="Afrekenen.dc.html", compact=False):
    mock = f'''<div class="mock"><div class="dotsC" style="position:absolute;inset:0"></div><div class="phone"><img src="{PORTRAIT}" alt="Trude in de video van dag 1"><div class="t">Dag 1 van 7</div><div class="n">Trigger Breakfree Challenge</div><div class="d"><i class="f"></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div></div>'''
    return f'''<div class="buy">{mock}
<p class="cap" style="margin-top:24px">Trigger Breakfree Challenge</p>
<ul class="list" style="margin-bottom:18px">
<li style="font-size:16px">{CHECK}<span>7 dagen, elke dag een korte video van mij</span></li>
<li style="font-size:16px">{CHECK}<span>1 patroon van jezelf als werkmateriaal</span></li>
<li style="font-size:16px">{CHECK}<span>Samen in de community, en ik kijk mee</span></li>
</ul>
{tbc("Prijs en start", "[Prijs] &#183; [Startdatum]<br>In het concept van 8 nov stond: introductieprijs &#8364;49, daarna &#8364;79. Niet bevestigd.")}
<a class="btn" href="{btn_href}" style="display:block;margin-top:20px">Ja, ik doe mee</a>
<p class="ps" style="text-align:center;margin-top:12px;font-size:13px">Veilig afrekenen via Plug&amp;Pay &#183; [betaalmethoden bevestigen]</p>
</div>'''

def optin_card():
    return f'''<div class="buy" style="position:relative;padding:36px 36px 30px">
<div style="display:flex;gap:22px;align-items:center;margin-bottom:22px">
<img src="{COVER}" alt="Omslag Handboek Patroon-Reset" style="width:96px;flex:0 0 96px;box-shadow:0 10px 24px rgba(120,95,60,.18)">
<div><p class="kick" style="margin-bottom:8px">Gratis handboek</p><h2 class="h2" style="font-size:26px;margin:0">Handboek Patroon-Reset</h2></div>
</div>
<p class="ps" style="font-size:16px;margin-bottom:20px">Ontdek waarom je patroon terugkomt terwijl je het allang begrijpt. En waar echte verandering begint.</p>
<form>
<div class="field"><label>Voornaam</label><input type="text" placeholder="Je voornaam" aria-label="Voornaam"></div>
<div class="field"><label>E-mailadres</label><input type="email" placeholder="jij@voorbeeld.nl" aria-label="E-mailadres"></div>
<a class="btn" href="Bedankt.dc.html" style="display:block;margin-top:8px">Stuur mij het handboek</a>
</form>
<p class="ps" style="font-size:13px;margin-top:14px">Elf pagina&#8217;s, direct in je mailbox. Uitschrijven kan altijd. <a href="#">Privacyverklaring</a></p>
</div>'''

def hero(kick, h1, leads, right, extra="", sid=""):
    ps = ''.join(f'<p class="lead">{l}</p>' for l in leads)
    idattr = f' id="{sid}"' if sid else ''
    return f'''<section{idattr} style="padding:90px 0 100px;position:relative;overflow:hidden">
<div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div>
<div class="w"><div class="row" style="gap:72px">
<div class="c1" style="flex:1.25 1 0"><p class="kick">{kick}</p><h1 class="h1">{h1}</h1>{ps}{extra}</div>
<div class="c1" style="flex:1 1 0">{right}</div>
</div></div></section>'''
