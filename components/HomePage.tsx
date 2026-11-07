/* eslint-disable @next/next/no-img-element */
import type { Content } from "@/content/nl";
import Header from "./Header";
import Footer from "./Footer";
import ChallengeLink from "./ChallengeLink";
import HandbookForm from "./HandbookForm";
import { CoverPlaceholder } from "./Bits";

/*
  Homepage — opbouw:
  1 Hero (belofte → handboek, met formulier in de kaart)
  2 Oudroze balk
  3 Herkenning
  4 De denkshift
  5 Ervaring (cijfers)
  6 Programma's (aanbod in 4 stappen)
  7 Over Trude
  8 Afsluiting
*/
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
              <p className="eyebrow">{c.hero.eyebrow}</p>
              <h1 id="hero-titel">{c.hero.title}</h1>
              <p className="hero-lead">{c.hero.p1}</p>
              <p className="hero-bridge">{c.hero.p2}</p>
            </div>

            <aside className="offer-card reveal" id={ids.handbook} aria-labelledby="offer-titel">
              <p className="eyebrow">{c.hero.card.eyebrow}</p>
              <h2 id="offer-titel">{c.hero.card.title}</h2>
              <p className="offer-sub">{c.hero.card.subtitle}</p>
              <div className="offer-body">
                <div className="book-wrap" aria-hidden="true">
                  <div className="book">
                    {c.handbook.cover ? <img src={c.handbook.cover} alt="" /> : <CoverPlaceholder c={c} small />}
                    <span className="pages" />
                  </div>
                  <span className="book-shadow" />
                </div>
                <div className="offer-form">
                  <HandbookForm c={c} />
                  <p className="offer-note">{c.hero.card.note}</p>
                </div>
              </div>
            </aside>
          </div>
        </section>

        {/* 2 · OUDROZE BALK */}
        <section className="band-rose" aria-label={c.band.line1}>
          <div className="wrap center reveal">
            <p className="band-text">{c.band.line1}<br />{c.band.line2}</p>
          </div>
        </section>

        {/* 3 · HERKENNING */}
        <section className="section bg-white" aria-labelledby="herkenning-titel">
          <div className="wrap narrow center reveal">
            <h2 id="herkenning-titel" className="quote-heading">{c.recognition.title}</h2>
            {c.recognition.paragraphs.map((p) => <p key={p}>{p}</p>)}
            <p className="callout">{c.recognition.callout}</p>
          </div>
        </section>

        {/* 4 · DE DENKSHIFT */}
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

        {/* 5 · ERVARING */}
        <section className="section-tight bg-white" aria-labelledby="ervaring-titel">
          <div className="wrap center reveal">
            <h2 id="ervaring-titel" className="exp-title">{c.experience.title}</h2>
            <ul className="stats">
              {c.experience.stats.map((s) => (
                <li key={s.label}><strong>{s.n}</strong>{s.label}</li>
              ))}
            </ul>
          </div>
        </section>

        {/* 6 · PROGRAMMA'S */}
        <section className="section bg-seashell" id={ids.offer} aria-labelledby="aanbod-titel">
          <div className="wrap">
            <div className="narrow center reveal">
              <p className="eyebrow">{c.offer.eyebrow}</p>
              <h2 id="aanbod-titel">{c.offer.title}</h2>
              <p>{c.offer.intro}</p>
            </div>
            <ul className="offer-grid">
              {c.offer.cards.map((o) => (
                <li key={o.title} className={"offer-item reveal" + (o.kind === "form" ? " is-first" : "")}>
                  <img className="offer-icon" src="/img/logo-icoon.png" alt="" aria-hidden="true" />
                  <p className="offer-step">{o.step}</p>
                  <h3>{o.title}</h3>
                  <p className="offer-tag">{o.tag}</p>
                  <p className="offer-text">{o.text}</p>
                  <div className="offer-action">
                    {o.kind === "form" && <a className="btn btn-primary" href={`#${ids.form}`}>{o.cta}</a>}
                    {o.kind === "challenge" && (
                      <ChallengeLink lang={c.lang} className="btn btn-secondary" message={c.ui.noSales}>{o.cta}</ChallengeLink>
                    )}
                    {o.kind === "note" && <p className="offer-hint">{o.cta}</p>}
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </section>

        {/* 7 · OVER TRUDE */}
        <section className="section bg-white" id={ids.about} aria-labelledby="over-titel">
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
              <a className="btn btn-primary" href={`#${ids.form}`}>{c.closing.primary}</a>
            </div>
          </div>
        </section>
      </main>
      <Footer c={c} onHome />
    </>
  );
}
