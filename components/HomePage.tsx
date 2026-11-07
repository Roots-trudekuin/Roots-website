/* eslint-disable @next/next/no-img-element */
import type { Content } from "@/content/nl";
import Header from "./Header";
import Footer from "./Footer";
import ChallengeLink from "./ChallengeLink";
import HandbookForm from "./HandbookForm";
import { Eyebrow, PriceLine, CoverPlaceholder } from "./Bits";
import { Download, Lock } from "./Icons";

export default function HomePage({ c }: { c: Content }) {
  const { ids } = c;
  return (
    <>
      <a className="skip-link" href="#inhoud">{c.ui.skip}</a>
      <Header c={c} page="home" />
      <main id="inhoud">

        {/* 1 · HERO */}
        <section className="section hero bg-seashell" id={ids.start} aria-labelledby="hero-titel">
          <div className="wrap hero-grid">
            <div className="reveal">
              <p className="eyebrow eyebrow-plain">{c.hero.eyebrow}</p>
              <h1 id="hero-titel">
                {c.hero.titleBefore}<span className="hl">{c.hero.titleHighlight}</span>{c.hero.titleAfter}
              </h1>
              <p className="hero-intro">{c.hero.intro}</p>
              <ul className="sparkle-list">
                {c.hero.bullets.map((b) => <li key={b}>{b}</li>)}
              </ul>
              <div className="btn-row">
                <a className="btn btn-primary btn-icon" href={`#${ids.form}`}><Download /> {c.hero.primary}</a>
              </div>
            </div>

            <aside className="offer-card reveal" aria-labelledby="offer-titel">
              <p className="eyebrow eyebrow-plain">{c.hero.card.eyebrow}</p>
              <h2 id="offer-titel">{c.hero.card.title}</h2>
              <p className="offer-sub">{c.hero.card.subtitle}</p>
              <div className="star-divider" aria-hidden="true"><span>✦</span></div>
              <div className="book-wrap" aria-hidden="true">
                <div className="book">
                  {c.handbook.cover ? <img src={c.handbook.cover} alt="" /> : <CoverPlaceholder c={c} small />}
                  <span className="pages" />
                </div>
                <span className="book-shadow" />
              </div>
              <a className="btn btn-primary btn-icon" href={`#${ids.form}`}><Download /> {c.hero.card.button}</a>
              <p className="offer-note"><Lock /> {c.hero.card.note}</p>
            </aside>
          </div>
        </section>

        {/* 2 · HERKENNING */}
        <section className="section bg-white" aria-labelledby="herkenning-titel">
          <div className="wrap narrow center reveal">
            <h2 id="herkenning-titel" className="quote-heading">{c.recognition.title}</h2>
            {c.recognition.paragraphs.map((p) => <p key={p}>{p}</p>)}
            <p className="callout">{c.recognition.callout}</p>
          </div>
        </section>

        {/* 3 · DE DENKSHIFT */}
        <section className="section bg-seashell" aria-labelledby="shift-titel">
          <div className="wrap split">
            <div className="reveal">
              <h2 id="shift-titel">{c.shift.title}</h2>
              <div className="rule" />
            </div>
            <div className="reveal">
              {c.shift.paragraphs.map((p) => <p key={p}>{p}</p>)}
              <p className="callout">{c.shift.callout}</p>
            </div>
          </div>
        </section>

        {/* OUDROZE BALK — samenvatting van de denkshift */}
        <section className="band-purple" aria-label={c.band.line1}>
          {["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"].map((s) => (
            <span key={s} className={`star ${s}`} aria-hidden="true">✦</span>
          ))}
          <div className="wrap center reveal">
            <p className="band-text">{c.band.line1}<br />{c.band.line2}</p>
            <div className="star-divider" aria-hidden="true"><span>✦</span></div>
          </div>
        </section>

        {/* 4 · ONTDEK · HANDBOEK */}
        <section className="section bg-white" id={ids.handbook} aria-labelledby="handboek-titel">
          <div className="wrap handboek-grid">
            <figure className="reveal" style={{ margin: 0 }}>
              <div className="cover-frame">
                {c.handbook.cover
                  ? <img src={c.handbook.cover} width={900} height={1272} alt={c.handbook.coverAlt} />
                  : <CoverPlaceholder c={c} />}
              </div>
              <figcaption className="cover-caption">{c.handbook.caption}</figcaption>
            </figure>
            <div className="reveal">
              <Eyebrow step={c.handbook.step} label={c.handbook.eyebrow} />
              <h2 id="handboek-titel">{c.handbook.title}</h2>
              {c.handbook.paragraphs.map((p) => <p key={p}>{p}</p>)}
              <HandbookForm c={c} />
            </div>
          </div>
        </section>

        {/* 5 · BEGRIJP · MASTERCLASS */}
        <section className="section bg-seashell" id={ids.masterclass} aria-labelledby="masterclass-titel">
          <div className="wrap">
            <div className="panel reveal">
              <div className="narrow">
                <Eyebrow step={c.masterclass.step} label={c.masterclass.eyebrow} />
                <h2 id="masterclass-titel">{c.masterclass.title}</h2>
                {c.masterclass.paragraphs.map((p) => <p key={p}>{p}</p>)}
                <div className="btn-row">
                  <a className="btn btn-secondary btn-arrow" href={`#${ids.handbook}`}>{c.masterclass.landingButton}</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 6 · ERVAAR · BREAKFREE CHALLENGE */}
        <section className="section bg-white" id={ids.challenge} aria-labelledby="challenge-titel">
          <div className="wrap">
            <div className="narrow center reveal">
              <Eyebrow step={c.challenge.step} label={c.challenge.eyebrow} />
              <h2 id="challenge-titel">{c.challenge.title}</h2>
              {c.challenge.paragraphs.map((p) => <p key={p}>{p}</p>)}
            </div>
            <ul className="facts reveal" aria-label={c.challenge.factsLabel}>
              {c.challenge.facts.map((f) => <li key={f.big}><strong>{f.big}</strong>{f.small}</li>)}
            </ul>
            <div className="center reveal">
              <PriceLine c={c} />
              <div className="btn-row">
                <ChallengeLink lang={c.lang} className="btn btn-primary btn-arrow" message={c.ui.noSales}>{c.challenge.button}</ChallengeLink>
              </div>
            </div>
          </div>
        </section>

        {/* 7 · OVER TRUDE */}
        <section className="section bg-seashell" id={ids.about} aria-labelledby="over-titel">
          <div className="wrap about-grid">
            <div className="portrait reveal">
              <img src={c.about.portrait} width={800} height={800} alt={c.about.portraitAlt} />
            </div>
            <div className="reveal">
              <h2 id="over-titel">{c.about.title}</h2>
              {c.about.paragraphs.map((p) => <p key={p}>{p}</p>)}
              <p className="signature">{c.about.signature}</p>
            </div>
          </div>
        </section>

        {/* 8 · AFSLUITING */}
        <section className="section bg-rose closing" aria-labelledby="slot-titel">
          <div className="wrap narrow center reveal">
            <h2 id="slot-titel">{c.closing.title}</h2>
            <p>{c.closing.p1}</p>
            <p className="contrast">{c.closing.notOnlyLead} <em>{c.closing.notOnly}</em></p>
            <p className="contrast">{c.closing.butAlsoLead} <em>{c.closing.butAlso}</em></p>
            <div className="btn-row">
              <a className="btn btn-primary btn-arrow" href={`#${ids.handbook}`}>{c.closing.primary}</a>
            </div>
            <ChallengeLink lang={c.lang} className="text-link" message={c.ui.noSales}>{c.closing.link}</ChallengeLink>
          </div>
        </section>
      </main>
      <Footer c={c} onHome />
    </>
  );
}
