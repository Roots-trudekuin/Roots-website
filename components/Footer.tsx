import type { Content } from "@/content/nl";
import Logo from "./Logo";
import ChallengeLink from "./ChallengeLink";

export default function Footer({ c, onHome }: { c: Content; onHome: boolean }) {
  const base = onHome ? "" : c.routes.home;
  return (
    <footer className="site-footer">
      <div className="wrap">
        <div className="footer-grid">
          <Logo />
          <ul className="footer-links">
            <li><a href={`${base}#${c.ids.handbook}`}>{c.nav.handbook}</a></li>
            <li><ChallengeLink lang={c.lang} message={c.ui.noSales}>{c.nav.challenge}</ChallengeLink></li>
            <li><a href={`${base}#${c.ids.about}`}>{c.nav.about}</a></li>
            <li><a href={c.other.home} lang={c.lang === "nl" ? "en" : "nl"}>{c.footer.otherLanguage}</a></li>
          </ul>
        </div>
        <div className="footer-bottom">{c.footer.copyright}</div>
      </div>
    </footer>
  );
}
