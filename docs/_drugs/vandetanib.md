---
layout: default
title: Vandetanib
parent: Vahva näyttö (L1-L2)
nav_order: 397
evidence_level: L2
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **10** kpl
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

# Vandetanib: märekilpirauhasisestä syövästä munuaissolakarkimoon

## Yhdessä lauseessa yhteenveto

Vandetanib (DrugBank DB05294) on suullinen usean tyrosiinikinaasin estäjä, jonka alkuperäisen hyväksynnän perusteella sisältyvät todisteet viittaavat alkuperäiseen käyttöön **märekilpirauhasisyövässä (Medullary Thyroid Cancer, MTC)**; TxGNN-malli ennustaa, että se voisi olla tehokas **munuaissolakarkimoon (Renal Cell Carcinoma)**, ennustepisteiden ollessa **99,92%**, ja tällä hetkellä on **4 asiaan liittyvää kliinistä tutkimusta** ja **6 julkaisua** tukevia näyttöjä. Useimmat tutkimukset on kuitenkin pysäytetty ennenaikaisesti ja näytteiden koko on pieni, mikä viittaa kohtalaisesti heikon todisteen vahvuuteen.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen käyttöindikaatio | Märekilpirauhasisyöpä (perustettu todistusaineiston sisältämiin julkaisuihin; Taiwanin lupatieto puuttuu) |
| Ennustettu uusi käyttöindikaatio | Munuaissolakarkino (Renal Cell Carcinoma) |
| TxGNN-ennustepiste | 99,92% (score = 0.99917870759964, rank 1186) |
| Todistenastetta | L2 |
| Taiwanin markkinoille-asema | Ei markkinoilla |
| Lupien määrä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennustus on kohtuullinen?

