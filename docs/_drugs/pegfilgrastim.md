---
layout: default
title: Pegfilgrastim
parent: Pelkkä mallin ennuste (L5)
nav_order: 288
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Pegfilgrastiimi: sytostaattikäsittelystä aiheutuvasta neutropeniasta vaikean ei-proliferatiivisen diabeettisen retinopatian hoitoon

> **Huomautus lokalisaatiosta:** Tämän kandidaatin todistusaineisto (`TW-DB00019-multi`) on Taiwanin laajuinen (`taiwan_regulatory`, TFDA-tietoaukot `meta.data_gaps`-kentässä), joten tämä raportti käyttää Taiwan/TFDA-terminologiaa Suomen/Fimea-merkintöjen sijaan.

## Yhden lauseen yhteenveto

Pegfilgrastiimi on pegyloidun rekombinantti G-CSF:n sisältävä lääke, jota käytetään neutrofiilin palautumisen tukemiseen potilailla, jotka saavat myelosuppressiivista solunsalpaajahoidon. TxGNN-malli ennustaa mahdollista yhteyttä **vakavaan ei-proliferatiiviseen diabeettiseen retinopatiaan (NPDR)**, mutta tukeva perustelun itsessään osoittaa **mekanistisesti vastakkaisen, mahdollisesti vahingollisen** suunnan (patologisen uusien verisuonten muodostumisen edistäminen sen sijaan että sitä estettäisiin), ja tällä hetkellä on **nolla kliinisiä tutkimuksia ja nolla julkaisuja**, jotka tukevat tätä indikaatiota.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla tässä todistusaineistossa (`original_indications` on tyhjä; TFDA:n pakkausseloste on tietoaukko, joka estää etenemisen — DG001). Pegfilgrastiimin kansainvälisesti tunnustettu käyttö on sytostatiikan aiheuttavan (febriili) neutropenia. |
| Ennustettu uusi indikaatio | Vakava ei-proliferatiivinen diabeettinen retinopatiaa |
| TxGNN-ennustepisteet | 99.89% (sijoitus 1638) |
| Todisteen taso | L5 |
| Taiwanin markkina-asema | Ei markkinoilla (Not marketed) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi tämä ennustus on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla (`original_moa` = tietoaukko, DG002). Tämän ennusteen yhteydessä olevien mekanististen muistiinpanojen perusteella pegfilgrastiimi on G-CSF-reseptorin agonisti, jonka pääasiallinen farmakologinen vaikutus on liikutella luuytimen granulosyytin edeltäjiä ja endoteelisen progenituurin soluja (EPC) järjestelmäkiertoon.

Alkuperäisen käytön (neutrofiilin määrän tukeminen kemoterapian aikana) ja ennustetun uuden indikaation (vakava NPDR, diabeettisen retinopatian esiproliteratiivinen vaihe) välinen suhde ei ole suoraviivainen "sama mekanismi, uusi sairaus" -tarina. Tämän ennusteen yhteydessä annettujen perusteluiden mukaan EPC/granulosyytin liikuttaminen liittyy kirjallisuudessa useammin **edistämiseen** patologista retinaalista uusien verisuonten muodostusta — prosessia, johon vakava NPDR on suurella riskillä edetä kohti — eikä sen hoitoon. Toisin sanoen mekanistinen yhteys tukee mahdollista **turvallisuushuolta (edistämällä progressiota proliferatiivisen taudin suuntaan)** eikä terapeuttista perustelua.

Näiden seikkojen perusteella korkea TxGNN-pistemäärä heijastaa todennäköisesti epäsuoraa sairauden–geeni/reseptorin yhteesiintymiskuviota tietoverkossa pikemminkin kuin kausaalia tai suunnallisesti tukevaa hoitosuhdetta. Tämä on eksplisiittisesti merkitty tapauksena, jossa mallin varmuutta **ei** pidä lukea tehokkuuden todisteeksi.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia (0 tulosta ClinicalTrials.gov- ja ICTRP-palveluissa sekä "severe nonproliferative diabetic retinopathy" että "diabetic retinopathy" -kyselyillä, päivätty 2026-04-20).

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta (0 PubMed-tulosta molemmille asiaan liittyville sairausehdoille, haku päivätty 2026-04-20).

