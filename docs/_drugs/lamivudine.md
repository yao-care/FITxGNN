---
layout: default
title: Lamivudine
parent: Pelkkä mallin ennuste (L5)
nav_order: 211
evidence_level: L5
indication_count: 5
---

# Lamivudine
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

# Lamivudiini: TxGNN-monien indikaatioiden seulonta — Ei löydetty toimeenpantavaa uudelleenkäyttökandidaattia

## Yhden lauseen yhteenveto

Lamivudiini (Lamivudine, DB00709) on vakiintunut nukleosidi-käänteisen transkriptaasin inhibiittori (NRTI), jota käytetään HIV-1:tä ja kroonista hepatiitti B:tä vastaan; Evidence Pack ei sisällä sen alkuperäisen indikaation tekstiä tiedon puutteen vuoksi. TxGNN palautti **5 parhaiten sijoittunutta ennustettua indikaatiota** (pistemäärä ≈ 99,1–99,9%), mutta todisteiden perusteella **yksikään ei täytä toimeenpantavan ihmisten uudelleenkäyttökandidaatin kriteerejä** — paras signaali on eläinlääkinnöllinen sairaus (kissat), toinen on vain eläinmalleista johdettu sairaus (ihmisiin kuulumattomat primaatit), ja loput kolme ovat riittämättömiä tai virheellisesti sovitettuja todisteiden kannalta. Kaikki viisi kandidaattia saavat **Pidä**-suosituksen.

---

## Nopea yleiskatsaus

*(Alla olevat arvot heijastavat parhaiten sijoittunutta kandidaattia (predicted_indications[0]); katso "Kaikki ennustetut indikaatiot" täydellisen joukon osalta.)*

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — tiedostossa ei ole Taiwanin lupaa (`total_licenses = 0`); Lamivudiini tunnetaan laajalti antiretroviraaleista HIV-1-infektioita ja kroonista hepatiitti B:tä vastaan, mutta tämä on yleinen tausta, ei Evidence Pack -dataa |
| Ennustettu uusi indikaatio (Sijoitus 1) | Kissojen hankkittu immuunivajaavuussyndrooma (kissan FIV) — **ei ihmisten indikaatio** |
| TxGNN:n ennusteen pistemäärä | 99,93% |
| Todisteiden taso | L4 (Evidence Pack -pisteytyksessä; kirjallisuus on eläinlääkinnöllinen kohortti/prekliininen, ei ihmisten) |
| Taiwanin markkinoinnin tila | Ei markkinoitu (Ei markkinoitu) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidä** |

### Kaikki ennustetut indikaatiot (Sijoituksen mukaan)

| Sijoitus | Sairaus | TxGNN-pistemäärä | Todisteiden taso | Suositus | Pääkysymys |
|------|---------|------------|-----------------|-----------|-----------|
| 1 | Kissojen hankkittu immuunivajaavuussyndrooma | 99,93% | L4 | Pidä | Eläinlääkinnöllinen sairaus (kissat); liitetyt kliiniset tutkimukset ovat ihmisten HIV/dolutegravir-tutkimuksia, eivät liity FIV:ään (relevanssiluokitus C) |
| 2 | Simiaanisen immuunivajaavuusviruksen infektio | 99,93% | L5 | Pidä | Vain ihmisiin kuulumattomien primaattien malli; ei kliinisiä tutkimuksia; 20 kirjallisuusviitettä ovat kaikki eläin-/mekanistisia tutkimuksia |
| 3 | Neurokehi­tyk­sel­li­nen häiriö ataksisella kävelyllä, puheentuotannon puutteella ja vähentyneellä aivokuoren valkoaineen määrällä | 99,93% | L5 | Pidä | Nolla kliinisiä tutkimuksia tai kirjallisuutta; ei tunnettua mekanistista yhteyttä NRTI:hen |
| 4 | Vanhentunut familiaalisesti yhdistetty hyperlipidemie | 99,63% | L5 | Pidä | Sairaustermi merkitty "vanhentuneeksi" ontologiassa; ei mekanistista perustelua (antiretroviraali vs. lipidimetabolismi); ei todistetta |
| 5 | Krooninen hepatiitti C -viruksen infektio | 99,11% | L4 | Pidä | Todennäköinen ontologian vääritys — kaikki 16 liitettyä tutkimusta ja suurin osa kirjallisuudesta käsittelevät kroonista **hepatiitti B:tä**, ei HCV:tä; Lamivodiinilla ei ole tunnettua aktiviteettiä HCV:n RNA-riippuvaiselle RNA-polymeraasille |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismi-tietoja ei ole saatavilla (DrugBank MOA -kenttä: Tiedon puute). Tunnettujen tietojen perusteella Lamivudiini on sytidinukleosidi-analogi (NRTI), joka solun sisäisen fosforylaation jälkeen estää retroviraali-käänteisen transkriptaasin. Sen teho HIV-1:tä ja hepatiitti B -virusta vastaan (molemmat riippuvat käänteisestä transkriptiosta) on hyvin vakiintunut ihmisillä.

