import type { Content } from "@/content/nl";
import Header from "./Header";
import Footer from "./Footer";

export default function BlogPage({ c }: { c: Content }) {
  return (
    <>
      <a className="skip-link" href="#inhoud">{c.ui.skip}</a>
      <Header c={c} page="blog" />
      <main id="inhoud">
        <section className="page-intro bg-seashell" aria-labelledby="blog-titel">
          <div className="wrap narrow center reveal">
            <h1 id="blog-titel">{c.blog.title}</h1>
            <p>{c.blog.text}</p>
            <div className="btn-row">
              <a className="btn btn-primary" href={`${c.routes.home}#${c.ids.form}`}>{c.offer.cards[0].cta}</a>
            </div>
          </div>
        </section>
      </main>
      <Footer c={c} onHome={false} />
    </>
  );
}
