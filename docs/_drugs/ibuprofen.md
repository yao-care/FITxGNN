---
layout: default
title: Ibuprofen
parent: Pelkkä mallin ennuste (L5)
nav_order: 217
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Ibuprofen: ennustettu uusi käyttöaihe Akromesomeelinen dysplasia, Hunter-Thompson-tyyppi (näytön taso L5). Alkuperäinen käyttöaihe: Avoin valtimotiehyt (Ductus arteriosus, patent)"
---

# Ibuprofen
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **7** kpl
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

# Ibuprofeeni: Avoautuneesta valtimotiehyestä (PDA) akromesomeeliseen dysplasiaan (Hunter-Thompson-tyyppi)

## Yhden lauseen tiivistelmä

Ibuprofeeni on tulehduskipulääke (COX-estäjä), jota on käytetty avoimen valtimotiehyen (persistoiva ductus arteriosus) sulkemiseen. TxGNN-malli ennustaa sen voivan tehota sairauteen **akromesomeelinen dysplasia, Hunter-Thompson-tyyppi**, mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään laskennalliseen malliin.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Avoin valtimotiehyt (Ductus arteriosus, patent) |
| Ennustettu uusi käyttöaihe | Akromesomeelinen dysplasia, Hunter-Thompson-tyyppi |
| TxGNN-ennustepistemäärä | 99,74 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) järkevä?

Yksityiskohtaisia tietoja ibuprofeenin vaikutusmekanismista ei ole tähän raporttiin koottu. Tiedetään, että ibuprofeeni on epäselektiivinen syklo-oksigenaasin (COX) estäjä, joka vähentää prostaglandiinien tuotantoa. Tämä selittää sen vaikutuksen valtimotiehyen sulkemisessa sekä sen kipua lievittävät ja tulehdusta hillitsevät vaikutukset.

Akromesomeelinen dysplasia (Hunter-Thompson-tyyppi) on geneettinen luuston kehityshäiriö, joka johtuu CDMP1/GDF5-geenin toiminnan menetystä aiheuttavista muutoksista ja häiriintyneestä BMP-signaloinnista. COX- ja prostaglandiinireitin estäminen ei korjaa tätä BMP-reitin vikaa. Nivelkivun oireenmukainen hoito on ajateltavissa, mutta se ei muuta taudin kulkua.

Korkea TxGNN-pistemäärä (0,997) on mallin ennuste, ja se johtuu todennäköisesti verkkorakenteen läheisyydestä eikä todellisesta biologiasta. Uskottavaa mekanistista yhteyttä alkuperäiseen käyttöaiheeseen ei tunnistettu.

### Muut ennustetut käyttöaiheet

Samalla pistemäärätasolla mallin ennustamat muut sairaudet eivät myöskään saa tukea:

| Sijoitus | Sairaus | TxGNN-pisteet | Arvio mekanistisesta yhteydestä |
|------|------|------|------|
| 2 | Brakyolmia–amelogenesis imperfecta -oireyhtymä | 99,71 % | Ei uskottavaa yhteyttä (LTBP3, TGF-beeta) |
| 3 | Myoskleroosi | 99,68 % | Vain heikko, spekulatiivinen oireenmukainen perustelu |
| 4 | Brakyolmia | 99,67 % | Ei uskottavaa mekanismia |
| 5 | Brakydaktylia–syndaktylia-oireyhtymä | 99,66 % | Ei uskottavaa mekanismia (kehityshäiriö) |
| 6 | Pseudoakondroplasia | 99,66 % | Epäsuora ja heikko; mahdollinen oireenmukainen kivunlievitys |
| 7 | Kolobomatoottinen mikroftalmia–rhizomeelinen dysplasia -oireyhtymä | 99,60 % | Ei uskottavaa yhteyttä |

Kaikkien näiden näytön taso on L5 eikä niistä löytynyt kliinisiä tutkimuksia tai kirjallisuutta.

---

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/006129 | Ibuprofen Gen.Orph (peruutettu) | – | Ductus arteriosus, patent |
| EMEA/H/C/000549 | Pedea (peruutettu) | – | Ductus arteriosus, patent |

Molemmat myyntiluvat on peruutettu, joten voimassa olevia valmisteita ei ole.

---

## Turvallisuusnäkökohdat

Tutkimusta varten koottu tieto sisältää lääkkeiden yhteisvaikutuksia ja tietämysgraafiin perustuvia vasta-aiheita. Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla, joten niiden osalta on tutustuttava valmisteyhteenvetoon.

**Tietämysgraafin mukaiset mahdolliset vasta-aiheet** (TxGNN/PrimeKG, ei perustu valmisteyhteenvetoon):
- Sydän- ja verisuonitaudit: verenpainetauti, matala verenpaine, sydäninfarkti, aivohalvaus, aivoverenkiertohäiriöt, aivoinfarkti
- Maksa ja munuaiset: maksan vajaatoiminta, maksasairaus, munuaissairaus, sappirakon sairaus
- Ruoansulatuskanava: peptinen haavauma, tulehduksellinen suolistosairaus
- Veri: trombosytopenia, hyytymishäiriöt
- Aineenvaihdunta ja hormonit: diabetes, diabeettinen ketoasidoosi, kilpirauhasen vajaatoiminta (myksedeema, synnynnäinen), kaliumin puutos
- Muut: epilepsia, keuhkoahtaumatauti (COPD), systeeminen lupus erythematosus (myös lapsuusiän), hyvänlaatuinen eturauhasen liikakasvu, päihteiden väärinkäyttö/riippuvuus

**Lääkeyhteisvaikutukset** (haettu 100 yhteisvaikutusta, alla keskeisiä):
- **Merkittävä (Major):** asetyylisalisyylihappo
- **Kohtalainen (Moderate):** kortikosteroidit (beetametasoni, budesonidi, deksametasoni, hydrokortisoni), sulfonyyliureat ja muut diabeteslääkkeet (asetoheksamidi, klooripropamidi, glimepiridi, glipitsidi, glyburidi, eksenatidi), aprepitantti, balsalatsidi, kanamysiini, levofloksasiini, fenfluramiini ja deksfenfluramiini
- **Lievä (Minor):** famotidiini, ranitidiini, simetidiini

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennuste perustuu pelkkään mallipisteeseen (L5), eikä kliinisiä tutkimuksia tai julkaisuja ole. Uskottavaa mekanistista yhteyttä ei tunnistettu: ibuprofeenin COX-esto ei vaikuta BMP/GDF5-reitin geneettiseen vikaan. Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa ja tietämysgraafi listaa useita mahdollisia vasta-aiheita.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimean sivustolta (estää turvallisuusseulonnan etenemisen)
- Yksityiskohtaiset vaikutusmekanismitiedot (esim. DrugBank)
- Prekliininen tai mekanistinen näyttö BMP/GDF5-reitin yhteydestä ennen mitään kliinistä arviointia
- Jos oireenmukaista kivunhoitoa harkitaan, erillinen arvio pitkäaikaisen NSAID-käytön riskeistä (maha-suolikanava, munuaiset, sydän- ja verisuonisto), erityisesti lapsilla
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

