"use client";
import { useEffect, useState } from "react";
import type { Content } from "@/content/nl";
import Logo from "./Logo";

type Page = "home" | "masterclass" | "thanks" | "blog";

export default function Header({ c, page }: { c: Content; page: Page }) {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("keydown", onKey);
    return () => { window.removeEventListener("scroll", onScroll); document.removeEventListener("keydown", onKey); };
  }, []);

  const base = page === "home" ? "" : c.routes.home;
  const a = (id: string) => `${base}#${id}`;
  const otherHref = page === "home" ? c.other.home : page === "masterclass" ? c.other.masterclass : page === "blog" ? c.other.blog : c.other.thanks;
  const menuId = "hoofdmenu";

  const items = [
    { href: a(c.ids.form), label: c.nav.start },
    { href: a(c.ids.offer), label: c.nav.programs },
    { href: c.routes.blog, label: c.nav.blog },
    { href: a(c.ids.about), label: c.nav.about },
  ];

  return (
    <header className={"site-header" + (scrolled ? " is-scrolled" : "")}>
      <div className="wrap nav">
        <a className="logo" href={page === "home" ? `#${c.ids.start}` : c.routes.home} aria-label={c.ui.logoLabel}>
          <Logo />
        </a>
        <button
          className="nav-toggle" type="button" aria-expanded={open} aria-controls={menuId} aria-label={c.ui.menu}
          onClick={() => setOpen((o) => !o)}
        >
          <span className="bars"><span /></span>
        </button>
        <nav aria-label={c.ui.mainNav}>
          <ul className={"nav-menu" + (open ? " is-open" : "")} id={menuId} onClick={(e) => (e.target as HTMLElement).closest("a") && setOpen(false)}>
            {items.map((it) => (
              <li key={it.label}>
                <a href={it.href}>{it.label}</a>
              </li>
            ))}
            <li className="lang-switch">
              {c.lang === "nl" ? (
                <>
                  <a href="#" aria-current="true" lang="nl" aria-label="Nederlands" onClick={(e) => e.preventDefault()}>NL</a>
                  <span aria-hidden="true">/</span>
                  <a href={otherHref} lang="en" hrefLang="en" aria-label="English">EN</a>
                </>
              ) : (
                <>
                  <a href={otherHref} lang="nl" hrefLang="nl" aria-label="Nederlands">NL</a>
                  <span aria-hidden="true">/</span>
                  <a href="#" aria-current="true" lang="en" aria-label="English" onClick={(e) => e.preventDefault()}>EN</a>
                </>
              )}
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}
