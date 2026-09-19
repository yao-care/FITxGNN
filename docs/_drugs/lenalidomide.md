---
layout: default
title: Lenalidomide
parent: Pelkkä mallin ennuste (L5)
nav_order: 223
evidence_level: L5
indication_count: 6
---

# Lenalidomide
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

# Lenalidomidi: Multippelista myeloomasta / MDS with del(5q) -taudista myeloidileukemiaan

## Yksirivinen yhteenveto

Lenalidomidi on thalidomidista johdettu immunomodulatoryinen lääke (IMiD), jonka käyttö on vakiintunutta multippelin myelooman ja transfuusio-riippuvaisen myelodysplastisen oireyhtymän (MDS with isolated del(5q)) hoidossa. TxGNN-malli ennustaa, että se voi olla tehokas myös **myeloidileukemiassa** (AML/korkeamman riskin MDS-spektri), ja sen puolesta on tällä hetkellä saatavilla **50 kliinistä tutkimusta** ja **20 julkaisua**, vaikka näyttöjen laatu on sekalaista (monet tutkimukset päättyneet tai tuntemattomassa tilassa).

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Multippeli myelooma; MDS with del(5q) (perustuu vakiintuneen lääketiedon perusteella — ei sisälly tähän näyttöpakettiin, katso Data Gap DG002) |
| Ennustettu uusi indikaatio | Myeloidileukemia |
| TxGNN-ennustepisteet | 99.49% (sijaluku 5525) |
| Näyttöjen taso | L2 (1 valmistunut Vaihe 2 -satunnaistettu tutkimus tunnistettu; ei valmiintunut Vaihe 3 -satunnaistettu tutkimus) |
| Taiwanin markkinointi status | Ei markkinoitu (Not marketed) |
| Lupien määrä | 0 |
| Suositeltu päätös | Pidä |

## Miksi tämä ennuste on kohtuullinen?

Yksityiskohtaiset vaikutusmekanismin tiedot eivät tällä hetkellä ole saatavilla tässä näyttöpaketissa (merkitty Data Gap DG002, korkea vakavuus). Vakiintuneen farmakologisen tiedon perusteella lenalidomidi on toisessa sukupolvessa oleva IMiD (immunomodulatoryinen imidi-lääke), joka on johdettu thalidomidista. Se toimii cereblon (CRBN) -välitteisen transkripsio tekijöiden IKZF1/IKZF3 ubikitinaation ja hajoamisen kautta, mikä tuottaa sekä suoraa sytotoksista/anti-proliferatiivista vaikutusta pahanlaatuisiin klooneihin että immuunia vahvistavia vaikutuksia (parantuneet T-solujen ja NK-solujen aktiviteetti). Se on jo vakiintuneet multippelin myelooman ja punasolujen transfuusioon riippuvaisen MDS:n hoidossa, joka liittyy del(5q) -karyo-tyyppi poikkeavuuteen.

MDS ja AML ovat biologisessa jatkumossa — MDS on pre-leukeminen klonaalinen kantasolujen häiriö, joka usein muuntuu AML:ksi, ja korkeamman riskin MDS/CMML/AML tutkitaan usein samoissa tutkimusohjelmissa. Tämä heijastuu näyttöpaketissa: suurin osa 50 haetusta tutkimuksesta ja useista katsausartikkeleista (esim. PMID 37288607, PMID 24656536) käsittelevät MDS:ää, AML:aa ja CMML:aa jaetuina tautispektrina, ja käyttävät usein lenalidomiidia yhdessä hypometylointiaineiden (asatsitidin) tai tavanomaisen kemoterapian (sytorabiini, idarubisini, mitoksantroni) kanssa.

