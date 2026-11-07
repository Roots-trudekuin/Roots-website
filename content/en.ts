/* All English texts of the site. Edit texts here. */
import type { Content } from "./nl";

export const en: Content = {
  lang: "en",
  routes: { home: "/en", masterclass: "/en/masterclass", thanks: "/en/thank-you", blog: "/en/blog" },
  other: { label: "NL", name: "Nederlands", home: "/", masterclass: "/masterclass", thanks: "/bedankt", blog: "/blog" },
  ids: { offer: "programmes", start: "start", form: "signup", handbook: "handbook", masterclass: "masterclass", challenge: "challenge", about: "about-trude" },

  meta: {
    homeTitle: "TrudeThecla | ROOTS",
    homeDescription:
      "You know why you keep falling back. So why does it still happen? Start here with Trude Kuin's free handbook.",
    masterclassTitle: "Free masterclass · TrudeThecla | ROOTS",
    masterclassDescription:
      "Free masterclass by Trude Kuin on the connection between your biological survival system and recurring patterns.",
    thanksTitle: "Thank you · TrudeThecla | ROOTS",
  },

  ui: {
    skip: "Skip to content",
    menu: "Menu",
    mainNav: "Main navigation",
    logoLabel: "ROOTS — to Start here",
    noSales:
      "Placeholder: the URL of the English Breakfree Challenge sales page has not been set yet (en.challengeSalesUrl in config/site.ts).",
    invalid: "Please enter your name and a valid email address.",
    noForm:
      "Placeholder: this form is not yet connected to an email marketing service. Nothing has been sent. (Set en.emailMarketing.formAction in config/site.ts.)",
    sending: "Sending your sign-up…",
    videoTitle: "Free masterclass — Trude Kuin",
    videoPlaceholder: "Placeholder masterclass video",
    videoPlaceholderHint: "en.masterclassVideoUrl in config/site.ts",
  },

  nav: {
    programs: "Programmes",
    blog: "Blog",
    start: "Start here",
    handbook: "The handbook",
    masterclass: "Masterclass",
    challenge: "Breakfree Challenge",
    about: "About Trude",
  },

  hero: {
    eyebrow: "ROOTS | Start here",
    title: "Lasting change doesn't have to be a struggle with yourself.",
    p1: "You know your pattern. You understand where it comes from. And yet it comes back.",
    p2: "In the free Pattern Reset Handbook, you discover why it keeps coming back – and where real change begins.",
    card: {
      eyebrow: "Free handbook",
      title: "The Pattern Reset Handbook",
      subtitle: "From insight to lasting change",
      note: "You receive the handbook straight in your inbox.",
    },
  },

  band: {
    line1: "Change in a way your body can follow.",
    line2: "So you can live again from your natural flow.",
  },

  experience: {
    title: "For more than thirty years, my work has revolved around people, health, behaviour and change.",
    stats: [
      { n: "300+", label: "trainings" },
      { n: "500+", label: "coaching journeys" },
      { n: "900+", label: "vitality consultations" },
      { n: "1,200+", label: "career consultations" },
    ],
  },

  offer: {
    eyebrow: "Programmes",
    title: "How to continue",
    intro: "Step by step, at your own pace. Start with the handbook, or choose what suits you.",
    cards: [
      { step: "01 · Discover", title: "The Pattern Reset Handbook", tag: "Free", text: "The handbook helps you understand why old patterns can return, even when you already know a great deal about yourself.", cta: "Send me the free handbook", kind: "form" },
      { step: "02 · Understand", title: "Masterclass: Switch off your pattern at the source", tag: "Free", text: "In the free masterclass, I take you through the connection between your biological survival system and recurring patterns.", cta: "You receive the masterclass after the handbook", kind: "note" },
      { step: "03 · Experience", title: "Breakfree Challenge", tag: "7 days", text: "In the Breakfree Challenge, you work with one recurring pattern of your own.", cta: "More about the Breakfree Challenge", kind: "challenge" },
      { step: "04 · ROOTS", title: "ROOTS online programme", tag: "Coming soon", text: "In 7 steps to a reset.", cta: "Coming soon", kind: "note" },
    ],
  },

  recognition: {
    title: "‘I thought I had sorted this out by now.’",
    paragraphs: [
      "You have worked on yourself. Perhaps for years.",
      "You know where certain reactions come from. You have gained insights and made new choices.",
      "But sometimes you react before you can truly choose.",
    ],
    callout:
      "That raises a different question: what happens at the moment an old pattern is activated again?",
  },

  shift: {
    title: "Insight matters. But insight alone does not automatically change your reaction.",
    paragraphs: [
      "When your system recognises something as a threat, a familiar reaction can already be set in motion before you consciously think about it.",
      "That is why, within ROOTS, we look not only at where your pattern comes from, but also at what activates it in the present.",
    ],
    callout: "That opens up a different way of looking at falling back.",
  },

  handbook: {
    step: "01",
    eyebrow: "Discover",
    title: "Start with the free handbook",
    paragraphs: [
      "The handbook helps you understand why old patterns can return, even when you already know a great deal about yourself.",
      "You are introduced to a different way of looking at your automatic reactions.",
    ],
    cover: "", // English cover not available yet → placeholder
    coverAlt: "Cover of the Pattern Reset Handbook",
    coverPlaceholder: { t1: "Handbook", t2: "Pattern Reset", t3: "From insight to lasting change", label: "Placeholder · English cover" },
    caption: "The Pattern Reset Handbook · free",
    nameLabel: "Name",
    emailLabel: "Email address",
    submit: "Send me the free handbook",
  },

  masterclass: {
    step: "02",
    eyebrow: "Understand",
    title: "You have discovered why insight is not always enough. So what does happen?",
    paragraphs: [
      "In the free masterclass, I take you through the connection between your biological survival system and recurring patterns.",
      "You discover how to look differently at the moments when you react automatically.",
    ],
    button: "Discover the free masterclass",
    landingButton: "Get the handbook and the masterclass",
    pageEyebrow: "Understand · Free masterclass",
    pageTitle: "Switch off your pattern at the source",
    noHandbook: "Don't have the free handbook yet? Download it here",
  },

  challenge: {
    step: "03",
    eyebrow: "Experience",
    title: "Ready to work with your own pattern?",
    paragraphs: [
      "Understanding how your system works is one step. Exploring it in yourself and working with it is the next.",
      "In the Breakfree Challenge, you work with one recurring pattern of your own.",
    ],
    factsLabel: "The Breakfree Challenge at a glance",
    facts: [
      { big: "7 days", small: "starting together online" },
      { big: "1 pattern", small: "of your own" },
      { big: "± 1 hour", small: "a day: video and assignment" },
      { big: "3 months", small: "access to all videos" },
    ],
    button: "Discover the Breakfree Challenge",
  },

  about: {
    title: "I'm Trude.",
    paragraphs: [
      "For more than thirty years, my work has revolved around people, health, behaviour and change.",
      "Drawing on my background in health sciences, vocational guidance and hypnotherapy, I developed ROOTS: a method for exploring how automatic patterns form, are activated and can be changed.",
    ],
    portrait: "/img/portret-trude.jpg",
    portraitAlt: "Portrait of Trude Kuin",
    signature: "Trude Kuin · ROOTS",
  },

  closing: {
    title: "You don't need to start understanding yourself all over again.",
    p1: "Perhaps the next step begins with a different question.",
    notOnlyLead: "Not only:",
    notOnly: "why do I do this?",
    butAlsoLead: "But also:",
    butAlso: "what sets it off, at the very moment it happens?",
    primary: "Start here — download the free handbook",
    link: "I want to go straight to the Breakfree Challenge",
  },

  thanks: {
    title: "Thank you. The handbook is on its way to your inbox.",
    p: "Nothing there within a few minutes? Please check your spam or promotions folder too.",
    nextEyebrow: "Your next step · Understand",
  },

  blog: {
    title: "Blog",
    text: "Articles about patterns, change and the ROOTS method will appear here soon.",
    metaTitle: "Blog · TrudeThecla | ROOTS",
  },

  footer: {
    copyright: "© TrudeThecla",
    otherLanguage: "Nederlands",
  },
};
