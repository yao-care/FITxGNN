---
layout: default
title: Enfortumab Vedotin
parent: Pelkkä mallin ennuste (L5)
nav_order: 145
evidence_level: L5
indication_count: 9
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

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Enfortumab vedotin: uroteliaalisyövästä (virtsarakon) pakkotautiin

## Yhden lauseen yhteenveto

Enfortumab vedotin on Nectin-4-kohdistettu vasta-aine-lääkekonjugaatti (ADC), joka kuljettaa mikrotubuluksien estäjän kuormaksi MMAE:ta, ja se on kehitetty edistyneen uroteliaalisyövän (virtsarakon) hoitoon — vaikka tätä alkuperäistä indikaatiota **ei ole suoraan dokumentoitu** nykyisessä todistusaineistossaan (`original_indications` on tyhjä; vain päätelty liittyvästä kirjallisuudesta). TxGNN-mallin parhaiten sijoittuva uusi ennustus, **Pakkotauti**, saavuttaa erittäin korkean samankaltaisuuspistemäärän, mutta sillä on **nolla tukevia kliinisiä tutkimuksia tai kirjallisuusviitteitä**, ja todistusaineiston oma mekanistinen arvio toteaa eksplisiittisesti, että **ei ole uskottavaa biologista yhteyttä** lääkkeen mekanismin ja *Mycobacterium leprae* -infektioiden välillä. Tätä ehdokasta tulee käsitellä pelkästään mallin tuottamana signaalina, ei validoiduksi uudelleenkäytön mahdollisuudeksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu todistusaineistossa (`original_indications` tyhjä); kirjallisuuskonteksti (PMID 41341429) yhdistää enfortumab vedotin ADC:t **virtsarakon/uroteliaalisyöpään** — vahvistamaton, odottaa DrugBank/pakkausseloste-vahvistusta |
| Ennustettu uusi indikaatio | Pakkotauti |
| TxGNN-ennustepiste | 99.53% |
| Näyttötaso | L5 (pelkkä mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkina-asema | Ei markkinoilla |
| Lupakäsittelyjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätys** |

---

## Miksi tämä ennustus on järkevä?

Tällä hetkellä yksityiskohtaiset toimintamekanismin tiedot eivät ole saatavilla jäsennellyssä `original_moa` -kentässä (tietoaukko DG002, korkea vakavuus). Tämän todistusaineiston muualla olevan tiedon perusteella enfortumab vedotin on kuvattu **Nectin-4-kohdistettuna vasta-aine-lääkekonjugaattina**, jonka kuorma MMAE (monomethyl auristatin E) on mikrotubuluksien estäjä, joka vaikuttaa syöpäsolujen mitoosiin — mikä on yhdenmukaista sen tunnetun roolin kanssa onkologisena ADC:nä.

Parhaiten sijoittuvan ennustuksen, **pakkotaudin**, osalta todistusaineiston oma uudelleenkäytön perustelut sanovat eksplisiittisesti, että **ei ole järkevää mekanistista yhteyttä**: pakkotauti johtuu *Mycobacterium leprae* -infektiosta ja sen liittyvästä immuuni-/hermopathologiasta, jolla ei ole tunnettua yhteyttä Nectin-4-ilmentymiseen tai mikrotubuluksiin kohdistettuun sytotoksisuuteen. Perustelut huomauttavat, että korkea TxGNN-pistemäärä todennäköisesti heijastaa epäsuoraa solmujen yhteyttä tietokaavion sisällä todellisen biologisen mekanismin sijaan.

Huoli vahvistuu laajemman ennustejonon laadusta: yhdeksästä sijoitetusta indikaatiosta **kaikki yhdeksän on luokiteltu L5/S0/Pidätys**, kaksi (sijoitus 8 "naudan infektiivinen rhinotraheiitti" ja sijoitus 9 "paha kataari") ovat **eläinlääketieteellisiä sairauksia naudoilla/märehtijöillä**, jotka on eksplisiittisesti merkitty todistusaineistossa todennäköisiksi lajisekaannusartefakteiksi tietokaavion sisällä, ja yksi (sijoitus 4, kandidiaasi) on tuettu ainoastaan lääketurvallisuus-kirjallisuussignaalilla, joka kuvaa kandidiaasia **haitallisena turvallisuussignaalina** ADC-indusoidusta immuunosupresiosta, ei hoito-indikaationa. Kaiken kaikkiaan tämä kaava viittaa siihen, että tämän lääkkeen nykyinen ennustejoukko heijastaa enemmän graafi-tason kohinaa kuin uskottavia farmakologisia hypoteeseja, eikä yksikään parhaista ehdokkaista — mukaan lukien pakkotauti — tällä hetkellä ylitä spekulatiivista, pelkästään malliin perustuvaa signaalia.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusaineiston näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

*(Huomautus: kirjallisuusaineiston näyttö on olemassa muualla tässä aineistossa eri ehdokkaalle — sijoitus 4, "kandidiaasi," PMID 41341429 — mutta tämä koskee ADC-luokan turvallisuussignaalia, ei pakkotautia, ja sitä käsitellään alla olevan turvallisuusnäkökohtien kohdalla.)*

---

## Suomen markkinatiedot

Suomessa ei ole tällä hetkellä rekisteröityä myyntilupaa (`total_licenses: 0`). Enfortumab vedotin ei ole tällä hetkellä markkinoilla tässä lainkäyttöalueella.

---

## Sytotoksisuus

Enfortumab vedotin on vasta-aine-lääkekonjugaatti, joka sisältää sytotoksisen mikrotubuluksien estäjä-kuorman, joten tämä osio on asiaankuuluvaa.

| Kohta | Sisältö |
|------|---------|
| Sytotoksisuusluokittelu | Kohdennettu hoito (Vasta-aine-lääkekonjugaatti), joka toimittaa perinteistä sytotoksista kuormaa (MMAE, mikrotubuluksien/mitoosien estäjä auriin-luokasta) |
| Luuydintukahduttamisen riski | Ei ole muodollisesti määritelty tässä todistusaineistossa. Liittyvä lääketurvallisuus-kirjallisuussignaali (PMID 41341429, sijoitus 4 kandidiaasi-perustelut) yhdistää ADC-hoitoa neutropeniaan/immuunosupresioon, joka ilmenee opportunistisena infektiona — katso vahvistettuja tietoja pakkausselosteesta |
| Oksentamispotentiaalin luokittelu | Ei saatavilla todistusaineistossa — katso pakkausseloste |
| Seurantakohdat | Täydellinen veritutkimus differentiaalilla (erityisesti neutrofiilit), infektioiden merkit/oireet, maksan ja munuaisten toiminta |
| Käsittelysuojaus | Sytotoksisen lääkkeen käsittelyvarotoimet pitäisi noudattaa MMAE-kuorman vuoksi; vahvista spesifinen protokolla pakkausselosteen perusteella |

---

## Turvallisuusnäkököhdat

Virallinen pakkausselosteen tieto (tärkeät varoitukset, vasta-aiheet, lääkkeiden yhteisvaikutukset) on **estävä** tietoaukko (DG001) — TFDA/valmistajan merkinnät eivät ole vielä käytettävissä, joten täydellinen turvallisuusarvio ei ole tällä hetkellä mahdollinen. Lääkkeiden yhteisvaikutusseulonta ei tuottanut tuloksia (`ddi.query_status: not_found`), mikä heijastaa lääkkeen puuttumista kyseisestä tietokannasta eikä yhteisvaikutusten puuttumisen vahvistusta.

Yksi asiaa koskeva turvallisuussignaali löydettiin lähteistä: vuonna 2025 julkaistu FAERS-pohjainen lääketurvallisuustutkimus virtsarakon syövän ADC-hoidoista (PMID 41341429) raportoi turvallisuussignaaleja, joihin kuuluvat opportunistiset infektiot, kuten kandidiaasi, joiden epäillään johtuvan ADC-indusoidusta immuunosupresiosta tai neutropeniasta. Tätä pitää käsitellä monitoroitavana riskinä, ei hoito-indikaationa.

Tutustu pakkausselosteen täydellisiin turvallisuustietoihin niiden ollessa saatavilla.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
Pakkotaudin ennusteella ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta, todistusaineiston oma mekanistinen analyysi arvioi eksplisiittisesti, että sillä ei ole uskottavaa biologista perustelua, ja se sijaitsee ennustejoukon sisällä, jossa kaikki yhdeksän sijoitettua indikaatiota ovat L5/Pidätys — joista kaksi näyttävät olevan eläinlääketieteellisten sairauksien artefakteja. Estävän vakavuuden tietoaukon (DG001) pakkausselosteesta/turvallisuustiedoista ja lääkkeen markkinoimattomasta asemasta Suomessa ei ole tällä hetkellä perustetta siirtää tätä ehdokasta mallin seulonnasta eteenpäin.

**Etenemisvaiheille tarvitaan seuraavaa:**
- TFDA/EMA pakkausselosteen tiedot (varoitukset, vasta-aiheet, lääkkeiden yhteisvaikutukset) — DG001, Estävä
- Vahvistettu toimintamekanismi ja alkuperäinen indikaatio DrugBankin/sääntelylabelien kautta — DG002, Korkea
- Prekliininen tai biologisen plausibiliteettiin liittyvä tieto, joka yhdistää erityisesti Nectin-4/MMAE-aktiviteetin *M. leprae* -infektioon tai pakkotaudin patofysiologiaan, mikäli tätä hypoteesia halutaan tutkia edelleen
- Tämän lääkkeen laajemman TxGNN-ennustejonon tietojen laadun tarkistus, ottaen huomioon eläinlääketieteellisten sairauksien merkinnöt (sijoitukset 8–9), jotka viittaavat mahdolliseen tietokaavion solmusekaannukseen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

