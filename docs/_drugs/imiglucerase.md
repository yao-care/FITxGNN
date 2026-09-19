---
layout: default
title: Imiglucerase
parent: Kohtalainen näyttö (L3-L4)
nav_order: 192
evidence_level: L4
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **5** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Imiglucerase: Gaucherin taudista Hurlerin oireyhtymään

## Yhden lauseen yhteenveto

Imiglucerase on rekombinantti glukoserebrosidasientsyymiaineenvaihtohoidon valmiste, jota on historiallisesti käytetty Gaucherin taudin hoitoon.
TxGNN-malli ennustaa sen saattavan olla tehokas **Hurlerin oireyhtymään**,
mutta tämä suunta on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja vain **2 yleisellä (ei tautikohtaisella) katsauksella**, ja taustalla oleva mekanistinen perustelu näyttää heikolta.

## Pikayleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Gaucherin tauti (kirjallisuusnäytön perusteella tässä paketissa; strukturoitua sääntelyllä hyväksytyn indikaation tekstiä ei ole saatavilla) |
| Ennustettu uusi indikaatio | Hurlerin oireyhtymä |
| TxGNN-ennustepistemäärä | 99.52% |
| Näyttötaso | L4 |
| Suomen markkinatilanne | Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla (DG002, tietoaukko). Tässä näyttöpaketissa olevan tiedon perusteella imiglucerase on rekombinantti muoto glukoserebrosidasientsyymistä (hapan β-glukosidaasi), jota käytetään entsyymiaineenvaihtohoidossa (ERT) glukoserebrosidin kertymän hajottamiseen Gaucherin taudissa.

Hurlerin oireyhtymä on kuitenkin mukopolysakkariidoosi tyypi I (MPS I), joka aiheutuu α-L-iduronidaasin (IDUA) puutteesta, täysin eroavasta lysosomaalista entsyymistä, joka vaikuttaa eri substraattiluokkaan (heparaani/dermataanisulfaatti, ei glukoserebroisidi). Hurlerin oireyhtymän vakioentsyymiaineenvaihtohoidon valmiste on laronidaasi (rekombinantti IDUA), ei imiglucerase.

Tämän perusteella imiglucerasin ja Hurlerin oireyhtymän välinen mekanistinen yhteys on heikko tai olematon. Korkea TxGNN-pistemäärä todennäköisesti heijastavat sitä, että malli yleistää laajemmin "lysosomaalinen varastointisairaus + entsyymiaineenvaihtohoidot" -kategoriaa sen sijaan, että se kuvaisi substraattikohtaista farmakologista suhdetta. Tämä arvio on johdonmukainen mallin muiden huippuennusteiden kanssa tässä näyttöpaketissa (Scheien oireyhtymä, kolesteryyliesterien varastointisairaus), joista näkyy sama kaava — eri aiheuttavat entsyymit/substraatit, ei tautikohtaista näyttöä ja "Pidätä"-suositus.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei liittyviä kliinisiä tutkimuksia rekisteröity

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Pääasialliset havainnot |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Katsaus | Proceedings of the National Academy of Sciences of the United States of America | Kuvailee entsyymiaineenvaihtohoitoa PET-kuvauksella; huomioi, että ERT (mukaan lukien imiglucerase-luokkaisten rekombinanttien lysosomaalisten entsyymien) on osoittautunut tehokkaaksi Gaucherin, Fabryn, Hurlerin, Hunterin, Maroteaux-Lamyn ja Pompen taudeissa, mutta ei esitä imiglucerase-kohtaista tietoa Hurlerin oireyhtymästä |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Katsaus | La Revue de medecine interne | Yleiskatsaus entsyymiaineenvaihtohoidosta lysosomaalisten varastointisairauksien osalta; kuvaa imiglucerasin (Cerezyme) historiallista kehitystä Gaucherin taudissa ja muita tautikohtaisia ERT-hoitoja (esim. agalsidaasi Fabryn taudissa); ei käsittele Hurlerin oireyhtymää erikseen |

## Suomen markkinatiedot

Imiglucerasella ei ole tällä hetkellä rekisteröityä myyntilupaa Suomessa (markkinatilanne: Ei markkinoitu; 0 hyväksyntää).

## Turvallisuusnäkökohdat

Turvallisuustietoja varten katso pakkausseloste.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelu:**
Ennustetulla Hurlerin oireyhtymän indikaatiolla ei ole minkäänlaista tautikohtaista kliinistä tai kirjallisuusnäyttöä, ja ehdotettu mekanismi ei kestä tarkastelua — imiglucerase kohdistuu glukoserebrosidasin puutteeseen (Gaucherin taudin reitti), kun taas Hurlerin oireyhtymä aiheutuu eri entsyymin puutteesta (IDUA), jolla on vakiintunut, erilainen hoitostandardi (laronidaasi). Näyttötaso on L4 (vain mekanismi/malli-tasolla), eikä lääkettä ole tällä hetkellä markkinoitu Suomessa.

**Jatkamisen kannalta seuraavat tiedot ovat tarpeen:**
- TFDA/viralliset pakkausseloste-tiedot varoituksista ja vasta-aiheista (DG001, esto — estää tällä hetkellä pääsyn S1 turvallisuuskatsaukseen)
- Vahvistetut vaikutusmekanismin tiedot (DG002)
- Tautikohtainen esikliininen tai kliininen näyttö, joka yhdistää glukoserebrosidasin reitin suoraan MPS I -patofysiologiaan, jos tätä kandidaattia halutaan harkita uudelleen
- Huomio: kaikki 5 TxGNN-ennustettua indikaatiota tässä näyttöpaketissa (Hurlerin oireyhtymä, Scheien oireyhtymä, lisämunuaisen adenooma, kuolettava iktyoosi-oireyhtymä, kolesteryyliesterien varastointisairaus) on tällä hetkellä luokiteltu Pidätä-kategoriaan samanlaisten mekanististen ristiriitaisuuksien tai tukevan näytön puutteen vuoksi.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