**Sijoitukselle 1 (kissojen FIV)** ja **Sijoitukselle 2 (simiaanien SIV)**, mekanistinen logiikka on aito biologian tasolla — FIV ja SIV ovat lentiviruksia, jotka liittyvät läheisesti HIV:iin, ja käänteisen transkriptaasin estäminen on jaettu haavoittuvuus (M184V-resistenssi-mutaatio, joka raportoitu SIV-malleissa, peilaa samaa mutaatiota, joka nähdään HIV-1:ssä lamivudiini-terapian alaisina, kirjallisuuden todisteen mukaan). Kuitenkin nämä ovat **eläinlääkinnöllisiä ja ihmisiin kuulumattomien primaattien sairauksien malleja**, eivät ihmisten indikaatioita, joten ne eivät ole kelvollisia kohteita ihmisten lääkkeiden uudelleenkäyttöputkelle riippumatta mekanistisesta uskottavuudesta.

**Sijoitukselle 5 (krooninen HCV)**, mekanistinen perustelu *ei* ole: HCV on *Flaviviridae*-RNA-virus, joka monistuu NS5B-RNA-riippuvaisen RNA-polymeraasin kautta, ei käänteisen transkription kautta, joten Lamivodiinilla ei ole tunnettua antiviraalista aktiviteettiä sitä vastaan. Kriittisesti, olennaisesti kaikki tähän kandidaattiin liitetyt kliinisen tutkimuksen ja kirjallisuuden todisteet koskevat itse asiassa **kroonista hepatiitti B:tä** (entecavir/adefovir/tenofovir/peginterferoni vs. lamivudiini-tutkimuksia), mikä viittaa sairausontologian merkintävirheeseen taustalla olevassa ennusteessa sen sijaan, että olisi aito HCV-signaali. Sijoituksilla 3 ja 4 ei ole minkäänlaisia tukevia todisteia, ja Sijoituksella 4 viitattaessa ontologiatermiin, joka on nimenomaisesti merkitty "vanhentuneeksi".

---

## Kliinisen tutkimuksen todisteet

*(Poimittu predicted_indications[0]:sta — kissojen FIV. Kaikki 5 tutkimusta ovat ihmisten HIV-tutkimuksia dolutegravir/abacavir/lamivudiini-säännöillä ja on arvosteltu "C"-relevanssilla — eli eivät itse asiassa koske ennustettua indikaatiota.)*

| Tutkimuksen numero | Vaihe | Tila | Osallistujien määrä | Keskeisiä löydöksiä |
|---------|------|------|------|---------|
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Vaihe 3 | Valmis | 13 | Dolutegravir + abacavir/lamivudiini CNS/plasman PK-tutkimus ART-naiiville HIV-1-potilaille — ihmisten tutkimus, ei liity FIV:ään |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Vaihe 3 | Valmis | 844 | Dolutegravir + abacavir/lamivudiini vs. Atripla ART-naiiville HIV-1-potilaille — ihmisten tutkimus, ei liity FIV:ään |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Vaihe 2 | Valmis | 208 | Dolutegravir-annoksen valinta abacavir/lamivudiini- tai tenofovir/emtricitabiini-kanssa HIV-1-potilailla — ihmisten tutkimus, ei liity FIV:ään |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Vaihe 4 | Valmis | 145 | Darunavir + lamivudiini vs. darunavir + emtricitabiini/tenofovir tai lamivudiini/tenofovir HIV-1-potilailla — ihmisten tutkimus, ei liity FIV:ään |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Vaihe 3 | Valmis | 828 | Dolutegravir vs. raltegravir, molemmat kaksinkertaisella NRTI-selkärankaisella, HIV-1-potilailla — ihmisten tutkimus, ei liity FIV:ään |

**Huomautus:** Lamivodiinin kliinisiä tutkimuksia ei ole olemassa missään 5:stä ennustetusta indikaatiosta sellaisena kuin ne on todellisuudessa määritelty (FIV, SIV, neurokehi­tyk­sel­li­nen häiriö tai vanhentunut hyperlipidemie). Sijoitukselle 5 liitetyt 16 tutkimusta (krooninen HCV) ovat myös virheellisiä — ne ovat kroonisen hepatiitti B:n tutkimuksia — ja jätetään tässä pois välttämään asiattomien tietojen toistamisen.

---

## Kirjallisuuden todisteet

