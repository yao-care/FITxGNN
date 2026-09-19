---
layout: default
title: Daptomycin
parent: Kohtalainen näyttö (L3-L4)
nav_order: 109
evidence_level: L4
indication_count: 10
---

# Daptomycin
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **10** kpl
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

# Daptomysiini: gram-positiivisista bakteeri-infektioista nivelrikkoihin

## Yhden lauseen yhteenveto

> Daptomysiini on syklinen lipopeptidiä antibioottiä, jota käytetään alun perin vakavien gram-positiivisten bakteeri-infektioiden hoitoon (monimutkainen ihon/ihonalaisen kudoksen infektiot, *S. aureus* -bakteeremia, oikean puoleinen endokardiitti).
> TxGNN-malli ennustaa, että se saattaa olla tehokas **nivelrikkoihin**, ja tällä signaalilla on tällä hetkellä liitetty **0 kliinistä tutkimusta** ja **10 julkaisua** — kuitenkin tarkempi tarkastelu osoittaa, että kirjallisuus käsittelee itse asiassa *tekonivelten/nivelten infektioiden* hoitoa potilaissa, joilla sattuu olemaan nivel­rikat­ta, ei itse nivelrikoilla potilaan hoitoa. Tämä näyttää olevan avainsana-häiriöartefakti eikä aito uudelleenkäytön signaali.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Gram-positiiviset bakteeri-infektiot (monimutkainen ihon/ihonalaisen kudoksen infektio, *S. aureus* -bakteeremia, oikean puoleinen endokardiitti) — Suomen markkina-spesifinen pakkausseloste ei ole saatavilla (lääketta ei jaeta siellä) |
| Ennustettu uusi indikaatio | Nivelrikko |
| TxGNN-ennusteen pistemäärä | 99,86% |
| Näytön taso | L4 |
| Markkina-asema Suomessa | ✗ Ei ole markkinoilla |
| Myyntilupien määrä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla tässä näyttöpaketissa (`original_moa: [Data Gap]`). Yleisesti tunnetun farmakologian perusteella (ja johdonmukaisesti kirjallisuudesta löydetyistä lausunnoista tässä paketissa, esim. PMID 39571268), daptomysiini on kalsiums­iippuvainen syklinen lipopeptidi, joka häiritsee gram-positiivisten bakteerien solukalvoa, aiheuttaen nopeaa depolarisaatiota ja solun kuolemaa. Sillä ei tiedetä olevan spesifistä mekaanista yhteyttä degeneratiiviseen niveisairauteen.

Korkea TxGNN-pistemäärä nivelrikoille **ei näy heijastavan** aidon farmakologisen suhteen olemassaoloa. Kaikissa kymmenen haetusta julkaisusta kuvataan daptomysiinin käyttöä **tekonivelinfektioiden (PJI)** tai muiden **nivelten infektioiden** hoitoon — vakavat komplikaatiot, jotka voivat esiintyä *leikkayksen jälkeen*, ja joiden johdosta potilaat usein käyvät leikkauksessa, *koska heillä on* nivelrikko. Toisin sanoen, kirjallisuuden rinnakkaisesiintyminen johtuu jaetusta sanastosta ("nivel", "nivelten", potilaat, joilla on OA-historia) eikä mistään todisteesta, että daptomysiini hoitaa nivelrikkoa itseään. Mikään tutkimuksista ei testaa daptomysiinia taudin muokkaavaksi tai oireenhilintähoitona nivelrikolle.

