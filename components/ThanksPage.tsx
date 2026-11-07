import type { Content } from "@/content/nl";
import Header from "./Header";
import Footer from "./Footer";
import { Eyebrow } from "./Bits";

export default function ThanksPage({ c }: { c: Content }) {
  return (
    <>
      <a className="skip-link" href="#inhoud">{c.ui.skip}</a>
      <Header c={c} page="thanks" />
      <main id="inhoud">
        <section className="page-intro bg-seashell" aria-labelledby="bd-titel">
          <div className="wrap narrow center reveal">
            <div className="check" aria-hidden="true">✓</div>
            <h1 id="bd-titel">{c.thanks.title}</h1>
            <p>{c.thanks.p}</p>
          </div>
        </section>
        <section className="section bg-seashell" style={{ paddingTop: 0 }} aria-labelledby="bd-volgende">
          <div className="wrap">
            <div className="panel reveal">
              <div className="narrow">
                <Eyebrow step={c.masterclass.step} label={c.thanks.nextEyebrow} />
                <h2 id="bd-volgende">{c.masterclass.title}</h2>
                {c.masterclass.paragraphs.map((p) => <p key={p}>{p}</p>)}
                <div className="btn-row">
                  <a className="btn btn-primary btn-arrow" href={c.routes.masterclass}>{c.masterclass.button}</a>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <Footer c={c} onHome={false} />
    </>
  );
}
