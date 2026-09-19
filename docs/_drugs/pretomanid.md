---
layout: default
title: Pretomanid
parent: Pelkkä mallin ennuste (L5)
nav_order: 309
evidence_level: L5
indication_count: 5
---

# Pretomanid
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

# Pretomanidi: Moniresistentista tuberkuloosista kandidiasisiin

## Yhden lauseen tiivistelmä

Pretomanidi (PA-824) on nitroimidazoksatiini-antimykobakteeriaine, joka on hyväksytty kansainvälisesti osana BPaL/BPaLM-yhdistelmää laajasti lääkeresistentin (XDR) ja hoitokelvottoman/hoitoon vastaamattoman moniresistentin (MDR) keuhkotuberkuloosin hoitoon. TxGNN-malli ennustaa, että se saattaa olla tehokas **kandidiaasin** hoitoon ennustepisteinä **99.69%**, mutta tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä suuntaa, eikä näyttöpaketin oma mekanistinen analyysi löydä biologista perustelua tälle yhteydelle.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Monilääkeresistentti / laajasti lääkeresistentti keuhkotuberkuloosi (BPaL/BPaLM-yhdistelmä) — paikallista lääkehyväksyntää ei ole; tämä on johdettu näyttöpaketin kirjallisuusviitatuksista, ei muodollisesta indikaatiokentästä |
| Ennustettu uusi indikaatio | Kandidiaasi |
| TxGNN-ennustepiste | 99.69% |
| Näytön taso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidätys |

## Miksi tämä ennuste on kohtuullinen?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla jäsennelyssä lääkkeen tietueessa (`original_moa` on tieto-aukko). Kuitenkin näyttöpaketin tueksi ottama teksti kuvaa pretomaniidin tunnetun farmakologian: se on syklinen nitroimidatsoli-esisyy, joka aktivoidaan mykobakteeri-spesifisen Ddn-nitroredukentsin avulla, joka estää mykoliinihapon synteesiä ja vapauttaa typpimonioksidia, jolloin syntyy bakteereja tuhoava aktiivisuus *Mycobacterium*-lajeja vastaan.

Tämä mekanismi on spesifinen mykobakteerisen seinäbiosynteesin osalta ja sillä ei ole tunnettua vastaavaa sieni-biologiassa. Kandidiaasin aiheuttavat *Candida*-lajit (sieni), joilla ei ole Ddn-nitroredukentsin aktivaatioreittiä eikä mykoliinihapon synteesiä, joihin pretomanidi kohdistuu. Näyttöpaketin omat perustelut tälle ennusteelle sanovat selvästi: *"無。Pretomanid 作用標的為分枝桿菌特有的 Ddn 硝基還原酶活化路徑與分枝菌酸合成抑制，Candida 為真菌，無同源標的，亦無已知抗真菌活性機轉"* — toisin sanoen mekanistista yhteyttä ei ole olemassa.

Koska mekanistista yhteyttä ei ole, kliinistä tutkimusta tai kirjallisuustodistetta ei ole, tätä ennustetta tulee käsitellä todennäköisesti mallin artefaktina eikä aitoina lääkkeen uudelleenkäytön signaalina.

## Kliinisen tutkimuksen näyttö

Ei tällä hetkellä liittyviä rekisteröityjä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Ei tällä hetkellä saatavilla olevaa kirjallisuutta

## Suomen markkinatiedot

Pretomanidilla ei ole paikallista markkinahyväksyntää tällä markkinalla (`market_status: Not marketed`, `total_licenses: 0`), joten mitään hyväksyntätietueita ei ole saatavilla luetteloitavaksi.

## Turvallisuuteen liittyvät näkökohdat

Turvalllisuustietoja varten katso pakkausesitettä.

**Huomio:** Pohjalla oleva tietopaketti merkitsee tämän lääkkeen paikallisten pakkausesitteen varoitukset/vasta-aiheet **estäväksi tieto-aukoksi (DG001)** — mikä tarkoittaa, että muodollista S1-turvallisuusarviointia ei voi suorittaa vielä. Lisäksi paketin oma analyysi eri ehdokkaan indikaation (myokardin iskemia) osalta huomauttaa, että pretomanidilla on **tunnettu QT-pidentymisriski**, erityisesti käytettäessä BPaL-yhdistelmässä bedakviiniinin kanssa. Tämä ei ole virallista turvallisuustietoa, joka on poimittu merkinnöistä, mutta se on dokumentoitu signaali, joka kannattaa kuljettaa eteenpäin tuleviin arviointeihin.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
TxGNN-pistemäärä on korkea, mutta kandidiaasin kohdalla ei ole kliinistä tai kirjallisuustodistetta, ja näyttöpaketin oma mekanistinen katsaus päättelee, että biologista linkkiä ei ole (antimykobakteeri vs. antisieni-kohderistiriita). Tieto-aukko paikallisissa pakkausesitteen varoituksissa/vasta-aiheissa (DG001) estää myös muodollisen turvallisuusarvioinnin aloittamisen.

**Jatkamista varten tarvitaan seuraava:**
- Paikallisen sääntelyviranomaisen pakkausesite (varoitukset/vasta-aiheet) DG001:n ratkaisemiseksi ennen mitään S1-turvallisuusarviointia
- Vahvistetut MOA-tiedot DrugBank API:n kautta DG002:n ratkaisemiseksi
- In vitro/in vivo -antisieni-aktiivisuustiedot pretomanidista *Candida*-lajeja vastaan, koska sellaisia ei tällä hetkellä ole
- Viitteeksi, seuraavaksi sijoittunut ennuste (lepra, L4) sisältää todellista tutkimus-/kirjallisuuskatetta, mutta sitä kumoaa myös suora in vitro -todiste (PMID 17005816), joka osoittaa, että *M. leprae* on luontaisesti resistentti PA-824:lle — joten se ei ole vahvempi ehdokas sekään. Sijoitukset 3–5 (sepelvaltimon tauti, myokardin iskemia, epänormaali sepelvaltimo) eivät ole mekanistista perustaa eivätkä todistetta, ja niitä tulee käsitellä matalan prioriteetin mallin kohinana.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

