from gen_common import *
from gen_en import header_en, footer_en, optin_en, PORTRAIT_EN
from gen_en_pages import hero_en
from gen_sales import faq

PAY_IND, PAY_HAV, BOOK = "PAY-IND", "PAY-HAV", "BOOK-KM"
PRIJS_IND, PRIJS_HAV = "&#8364;1,335", "&#8364;500"


def intro_call(label="Book a free 20-minute introductory call"):
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
<p class="ps" style="text-align:center;margin-top:16px">{intro_call("Want to meet first? Book 20 minutes for free")}</p>
<p class="ps" style="text-align:center;margin-top:12px"><a class="btn2" href="EN-Contact.dc.html">Rather ask a question first? Get in touch &#8594;</a></p>
</div>'''


IND_OFFER = offer("Individual programme", "Your pattern, one to one with me",
                  ["8 online sessions with me", "Your own pattern is what we work with", "The same steps as the Challenge, at your pace"],
                  PRIJS_IND, "For the full programme of 8 sessions", "Yes, I want to start", PAY_IND)
HAV_OFFER = offer("Havening &amp; hypnosis", "3 sessions for one theme",
                  ["3 online sessions of 1.5 hours", "One theme of your choice", "Havening and hypnosis combined"],
                  PRIJS_HAV, "For 3 sessions together", "Book 3 sessions", PAY_HAV)


def sessie(n, titel, tekst):
    return f'<div class="step" style="padding:22px 0;border-top:1px solid #E3D3BF"><div class="num">{n}</div><div><h3 class="h3">{titel}</h3><p class="ps" style="font-size:16px">{tekst}</p></div></div>'


def progcard(cap, title, text, href, label, extra=""):
    return f'''<div class="card" style="display:flex;flex-direction:column;background:#FAF1E8">
<p class="cap">{cap}</p><h3 class="h3" style="font-size:26px;font-weight:400">{title}</h3>
<p class="p" style="flex:1 1 auto">{text}</p>{extra}
<a class="btn" href="{href}" style="align-self:flex-start">{label}</a></div>'''


EN_PROGRAMMES = header_en("prog") + hero_en(
    "Programmes",
    'Choose how you work with your pattern. <span class="cam">On your own, in a group or with me.</span>',
    ["Every programme is about the same thing: your old pattern no longer automatically decides how you react. You choose how you get there, and at what pace.",
     "Not sure yet? Start with the free handbook."],
    optin_en()) + f'''
<section class="sec white"><div class="w">
<p class="kick" style="text-align:center">What I offer</p>
<h2 class="h2" style="text-align:center">Three ways to begin</h2>
<div class="grid3" style="margin-top:46px">
{progcard("One to one &#183; 8 sessions", "Individual programme", "You work with one of your own patterns, together with me. The same steps as the Challenge, fully tailored to you and at your pace. Online.", "EN-Individual.dc.html", "View the programme", f'<p class="ps" style="margin-bottom:20px;font-weight:600">{PRIJS_IND} &#183; 8 online sessions</p>')}
{progcard("In a group &#183; 7 days", "Trigger Breakfree Challenge", "Seven days, one pattern of your own. A short video and one thing to do every day, with the community around you. I&#8217;m there with you.", "EN-Challenge.dc.html", "View the Challenge", '<p class="ps" style="margin-bottom:20px;font-weight:600">Coming soon in English</p>')}
{progcard("Short track &#183; 3 sessions", "Havening &amp; hypnosis", "For one clear theme: a reaction that keeps coming back, tension around a particular moment, or a goal you keep getting stuck on.", "EN-Havening.dc.html", "View the themes", f'<p class="ps" style="margin-bottom:20px;font-weight:600">{PRIJS_HAV} &#183; 3 online sessions of 1.5 hours</p>')}
</div>
</div></section>
<section class="sec"><div class="wn" style="text-align:center">
<p class="kick">Not sure what suits you?</p>
<h2 class="h2">Let&#8217;s talk for 20 minutes.</h2>
<p class="p">You tell me what you run into. I&#8217;ll tell you honestly which programme fits, or that none of them does. Free and online.</p>
<div style="display:flex;gap:26px;justify-content:center;align-items:center;flex-wrap:wrap"><a class="btn" href="{BOOK}">Book a free introductory call</a><a class="btn2" href="EN-Contact.dc.html">Or get in touch &#8594;</a></div>
</div></section>
''' + footer_en()

EN_INDIVIDUAL = header_en("prog") + hero_en(
    "Individual programme &#183; 8 online sessions",
    'Imagine your old pattern <span class="cam">no longer automatically deciding</span> how you react. With me by your side.',
    ["You choose one pattern you really want to be free of. In eight sessions we discover together what it protects you from, what switches it on in <em>you</em>, and what it is like when it no longer switches on automatically.",
     "The same steps as the Trigger Breakfree Challenge. Only now fully tailored to you, at your pace."],
    IND_OFFER) + f'''
