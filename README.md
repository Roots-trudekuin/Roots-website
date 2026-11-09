# TrudeThecla | ROOTS — website

Statische website (HTML en CSS) voor trudethecla.nl, met ROOTS als methode en de Trigger Breakfree Challenge als hoofdproduct. Vercel serveert de map `public/`; er is geen build-stap op Vercel.

De migratie naar React en Tailwind volgt later (migratieplan met Nigel).

## Pagina's

| Adres | Pagina |
|---|---|
| `/` | Homepage (Start hier) met de opt-in voor het gratis Handboek Patroon-Reset (`/#handboek`) |
| `/challenge` | Salespagina Trigger Breakfree Challenge |
| `/inzicht` | Inzicht: Artikelen en Video's |
| `/over-trude` | Over Trude |
| `/contact` | Contact |
| `/bedankt` | Na aanmelding handboek (niet in Google) |
| `/welkom` | Na aankoop Challenge (niet in Google) |
| `/masterclass-zet-je-patroon-uit` | Masterclass, alleen via de link in het handboek (verschijnt zodra de video-URL is ingevuld) |
| `/en` | Engelse homepage |

## Aanpassen

- **`bron/config.json`**: betaallink, prijs, startdatum, formulierkoppelingen, Instagram, community, privacy- en voorwaardenlinks, masterclassvideo. Een leeg veld betekent dat het onderdeel niet op de site staat.
- **`bron/gen_*.py`**: de teksten en opbouw van de pagina's.
- **`bron/assets/`**: foto's, logo-icoon en lettertypen (Montserrat en Cinzel, zelf gehost).

Daarna opnieuw bouwen:

```
python3 bron/build.py
```

Dat vult `public/` opnieuw. Commit `public/` mee.

## Nog niet gekoppeld

- Handboekformulier: zolang `handboek_formulier_action` leeg is, gaat het formulier alleen naar `/bedankt` en wordt er niets verstuurd.
- Koopknoppen Challenge: verschijnen pas als `challenge_betaallink` (Plug&Pay) is ingevuld; voor de Engelse pagina's `challenge_betaallink_en`.
- Contactformulier: verschijnt pas als `contact_formulier_action` of `contact_email` is ingevuld.
