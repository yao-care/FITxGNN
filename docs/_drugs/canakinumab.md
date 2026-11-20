---
layout: default
title: Canakinumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 96
evidence_level: L5
indication_count: 9
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
last_modified_at: 2026-11-20
description: "Canakinumab: ennustettu uusi käyttöaihe Maksainfarkti (hepatic infarction) (näytön taso L5). Alkuperäinen käyttöaihe: Cryopyrin-Associated Periodic Syndromes"
---

# Canakinumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

## Kanakinumabi: IL-1β-vasta-aine → maksainfarkti (hepatic infarction)
{: .text-alpha }

## Yhden lauseen yhteenveto

Kanakinumabi on interleukiini-1β:ta (IL-1β) estävä monoklonaalinen vasta-aine, jota käytetään autoinflammatoristen sairauksien hoidossa. TxGNN-malli ennustaa sen mahdolliseksi hoidoksi sairauteen **maksainfarkti (hepatic infarction)**. Tälle ennusteelle ei ole kliinisiä tutkimuksia eikä julkaisuja, joten ennuste perustuu pelkästään mallin laskentaan.

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Cryopyrin-Associated Periodic Syndromes;Arthritis, Juvenile Rheumatoid;Arthritis, Gouty |
| Ennustettu uusi käyttöaihe | Maksainfarkti (hepatic infarction) |
| TxGNN-ennustepisteet | 0,9986 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Canakinumab (epävirallinen käännös): ”Kanakinumabi on IgG1/κ-isotyypin ihmisen monoklonaalinen vasta-aine ihmisen IL-1β:aa vastaan. Kanakinumabi sitoutuu ihmisen IL-1β:aan ja neutraloi sen aktiivisuuden estämällä sen vuorovaikutuksen IL-1-reseptorien kanssa, mutta se ei sitoudu IL-1α:aan eikä IL-1-reseptorin antagonistiin (IL-1ra).” Englanninkielinen alkuteksti: "Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)." ([DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e), versio 2026-06-08; haettu 2026-11-19). Tiedossa on, että kanakinumabi neutraloi IL-1β:ta ja sitä käytetään IL-1β:n liikatuotantoon liittyvissä autoinflammatorisissa sairauksissa.

Teoriassa IL-1β:n esto voisi vaimentaa iskemiaan liittyvää steriiliä tulehdusta, jota maksainfarktissa voi esiintyä. Tämä on kuitenkin pelkkä hypoteesi: yhteen ei ole toimitettu tukevaa kliinistä tai prekliinistä aineistoa, eikä alkuperäisen käyttöaiheen ja ennustetun sairauden samankaltaisuutta ole arvioitu.

Koska maksainfarkti on pääosin verisuoni- ja iskemiaperäinen tila, ennustetta tulee pitää tutkimushypoteesina, ei hoitosuosituksena.

## Kliininen tutkimusnäyttö

Tällä hetkellä aiheeseen ei ole rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä aiheeseen ei ole saatavilla kirjallisuutta.

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/001109 | Ilaris | – | Cryopyrin-assosioituneet jaksottaiset oireyhtymät; nuorten reumatoidi artriitti; kihtiartriitti |

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Haetuista tiedoista löytyi 100 yhteisvaikutusta. Merkittävimpiä ovat kohtalaisen tason yhteisvaikutukset kortikosteroidien (hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisoloni, prednisoni), simvastatiinin, antikoagulanttien (apiksabaani, rivaroksabaani, varfariini, dikumaroli) sekä tiettyjen radioaktiivisten lääkevalmisteiden (ibritumomabi tiuksetaani, jobenguaani I-131, tositumomabi) kanssa. Sinkkivalmisteiden kanssa yhteisvaikutus on lievä.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain TxGNN-mallin pisteytykseen (0,9986) ilman kliinisiä tutkimuksia tai julkaisuja, joten näytön taso on L5.

**Etenemiseksi tarvitaan:**
- Tarkempi vaikutusmekanismitieto ja mekanistinen perustelu IL-1β:n roolista maksan iskemiassa
- Prekliininen tai tapaustason näyttö kanakinumabin vaikutuksesta maksainfarktiin
- Valmisteyhteenvedon varoitus- ja vasta-aihetietojen kerääminen turvallisuusarviota varten
- Selvitys antotien ja potilasryhmän soveltuvuudesta

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera); mallin ennusteita, näytön tasoja ja johtopäätöksiä ei kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