<section class="sec white"><div class="wn">
<p class="kick">You know this</p>
<h2 class="h2">You know where it comes from. And still it happens again.</h2>
<p class="p">A silence in the meeting. That one tone in your partner&#8217;s voice. Feedback from a colleague. And before you know it you say yes, you snap, you withdraw or you start explaining. Afterwards you know exactly what you would rather have done.</p>
<p class="p">You have done a lot already. Conversations, books, courses. You understand your pattern inside out. Only in the moment itself, that understanding doesn&#8217;t help you.</p>
<p class="lead cam" style="font-weight:500;margin-top:30px">That is not your fault. You were working on a different layer from the one where your pattern is switched on.</p>
</div></section>

<section class="sec"><div class="w"><div class="row top" style="gap:72px">
<div class="c1">
<p class="kick">Why one to one</p>
<h2 class="h2">Sometimes you don&#8217;t want to do this in a group.</h2>
<p class="p">Because your pattern is stubborn. Because you would rather not share in a community. Because you want someone to see exactly what happens in <em>you</em>, and adjust straight away.</p>
<p class="p">In the individual programme you have me just for you. We take the time your pattern needs. And I see what you can&#8217;t see yourself in that moment.</p>
</div>
<div class="c1">
<div class="cardS" style="background:#FFFFFF">
<p class="cap">Challenge or individual?</p>
<ul class="list" style="margin:0">
<li style="font-size:16px">{CHECK}<span><b style="font-weight:600">Challenge:</b> seven days, in a group, with videos and the community.</span></li>
<li style="font-size:16px">{CHECK}<span><b style="font-weight:600">Individual:</b> eight sessions with me, on your pattern and at your pace.</span></li>
</ul>
</div>
</div>
</div></div></section>

<section class="sec white"><div class="wn">
<p class="kick">What the programme looks like</p>
<h2 class="h2">Eight sessions, one pattern</h2>
{sessie(1, "Getting to know each other and choosing your pattern", "Which pattern do you want to be free of? When does it take over, and what does it cost you?")}
{sessie(2, "Mapping your pattern", "The circle it keeps coming back in, and what it protects you from.")}
{sessie(3, "Finding", "What switches it on in <em>you</em>? We look for the piece your system uses.")}
{sessie(4, "Finding, further", "The moment, the body, the small details that set off the alarm.")}
{sessie(5, "Breaking the link", "So the alarm no longer goes off at that piece.")}
{sessie(6, "Breaking through your pattern", "No longer doing the old part of the pattern, in your own life.")}
{sessie(7, "Strengthening", "What do you <em>want</em> to run automatically? That is what we build.")}
{sessie(8, "Carrying on yourself", "You know how to read a relapse and what to do then. You have influence yourself.")}
<div style="border-top:1px solid #E3D3BF"></div>
<p class="ps" style="margin-top:22px">All sessions are online. We schedule them together.</p>
</div></section>

<section class="sec"><div class="w"><div class="row" style="gap:72px">
<div style="flex:0 0 360px" class="photo"><img src="{PORTRAIT}" alt="Portrait of Trude Kuin"></div>
<div class="c1">
<p class="kick">Who will you work with?</p>
<h2 class="h2">I&#8217;m Trude.</h2>
<p class="p">Since 1988 I have guided people through personal change. As a consultant, coach, hypnotherapist and Havening practitioner. Always with the same question: how do I help people change in a way that gives them lasting influence over it themselves?</p>
<p class="p">My answer to that is ROOTS. In the individual programme I use it on your pattern, together with you.</p>
<a class="btn2" href="EN-About.dc.html">More about me &#8594;</a>
</div>
</div></div></section>

<section class="sec white"><div class="w"><div class="grid2" style="gap:56px">
<div><h3 class="h3">For you if</h3><ul class="list">
<li>{CHECK}<span>you have understood your pattern for a long time, and it still takes over</span></li>
<li>{CHECK}<span>you really want to be free of one pattern</span></li>
<li>{CHECK}<span>you would rather work one to one than in a group</span></li>
</ul></div>
<div><h3 class="h3">Not for you if</h3><ul class="list">
<li>{DASH}<span>you are looking for more insight. You have enough of that.</span></li>
<li>{DASH}<span>you would rather try it in a group first. Then look at the <a href="EN-Challenge.dc.html">Challenge</a>.</span></li>
</ul></div>
</div></div></section>

