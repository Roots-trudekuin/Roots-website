import type { Content } from "@/content/nl";
import Header from "./Header";
import Footer from "./Footer";
import ChallengeLink from "./ChallengeLink";
import { Eyebrow, PriceLine, MasterclassVideo } from "./Bits";

export default function MasterclassPage({ c }: { c: Content }) {
  return (
    <>
      <a className="skip-link" href="#inhoud">{c.ui.skip}</a>
      <Header c={c} page="masterclass" />
      <main id="inhoud">
        <section className="page-intro bg-seashell" aria-labelledby="mc-titel">
          <div className="wrap narrow reveal">
            <Eyebrow step={c.masterclass.step} label={c.masterclass.pageEyebrow} />
            <h1 id="mc-titel">{c.masterclass.pageTitle}</h1>
            <p><strong>{c.masterclass.title}</strong></p>
            {c.masterclass.paragraphs.map((p) => <p key={p}>{p}</p>)}
          </div>
        </section>
        <section className="bg-seashell" style={{ paddingBottom: "var(--section)" }} aria-label={c.ui.videoTitle}>
          <div className="wrap reveal"><MasterclassVideo c={c} /></div>
        </section>
        <section className="section bg-white" aria-labelledby="mc-volgende">
          <div className="wrap narrow center reveal">
            <Eyebrow step={c.challenge.step} label={c.challenge.eyebrow} />
            <h2 id="mc-volgende">{c.challenge.title}</h2>
            {c.challenge.paragraphs.map((p) => <p key={p}>{p}</p>)}
            <PriceLine c={c} />
            <div className="btn-row">
              <ChallengeLink lang={c.lang} className="btn btn-primary btn-arrow" message={c.ui.noSales}>{c.challenge.button}</ChallengeLink>
            </div>
            <a className="text-link" href={`${c.routes.home}#${c.ids.form}`}>{c.masterclass.noHandbook}</a>
          </div>
        </section>
      </main>
      <Footer c={c} onHome={false} />
    </>
  );
}
