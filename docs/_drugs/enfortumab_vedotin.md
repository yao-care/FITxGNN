---
layout: default
title: Enfortumab Vedotin
parent: Pelkkä mallin ennuste (L5)
nav_order: 164
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Enfortumab Vedotin: ennustettu uusi käyttöaihe Lepra (näytön taso L5). Alkuperäinen käyttöaihe: Siirtymäsolusyöpä (urotelikarsinooma)"
monitor_inn: "ENFORTUMAB VEDOTIN"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "infectious bovine rhinotracheitis", "malignant catarrh"]
---

# Enfortumab Vedotin
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

## Enfortumabivedotiini: Urotelisyövästä ennustettuun uuteen käyttöaiheeseen (lepra)
{: .text-alpha }

## Yhteenveto

Enfortumabivedotiini on Nectin-4-kohdennettu vasta-aine-lääkekonjugaatti (MMAE-toksiini), jota on alun perin käytetty siirtymäsolusyövän (urotelikarsinooma) ja virtsatiesyöpien hoitoon.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **lepran**, mutta ennuste perustuu pelkästään laskennalliseen malliin: **kliinisiä tutkimuksia ei ole** eikä **lepraa tukevaa kirjallisuutta** ole löytynyt.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Siirtymäsolusyöpä (urotelikarsinooma); virtsatiesyövät |
| Ennustettu uusi käyttöaihe | Lepra |
| TxGNN-ennustepisteet | 0.9953 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Tämän raportin laatimiseen koottu aineisto ei sisällä yksityiskohtaista vaikutusmekanismitietoa. Tunnetun tiedon mukaan enfortumabivedotiini on Nectin-4-kohdennettu vasta-aine-lääkekonjugaatti, jonka MMAE-osa tuhoaa Nectin-4:ää ilmentäviä kasvainsoluja häiritsemällä mikrotubuluksia. Teho urotelisyövässä on osoitettu.

Mikään käytettävissä oleva tieto ei yhdistä Nectin-4-kohdennusta tai mikrotubulusten häirintää *Mycobacterium leprae* -infektioon. Korkea TxGNN-pistemäärä (0.9953) on laskennallinen ennuste, ja se tulee TxGNN-mallista (syväoppiminen). Se voi heijastaa mallin oppimia samankaltaisuuksia toisiinsa liittyvien tautien välillä, ei biologista näyttöä.

Muut mallin tuottamat ennusteet ovat samalla tavalla heikosti perusteltuja:

- **Multippeli endokriininen neoplasia** (99,43 %): spekulatiivinen, ei tutkimuksia eikä kirjallisuutta. Syöpäindikaationa ennakkoon uskottavampi kuin infektiot, mutta näyttöä ei ole.
- **Sytomegalovirusinfektio** (99,36 %, L4): ainoa julkaisu on tapausselostus vaikeasta haavaisesta ruokatorvitulehduksesta enfortumabivedotiini–pembrolitsumabi-hoidon jälkeen. Se on haittatapahtumailmoitus, joka viittaa pikemminkin riskiin kuin hyötyyn.
- **Kandidiaasi** (99,30 %, L4): ainoa julkaisu on FAERS-lääketurvatutkimus vasta-aine-lääkekonjugaattien riskisignaaleista virtsarakkosyövässä. Se puhuu käyttöä vastaan.
- **Aivoinfarkti** (99,23 %), **HIV-infektio** (99,19 %), **homotsygoottinen familiaalinen hyperkolesterolemia** (99,18 %): ei uskottavaa mekanistista yhteyttä, ei tutkimuksia.
- **Nautojen tarttuva nuha (IBR)** ja **malignikatarri** (0.9913): eläintauteja, jotka eivät liity ihmisen lääkehoitoon; todennäköisesti mallin oppimia samankaltaisuuksia, ei biologista näyttöä.

---

## Kliiniset tutkimukset

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Lepran osalta aiheeseen liittyvää kirjallisuutta ei ole saatavilla.

Muiden ennustettujen käyttöaiheiden osalta löytyi vain kaksi haittatapahtumiin liittyvää julkaisua:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Tapausselostus | Reports (MDPI) | Vaikea diffuusi haavainen ruokatorvitulehdus potilaalla, jolla oli etäpesäkkeinen urotelikarsinooma ja jota hoidettiin enfortumabivedotiinilla ja pembrolitsumabilla (liittyy CMV-ennusteeseen) |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Lääketurvatutkimus (FAERS, retrospektiivinen) | Clinical Epidemiology | Vasta-aine-lääkekonjugaattien riskisignaalit virtsarakkosyövässä (liittyy kandidiaasiennusteeseen) |

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005392 | Padcev | – | Siirtymäsolusyöpä; virtsatiesyövät (tila: peruutettu) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Vasta-aine-lääkekonjugaatti (Nectin-4-kohdennettu, MMAE-mikrotubulusinhibiittori); kohdennettu hoito, johon liittyy sytotoksinen kuorma |
| Myelosuppression riski | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Emetogeenisuusluokitus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Seurattavat parametrit | Katso valmisteyhteenveto; yleisesti verenkuva sekä maksa- ja munuaisarvot |
| Käsittelysuojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutuskyselyssä löytyi yhteensä 100 yhteisvaikutusta. Merkittävin on:

- **Klaritromysiini**: vakava (Major) yhteisvaikutus.

Useimmat muut listatut yhteisvaikutukset on luokiteltu kohtalaisiksi (Moderate), mm. diabeteslääkkeet: akarboosi, metformiini, pioglitatsoni, glimepiridi, glipitsidi, glibenklamidi, kanagliflotsiini, dapagliflotsiini, empagliflotsiini, linagliptiini, saksagliptiini sekä GLP-1-agonistit (eksenatidi, dulaglutidi, albiglutidi), sekä aprepitantti.

Varoituksista ja vasta-aiheista tietoa ei ole saatavilla; ne on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-pisteisiin (näytön taso L5). Kliinisiä tutkimuksia tai tukevaa kirjallisuutta ei ole, eikä biologista yhteyttä lepraan ole osoitettu.
- Ainoat muihin ennusteisiin liittyvät julkaisut ovat haittatapahtumaraportteja, jotka viittaavat riskiin eikä hyötyyn. Lisäksi Suomen myyntilupa on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivuilta (estää turvallisuusseulonnan jatkamisen)
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBankista)
- Mekanistisen perustelun selvittämistä lepralle (esim. Nectin-4-ilmentymä tai muu biologinen yhteys) sekä prekliinistä näyttöä
- Myyntilupatilanteen ja saatavuuden selvittämistä Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

