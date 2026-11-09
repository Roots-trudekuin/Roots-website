from gen_common import *
COVER_EN = "/_blob/9c771f73242de6925af332c753654877"
PORTRAIT_EN = "/_blob/b75005e3606297823a6d47a9e3562265"

def header_en(active="home"):
    logo = f'<a class="logo" href="EN-Home.dc.html"><img src="{ICON}" alt=""><span><span class="wm">ROOTS</span><span class="sub">by TrudeThecla</span></span></a>'
    items = [("EN-Home.dc.html#handbook", "Start here", "home"), ("EN-Challenge.dc.html", "Challenge", "chal"),
             ("EN-Insights.dc.html", "Insights", "ins"), ("EN-About.dc.html", "About Trude", "about"), ("EN-Contact.dc.html", "Contact", "contact")]
    nav = ''.join(f'<a href="{h}"' + (' class="on"' if k == active else '') + f'>{l}</a>' for h, l, k in items)
    return (f'<header class="hdr"><div class="in">{logo}<nav class="nav" aria-label="Main menu">{nav}</nav>'
            f'<div class="lang dsk"><a href="Main.dc.html">NL</a> | <span class="on">EN</span></div>'
            f'<a class="hbtn dsk" href="EN-Home.dc.html#handbook">Free handbook</a>'
            f'<button class="burger" type="button" aria-label="Open menu">{BURGER}</button></div></header>')

def header_en_min():
    return f'<header class="hdr"><div class="in"><a class="logo" href="EN-Home.dc.html"><img src="{ICON}" alt=""><span><span class="wm">ROOTS</span><span class="sub">by TrudeThecla</span></span></a></div></header>'

def optin_en():
    return f'''<div class="buy" style="position:relative;padding:36px 36px 30px">
<div style="display:flex;gap:22px;align-items:center;margin-bottom:22px">
<img src="{COVER_EN}" alt="Handbook cover" style="width:96px;flex:0 0 96px;box-shadow:0 10px 24px rgba(120,95,60,.18)">
<div><p class="kick" style="margin-bottom:8px">Free handbook</p><h2 class="h2" style="font-size:26px;margin:0">Pattern Reset Handbook</h2></div>
</div>
<p class="ps" style="font-size:16px;margin-bottom:20px">Discover why your pattern keeps coming back even though you understood it long ago. And where real change begins.</p>
<form>
<div class="field"><label>First name</label><input type="text" placeholder="Your first name" aria-label="First name"></div>
<div class="field"><label>Email address</label><input type="email" placeholder="you@example.com" aria-label="Email address"></div>
<a class="btn" href="#" style="display:block;margin-top:8px">Send me the handbook</a>
</form>
<p class="ps" style="font-size:13px;margin-top:14px">Eleven pages, straight to your inbox. Unsubscribe anytime. <a href="#">Privacy policy</a></p>
</div>'''

def scene(where, intent, what, after):
    lab='font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#8E7372;margin-bottom:6px'
    return f'''<div class="row top" style="gap:44px;padding:34px 0;border-top:1px solid #E3D3BF">
<div style="flex:0 0 170px"><p class="cap" style="margin:6px 0 0">{where}</p></div>
<div class="c1"><p class="ps" style="{lab}">What you intended</p><p class="p" style="margin:0">{intent}</p></div>
<div class="c1" style="flex:1.6 1 0"><p class="ps" style="{lab}">What happened</p><p class="p" style="margin:0">{what}</p></div>
<div class="c1"><p class="ps" style="{lab}">And afterwards</p><p class="p" style="margin:0">{after}</p></div>
</div>'''

def wish(t, x): return f'<div class="card" style="padding:36px"><p class="cap">{t}</p><p class="p" style="margin:0">{x}</p></div>'

def footer_en():
    return f'''<footer class="ftr"><div class="w"><div class="cols">
<div style="flex:1 1 260px"><div class="wm">ROOTS</div><p class="ps" style="margin-top:10px;color:#FFFFFF">Switch off your pattern at the source.</p><p class="ps" style="margin-top:22px;color:#FFFFFF">A method by TrudeThecla.</p></div>
<div><p class="h">Website</p><ul><li><a href="EN-Home.dc.html#handbook">Start here</a></li><li><a href="EN-Challenge.dc.html">Trigger Breakfree Challenge</a></li><li><a href="EN-Insights.dc.html">Insights</a></li><li><a href="EN-Home.dc.html#handbook">Free handbook</a></li><li><a href="EN-About.dc.html">About Trude</a></li></ul></div>
<div><p class="h">Contact</p><ul><li><a href="EN-Contact.dc.html">Send a message</a></li><li><a href="#">Instagram [@handle]</a></li><li><a href="#">Skool community [name and link]</a></li></ul></div>
<div><p class="h">Info</p><ul><li><a href="#">Privacy policy</a></li><li><a href="#">Terms and conditions</a></li><li><a href="#">Cookies</a></li></ul></div>
</div><hr class="line" style="background:rgba(255,255,255,.4);margin:48px 0 20px"><p class="ps" style="color:#FFFFFF">&#169; TrudeThecla</p></div></footer>'''