---

## Taiwanin markkina-asema

Pegfilgrastiimilla ei tällä hetkellä ole **myyntilupaa Taiwanissa** (`market_status`: Not marketed; `total_licenses`: 0; `licenses`: tiedostossa ei ole listaa). Tuotteen nimeä, lääkemuotoa tai hyväksyttyä indikaatiotekstiä ei ole saatavilla.

---

## Turvallisuushuomiot

Katso pakkausselosteesta turvallisuustiedot. (Kaikki tämän todistusaineiston turvallisuuskentät — päävaroitukset, vasta-aiheet ja lääkeyhteisvaikutukset — ovat tällä hetkellä tietoaukkoja; TFDA:n pakkausseloste-tietoaukko (DG001) on merkitty **Estävä**, mikä tarkoittaa, että muodollinen S1-turvallisuuden esitarkastus ei voi edetä, kunnes se ratkaistaan.)

---

## Lisähuomautus: Asiaan liittyvä ennustettu indikaatio

Toinen, läheisesti liittyvä ennustus — **diabeettinen retinopatiaa** (yleinen, määrittelemätön vakavuusaste) — sai pistemäärän 99.73% (sijoitus 3482), myös L5, myös ilman kliinisiä tutkimuksia tai kirjallisuutta, ja se sisältää saman mekanistisen varoituksen kuin edellä (mahdollisen retinaalisen uusien verisuonten muodostumisen edistämisen pikemminkin kuin sen hoitamisen). Sitä ei käsitellä erillään tässä, koska se päällekkäinen sairausluokan ja todisteen tilan kanssa ensisijaisen kandidaatin kanssa.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Tällä kandidaatilla on vain L5-todisteet (mallin ennuste, ei kliinisiä tutkimuksia, ei kirjallisuutta), ja mekanistinen perustelun itsessään nostaa esiin mahdollisen turvallisuushuolen — että G-CSF:ään perustuva progenituurin solujen liikuttaminen voisi **kiihdyttää** pikemminkin kuin hoitaa diabeettisen retinopatian uusien verisuonten muodostumisen progressiota. Yhdessä TFDA-turvallissuusseloste-tietoaukon (DG001) kanssa ei ole tällä hetkellä perusteita edetä tämän kandidaatin tutkimushypoteesin ulkopuolella.

**Edistymisen edellyttämät seikat:**
- TFDA:n pakkausseloste tiedot (varoitukset/vasta-aiheet) Estävän tietoaukon DG001 ratkaisemiseksi, vaadittava ennen mitä tahansa S1-turvallisuuden esitarkastusta
- Vahvistettu alkuperäinen vaikutusmekanismi DrugBankista tietoaukon DG002 ratkaisemiseksi ja G-CSF/retinaalisen uusien verisuonten muodostumisen suhteen suuntaisuuden asianmukaiseksi arvioinniksi
- Preklin tai mekanistiset tutkimukset, jotka erityisesti tutkivat pegfilgrastiimin vaikutusta diabeettisen retinopatian progressioon (sekä riski että mahdollisen hyödyn suuntiin), koska niitä ei tällä hetkellä ole
- Pegfilgrastiimin alkuperäisen hyväksytyn indikaation ja Taiwanin lisensointi-aseman vahvistaminen (tällä hetkellä puuttuu tästä todistusaineistosta)
- Jos tämä kandidaatti säilytetään seurannan kohteena, selkeä farmakovalvonnan merkintä retinaalisten/oftalmologisten haittatapahtumatilaisuuksille turvallisuushuoli-hypoteesin perusteella, joka on nostettu esiin edellä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

