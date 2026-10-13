---
layout: default
title: Glucarpidase
parent: Pelkkä mallin ennuste (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glukarpidaasi: Metabolisista haittavaikutuksesta diabeettiseen kaihiin

## Yhden lauseen yhteenveto

Glukarpidaasi on rekombinantti entsyymi, jonka alkuperäinen käyttöaihe on lääkeaineiden ja aineiden aiheuttamien metabolisten haittavaikutusten hoito (käytännössä metotreksaatin poistaminen elimistöstä).
TxGNN-malli ennustaa sen mahdollisesti tehoavan **diabeettiseen kaihiin**, mutta ennusteelle ei löydy **yhtään kliinistä tutkimusta eikä julkaisua**.
Ennuste vaikuttaa pikemminkin tietograafin rakenteen sivutuotteelta kuin lääkkeen farmakologiaan perustuvalta löydökseltä.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Lääkeaineiden ja aineiden metaboliset haittavaikutukset |
| Ennustettu uusi käyttöaihe | Diabeettinen kaihi |
| TxGNN-ennustepisteet | 99,85 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (ei) perusteltu?

Glukarpidaasi on rekombinantti bakteeriperäinen karboksipeptidaasi G2, joka hydrolysoi solunulkoista metotreksaattia ja foliaattiyhdisteitä inaktiivisiksi metaboliiteiksi. Yksityiskohtaista vaikutusmekanismitietoa ei ole tämän raportin aineistossa saatavilla.

Alkuperäinen käyttöaihe (metotreksaatin aiheuttamien haittojen hallinta) ja ennustettu käyttöaihe (diabeettinen kaihi) eivät liity toisiinsa mekanistisesti. Glukarpidaasilla ei tunneta vaikutusta linssin polyolireittiin, glykaatioon tai oksidatiiviseen stressiin. Lääke on lisäksi suuri entsyymi, jota annetaan laskimoon, eikä silmään kohdistuvalle annostelulle ole perustetta.

Korkea pistemäärä johtuu todennäköisesti tietograafin ("metabolinen" ja "diabetes") naapurustosta eikä mekanismiin perustuvasta ennusteesta. Kaikki kymmenen ennustetta (diabeettinen kaihi, diabeettinen retinopatia, kraniostenoosiin liittyvä kaihi, tetaaninen kaihi, tyypin 2 diabetekseen liittyvä kaihi, kypsymätön kaihi, kypsä kaihi, ydinkaihi, kuorikaihi ja seniili kaihi) kuuluvat samaan kaihi- ja diabeettisen silmäsairauden klusteriin, mikä viittaa järjestelmälliseen mallin artefaktaan eikä toisistaan riippumattomiin signaaleihin.

---

## Kliiniset tutkimukset

Tällä hetkellä aiheeseen ei ole rekisteröity kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Tällä hetkellä aiheesta ei ole saatavilla kirjallisuutta.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005467 | Voraxaze (SERB SAS) | – | Lääkeaineiden ja aineiden metaboliset haittavaikutukset (tila: peruutettu) |

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Tietokannasta löytyi 8 kohtalaisen tason yhteisvaikutusta: proguaniili, trimetopriimi, levoleukovoriini, pemetreksedi, pralatreksaatti, pyrimetamiini, leukovoriini ja trimetreksaatti.

Muuten turvallisuustietojen osalta tulee tutustua valmisteyhteenvetoon.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteelle ei ole kliinistä eikä kirjallista näyttöä, eikä lääkkeen farmakologialla ole uskottavaa yhteyttä kaihiin tai diabeettisiin silmäsairauksiin. Korkea pistemäärä näyttää tietograafin artefaktalta.
- Voraxazen ainoa Suomessa tunnettu myyntilupa on peruutettu.

**Jatkotoimenpiteet, jos asiaa halutaan viedä eteenpäin:**
- Valmisteyhteenvedon varoitus- ja vasta-aihetietojen hankinta Fimean sivustolta
- Vaikutusmekanismitietojen täydentäminen (esim. DrugBank)
- Prekliininen näyttö mahdollisesta yhteydestä silmäsairauksiin sekä perustelu silmään kohdistuvalle annostelulle
- Arvio siitä, onko ennustetun klusterin tulos yleisesti tietograafin artefakta
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

