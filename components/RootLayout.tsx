import type { ReactNode } from "react";
import Notice from "./Notice";
import RevealObserver from "./RevealObserver";

export default function RootLayout({ lang, children }: { lang: "nl" | "en"; children: ReactNode }) {
  return (
    <html lang={lang}>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        {/* eslint-disable-next-line @next/next/no-page-custom-font */}
        <link
          href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        {children}
        <Notice />
        <RevealObserver />
      </body>
    </html>
  );
}
