"use client";
import type { ReactNode } from "react";
import { siteConfig } from "@/config/site";
import { showNotice } from "./Notice";

/** Alle Challenge-knoppen gebruiken één centrale URL uit config/site.ts. */
export default function ChallengeLink({
  lang, className, children, message,
}: { lang: "nl" | "en"; className?: string; children: ReactNode; message: string }) {
  const url = siteConfig[lang].challengeSalesUrl;
  if (url) return <a className={className} href={url}>{children}</a>;
  return (
    <a
      className={className}
      href="#"
      data-placeholder="true"
      onClick={(e) => { e.preventDefault(); showNotice(message); }}
    >
      {children}
    </a>
  );
}
