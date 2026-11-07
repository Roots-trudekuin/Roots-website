import type { Content } from "@/content/nl";
import Logo from "./Logo";

export default function Footer({ c, onHome }: { c: Content; onHome: boolean }) {
  const base = onHome ? "" : c.routes.home;
  return (
    <footer className="site-footer">
      <div className="wrap">
        <div className="footer-grid">
          <Logo />
          <ul className="footer-links">
            <li><a href={`${base}#${c.ids.form}`}>{c.nav.start}</a></li>
            <li><a href={`${base}#${c.ids.offer}`}>{c.nav.programs}</a></li>
            <li><a href={c.routes.blog}>{c.nav.blog}</a></li>
            <li><a href={`${base}#${c.ids.about}`}>{c.nav.about}</a></li>
            <li><a href={c.other.home} lang={c.lang === "nl" ? "en" : "nl"}>{c.footer.otherLanguage}</a></li>
          </ul>
        </div>
        <div className="footer-bottom">{c.footer.copyright}</div>
      </div>
    </footer>
  );
}