<section class="sec"><div class="wn">
<p class="kick">&#8220;But&#8230;&#8221;</p>
<h2 class="h2">Maybe you&#8217;re thinking&#8230;</h2>
{faq("&#8220;I&#8217;ve already done so much.&#8221;", "Exactly. Everything you did worked on your story, your understanding or your behaviour. This works on the layer underneath.")}
{faq("&#8220;Do I have to go back to the past again?&#8221;", "No. We are not looking for a new explanation. We look for the piece your survival system uses now.")}
{faq("&#8220;Does this work online?&#8221;", "Yes. All sessions are online, from your own home.")}
{faq("&#8220;I don&#8217;t know if this is right for me.&#8221;", "Then book a free 20-minute introductory call first. We&#8217;ll see together whether it fits.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>

<section class="rose" style="padding:90px 0"><div class="wn" style="text-align:center">
<h2 class="h2">Ready to begin?</h2>
<p class="lead">Eight online sessions with me, on your pattern. {PRIJS_IND} for the full programme.</p>
<a class="btn" href="{PAY_IND}" style="background:#FFFFFF;color:#333333">Yes, I want to start</a>
<p class="ps" style="margin-top:20px"><a href="{BOOK}" style="color:#FFFFFF">Or book a free 20-minute introductory call first &#8594;</a></p>
<p class="lead" style="margin-top:36px">And you are going to make it!</p>
<p class="lead" style="font-weight:500">Love, Trude</p>
</div></section>
''' + footer_en()

THEMES = [
    ("recurring-reaction", "A reaction that keeps coming back",
     "You know how you want to react. And still that one reaction takes over every time.",
     ["You snap, when you wanted to stay calm", "You say yes, when you mean no", "You shut down in a conversation that matters", "Afterwards you think: I did it <em>again</em>"],
     "We choose one reaction that keeps coming back. We look at the moment it switches on, and work with what happens in your body then. The aim: that this reaction no longer switches on automatically, so you can choose for yourself."),
    ("tension-around-a-moment", "Tension around a specific moment",
     "A presentation, a difficult conversation, an appointment coming up. Your body braces itself before it even happens.",
     ["You sleep badly before an important conversation", "Your body tenses as soon as you think about it", "You put things off because the moment feels so heavy", "You want to do it well, and that is exactly why it works less well"],
     "We take that one moment as our starting point. We work with the tension that belongs to it, and with how you <em>do</em> want to experience the moment. So you can stand in it more calmly."),
    ("memory-that-still-carries-tension", "A memory that still carries tension",
     "It was a long time ago. You know it is over. And still you feel it when you think about it.",
     ["A memory keeps coming back, even when you don&#8217;t want it to", "You feel the tension again when you think about it", "You avoid places, people or subjects that touch on it", "You want to give it a place, without having to talk about it again and again"],
     "We work with the alarm still attached to that memory. You don&#8217;t have to tell me everything about it. The aim: that you can think about it without your body sounding the alarm straight away."),
    ("stuck-on-your-goal", "Getting stuck on the way to your goal",
     "You know what you want. You have a plan. And still you don&#8217;t get moving, or you drop out halfway.",
     ["You postpone what really matters to you", "You start full of energy and stop halfway", "A little voice says it won&#8217;t work anyway", "You see others doing what you want to do too"],
     "We look at the moment you get stuck. What switches on then, and what does it protect you from? That is what we work with. And we strengthen how it feels to <em>get</em> moving."),
    ("longing-and-meaning", "Longing and meaning",
     "There is something you want, but you don&#8217;t quite know what. Or you do know, and it still feels far away.",
     ["You feel a longing for more, without being able to name it", "Your life runs, but it doesn&#8217;t really touch you", "You are looking for direction for the coming years", "You want to be closer to what really matters to you"],
     "We make room for what you really want. In hypnosis you can feel and explore that longing. With Havening we work with what holds you back. So you can choose a direction from within yourself."),
]


def theme_href(slug):
    return f"EN-Theme-{slug}.dc.html"


HAV_EXPLAIN = '''<div class="grid2" style="gap:48px;margin-top:30px">
<div class="card"><p class="cap">Havening</p><p class="p" style="margin:0">A method using gentle touch on your arms, hands and face, while your attention is on a particular feeling or moment. Online you do the touch yourself, and I guide you step by step.</p></div>
<div class="card"><p class="cap">Hypnosis</p><p class="p" style="margin:0">A calm, focused state in which it is easier to feel what you <em>do</em> want. In that state we strengthen the reaction you want to have, so it becomes more natural.</p></div>
</div>'''


def three_sessions():
    return f'''<section class="sec white"><div class="wn">
<p class="kick">How the 3 sessions work</p>
<h2 class="h2">Three times 1.5 hours, online</h2>
{sessie(1, "Your theme made clear", "What do you run into, and how <em>do</em> you want it? We choose what we work with and begin straight away.")}
{sessie(2, "Working with Havening and hypnosis", "We work with the tension that belongs to your theme, and strengthen what you <em>do</em> want.")}
{sessie(3, "Anchoring", "What do you notice in daily life? We continue where needed, and close with what you can do yourself.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>'''


IND_DIFF = 'The 3 sessions are for one clear theme. In the <a href="EN-Individual.dc.html">individual programme</a> you work on a pattern over 8 sessions, using the full ROOTS steps.'

HAV_FAQ = f'''<section class="sec"><div class="wn">
<p class="kick">Questions</p>
<h2 class="h2">Good to know</h2>
{faq("Does Havening work online?", "Yes. You do the touch yourself, and I guide you. All you need is a quiet place and a laptop or tablet with a camera.")}
{faq("Do I have to tell you everything?", "No. You tell me what you want to tell me. For Havening it is not necessary to explain everything.")}
{faq("What is the difference with the individual programme?", IND_DIFF)}
{faq("Not sure which theme fits you?", "Book a free 20-minute introductory call. We&#8217;ll look at it together.")}
<div style="border-top:1px solid #E3D3BF"></div>
</div></section>'''


def close_band(title):
    return f'''<section class="rose" style="padding:90px 0"><div class="wn" style="text-align:center">
<h2 class="h2">{title}</h2>
<p class="lead">3 online sessions of 1.5 hours. {PRIJS_HAV} together.</p>
<a class="btn" href="{PAY_HAV}" style="background:#FFFFFF;color:#333333">Book 3 sessions</a>
<p class="ps" style="margin-top:20px"><a href="{BOOK}" style="color:#FFFFFF">Or book a free 20-minute introductory call first &#8594;</a></p>
<p class="lead" style="margin-top:36px;font-weight:500">Love, Trude</p>
</div></section>'''


def themecard(slug, title, sub):
    return f'''<a href="{theme_href(slug)}" class="card" style="text-decoration:none;color:#333333;display:flex;flex-direction:column;background:#FAF1E8">
<h3 class="h3" style="font-size:22px;font-weight:400">{title}</h3><p class="ps" style="font-size:16px;flex:1 1 auto">{sub}</p>
<span class="btn2" style="align-self:flex-start;margin-top:18px">Read more &#8594;</span></a>'''


EN_HAVENING = header_en("prog") + hero_en(
    "Havening &amp; hypnosis &#183; 3 sessions",
    'One theme. Three sessions. <span class="cam">So it no longer takes over automatically.</span>',
    ["Sometimes you don&#8217;t want a whole programme. You have one thing that keeps coming back, one moment that brings tension, or one goal you keep getting stuck on.",
     "In three online sessions we work on that in a focused way, with Havening and hypnosis."],
    HAV_OFFER) + f'''
<section class="sec white"><div class="w">
<p class="kick" style="text-align:center">What can I help you with?</p>
<h2 class="h2" style="text-align:center">Choose your theme</h2>
<div class="grid3" style="margin-top:46px">
{''.join(themecard(s, t, sub) for s, t, sub, *_ in THEMES)}
<div class="card" style="background:#FFFFFF;border:1px solid #BD9D60;display:flex;flex-direction:column"><h3 class="h3" style="font-size:22px;font-weight:400">Is your theme not listed?</h3><p class="ps" style="font-size:16px;flex:1 1 auto">Tell me what you run into. Then we&#8217;ll see together whether this fits.</p><a class="btn2" href="{BOOK}" style="align-self:flex-start;margin-top:18px">Book a free introductory call &#8594;</a></div>
</div>
</div></section>
<section class="sec"><div class="wn">
<p class="kick">What it involves</p>
<h2 class="h2">Havening and hypnosis</h2>
<p class="p">I have worked with both for years. Together they are strong: Havening works with the alarm attached to a moment or memory, hypnosis strengthens how you <em>do</em> want it.</p>
{HAV_EXPLAIN}
</div></section>
{three_sessions()}
{HAV_FAQ}
''' + close_band("Ready to work on your theme?") + footer_en()


def theme_page(slug, title, sub, recog, approach):
    li = ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in recog)
    return header_en("prog") + hero_en(
        "Havening &amp; hypnosis &#183; theme", title, [sub],
        HAV_OFFER, '<a class="btn2" href="EN-Havening.dc.html">&#8592; All themes</a>') + f'''
<section class="sec white"><div class="w"><div class="row top" style="gap:72px">
<div class="c1"><p class="kick">Do you recognise this?</p><h2 class="h2">{title}</h2><ul class="list">{li}</ul></div>
<div class="c1"><p class="kick">What we do</p><h2 class="h2">How we work on it</h2><p class="p">{approach}</p></div>
</div></div></section>
<section class="sec"><div class="wn"><p class="kick">What it involves</p><h2 class="h2">Havening and hypnosis</h2>{HAV_EXPLAIN}</div></section>
{three_sessions()}
{HAV_FAQ}
''' + close_band("Would you like to work on this?") + footer_en()


THEME_PAGES = {slug: (t, sub, theme_page(slug, t, sub, r, a)) for slug, t, sub, r, a in THEMES}

THEMAS_EN = ["Breaking patterns", "Energy boost", "Changing habits", "Calm in your system", "Relationships", "Reaching your goal", "Direction and meaning", "Something else"]
_chips = ''.join(f'<label class="chip"><input type="checkbox" name="theme" value="{t}"><span>{t}</span></label>' for t in THEMAS_EN)

EN_CONTACT2 = header_en("contact") + f'''
<section style="padding:90px 0 110px;position:relative;overflow:hidden"><div class="dots hide-m" style="position:absolute;right:0;top:0;width:280px;height:220px;opacity:.5"></div><div class="w"><div class="row top" style="gap:72px">
<div class="c1" style="flex:1 1 0">
<p class="kick">Contact</p><h1 class="h1">Let&#8217;s <span class="cam">talk.</span></h1>
<p class="lead">A question, an idea, or just a feeling that it&#8217;s time for something different? Tell me. It doesn&#8217;t have to be completely clear yet. I read everything myself.</p>
<div style="display:flex;flex-direction:column;gap:14px;margin:34px 0 0;max-width:420px">
<a class="btn" href="WA-DIRECT">Message me on WhatsApp</a>
<a class="btn2" href="BOOK-KM" style="align-self:flex-start">Book a free 20-minute introductory call &#8594;</a>
</div>
<p class="kick" style="margin-top:64px">What happens next?</p>
<div style="display:flex;flex-direction:column;gap:22px">
<div class="step"><div class="num">1</div><div><h3 class="h3">I read your message</h3><p class="ps">Myself, and with attention.</p></div></div>
<div class="step"><div class="num">2</div><div><h3 class="h3">I get back to you</h3><p class="ps">With an answer, a question in return, or a suggestion for an introductory call.</p></div></div>
<div class="step"><div class="num">3</div><div><h3 class="h3">We look at what fits</h3><p class="ps">Honestly. Even if that means something else suits you better.</p></div></div>
</div>
</div>
<div class="c1" style="flex:1.1 1 0">
<form class="buy" id="cform" FORM-ATTR style="padding:40px;position:relative;z-index:1">
<p class="kick" style="margin-bottom:8px">Send a message</p>
<div class="grid2" style="gap:16px"><div class="field"><label for="c1">Name *</label><input id="c1" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="c2">Email address *</label><input id="c2" name="email" type="email" autocomplete="email" required></div></div>
<p class="field" style="margin-bottom:10px"><label>Choose your theme</label><span class="ps" style="font-size:13px">Pick all that apply</span></p>
<div class="chips">{_chips}</div>
<div class="field" style="margin-top:22px"><label for="c3">Tell me more</label><textarea id="c3" name="message" rows="7" placeholder="What do you run into, or what would you like to achieve?"></textarea></div>
<label style="display:flex;gap:10px;font-size:14px;line-height:1.5;margin:4px 0 20px"><input type="checkbox" required> I agree to the <a href="#">privacy policy</a>.</label>
<button class="btn" type="submit" style="width:100%">Send &#8594;</button>
</form>
</div>
</div></div></section>
''' + footer_en()
