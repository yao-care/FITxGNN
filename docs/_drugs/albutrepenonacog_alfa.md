---
layout: default
title: Albutrepenonacog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog alfa: Hemofiliasta B pseudo-von Willebrandi tautiin

## Yhden lauseen yhteenveto

Albutrepenonacog alfa on rekombinantti IX tekijä–albumiini-fuusioproteiiini, joka on alun perin kehitetty verenvuodosta ehkäisemiseen ja hoitoon hemofiliassa B (synnynnäinen IX tekijän puutos). TxGNN-malli ennustaa, että se saattaa olla tehokas myös **pseudo-von Willebrandi taudissa**, mutta tämä ennuste on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja todistusten paketin oma mekanistinen arvio merkitsee biologista perustelua heikoksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Hemofilia B / synnynnäinen IX tekijän puutos *(johdettu lääkkeen identiteetistä — ei läsnä todistusten paketissa; `original_indications` ja `taiwan_regulatory.licenses` ovat molemmat tyhjät)* |
| Ennustettu uusi indikaatio | Pseudo-von Willebrandi tauti |
| TxGNN-ennustepistemäärä | 99.94% (sijoitus 878 malliennusteiden joukossa) |
| Todistustaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoitu (Ei markkinoitu) |
| Lupien määrä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi tämä ennuste on kohtuullinen?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla (merkitty korkean vakavuusasteen tietovajeeksi, DG002). Tunnetun lääkkeen luokituksen perusteella albutrepenonacog alfa on rekombinantti IX tekijä -molekyyli, joka on yhdistetty albumiiniin puoliintumisajan pidentämiseksi, ja sen tehokkuus hemofiliassa B — **koagulaatiotekijän puutoksesta johtuvassa** sekundaarisen (plasmaattisen) hemostaasin häiriössä — on hyvin vakiintunut.

Kuitenkin mekanistinen uskottavuus parhaiten ennustetulle indikaatiolle on heikko. Pseudo-von Willebrandi tautia aiheuttaa **verihiuttaleen GPIbα-reseptorin kasvavuutta muunnos**, joka lisää sen affiniteettia von Willebrandi tekijää kohtaan. Tämä on **verihiuttaleen reseptorihäiriö**, ei veren hyytymistekijän puutos — IX tekijän lisääminen ei korjaa poikkeavaa reseptori-ligandi-sitoutumista, ja todistusten paketin oma uudelleenkäyttöperustelua selvästi karakterisoi mekanistisen yhteyden jakavaksi vain pinnallista "verenvuodotaipumusta" fenotyyppiä pelkkien oireiston saman reitin sijaan.

Huomionarvoista on, että todistusten paketti nostaa esiin viisi muuta TxGNN-sijoituksella varustetua ehdokasta samassa pistemäärän kaistalessa (0.9994–0.9928), jotka kaikki ovat **primaarisen hemostaasin / verihiuttaleen häiriöitä** eikä koagulaatiotekijän puutoksia: primaarinen verihiuttaleiden vapautushäiriö, Glanzmannin trombasthenia, Scottin oireyhtymä, kollageenireseptoriin liittyvä verenvuodotahäiriö ja verihiuttalemäärään liittyvä verenvuodotahäiriö. Jokainen sisältää saman L5-todistustason ja saman sisäisesti dokumentoidun varoituksen, että IX tekijällä ei ole vakiintunutta mekanismia verihiuttaletason defektien korjaamiseksi. Tämä johdonmukainen kuvio viittaa siihen, että malli klusteroi sairauksia jaettujen "verenvuodotahäiriö" fenotyypin upotuksien perusteella eikä tunnista todellista, toimintakelpoista farmakologista reittiä — kuvio, joka vaatii varovaisuutta pikaisemman etenemisen sijaan.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole liittyviä klinisia tutkimuksia rekisteröitynä.

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole liittyvää kirjallisuutta saatavilla.

---

## Suomen markkinatiedot

Lääke ei ole tällä hetkellä **markkinoitu** Suomessa (`market_status: Not marketed`, `total_licenses: 0`), eikä todistusten paketissa ole saatavilla mitään lupahallintotietueita.

---

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

*(Huomautus: `key_warnings`, `contraindications` ja lääkkeiden väliset yhteisvaikutuksien tiedot on kaikki merkitty tietovajeiksi tässä todistusten paketissa. TFDA:n pakkausselosteen varoitukset/vasta-aiheet on merkitty **estäväksi** vakavuuden vajeeksi (DG001), mikä tarkoittaa, että tätä ehdokasta ei voida vielä suorittaa S1-turvallisuus-esiarviointia.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ennustetulla indikaatiolla on tukenaan vain TxGNN-mallin pistemäärä, jolla ei ole tukevia klinisiä tutkimuksia tai kirjallisuutta (todistustaso L5), ja todistusten paketin oma mekanistinen analyysi päättelee, että IX tekijän korvaaminen ei ole vakiintuneet biologisen reitin korjaamaan pseudo-von Willebrandi taudin taustalla olevan verihiuttaleen reseptorin vika. TFDA-turvallisuus-/merkintätiedon estävän vakavuuden vajeeseen yhdessä ottaen, tämä ehdokas ei ole valmis etenemään alkuperäisen seulonnan yli.

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA:n pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävät S1-turvallisuusarvion
- Albutrepenonacog-alfan vahvistetut vaikutusmekanismin tiedot
- Prekliniikat tai translatiiviset tutkimukset, jotka suoraan testaavat IX tekijän lisäämistä verihiuttaleen-reseptori-vika-verenvuodotahäiriöissä, vakiinnuttaakseen biologisen uskottavuuden ennen lisäinvestointeja
- TxGNN-lähdön uudelleenseulonta erottaakseen todelliset mekanistiset ehdokkaat fenotyyppi-klusteroinnin artefakteista (annettu 6 samalla tavalla pisteytettynä, samalla tavalla heikosti plateaalisesti häiriöiden ennusteina)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

