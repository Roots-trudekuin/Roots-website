/* Alle Nederlandse teksten van de site. Wijzig teksten hier. */

export const nl = {
  lang: "nl" as "nl" | "en",
  routes: { home: "/", masterclass: "/masterclass", thanks: "/bedankt" },
  other: { label: "EN", name: "English", home: "/en", masterclass: "/en/masterclass", thanks: "/en/thank-you" },
  ids: { start: "start", form: "aanmelden", handbook: "handboek", masterclass: "masterclass", challenge: "challenge", about: "over-trude" },

  meta: {
    homeTitle: "TrudeThecla | ROOTS",
    homeDescription:
      "Je weet waarom je steeds terugvalt. Maar waarom gebeurt het dan toch? Start hier met het gratis Handboek Patroon-Reset van Trude Kuin.",
    masterclassTitle: "Gratis masterclass · TrudeThecla | ROOTS",
    masterclassDescription:
      "Gratis masterclass van Trude Kuin over de samenhang tussen je biologische overlevingssysteem en terugkerende patronen.",
    thanksTitle: "Dank je wel · TrudeThecla | ROOTS",
  },

  ui: {
    skip: "Naar de inhoud",
    menu: "Menu",
    mainNav: "Hoofdnavigatie",
    logoLabel: "ROOTS — naar Start hier",
    noSales:
      "Placeholder: de URL van de Breakfree Challenge-salespagina is nog niet ingesteld (challengeSalesUrl in config/site.ts).",
    invalid: "Vul je naam en een geldig e-mailadres in.",
    noForm:
      "Placeholder: het formulier is nog niet gekoppeld aan een e-mailmarketingdienst. Er is niets verzonden. (Stel emailMarketing.formAction in, in config/site.ts.)",
    sending: "Je aanmelding wordt verstuurd…",
    videoTitle: "Gratis masterclass — Trude Kuin",
    videoPlaceholder: "Placeholder masterclassvideo",
    videoPlaceholderHint: "masterclassVideoUrl in config/site.ts",
  },

  nav: {
    cta: "Gratis handboek",
    start: "Start hier",
    handbook: "Het handboek",
    masterclass: "Masterclass",
    challenge: "Breakfree Challenge",
    about: "Over Trude",
  },

  hero: {
    eyebrow: "ROOTS | Start hier",
    titleBefore: "Blijvende verandering hoeft ",
    titleHighlight: "geen strijd",
    titleAfter: " met jezelf te zijn.",
    intro:
      "Met de ROOTS-methode ontkoppel je patronen bij de bron – gegrond in je biologie – zodat je weer kunt bewegen vanuit wie jij werkelijk bent.",
    bullets: [
      "Patronen los bij de bron, niet alleen de symptomen",
      "Gegrond in biologie, lichaam en zenuwstelsel",
      "Zacht, natuurlijk en in jouw tempo",
      "Resultaat dat blijft, zonder dat het al je kracht kost",
    ],
    primary: "Start hier — download het gratis handboek",
    challengeLink: "Ik wil direct de Breakfree Challenge ontdekken",
    card: {
      eyebrow: "Gratis handboek",
      title: "Handboek Patroon-Reset",
      subtitle: "Van inzicht naar blijvende verandering",
      button: "Stuur mij het gratis handboek",
      note: "Je gegevens zijn veilig. Geen spam, ooit.",
    },
  },

  band: {
    line1: "Veranderen op een manier die je lichaam kan volgen.",
    line2: "Zodat je weer kunt leven vanuit jouw natuurlijke stroom.",
  },

  recognition: {
    title: "‘Ik dacht dat ik dit inmiddels had opgelost.’",
    paragraphs: [
      "Je hebt aan jezelf gewerkt. Misschien jarenlang.",
      "Je weet waar bepaalde reacties vandaan komen. Je hebt inzichten opgedaan en nieuwe keuzes gemaakt.",
      "Maar soms reageer je voordat je werkelijk kunt kiezen.",
    ],
    callout:
      "Dat roept een andere vraag op: wat gebeurt er op het moment dat zo'n oud patroon opnieuw wordt geactiveerd?",
  },

  shift: {
    title: "Inzicht is belangrijk. Maar inzicht alleen verandert niet automatisch je reactie.",
    paragraphs: [
      "Wanneer je systeem iets als dreiging herkent, kan een vertrouwde reactie al worden ingezet voordat je er bewust over nadenkt.",
      "Daarom kijken we binnen ROOTS niet alleen naar de oorsprong van je patroon, maar ook naar wat het in het heden activeert.",
    ],
    callout: "Dat opent een andere manier van kijken naar terugval.",
  },

  handbook: {
    step: "01",
    eyebrow: "Ontdek",
    title: "Begin met het gratis handboek",
    paragraphs: [
      "Het handboek helpt je begrijpen waarom oude patronen kunnen terugkomen, ook als je al veel over jezelf weet.",
      "Je maakt kennis met een andere manier om naar je automatische reacties te kijken.",
    ],
    /** pad naar omslag in /public, of "" voor placeholder */
    cover: "/img/omslag-handboek.jpg",
    coverAlt: "Omslag van het Handboek Patroon-Reset — Van inzicht naar blijvende verandering",
    coverPlaceholder: { t1: "Handboek", t2: "Patroon-Reset", t3: "Van inzicht naar blijvende verandering", label: "Placeholder · omslag" },
    caption: "Handboek Patroon-Reset · gratis",
    nameLabel: "Naam",
    emailLabel: "E-mailadres",
    submit: "Stuur mij het gratis handboek",
  },

  masterclass: {
    step: "02",
    eyebrow: "Begrijp",
    title: "Je hebt ontdekt waarom inzicht niet altijd voldoende is. Wat gebeurt er dan wél?",
    paragraphs: [
      "In de gratis masterclass neem ik je mee in de samenhang tussen je biologische overlevingssysteem en terugkerende patronen.",
      "Je ontdekt hoe je anders kunt kijken naar de momenten waarop je automatisch reageert.",
    ],
    button: "Ontdek de gratis masterclass",
    /** knop in sectie 5 op de startpagina: gaat naar het handboekformulier */
    landingButton: "Ontvang het handboek en de masterclass",
    pageEyebrow: "Begrijp · Gratis masterclass",
    pageTitle: "Zet je patroon uit bij de bron",
    noHandbook: "Heb je het gratis handboek nog niet? Download het hier",
  },

  challenge: {
    step: "03",
    eyebrow: "Ervaar",
    title: "Wil je met je eigen patroon aan de slag?",
    paragraphs: [
      "Begrijpen hoe je systeem werkt is één stap. Het bij jezelf onderzoeken en ermee werken is een volgende.",
      "In de Breakfree Challenge ga je aan de slag met één terugkerend patroon van jezelf.",
    ],
    factsLabel: "De Breakfree Challenge in het kort",
    /* Uit de definitieve salespagina Breakfree Challenge */
    facts: [
      { big: "7 dagen", small: "samen online van start" },
      { big: "1 patroon", small: "van jezelf" },
      { big: "± 1 uur", small: "per dag: video en opdracht" },
      { big: "3 maanden", small: "toegang tot alle video's" },
    ],
    button: "Ontdek de Breakfree Challenge",
  },

  about: {
    title: "Ik ben Trude.",
    paragraphs: [
      "Mijn werk draait al meer dan dertig jaar om mensen, gezondheid, gedrag en verandering.",
      "Vanuit mijn achtergrond in gezondheidskunde, arbeidsbegeleiding en hypnotherapie ontwikkelde ik ROOTS: een methode waarmee we onderzoeken hoe automatische patronen ontstaan, geactiveerd worden en veranderd kunnen worden.",
    ],
    portrait: "/img/portret-trude.jpg",
    portraitAlt: "Portret van Trude Kuin",
    signature: "Trude Kuin · ROOTS",
  },

  closing: {
    title: "Je hoeft niet opnieuw te beginnen met jezelf begrijpen.",
    p1: "Misschien begint de volgende stap met een andere vraag.",
    notOnlyLead: "Niet alleen:",
    notOnly: "waarom doe ik dit?",
    butAlsoLead: "Maar ook:",
    butAlso: "wat zet het aan, precies op het moment dat het gebeurt?",
    primary: "Start hier — download het gratis handboek",
    link: "Ik wil direct de Breakfree Challenge ontdekken",
  },

  thanks: {
    title: "Dank je wel. Het handboek is onderweg naar je inbox.",
    p: "Zie je niets binnen een paar minuten? Kijk dan ook in je spam- of reclamemap.",
    nextEyebrow: "Je volgende stap · Begrijp",
  },

  footer: {
    copyright: "© TrudeThecla",
    otherLanguage: "English",
  },
};

export type Content = typeof nl;
