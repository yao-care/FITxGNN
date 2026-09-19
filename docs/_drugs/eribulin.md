---
layout: default
title: Eribulin
parent: Pelkkä mallin ennuste (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribuliini: Rintasyövästa ja liposarkoomatosta solitaariseen fibroosikasvaimeen

## Yhden lauseen yhteenveto

Eribuliini (DB08871) on kansainvälisesti hyväksytty etäpesäkkeisenä rintasyöpään ja leikkauskelvottomaan liposarkoomataan kohdistuva mikrotubuliiestäjä, mutta Suomessa sillä ei ole yhtään lupahyväksyntää (0 lupaa). TxGNN ennustaa tälle lääkeaineelle yhteensä 10 uutta indikaatiota, joista vahvimman näytön mukainen ehdokas on **Fibroblastic Neoplasm (solitaarinen fibroosikasvain / Solitary Fibrous Tumor)**, jota tukee **1 valmis Phase II -kliininen tutkimus** ja **8 julkaisua**; muut ehdokkaat ovat pääosin mallin ainoita ennusteita (L5), ja korkeimman pistemäärän saanut familiaaliset Välimeren kuume (FMF) on jopa merkitty näytöpaktin itsensä puolesta epäuskottavaksi väärän positiivisen tuloksen vuoksi.

---

## Nopea yhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Suomessa ei löytynyt hyväksyttyjä indikaatioita (Not marketed); kansainvälisesti tunnetut hyväksytyt indikaatiot ovat metastasoitunut rintasyöpä ja leikkauskelvotonta liposarkooma |
| Ennustettu uusi indikaatio (vahvin näyttö) | Fibroblastic Neoplasm (solitaarinen fibroosikasvain, Solitary Fibrous Tumor) |
| TxGNN-ennustepisteet | 99.36% (sijainti 8 / kaikista mallin 6 643 ehdokkaasta) |
| Näyttötaso | L3 (1 valmis satunnaisoimaton Phase II -kliininen tutkimus + useita prekliinisiä / katsauspublikaatioita) |
| Suomen markkinatila | Not marketed |
| Lupahyväksyntöjen määrä | 0 |
| Suositeltu päätös | Hold |

> Huomio: Mallin korkeimman pistemäärän saanut ehdokas on autosomaalisesti resessiivinen familiaali Välimeren kuume (99.82%), mutta näyttöpaketti on jo merkinnyt sen "mekanismiltään epäuskottavaksi väärän positiivisen tuloksen" vuoksi, joten se ei ole tämän raportin pääkohde. Yksityiskohdat löytyvät monista indikaatioista seuraavan taulukon alta.

---

## Monien indikaatioiden ennusteiden yleiskatsaus

| Sijainti | Ennustettu indikaatio | TxGNN-pisteet | Kliniset tutkimukset | Julkaisut | Näyttötaso | Tulkinta |
|------|-----------|-------------|---------|------|---------|------|
| 1 | Autosomaalisesti resessiivinen familiaali Välimeren kuume | 99.82% | 0 | 0 | L5 | **Väärä positiivinen**: Ei biologista yhteyttä eribuliinin mikrotubuliiestävään mekanismiin |
| 2 | Dermatofibrosarkooma protuberans | 99.66% | 0 | 1 (Review) | L4 | Pehmytkudoksen sarkooman laajaperustaisuus mekanismilla järkevä, puuttuu DFSP-spesifinen näyttö |
| 3 | Pleuraaliset mesoteliooma | 99.51% | 0 | 0 | L5 | Vain mallin ennuste, ei empiiristä näyttöä |
| 4 | Pahanlaatuinen peritonealinen mesoteliooma | 99.47% | 0 | 0 | L5 | Vain mallin ennuste, ei empiiristä näyttöä |
| 5 | Mucinous liposarcoma | 99.47% | 0 | 0 | L4 | Liposarkooman mekanismi tunnettu, mutta munasarjan alkuperän harvinainen variantti, ei suoraa näyttöä |
| 6 | Pleuraaliset adenomatoitunut kasvain | 99.46% | 0 | 0 | L5 | Usein hyvänlaatuinen kasvain, kemoterapian väliintulo kyseenalainen |
| **8** | **Fibroblastic neoplasm** | **99.36%** | **1 (valmis Phase II)** | **8** | **L3** | **Vahvin näyttö, suositellaan tutkimuksen prioriteetiksi** |
| 9 | Pleuraaliset epithelioidiset mesoteliooma | 99.35% | 0 | 0 | L5 | Vain mallin ennuste, ei empiiristä näyttöä |
| 10 | Sydämen fibrosarkooma | 99.35% | 0 | 0 | L4 | Kuuluu samaan fibroosikasvainperheeseen kuin fibroblastic neoplasm, ulkopuolinen johtopäätös mahdollinen, mutta ei suoraa näyttöä |
| 7 | Pleuraaliset kaksivaiheinen mesoteliooma | 99.37% | 0 | 0 | L5 | Vain mallin ennuste, ei empiiristä näyttöä |

Seuraavissa osioissa keskitytään vahvimman näytön omaavaan ehdokkaaseen (Fibroblastic Neoplasm / solitaarinen fibroosikasvain).

---

## Miksi tämä ennuste on järkevä?

Eribuliinin yksityiskohtaisesta vaikutusmekanismista (MOA) ei tällä hetkellä ole saatavilla jäsenneltyä tietoa (TFDA-pakkaukseen merkitty tieto puuttuu, katso Data Gap DG002). Julkisesti tunnetuista tiedoista eribuliini kuuluu ei-taksiini-luokkaan (non-taxane) mikrotubuliihydrodynamiikan estäjiin (halichondrin B -analogit), joiden antituumorivaikutus on osoitettu sekä rintasyövässä että liposarkoomatassa.

Fibroblastic neoplasm (erityisesti solitaarinen fibroosikasvain SFT) ja eribuliinin alkuperäisen hyväksynnän yksi indikaatio "liposarkooma" kuuluvat samaan pehmytkudoksen sarkooman (soft tissue sarcoma) perheeseen, joilla on samankaltaiset solujen lisääntymisen ja mikrotubuleihin riippuvaiset biologian piirteet. Tämä on linjassa Italian sarkooma-ryhmän (Italian Sarcoma Group) loppuvaiheen SFT:lle suorittaman Phase II -tutkimuksen (ERASING, NCT03840772) suunnan kanssa, mikä osoittaa, että eribuliinin teho voidaan ulottaa sarkooma-perheeseen kohtuullisella perusteella.

Lisäksi useat in vitro- ja ksenovarastetutkimukset (kuten ihmisen fibrosarkooma-solulinja HT1080) osoittavat, että eribuliinilla on solumyrkykkyysvaikutus fibrosarkooma-soluihin ja tutkivat lääkkeisiin vastustuskykyisyyden mekanismeja ja yhdistelmähoitojen (esim. methioninaasin yhdistetty hoito) synergistisiä vaikutuksia, mikä edelleen tukee mekanismin tasolla uskottavuutta, vaikka tällä hetkellä pääasiassa prekliinisen ja yksivaraisen toisen vaiheen tutkimuksen tiedoilla, satunnaistettujen vertailevien tutkimusten (RCT) tasoinen näyttö puuttuu.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujien määrä | Keskeisiä löydöksiä |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | Italian sarkooma-ryhmän eribuliinin yksivarainen toisen vaiheen tutkimus loppuvaiheen solitaarisen fibroosikasvaimeen (SFT) (ERASING study), valmistunut 2024-09 |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeisiä löydöksiä |
|------|-----|------|------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Prekliininen | European Journal of Cancer | Potilaan alkuperäisen SFT ksenovaraste malli osoitti korkean herkkyyden doksirubisiinille/dakarbatsiinille ja vihjasi eribuliinin tai trabektediinin mahdolliseen tehoon |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Katsaus | Cancers | Solitaarisen fibroosikasvaimet (mukaan lukien ekstrameningeaalinen SFT) diagnoosi ja hoito, joka sisältää NAB2-STAT6-fusiogeenin patogeneettisen mekanismin |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Prekliininen | Anticancer Research | Rekombinantti methioninase ja eribuliini osoittavat merkittävää synergistista solumyrkkyvaikutusta fibrosarkooma-soluihin, eivät normaaleihin fibroblastteihin |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Prekliininen | Anticancer Research | Methioninase voi nostaa erittäin eribuliinille vastustuskykyisten HT1080 fibrosarkooma-solujen herkkyyden 16-kertaiseksi |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Prekliininen | In Vivo | Super eribuliinille vastustuskykyisten HT1080 -solujen pahanlaataisuus lisääntyi, mutta voidaan minimoida methioniinierajoituksella yhdessä eribuliinin kanssa alastoissa hiirimalleissa |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Prekliininen | Human Cell | Uuden mucinoosisen fibrosarkooma (MFS) -solulinjaa kehitettiin kemoterapian reagiivisuustutkimukseen |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Prekliininen | Human Cell | Mucinoosisen fibrosarkooman potilaan alkuperäinen solulinja NCC-MFS4-C1 kehitettiin, MFS on yleensä vastustuskykyinen kemoterapialle |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Tapauskertomus | Genes, Chromosomes & Cancer | Pahanlaatuinen perifieraalisen hermoston kalvon kasvain (MPNST) tapaus, jossa on NTRK3-fusiogeeni, osoitti merkittävää vastetta entrektiniibille (ei suoraa yhteyttä eribuliiniin, vain sarkooman kohdistushoitojen yhteydessä viitteeksi) |

---

## Suomi / Suomen markkinatiedot

Suomessa ei tällä hetkellä ole eribuliinin lupahyväksyntää (Not marketed, 0 lupaa), joten ei ole luettavissa hyväksyttyjä vahvuuksia ja indikaatioita.

---

## Solumyrkyllisyys

Eribuliini kuuluu kemoterapiassa käytettäviin solumyrkkyllisiin antituumorilääkkeisiin (mikrotubuliiestäjät), jotka täyttävät tämän osion soveltuvuusehdot.

| Kohta | Sisältö |
|------|------|
| Solumyrkyllisyyden luokitteleminen | Perinteinen sytotoksinen (ei-taksiini-luokkaan kuuluva mikrotubuliihydrodynamiikan estäjä, halichondrin B -analogi) |
| Luuydinvaikutuksen riski | Katso pakkaukseen merkitty varoitukset ja erityiset huomautukset (myrkyllisyyden luokittelutieto puuttuu) |
| Pahoinvointien aiheuttamisen luokitteleminen | Katso pakkaukseen merkitty varoitukset ja erityiset huomautukset (luokittelutieto puuttuu) |
| Seurantakohteet | Katso pakkaukseen merkitty varoitukset ja erityiset huomautukset |
| Käsittelysuojaus | Kuuluu solumyrkkyllisiin kemoterapialääkkeisiin, joita käsitellään solumyrkkyllisten lääkkeiden käsittelysääntöjen mukaisesti suojauksella |

---

## Turvallisuus näkökohdat

Katso pakkaukseen merkitty tieto turvallisuuden varmistamiseksi (TFDA-pakkaukseen merkitty varoitukset, vasta-aiheet ja lääkkeiden yhteisvaikutukset ovat tällä hetkellä puutteita, DG001 on luettelona Blocking-tasolla).

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold**

**Perustelu:**
TFDA-pakkaukseen merkitty varoitukset/vasta-aiheet ovat Blocking-tasolla puutteita (DG001), säännösten mukaan S1-turvallisuuden alustavaa arviointia ei voida suorittaa; lisäksi tällä lääkeaineella ei ole Suomessa lupaa (0 lupaa). Vaikka Fibroblastic Neoplasm (solitaarinen fibroosikasvain) -ehdokkaalla on 1 valmis Phase II -kliininen tutkimus ja useita mekanismia tukevia julkaisuja, näyttötaso saavuttaa L3:n, muut 9 ennustettua indikaatiota ovat heikosti tuettuja, useat ovat pelkästään mallin ennusteita (L5), joista korkeimman pistemäärän saanut FMF on jopa merkitty näyttöpaktin puolesta mekanismiltään epäuskottavaksi väärän positiivisen tuloksen vuoksi, eikä sitä tulisi priorisoida resurssien kohdentamisessa.

**Prosessin jatkamiseksi tarvitaan seuraavaa:**
- TFDA-pakkaukseen merkitty tiedon täydentäminen (DG001, Blocking) S1-turvallisuuden alustavaa arviointia varten
- DrugBank-mekanismin jäsennellyn tiedon täydentäminen (DG002) mekanismin yhteyttä koskevan analyysin vahvistamiseksi
- NCT03840772:n (ERASING study) virallisten tulosten seuranta, SFT-indikaation tehokkuussignaalin vahvistamiseksi
- L5-tasolla olevien ehdokkaitten (FMF, mesoteliooma-sarja, pleuraaliset adenomatoitunut kasvain) prioriteetin alenemisen tai poistamisen suosittelu, resurssien väärinkäyttöä varten

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