EN = header_en("home") + f'''
<section id="handbook" style="padding:90px 0 100px;position:relative;overflow:hidden">
<div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div>
<div class="w"><div class="row" style="gap:72px">
<div class="c1" style="flex:1.25 1 0">
<p class="kick">ROOTS &#183; Switch off your pattern at the source</p>
<h1 class="h1">You know your pattern inside out. <span class="cam">And yet it takes over,</span> before you even get to choose.</h1>
<p class="lead">You had promised yourself to handle it differently this time. Stay calm. Say no. Just listen. And then comes that silence, that tone of voice, that one remark. Before you know it, you say yes, you snap, or you shut down.</p>
<p class="lead" style="margin-bottom:36px">Only afterwards do you see it: there it went again. Even though you know exactly where it comes from.</p>
<div style="display:flex;gap:28px;align-items:center;flex-wrap:wrap">
<a class="btn" href="#">Yes, send me the free handbook</a>
<a class="btn2" href="EN-Challenge.dc.html">Or go straight to the Trigger Breakfree Challenge &#8594;</a>
</div>
</div>
<div class="c1" style="flex:1 1 0">{optin_en()}</div>
</div></div>
</section>

<section class="rose" style="padding:80px 0"><div class="wn" style="text-align:center">
<p class="quote" style="margin:0;color:#FFFFFF">The frustrating part is not that you understand nothing.<br>The frustrating part is precisely that you understand so much, and it still happens.</p>
</div></section>

<section class="sec white"><div class="w">
<p class="kick">Does this sound familiar?</p>
<h2 class="h2" style="max-width:780px">You wanted to respond differently. And yet the old pattern took over.</h2>
<div style="margin-top:30px">
{scene("At work", "This week I&#8217;m not taking on anything extra.", "Your manager asks who will take on the project. There&#8217;s a silence. You feel restlessness in your chest, your breath catches for a moment. &#8216;I&#8217;ll do it.&#8217; You hear yourself say it before you&#8217;ve decided.", "That evening you&#8217;re angry with yourself. And now you have to do it too.")}
{scene("In your relationship", "Tonight I&#8217;ll calmly tell him I felt alone.", "You have the words ready. He sighs and looks at his phone. And suddenly you hear yourself getting sharp. Or you say &#8216;never mind&#8217; and walk out of the room.", "You lie awake. Why can&#8217;t I just say what I feel?")}
{scene("In a conversation", "I&#8217;ll listen first, and respond afterwards.", "A colleague says: &#8216;Can I give you some feedback?&#8217; Your cheeks get warm. You start explaining, justifying, defending. You don&#8217;t even hear what she actually said.", "Afterwards you know exactly what you would rather have said.")}
{scene("With family", "I won&#8217;t get dragged in this time.", "At the birthday party your mother makes that one remark. Within a second you feel twelve again. You adapt, and smile.", "You drive home with a knot in your stomach.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div>
<p class="lead" style="max-width:820px;margin-top:44px">You know where it comes from. You&#8217;ve explored it, felt it, talked it through. And yet it happens. <span class="cam" style="font-weight:500">It&#8217;s not a matter of too little insight.</span></p>
</div></section>

<section class="sec" style="position:relative;overflow:hidden"><div class="w">
<p class="kick">Imagine</p>
<h2 class="h2" style="max-width:820px">That same moment. <span class="cam">But now it unfolds differently.</span></h2>
<div class="grid3" style="margin-top:40px">
{wish("Staying with yourself", "He sighs and picks up his phone. You notice it. And you stay with yourself. &#8216;I want to tell you something. Will you look at me for a moment?&#8217; And then you say what you felt.")}
{wish("Setting your boundary", "The silence falls after the question of who will take it on. You feel it, and your body stays calm. &#8216;Not this time, my week is full.&#8217; No explanation. No guilt afterwards.")}
{wish("Listening without defending", "&#8216;Can I give you some feedback?&#8217; You feel curious instead of tense. &#8216;What exactly do you mean?&#8217; And you hear the whole story.")}
</div>
<p class="lead" style="max-width:820px;margin-top:48px">Not because you&#8217;ve got yourself better under control. But because the old pattern no longer decides first. How would that feel? And what would you do with all that space?</p>
</div></section>

<section class="sec white"><div class="w"><div class="row" style="gap:80px">
<div class="c1">
<p class="kick">A different perspective</p>
<h2 class="h2">Knowing where your pattern comes from is different from knowing what sets it off <span class="cam">now.</span></h2>
<p class="p">We grew up with one way of looking at patterns: through your history. That way isn&#8217;t wrong. It just doesn&#8217;t look at the place where the pattern gets switched on.</p>
<p class="p">Your story does not switch on your pattern. Your neurobiology does, using a few fragments of your story. Your survival system wants to protect you. And it uses old information for that, information that hasn&#8217;t been updated yet.</p>
<p class="p">That&#8217;s not your fault. And it can be changed. At the source.</p>
</div>
<div class="c1" style="display:flex;flex-direction:column;gap:18px">
<div class="cardS"><p class="cap" style="color:#8E7372">The question you always asked</p><p class="quote" style="margin:0">&#8220;Where does this come from?&#8221;</p></div>
<div style="display:flex;justify-content:center">{ARROW}</div>
<div class="cardS" style="border:1px solid #BD9D60"><p class="cap">The question that makes the difference</p><p class="quote" style="margin:0">&#8220;What set it off this time?&#8221;</p></div>
</div>
</div></div></section>

<section class="sec" style="position:relative;overflow:hidden"><div class="w"><div class="row" style="gap:90px">
<div style="flex:0 0 380px;position:relative" class="photo"><div class="dots" style="position:absolute;left:-40px;bottom:-40px;width:220px;height:220px;opacity:.6"></div><span class="tape"></span><img src="{COVER_EN}" alt="Handbook cover" style="position:relative;box-shadow:0 24px 60px rgba(120,95,60,.18)"></div>
<div class="c1">
<p class="kick">Free &#183; Pattern Reset Handbook</p>
<h2 class="h2">From insight to lasting change</h2>
<p class="lead">Discover why your pattern keeps coming back even though you understood it long ago. And where real change begins.</p>
<ul class="list">
<li>{CHECK}<span>Why understanding your pattern and your pattern switching on automatically are two different things</span></li>
<li>{CHECK}<span>The shift: looking from your neurobiology, not only from your story</span></li>
<li>{CHECK}<span>The three stages of ROOTS, in outline</span></li>
<li>{CHECK}<span>Sanne&#8217;s story: the same silence, a different outcome</span></li>
<li>{CHECK}<span>With a link to my free masterclass</span></li>
</ul>
<div style="display:flex;gap:24px;align-items:center;flex-wrap:wrap"><a class="btn" href="#">Yes, send me the handbook</a><span class="ps">Eleven pages. Straight to your inbox.</span></div>
</div>
</div></div></section>

<section class="sec white"><div class="w"><div class="row" style="gap:80px">
<div style="flex:0 0 340px" class="photo"><span class="tape"></span><img src="{PORTRAIT_EN}" alt="Portrait of Trude Kuin"></div>
<div class="c1">
<p class="kick">Who I am</p>
<h2 class="h2">I&#8217;m Trude.</h2>
<p class="p">Since 1988 I have guided people through personal change. As a consultant, coach, hypnotherapist and Havening practitioner. Thousands of people.</p>
<p class="p">All those years, one question stayed with me: how do I help people change in a way that gives them lasting influence over it themselves? Out of that question, ROOTS grew: the method that lets you switch off your pattern at the source.</p>
<a class="btn2" href="EN-About.dc.html">Read my story &#8594;</a>
</div>
</div></div></section>

<section class="sec"><div class="w">
<p class="kick" style="text-align:center">Where would you like to start?</p>
<h2 class="h2" style="text-align:center;max-width:760px;margin-left:auto;margin-right:auto">Two paths. The same source.</h2>
<div class="grid2" style="margin-top:50px">
<div class="card"><p class="cap">Understand first &#183; free</p><h3 class="h3" style="font-size:26px;font-weight:400">Pattern Reset Handbook</h3><p class="p">Read why your pattern keeps coming back, and watch the masterclass via the link in the handbook. At your own pace.</p><a class="btn" href="#">Send me the handbook</a></div>
<div class="card" style="border:1px solid #BD9D60"><p class="cap">Experience it now &#183; 7 days</p><h3 class="h3" style="font-size:26px;font-weight:400">Trigger Breakfree Challenge</h3><p class="p">You choose one pattern of your own. You discover what switches it on for you, and experience what it&#8217;s like when it no longer starts automatically. With me alongside you.</p><a class="btn" href="EN-Challenge.dc.html">View the Challenge</a></div>
</div>
</div></section>
''' + footer_en()

open('project/EN-Home.dc.html','w').write(page("Homepage (English)", EN, 1440, 6800).replace('lang="nl"','lang="en"'))
print('ok')