Todistusaineistossa `original_moa`-kenttä on merkitty tietoaukoksi, ja tällä hetkellä ei ole virallisia mekanismin tietoja. Todistusaineiston mukana olevat julkaisut tarjoavat kuitenkin mekanismin vihjeitä: useat julkaisut kuvaavat vandetanibbia suullisena usean tyrosiinikinaasin estäjänä, joka estää VEGFR2/3-, EGFR- ja RET-kinaasin aktiivisuutta (PMID [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/), [15886878](https://pubmed.ncbi.nlm.nih.gov/15886878/), [30860683](https://pubmed.ncbi.nlm.nih.gov/30860683/)). Sen tehokkuus märekilpirauhasisyövässä perustuu RET:n konstitutiivisen aktivaation estämiseen.

Munuaissolakarkino (erityisesti kirkassoluinen RCC ja VHL-tautiin liittyvät munuaistuumorit) johtuu pääasiassa VHL-HIF-VEGF-reitin vioittumisesta, mikä aiheuttaa kasvainten angiogeneesin olevan erittäin riippuvainen VEGFR-signaloinnista. Tämä on suoraan yhteydessä vandetanibbin VEGFR2/3-estävään vaikutukseen, ja se on myös tällä hetkellä hyväksyttyjen ccRCC-kohdekäyttöjen (sunitinib, pazopanib, aksitinib) yhteinen toimintamekanismi (class effect).

Siksi vandetanibbin käyttö yleisessä hajanaisessa ccRCC:ssä tai VHL-liittyneissä munuaistuumoreissa on mekanistisesti kohtuullista; kuitenkin ykkössijoitus "renal cell carcinoma (disease)" on laajempi tautiluokitus, jonka alla samassa ennuste-sarjassa ovat myös Xp11.2/TFE3-fuusio-tyyppi, neuroblastoomaan liittyvät tuumorit, luokittamattomat tuumorit ja muut harvinaiset alatyyppit (rank 2–4, 7, 9, 10). Näiden alatyyppien ajavat mekanismit eivät ole VEGFR/RET-reitit, ja todistusaineisto itse merkitsee näiden mekanismien olevan "päättelyperäisiä", todistenastetta ollessa vain L5. Näin ollen ennusteen mekanismin kohtuullisuus keskittyy pääasiassa ccRCC/VHL-liittyneisiin väestöihin eikä kata kaikkia RCC-alatyypejä.

---

## Kliinisten tutkimusten todisteet

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Vaihe 2 | Valmistunut | 37 | Vandetanibbin arviointi VHL-tautiin liittyneissä munuaistuumoreissa, ainoa tällä hetkellä valmistunut suora näyttö, todistusaineiston arvio Grade A |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Vaihe 1/2 | Pysäytetty ennenaikaisesti | 7 | Vandetanib + metformiini HLRCC/SDH-liittyneissä munuaiskarsinoomissa tai hajanaisissa papillaalisissa RCC-tapauksissa; pysäytetty ennenaikaisesti, todistusaineiston arvio Grade B |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Vaihe 2 | Pysäytetty ennenaikaisesti | 3 | Vandetanib yksinään edistyneessä kirkassoluisessa munuaissyövässä; vain 3 potilasta osallistui ennen pysäytystä, tilastollinen teho erittäin heikko, todistusaineiston arvio Grade C |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Vaihe 2 | Valmistunut | 82 | Satunnaistettu tutkimus arvioitaessa carboplatin+gemcitabine ± vandetanib-yhdistelmää cisplatinille soveltumattomissa edistyneissä virtsateiden epiteelikasvaimissa; **todistusaineisto on vahvistanut, että tämän tutkimuksen väestö oli virtsateiden epiteelikarkino eikä RCC, mikä on tiedon virheellinen assosiaatio**, eikä sitä pitäisi käyttää suorana RCC:n todistuksena, todistusaineiston arvio Grade C |

---

## Julkaisutodisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Katsaus | Clinical Cancer Research | SDH-puuttuvaiset tuumorit (sisältäen HLRCC-liittyvät RCC-tapaukset) osoittavat vastustusta solunsalpaamisen kemoterapialle ja useimmille kohdekäyttöjen hoitoille |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Katsaus | Clinical & Experimental Metastasis | Fumaaraasin hydrataasin puuttuva RCC (FHdRCC) on WHO 2022 uusi luokitus, jolle ei ole vakiintunut hoitosuunnitelma, ja useita kohdekäyttöjen yhdistelmähoidon vaihe 2 -tutkimuksia on käynnissä |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Katsaus | Bulletin du Cancer | Selitys samankaltaisten monien kinaasin estäjien (cabozantinib) VEGFR2/c-MET/RET-mekanismeista ja niiden assosiaatioista munuaiskasvainten ja kilpirauhasisyövän tehokkuuksiin |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Katsaus/Prekliininen | Molecular Cancer Research | TFE3-RCC:n hiirimallit, tunnistettiin uudet hoitokohdat ja diagnostiset biomarkerit, ei-VEGFR-ajamat alatyypat |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Luokittamaton | OncoTargets and Therapy | Antiangiogeneesin lääkkeiden (sisältäen vandetanibbin) soveltamisen katsaus useisiin kiinteisiin kasvaimiin |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Luokittamaton | ASCO Educational Book | Vandetanibbin suullinen RET-kinaasin estäjä, FDA-hyväksytty metastaattisen märekilpirauhasisyövän hoitoon |

---

## Taiwanin markkinoille-asema

Taiwanin lääkepolitiikan tietojen mukaan tämä lääke **ei ole tällä hetkellä saanut lääkelupia** (`total_licenses = 0`), eikä lupien yksityiskohtia voida näyttää.

---

## Sytotoksisuustiedot (soveltuu vain kasvaintenvastaislääkkeisiin)

Vandetanibbin alkuperäinen käyttöindikaatio (märekilpirauhasisyöpä) ja ennustettu uusi käyttöindikaatio (munuaissolakarkino) ovat molemmat pahanlaatuisia kasvaimia, ja ne kuuluvat tyrosiinikinaasin estäjäluokkaan (TKI), joten tämä osio on merkitty.

| Kohta | Sisältö |
|------|--------|
| Sytotoksisuusluokitus | Kohdehoidot (Targeted therapy) — usean tyrosiinikinaasin estäjät (VEGFR2/3, EGFR, RET) |
| Luuytimen tukahduttamisriskit | Todistusaineistossa ei ole suoraa luuytimen tukahduttamisen tietoja; samankaltaisten VEGFR-TKI-lääkkeiden luuytimen tukahduttaminen on yleensä pienempi kuin perinteisen sytotoksisen kemoterapian (katso PMID [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) VEGFR-TKI kuolemaan johtavien haittatapahtumat sisältävä meta-analyysi) |
| Muut tunnetut myrkyllisyyskysymykset | Kirjallisuus raportoi VEGFR-TKI-lääkkeiden hepatotoksisuudesta (PMID [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/)), proteinuriasta (PMID [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/)); lisäksi kirjallisuudessa on otsikko "Vandetanib: too dangerous in medullary thyroid cancer" (PMID [23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/)), joka antaa suoraa varoitusta turvallisuushuolista, joiden ansaitsee huomion |
| Emetisyyden luokitus | Katso lääkkeen pakkaukselle kirjoitettu tieto saadaksesi täydellisen tiedon |
| Valvontakohteita | Maksatoiminnan arviointi, munuaisten toiminta/virtsassa olevan proteiinin määrä, täydellinen verisolujen lasku (CBC) |
| Käsittely- ja suojausvaatimukset | Noudata sytotoksisten lääkkeiden käsittelyä koskevia säännöksiä |

---

## Turvallisuushuolella

Todistusaineiston keskeisimpiä varoituksia (`key_warnings`), kieltojen (`contraindications`) ja lääkkeiden välisten vuorovaikutusten (`drug_interactions`) kentät ovat kaikki tietoaukkoja.

> Katso lääkkeen pakkaukselle kirjoitettu tieto saadaksesi täydellisen turvallisuustiedon.

Lisätieto: Todistusaineistoon sisältyneissä julkaisuissa on yksi, jonka otsikko on "Vandetanib: too dangerous in medullary thyroid cancer" (PMID [23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/)), mikä osoittaa, että olemassa olevassa kirjallisuudessa on jo huolia tämän lääkkeen turvallisuudesta. On suositeltavaa, että järjestelmällisessä turvallisuuden arvioinnissa nämä asiat tarkistetaan ensisijaisesti.

---

## Johtopäätökset ja jatkotoimenpiteet

**Päätös: Pidä**

**Perustelut:**
- Ainoa valmistunut ja suoraan asiaan liittyvä vaihe 2 -tutkimus (NCT00566995, n=37) kattaa vain VHL-tautiin liittyvät munuaistuumorit, ei yleisiä hajanaisesti esiintyviä munuaissolakarkimoja; muut tutkimukset pysäytettiin ennenaikaisesti ja näytteiden koko oli äärimmäisen pieni (n=3, n=7), tai todistusaineisto on jo merkinnyt nämä virheellisiksi tietoyhdistyksiksi (NCT01191892 oli todella virtsateiden epiteelikarkino).
- Fimean pakkaukselle kirjoitetun tiedon varoitukset/kiellot-kohta on esto-tason aukko (DG001), säännösten mukaisesti ei voida jatkaa S1-turvallisuuseulontaan; toimintamekanismin tiedot ovat myös korkea-tason aukko (DG002), mikä vaikuttaa mekanismin assosiaation määritelmän varmuusasteeseen.

**Edellytettävät lisätiedot jatkaakseen:**
- Hanki TFDA:n (tai alkuperäisen valmistajan) pakkaukselle kirjoitetun tiedon täydelliset varoitukset, kiellot ja lääkkeiden väliset vuorovaikutukset (DDI), poista DG001 esto
- Hanki viralliset DrugBank/pakkaukselle kirjoitetun tiedon lähteellä olevat toimintamekanismin tiedot, poista DG002
- Selvitä, voiko NCT00566995:n VHL-alaväestön tulokset ulottaa yleisen hajanaisesti esiintyvän ccRCC-väestön suhteen
- Poista NCT01191892 virtsateiden epiteelikarsinoman tiedon virheellisen yhdistyksen virhe ja arvioi uudelleen, ovatko suorat todisteet edelleen L2-tasolla

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

