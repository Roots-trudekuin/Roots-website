# TrudeThecla | ROOTS — website

Website van TrudeThecla (trudethecla.nl), met ROOTS als methode: tweetalig (NL/EN), gebouwd met Next.js en klaar om op Vercel te zetten.

## Pagina's

| NL | EN |
|---|---|
| `/` landingspagina Start hier | `/en` |
| `/masterclass` | `/en/masterclass` |
| `/bedankt` (na aanmelding handboek) | `/en/thank-you` |

## Waar staat wat

- **`config/site.ts`**: alle links en koppelingen, per taal:
  - `challengeSalesUrl`: één URL voor alle Breakfree Challenge-knoppen
  - `challengePrijsRegel`: prijsregel (leeg = niet tonen)
  - `masterclassVideoUrl`: embed-URL van de masterclassvideo
  - `emailMarketing`: koppeling van het handboekformulier (action-URL, veldnamen, verborgen velden)
- **`content/nl.ts`** en **`content/en.ts`**: alle teksten.
- **`app/globals.css`**: vormgeving (Seashell #FAF1E8, Camel #BD9D60, Jet #333333, Oudroze #BEA8A7, Montserrat).
- **`public/img/`**: omslag handboek en portret.
- **`components/Logo.tsx`**: logo-placeholder. Vervangen door het echte logo.

Lege waarden zijn placeholders: de site meldt dan dat de koppeling ontbreekt en verstuurt niets.

## Formulier

Het handboekformulier doet een gewone formulierpost naar de e-maildienst (MailerLite, ActiveCampaign, Brevo, Kit, …). Instellen in die dienst:
1. automatische e-mail met het handboek;
2. na aanmelden doorsturen naar `https://trudethecla.nl/bedankt` (EN: `https://trudethecla.nl/en/thank-you`).

Liever via de API van de dienst? Voeg een route handler toe (`app/api/subscribe/route.ts`) en laat `HandbookForm.tsx` daarheen posten.

## Lokaal draaien

```bash
npm install
npm run dev     # http://localhost:3000
```

## Online zetten (Vercel)

1. Zet deze map in een GitHub-repository.
2. Ga naar vercel.com → **Add New → Project** → kies de repository → **Deploy**. Instellingen kunnen standaard blijven.
3. Koppel het domein via **Settings → Domains**.

Elke push naar GitHub zet daarna automatisch een nieuwe versie online.