Mekanistisesti lenalidomiidin anti-klonaalinen ja immuunia vahvistava aktiivisuus del(5q) MDS:ssä voidaan perustellusti laajentaa laajemmille myeloidihäiriöille, erityisesti AML/MDS:lle, joilla on kromosomin 5 poikkeavuuksia tai monosomia 5, joka on yhtenäisin tehokkuussignaali kerätyissä tutkimuksissa. Tulokset ei-del(5q) AML/MDS-populaatioissa ovat kuitenkin heterogeenisempia, monissa Vaihe 1/2 -tutkimuksissa lopetettiin ennenaikaisesti (usein myrkyllisyyden, hitaan rekrytoinnin tai tehokkuuden puuttumisen vuoksi pikemminkin kuin vahvistetun hyödyn vuoksi), ja mikään valmistunut satunnaistettu Vaihe 3 -tutkimus ei vahvista tehokkuutta erityisesti "myeloidileukemia" itsenäisenä indikaationa.

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät tulokset |
|---------|------|------|------|---------|
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Vaihe 3 | Aktiivinen, ei rekrytoida | 247 | Satunnaistettu tutkimus lenalidomidista yksin vs. + epoetin alfa suuressa punasolujen vasteessa matalan-/väli-1-riskin MDS:ssä oireellisen anemia kanssa |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Vaihe 2 | Valmistunut | 120 | Satunnaistettu, monikeeskuksinen ylläpitohoito vuorotellen lenalidomidi ja asatsitidin syklit iäkkäissä AML-potilaissa ensimmäisen täydellisen remission aikana |
| [NCT00065156](https://clinicaltrials.gov/study/NCT00065156) | Vaihe 2 | Valmistunut | 148 | Keskeinen yhden haaran tutkimus lenalidomidi monoterapiasta punasolujen transfuusioon riippuvaisessa del(5q) MDS:ssä (alkuperäisen sääntelyvaatimuksen hyväksynnän perusta) |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Vaihe 2/3 | Aktiivinen, ei rekrytoida | 282 | Satunnaistettu tutkimus: asatsitidin ± lenalidomidi vs. asatsitidin + vorinostat korkeamman riskin MDS/CMML:ssä |
| [NCT02472691](https://clinicaltrials.gov/study/NCT02472691) | Vaihe 2 | Valmistunut | 50 | Lenalidomidi lisätty asatsitidiiniin + luovuttajan lymfosyytien infuusioon MDS/CMML/AML uusiutumiseen allo-siirron jälkeen |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Vaihe 2 | Valmistunut | 29 | Lenalidomidi ylläpitohoito korkean riskin AML-potilaissa remissiossa |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Vaihe 2 | Valmistunut | 48 | Lenalidomidi turvallisuus/tehokkuus hoitamattomassa AML:ssä (≥60v) ilman 5q-poikkeavuuksia |
| [NCT02538965](https://clinicaltrials.gov/study/NCT02538965) | Vaihe 2 | Valmistunut | 17 | Lenalidomidi aktiivisuus/turvallisuus/PK pediatrisessa uusiutuneessa/hoitoresistentissä AML:ssä |
| [NCT02921802](https://clinicaltrials.gov/study/NCT02921802) | N/A (jälkimarkkinoinnin valvonta) | Valmistunut | 4,626 | Laaja kaikkien tapausten valvonta Revlimid 5 mg -kapseleista todellisen maailman turvallisuus/tehokkuus |
| [NCT01016600](https://clinicaltrials.gov/study/NCT01016600) | Vaihe 1/2 | Valmistunut | 31 | Asatsitidin + lenalidomidi myrkyllisyys ja remission nopeus AML:ssä |

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät tulokset |
|------|-----|------|------|---------|
| [30653424](https://pubmed.ncbi.nlm.nih.gov/30653424/) | 2019 | Prospektiivinen kliininen tutkimus (JCO) | J Clin Oncol | Lenalidomidi + asatsitidin yhdistelmä pelastushoitona AML/MDS uusiutumiseen allo-siirron jälkeen |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Järjestelmällinen katsaus & meta-analyysi | Hematology (Amsterdam) | Asatsitidin + lenalidomidi tehokkuus ja haittavaikutukset AML:ssä, MDS:ssä ja CMML:ssä |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospektiivinen kliininen tutkimus (Azalena) | Haematologica | Asatsitidin + lenalidomidi + DLI uusiutuneeseen MDS/AML/CMML allogeneettisen siirron jälkeen |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Katsaus | American Journal of Hematology | 2023 päivitys MDS:n diagnoosiin, riskistratifikaatioon ja hoitoon |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Katsaus | Blood | Kliinisen päätöksenteon ja hoitosuunnitelman kehys MDS:ssä |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Katsaus | Lancet | MDS:n patofysiologian, kliinisen kulun ja etenemisen yleiskatsaus AML:ksi |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Katsaus/Pääkirjoitus | Leukemia | Perustelut asatsitidiinin ja lenalidomiidin yhdistämiselle MDS/AML:ssä |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Katsaus | Expert Opin Investig Drugs | Lenalidomidi uutena hoitolähestymistapana AML:ssä |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Vaihe Ib -kliininen tutkimus | J Geriatr Oncol | Lenalidomiidin turvallisuus jälkiremission hoitona vanhemmissa AML-potilaissa |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Mekanismin tutkimus | Cell Mol Biol Lett | KDM5C lisää AML:n herkkyyttä lenalidomidille stabiloimalla cereblonia (CRBN) |

## Taiwanin markkinatieto

Lenalidomidilla ei tällä hetkellä ole markkinointiluvan merkintää tässä näyttöpaketissa — markkinointi status on "Ei markkinoitu" (Not marketed), ja rekisterissä ei ole lupaa. Lupanumero, tuotteiden nimi, annostemuoto tai hyväksytyn indikaation teksti eivät ole saatavilla taulukkoon.

## Sytotoksisuus

Lenalidomiidin alkuperäiset hyväksytyt indikaatiot (multippeli myelooma; MDS/leukemia-spektrin häiriöt) täyttävät antineoplastisen kriteerin, joten tämä osio pätee. Huomio: DrugBank:n myrkyllisyystietoja tai TFDA:n pakkausselosteita ei ole saatavilla tässä näyttöpaketissa (Data Gap DG001, estävä; DG002, korkea) — seuraavat tiedot heijastavat vakiintunutta farmakologista tietoa, ei pakettiperäisiä tietoja, ja ne on vahvistettava vastaan todellista pakkausselostetta, kun se on saatu.

| Kohde | Sisältö |
|------|---------|
| Sytotoksisuuden luokitus | Kohdistettu/immunomodulatoryinen hoito (IMiD; cereblon-välitteinen — ei tavanomainen sytostaattinen kemoterapialääke) |
| Ydinaineiston tukahduttamisriski | Korkea — neutropenia ja trombosytopenia ovat vakiintuneet annoksen rajoittavat myrkyllisyydet, jotka vaativat annoksen muuttamista |
| Pahoinvointisuuden luokitus | Matala (tyypillistä IMiD:lle, vastoin tavanomaista sytostaattista kemoterapiaa) |
| Valvonnan kohdat | Täydellinen verenkuva differentiaalin kanssa (viikoittain varhaisten syklien aikana), munuaisten toiminta (annoksen säätö vaaditaan — munuaisissa erittyvä), VTE-riskin arviointi, raskauden testaus teratogenisuuden vuoksi |
| Käsittelyn suojaus | Kyllä — lenalidomidi on teratogeeninen (thalidomidi-analogi); käsittely ja toimitus vaativat valvotun jakelun/REMS-vastaavia turvatoimia tavanomaisten sytostaattisen käsittelyn varotoimien lisäksi |

## Turvallisuuden huomioitavat seikat

Katso pakkausselostetta turvallisuustiedoista. Tärkeimmät varoitukset, vasta-aiheet tai lääkkeen vuorovaikutustiedot eivät ole saatavilla tässä näyttöpaketissa — TFDA-pakkausseloste kysely (DG001) on merkitty **estäväksi** tietoaukoksi, joka on ratkaistava ennen turvallisuuden alkuarvioinnin (S1) suorittamista.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Vaikka TxGNN antaa korkean ennustepisteet (99.49%) ja huomattava määrä tutkimusta (50) ja kirjallisuutta (20) on saatavilla, tutkimusnäyttö on heterogeeninen — monet tutkimukset ovat Vaihe 1, lopetettu tai tuntemattomasta tilasta, eikä mikään valmistunut satunnaistettu Vaihe 3 -tutkimus vahvista tehokkuutta erityisesti myeloidileukemiaa varten. Kriittiset turvallisuuden tietoaukko (DG001, estävä) estää jopa alkuarvioinnin (S1) suorittamisen, joten vastuullisesti Go tai Guardrails -päätöstä ei voida tehdä tällä hetkellä.

**Jatkamista varten tarvitaan seuraavaa:**
- TFDA:n pakkausseloste (varoitukset, vasta-aiheet) — ratkaise estävä tietoaukko DG001
- Varmennettu vaikutusmekanismin tieto — ratkaise korkea-prioriteettinen tietoaukko DG002
- Alkuperäisten hyväksyttyjen indikaatioiden ja lupien tilan vahvistaminen (original_indications -kenttä on tällä hetkellä tyhjä)
- Käsitteinen tutkimuksen relevanssiluokittelun tarkistaminen (suurin osa tutkimuksista/kirjallisuudesta on edelleen merkitty "vireillä" relevanssiluokittelulla näyttöpaketissa) del(5q)-spesifisen signaalin erottamiseksi yleisestä AML/MDS-käytöstä
- Lääkkeen vuorovaikutus (DDI) tieto, tällä hetkellä ei hankittu ("not_found")

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

