---
layout: default
title: Evolocumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 159
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Evolocumab: hyperkolesterolemiastä oireiseen hemofiliaan naiskantajissa

## Yhden lauseen yhteenveto

Evolocumab on PCSK9:tä estävä monoklonaalinen vasta-aine, jota käytetään LDL-kolesterolin alentamiseen hyperkolesterolemian/dyslipidemiassa. TxGNN-mallin parhaan ennusteen mukaan lääke voisi mahdollisesti liittyä **oireiseen hemofiliaan naiskantajissa**, mutta tätä suuntaa tuetaan tällä hetkellä **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja todiste-paketin oma mekanistinen analyysi merkitsee sen todennäköiseksi graafitopologian artefaktiksi eikä todelliseksi biologiseksi linkiksi.

---

## Pikayhteenveto

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — Suomessa lääke ei ole markkinoitu, joten hyväksyttyä indikaatiotekstiä ei ole olemassa rekisterissä. (Yleinen toimintamekanismin konteksti todiste-paketista: lipidien aineenvaihdunta / LDL-C:n alentaminen.) |
| Ennustettu uusi indikaatio | Oireinen hemofilia naiskantajissa |
| TxGNN-ennustepistemäärä | 99.82% |
| Näyttöjen taso | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinointistatus | ✗ Ei markkinoitu |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaista toimintamekanismin tietoa (`original_moa`) ei ole saatavissa tässä todiste-paketissa. Ennusteisiin liitetyn perustelutekstin perusteella evolocumab on anti-PCSK9-monoklonaalinen vasta-aine, joka estää PCSK9-välitteisen LDL-reseptorin hajoamisen, mikä lisää LDL-C:n klirensia — toisin sanoen se vaikuttaa lipidien aineenvaihdanta- / LDL-reseptorisignaalointitielle.

Oireinen hemofilia naiskantajissa on verihyytymistekijän häiriö (faktori VIII/IX-puutos, joka liittyy X-kromosomaaliseen kantajuuteen), joka toimii täysin eri biologisella akselilla kuin LDL-reseptorin säätely. Todiste-paketin oma uudelleenkäyttöperustelu eksplisiittisesti toteaa, että **ei ole tunnettua mekanistista yhteyttä** PCSK9-eston ja verihyytymistekijöiden VIII/IX ilmentymisen välillä, ja ehdottaa, että korkea TxGNN-pistemäärä todennäköisesti heijastaa graafimallin läheisyyttä "harvinaisen perinnöllisen sairauden" solmuryppään eikä todellista farmakologista suhdetta.

Tämä kuvio toistuu kaikissa kuudessa arvoitussa ennusteessa tässä paketeissa (perinnöllinen ApoC-II-puutos, trombosytopeninen purpura, faktori XI-puutos, hemofilia A verisuonien poikkeavuuksilla ja ei-spesifinen ontologia-solmu "katalyyttisen aktiivisuuden sairaus") — jokainen perusteluteksti itsenäisesti päättelee, että mekanistinen perusta on heikko tai olematon, eikä millään näistä ole tällä hetkellä kliinisiä tutkimuksia tai kirjallisuustukea. Tämä on matalan luotettavuuden ennuste-joukko, joka vaatii huomattavaa lisätutkimusta ennen kuin uudelleenkäyttötoiminnalle on perustetta.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

Markkinointihyväksynnät eivät ole arkistossa — evolocumab ei ole tällä hetkellä **markkinoitu** Suomessa (0 lupaa rekisteröity), joten vertailtavaa hyväksytyn indikaation tekstiä ei ole saatavissa.

---

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta. (Tärkeät varoitukset, vasta-aiheet ja lääkkeiden välisen vuorovaikutuksen tiedot eivät ole tällä hetkellä saatavissa tässä todiste-paketissa — TFDA/Fimea-pakkausselosteen haku on merkitty **estäväksi** tietovajeeksi `meta.data_gaps`:issa (DG001).)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Kaikki kuusi TxGNN-ennustettua indikaatiota sijaitsevat näyttötason L5 tasolla (vain mallin ennuste) ilman tukevia kliinisiä tutkimuksia tai kirjallisuutta, ja paketin oma mekanistisen yhteyden analyysi arvioi parhaimmat ehdokkaat todennäköisiksi graafitopologian artefakteiksi eikä todellisiksi farmakologisiksi suhteiksi. Yhdessä lääkkeen luvittamattoman aseman kanssa Suomessa, ei ole tällä hetkellä perustetta tämän ehdokkaan edistämiselle.

**Etenemiseksi tarvitaan seuraavaa:**
- TFDA/Fimea-pakkausseloste (varoitukset, vasta-aiheet, lääkkeiden välinen vuorovaikutus) — tällä hetkellä estävä tietoaukko (DG001)
- Vahvistettu toimintamekanismi DrugBankista tai peruskirjallisuudesta — tällä hetkellä vakava tietoaukko (DG002)
- Itsenäinen mekanistinen tai prekliininen näyttö PCSK9-eston ja verihyytymis- tai hematologisten polkujen välisestä yhteydestä TxGNN-upotuksen läheisyyden lisäksi
- Jatkuva seuranta uusille kliinisen tutkimuksen tai julkaisun signaaleille tässä lääke–tauti-parissa, kun otetaan huomioon tämän hetkinen todellisen maailman näytön täydellinen puute

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