*(Poimittu predicted_indications[0]:sta — kissojen FIV; nämä ovat ainoat kirjallisuusviitteet, jotka ovat suoraan aiheellisia niiden ilmoitettujen indikaatioiden osalta.)*

| PMID | Vuosi | Tyyppi | Lehti | Keskeisiä löydöksiä |
|------|-----|------|------|---------|
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Kohortti | Veterinary Immunology and Immunopathology | AZT/3TC-yhdistelmä osoitti additiivisia-synergistisiä anti-FIV-aktivititeetteja primaarisissa PBMCs:issa, mutta tehokkuus väheni kroonisesti infektoituneissa soluissa |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Kohortti | Journal of Feline Medicine and Surgery | Pitkäaikaista antiretroviraali-terapiaa (AZT-pohjainen) arvioitiin FIV-infektoituneissa kissoissa 5–6 vuoden aikana |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Kohortti | Viruses | ZDV+3TC vs. muita säännöksiä verrattiin luonnollisesti FIV-infektoituneissa kissoissa; virusikuormaa ja CD4+/CD8+-suhteita seurattiin yhden vuoden ajan |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Kohortti | Antiviral Research | ZDV+3TC+ABC-yhdistelmä esti FIV-monistumisen in vitro; FIV ehdotettiin HIV-eläinmalliksi |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro/Prekliininen | American Journal of Veterinary Research | Karakterisoitu 3TC-resistentti FIV-pol-geeni-mutantit in vitro |

**Huomautus:** Kaikki 5 kohetta ovat eläinlääkinnöllisiä (kissojen) tutkimuksia — yksikään ei ole ihmisten kliinisiä todisteia. Sijoitukselle 2 (SIV, 20 kohdetta) ja lisäkohdille sijoitukselle 5 (HCV/HBV-väärityyppi, 20 kohdetta) on olemassa kirjallisuusviitteitä Evidence Packissa, mutta ne ovat eläinmalleja tai väärä-sairaus-tutkimuksia eivätkä ole tässä jäljennettyjä välttämään näiden kuvittelun tukevan ihmisten indikaatiota.

---

## Taiwanin markkinatiedot

Lamivudiini ei tällä hetkellä ole markkinoitu Taiwanissa (`market_status: Not marketed`), ja tiedostossa on **0 hyväksyntää**. Lupamerkinnöistä ei ole saatavilla yhteenveto.

---

## Turvallisuusnäkökohdat

Katso pakkausseloste turvallisuustiedoista. (Keskeisiä varoituksia, vasta-aiheita ja lääkkeiden välisiä vuorovaikutuksia koskevat tiedot ovat kaikki merkitty tiedon puutteeksi tässä Evidence Packissa — TFDA-pakkauselosteenhaku on merkitty **Estäväksi** tiedon puutteeksi, DG001.)

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Yksikään viidestä TxGNN:n ennustamasta indikaatiosta ei ole tällä hetkellä toimeenpantava ihmisten lääkkeiden uudelleenkäyttöön: Sijoitus 1 ja Sijoitus 2 ovat ihmisiin kuulumattomien sairauksien malleja (kissojen FIV, simiaanien SIV), joissa on vain eläintodisteet; Sijoituksilla 3 ja 4 ei ole minkäänlaisia tukevia todisteia (Sijoituksen 4 sairaustermi on jopa merkitty ontologisesti vanhentuneeksi); ja Sijoitus 5 (krooninen hepatiitti C) on hyvin todennäköisesti sairausontologian väärityyppi, koska sen kliinisen tutkimuksen ja kirjallisuuden todisteet käsittelevät ylivoimaisesti kroonista hepatiitti B:tä, NRTI:lle mekanistisesti uskottava indikaatio, sen sijaan, että olisivat HCV.

**Jotta voidaan edetä, seuraavaa tarvitaan:**
- TFDA-pakkauselosteenhaku (DG001, Estävä) perusturvallisuusprofiilin vahvistamiseksi ennen S1-arviointia
- DrugBank MOA/kategoria-data (DG002) mekanistisen uskottavuuden asianmukaiseen arviointiin
- Sijoituksen 5 sairauden ontologiakartituksen vahvistaminen/korjaaminen — jos aiottu kohde on krooninen hepatiitti B sen sijaan, että olisivat hepatiitti C, kyseisen kandidaatin pitäisi ohjata uudelleen ja uudelleenarvioida erilliseksi, todistepitoisaksi signaaliksi
- Ennustetun indikaation joukon uudelleenkäyttöönotto, jotta voidaan sulkea pois ihmisiin kuulumattomat sairaustermit (FIV, SIV) ihmisten uudelleenkäyttöputkesta mallinnuksessa/suodatusvaiheessa
- Ei muuta toimintaa suositeltu Sijoituksille 3 ja 4, koska tukevien todisteiden täydellinen puute

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

