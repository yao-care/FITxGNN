---
layout: default
title: Lomitapide
parent: Pelkkä mallin ennuste (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapide: Homotsygoottisesta perinnöllisestä hyperkolesterolemiasta makrotrombotsytopeniaan sydämen mitraaliventtiilien puudutuksella

## Yhden lauseen yhteenveto

Lomitapide on mikrosomaalisen trigliseridinsiirtoproteiinin (MTP) estäjä, joka on alkuperäisesti hyväksytty (tuoteniminä Juxtapid/Lojuxta) homotsygoottisen perinnöllisen hyperkolesterolemia (HoFH) hoitoon. TxGNN:n korkeimmalla sijalla oleva uuden käyttöaiheen ennuste, **makrotrombotsytopenia sydämen mitraaliventtiilien puudutuksella**, saavuttaa **99,92 % mallin pistemäärän**, mutta sitä tukee tällä hetkellä **nolla kliinistä tutkimusta ja nolla julkaisua** — signaali on olemassa vain mallin sisällä.

## Pikakatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Homotsygoottinen perinnöllinen hyperkolesterolemia (HoFH) — johdettu tutkimus- ja kirjallisuusnäytöstä (Juxtapid/Lojuxta); ei ole olemassa strukturoidussa `taiwan_regulatory`-lupausdatassa |
| Ennustettu uusi käyttöaihe | Makrotrombotsytopenia sydämen mitraaliventtiilien puudutuksella |
| TxGNN:n ennustepisteet | 99,92 % |
| Näyttötaso | L5 (vain mallin ennuste) |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on perusteltu?

Lomitapiden mekanismi on hyvin karakterisoitu taustalla olevassa tutkimus- ja kirjallisuusnäytössä, vaikka strukturoidussa `original_moa`-kentässä on tietoaukko: se estää MTP:tä maksassa ja ohutsuolessa, estäen apoB-sisältävien lipoproteiinien (VLDL, kylomikronit) kokoamisen ja erityksen, mikä laskee LDL-C:n, apoB:n ja kokonaiskolesterolin. Tämä on perusta sen hyväksynnälle HoFH:n hoitoon.

Makrotrombotsytopenia sydämen mitraaliventtiilien puudutuksella on harvinainen, pääosin geneettinen verihiutaleiden ja sidekudoksen häiriö. Ei ole vakiintunutta biologista polkua, joka yhdistäisi MTP:n välityksellistä lipoproteiinien kokoamisen verihiutaleiden koon säätelyyn tai mitraaliventtiilin rakenteeseen, ja näyttöpaketin omissa perusteluissa tämä on nimenomaisesti merkitty: "無機轉證據。屬罕見遺傳性巨大血小板症候群，與 MTP 抑制無已知關聯，零試驗零文獻，純模型預測" (ei mekanismin näyttöä; harvinainen perinnöllinen makrotrombotsytopenia-oireyhtymä, jolla ei ole tunnettu yhteyttä MTP-estoihin; nolla tutkimusta, nolla kirjallisuutta, puhdas mallin ennuste).

Tämä kuvio toistuu rankingin 1–8 ja 10 sisällä — kaikki verihiutaleiden/hyytymisen häiriöt (perinnölliset trombotsytopeniat, tiheän granulan tautia, pseudon von Willebrandt-tauti, Glantzmannin trombasteniaani, verihiutaleiden varastointialttiuden puutos jne.) saavuttavat erittäin korkeat pisteet (>99,5 %) ilman tukevia mekanismeja, tutkimuksia tai kirjallisuutta. Tämä klusteri, yhdistettynä siihen, että mekanistisesti *järkevä* käyttöaihe (hyperlipoproteinemia — sijoitus 9, joka on itse asiassa lomitapiden oma alkuperäinen hyväksyntä-alue) saa *pienemmät* pisteet kuin nämä epäuskottavat ehdokkaat, viittaa tietograafin embedding-artefaktiin — jota puolustaa todennäköisesti lipidi- ja hematologisten parametrien rinnakkaisesiintyminen jaetuissa potilastietueissa — todellisen farmakologisen signaalin sijaan.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyvien kliinisten tutkimusten rekisteröityä.

## Kirjallisuusnäyttö

Tällä hetkellä kirjallisuusnäyttö ei ole saatavilla.

## Suomen markkinatiedot

Lomitapidella ei ole kirjattuja markkinointilupia Suomelle (0 rekisteröityä lisenssiä; markkinatilanne: ei markkinoilla).

## Turvallisuusnäkökohdat

Muodolliset turvallisuuskentät (päävaroitukset, vasta-aiheet, lääkeyhteisvaikutukset) on merkitty tietovajeiksi lähdenäyttöpaketissa (DG001, Blocking severity) — katso yksityiskohtaisia turvallisuustietoja pakkaustiedotteesta.

**Huomio:** Vaikka strukturoiduissa `safety`-kentissä ei ole kuvattu, niihin liittyvien ennustettujen käyttöaiheiden uudelleenkäytön perusteluteksti nimenomaisesti huomauttaa, että lomitapidella on tunnettu maksatoksisuusriski ja se on vasta-aiheinen raskaana olevilla ja vastasyntyneiden väestöllä — oleellista yhteydessä olevia tietoja tulevaisuuden arvioinnissa.

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Korkeimmalla sijalla oleva ennustettu käyttöaihe (makrotrombotsytopenia sydämen mitraaliventtiilien puudutuksella) ei ole mekanistisesti uskottava, sillä ei ole kliinisiä tutkimuksia eikä kirjallisuustukea — näyttötaso L5, päätösvaihe S0. Sama koskee 8:sta muusta 9:stä rankitusta ehdokkaasta tässä paketissa. Ainoa ehdokas, jolla on vahva näyttö, hyperlipoproteinemia (L1, 12 tutkimusta, mukaan lukien pivotaaliset 3. vaiheen tutkimukset, 19 julkaisua), ei ole aidon uudelleenkäytön mahdollisuus — se heijastaa lomitapiden *olemassa olevan* hyväksynnän aiheen (HoFH) nousemista uuden tautien ontologia-termin alla, ei todellista uutta käyttöä.

**Jatkaakseen seuraavaa tarvitaan:**
- TFDA/Fimea:n pakkaustiedotteen tiedot (DG001, Blocking) ennen kuin turvallisuuden arviointi voidaan aloittaa
- Vahvistettu DrugBank MOA -tietue (DG002) mekanismin yhdistämisanalyysin asianmukaiseksi perustamiseksi
- Mallin/embedding-tason tarkastus siitä, miksi TxGNN keskittää korkeat pisteet MTP-estäjää varten liittymättömiin verihiutaleiden/hyytymisen häiriö-solmuihin
- Jos lipidi-vierekkäisten laajennusten tutkiminen on kiinnostavaa, arvioi sellaisia leimansa lähellä olevia olosuhteita kuin perheellinen ksantuuri-syndromi (PMID 36152419) off-label-laajennusarvioksi — ei uuden uudelleenkäytön ehdokkaaksi tästä ennustejoukosta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

