---
layout: default
title: Teprotumumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Teprotumumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Teprotumumab: kilpirauhasen silmäsairaudesta Monosomiaan X

## Yhden lauseen yhteenveto

Teprotumumab on anti-IGF-1R-monoklonaalinen vasta-aine, jonka vakiintunut käyttö (johon viitataan todistuspaketin mekanistisessa perustelussa) on kilpirauhasen silmäsairaus; virallisia alkuperäisen indikaation tietoja ei palautettu tällä kyselyllä. TxGNN-mallin huippuennuste on **Monosomia X** (Turnerin oireyhtymän karyytyyppi) 99.79 % pisteluvulla, mutta tätä kandidaattia tuetaan **0 kliinisillä tutkimuksilla** ja **0 julkaisulla**, ja todistuspaketti itsessään merkitsee ennusteen todennäköisesti tietokantaverkon väärä positiiviksi.

---

## Nopea katsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei vahvistettu lähdetiedoissa (`original_indications` tyhjä; mekanistinen perustelu viittaa kilpirauhasen silmäsairauteen tunnetuksi käytöksi) |
| Ennustettu uusi indikaatio | Monosomia X |
| TxGNN-ennusteen pisteluku | 99.79 % |
| Todistustaso | L5 (mallin ennuste vain, ilman tukevia tutkimuksia) |
| Suomen markkinoiden asema | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia toimintamekanismin tietoja ei ole tällä hetkellä saatavilla DrugBankista tällä kyselyllä (`original_moa: [Data Gap]`). Todistuspaketin omiin perustelukenttihin upotettujen tietojen perusteella teprotumumabin ymmärretään toimivan IGF-1R-reseptorin (insuliinin kaltaisen kasvutekijän 1 -reseptor) antagonistina, ja sillä on vakiintunut käyttö kilpirauhasen silmäsairaudessa.

Korkeimmalle rankattu ennuste, monosomia X, on Turnerin oireyhtymän sytogeeninen muoto. Todistuspaketin oma uudelleenkäytön perustelu merkitsee **suunnan ristiriidan**: Turnerin oireyhtymää hallitaan kliinisesti kasvuhormonin ja IGF-1-akselin terapioilla, jotka *edistävät* kasvua sairastuneilla potilailla, kun taas teprotumumab *estää* IGF-1R-signaloinnin. Saman akselin estäminen, jota klinisesti pyritään stimuloimaan, on mekanistisesti taaksepäin, ei täydentävä.

Lisäksi 6 kymmenestä huippusijoituksesta (sijoitukset 1, 4, 6, 7, 8, 10) ovat kaikki saman Turnerin oireyhtymä-/sukupuolikromosomianomalia-sairauden klusterin muunnoksia, ja 3 muuta (sijoitukset 2, 3, 9) ovat kaikki yhden laskimo-/verisuonisairauden klusterin muunnoksia (oesofageaaliset varitsit, varikositeetti). Tämä malli on yhteensopiva TxGNN-upotuksen läheisyyden kanssa sairauksien samankaltaisuusklustereiden sisällä pikemminkin kuin 10 riippumattoman farmakologisen hypoteesin kanssa. Nolla kliinisten tutkimusten ja nolla kirjallisuuden kanssa kaikissa 10 kandidaatissa, mikään ei selvästikään täytä edes alustavan uskottavuuden kynnystä.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole asiaan liittyvää kirjallisuutta saatavilla

---

## Suomen markkinoiden tiedot

Teprotumumabilla ei ole tällä hetkellä myyntilupaa Suomessa (0 lisenssiä rekisterissä); mihinkään taulukointiin ei ole saatavilla annosmuotoja tai hyväksyttyjen indikaatioiden tekstiä.

---

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät valmisteyhteenvedosta.

*(Huomio: Tämän lääkkeen TFDA:n valmisteyhteenvedon varoitukset/vasta-aiheet merkitään todistuspakettissa blokkavaksi tietovajeksi — DG001 — odottaen PDF-hakua ja jäsentelyä TFDA:n sivustolta.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelu:**
Huippuennuste (monosomia X) ja kaikki 9 muuta huippiehdokasta ovat todistustasolla L5, nolla kliinisen tutkimuksen ja nolla kirjallisuuden tuella. Todistuspaketin oma mekanistinen perustelu tunnistaa Turnerin oireyhtymäklusterin suunnan ristiriidan (IGF-1R-estävyys vs. kasvua edistävä terapia, jota tämä väestö tarvitsee) ja johtaa loput kandidaatit graafien klusterointiperusteihin pikemminkin kuin riippumattomiin biologisiin hypoteeseihin.

**Jatkamiseksi tarvitaan seuraavat:**
- TFDA:n valmisteyhteenveto (varoitukset, vasta-aiheet) — tällä hetkellä blokkava aukko (DG001)
- Vahvistettu alkuperäinen indikaatio ja MOA DrugBankista (tällä hetkellä tietovaje, DG002)
- Mekanistisesti yhtenäinen hypoteesi vähintään yhdelle indikaa... lle, itsenäisesti tarkistettu ennen kuin lisätodistusten keruusta päätetään
- Prekliiniset tai potilastasoiset todisteet vähintään yhdelle ehdokkaalle, ennen kuin edetään S0:n yli

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