Kontekstiksi mallin toiseksi sijoittuva ennuste — **reumatoidi artriitti** (pistemäärä 99,84%, ranking 2176) — on tuettu mekaanisesti suoremmin, vaikkakin vielä varhaisen vaiheen näytöllä: kaksi vuoden 2025 prekliinistä tutkimusta (PMID 39571268, PMID 40923559) raportoivat, että daptomysiini ja sen lipopeptidijohdannaiset estävät tulehduksellisia sytokiineja ja NF-κB-signaloitia kollageenia indusoivassa artriitin hiire-mallissa, mikä viittaa mahdolliseen itsenäiseen anti-inflammatooriseen aktiivisuuteen, joka eroaa sen antibakteerisista vaikutuksista. Tämä ei ole vielä ihmisillä saatu näyttö, mutta se on biologisesti vihjattavampi johtolanka kuin nivelrikko-signaali ja saattaa vaatia erillisen seurannan.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnaytto

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Kohortti | International Orthopaedics | Korkea-annoksinen daptomysiini + rifampiini gram-positiivisille nivelten infektioille — arvioi yhdistelmän turvallisuutta/tehokkuutta, ei nivelrikko-hoitoa |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Kohortti | J Antimicrob Chemother | Daptomysiini polvi-/lonkka-periprosteteetin nivelinfektioihin (PJI) |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Kohortti | Int J Antimicrob Agents | Korkea-annoksinen daptomysiini (>6 mg/kg) monimutkaisiin luu-/nivel- ja implanttiin liittyviin gram-positiivisiin infektioihin |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Kohortti | J Antimicrob Chemother | Daptomysiini vs. tavanomainen hoito nivelten infektioihin liittyneillä *S. aureus* -bakteeremiapotilailla |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Rekisteri/Kohortti | Medicina Clínica | EU-CORE-rekisteri: daptomysiinin käytön kokemus eri Espanjan sairaaloissa gram-positiivisten infektioiden hoidossa |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Kohortti/Tutkimus | Int J Antimicrob Agents | Tutkimus nykyisistä PJI-hoidon käytännöistä infektiosairauksien lääkäreiden keskuudessa |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In-vitro herkkyystesti | Journal of Antibiotics | *S. aureus*/*S. epidermidis* -herkkyystestaus PJI-isolaateissa |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Mikrobiologinen tutkimus | Surgical Infections | Staphylokokkien herkkyysprofiilien 10 vuoden kehitys nivelten infektioissa |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Tapausraportti | Case Reports in Orthopedics | *Corynebacterium striatum* -niveltulehdus potilaalla, jolle alun perin oli lähete kokonaispolviniveleen tekonivelleikkaukseen nivelrikkoihin |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Tapausraportti | ASM Case Reports | *Corynebacterium propinquum* -niveltulehdus, ensimmäinen sinoviaalifluidun eriste syntyväisestä nivelistä |

**Huomautus:** Mikään näistä julkaisuista ei tutki daptomysiinia nivelrikkojen hoitona — kaikki koskevat bakteeri-infektioiden hoitoa nivelistä tai nivelten ympäriltä (usein nivelrikkoisia potilaita tekonivelleikkauksen jälkeen).

---

## Markkina-asema Suomessa

Daptomysiinia ei jaeta Suomessa — tästä tuotteesta ei ole tällä hetkellä rekisteröityjä myyntilupajäteistä tässä aineistossa.

---

## Turvallisuutta koskevat näkökohdat

Turvallisuu­desta tulee viitata pakkausselosteeseen.

**Kirjallisuudesta saatu turvallisuus­signaali (ei strukturoidusta turvallisuus­aineistosta, mutta esiin tuotu näytön tarkistamisen aikana):** yksi tapaus­raportti (PMID [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), 2023) kuvaa daptomysiinin aiheuttamaa rabdomyolyysiä, jota komplisoi akuutti podagra (kihsi), mikä on johdonmukaista daptomysiinin tunnetun yhteyden kanssa kreatiinikinaasinarvojen nousuun/myopatia. Tämä on tunnustettu luokka-efekti, joka kannattaa mainita missä tahansa tulevassa kliinisessä käytössä, riippumatta uudelleenkäytön kysymyksestä.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelu:**
Nivelrikko-signaali ei ole tuettu aidon mekaanisen tai kliinisen näytön — kaikissa kymmenen haetusta julkaisusta käsitellään bakteeri-nivelten/tekonivelinfektioiden hoitoa, ei itse nivelrikkoa, ja ne näyttävät olevan avainsana-rinnakkaisesiintymisen artefakti eikä oikea uudelleenkäytön mahdollisuus (näytön taso L4, päätöksen vaihe S0, lähdelaskennan mukaan).

**Jatkaaksemme seuraava on tarpeen:**
- Vahvista, pitäisikö TxGNN:n nivelrikko-ennuste priorisoida alas/jättää pois, kun näyttöpohja on sekava
- Jos jaksotetaan yhtään niveleen liittyvää signaalia, ohjaa huomio **reumatoidi artriittiin** (ranking 2), jossa vuoden 2025 prekliininen aineisto (PMID 39571268, PMID 40923559) näyttää uskottavan itsenäisen anti-inflammaatoorisen mekanismin — vaikka tämä vaatii edelleen ihmisillä saadun validoinnin ennen kuin voidaan edetä S1:n yli
- Daptomysiinin vaikutusmekanismin (MOA) tiedot ja TFDA/EMA-merkin varoitukset ja vasta-aiheet (tällä hetkellä merkitty Blocking/High severity -tietovajeiksi) on hankittava, ennen kuin mikään turvallisuus-esivalmistelu (S1) voi edetä
- Koska lääkettä ei jaeta Suomessa, markkina-saatavuus ja sääntelytie-toteutettavuus olisi myös arvioitava erillisesti

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

