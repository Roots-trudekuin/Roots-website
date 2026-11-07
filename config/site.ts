/* =====================================================================
   ROOTS | Start hier — CENTRALE INSTELLINGEN
   Vul hier links en koppelingen in. Lege waarde ("") = placeholder:
   de site toont dan duidelijk dat de koppeling ontbreekt en simuleert niets.
   ===================================================================== */

export type EmailMarketing = {
  provider: string;      // alleen ter info, bijv. "MailerLite"
  formAction: string;    // 'action'-URL uit het embedformulier van de e-maildienst
  method: "POST" | "GET";
  nameField: string;     // veldnaam voor naam bij de e-maildienst
  emailField: string;    // veldnaam voor e-mailadres
  hiddenFields: Record<string, string>; // bijv. lijst-ID of tag
};

export type LangConfig = {
  /** Salespagina Breakfree Challenge — gebruikt door ALLE Challenge-knoppen */
  challengeSalesUrl: string;
  /** Prijsregel bij de Challenge (leeg = niet tonen) */
  challengePrijsRegel: string;
  /** Embed-URL masterclassvideo (YouTube/Vimeo embed) */
  masterclassVideoUrl: string;
  /** Koppeling handboekformulier. In de e-maildienst instellen:
   *  - automatische mail met het handboek
   *  - doorsturen na aanmelden naar https://trudethecla.nl/bedankt (NL) of https://trudethecla.nl/en/thank-you (EN) */
  emailMarketing: EmailMarketing;
};

export const siteConfig: { nl: LangConfig; en: LangConfig } = {
  nl: {
    challengeSalesUrl: "",
    challengePrijsRegel: "Introductieprijs €49, daarna €79.",
    masterclassVideoUrl: "",
    emailMarketing: {
      provider: "",
      formAction: "",
      method: "POST",
      nameField: "name",
      emailField: "email",
      hiddenFields: {},
    },
  },
  en: {
    challengeSalesUrl: "",
    challengePrijsRegel: "Introductory price €49, then €79.",
    masterclassVideoUrl: "",
    emailMarketing: {
      provider: "",
      formAction: "",
      method: "POST",
      nameField: "name",
      emailField: "email",
      hiddenFields: {},
    },
  },
};
