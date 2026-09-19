---
layout: default
title: Empagliflozin
parent: Pelkkä mallin ennuste (L5)
nav_order: 143
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Empagliflozin: Tyypin 2 diabeteksesta paikalliseen jäykän raajan oireyhtymään

## Yhden lauseen yhteenveto

Empagliflozin on SGLT2-esto-aine, joka tunnetaan yleisesti Tyypin 2 diabeteksen hoitoon, mutta tämä todistepaketti ei sisällä vahvistettua Taiwanissa hyväksytyn käyttöaiheeseen liittyvää tekstiä ja osoittaa, että lääke **ei ole tällä hetkellä markkinoilla Taiwanissa**. TxGNN-malli yhdistää sen **Paikalliseen jäykän raajan oireyhtymään** (joka on osa jäykän henkilön oireyhtymän spektriä), mutta tämä yhdistelmä sijaitsee sijoituksella 9036 ja sillä on **nolla kliinisiä tutkimuksia ja nolla julkaisuja**, jotka tukisivat sitä. Mallin oma perusteluteksti kuvaa yhdistelmää todennäköisesti tietokaavion häiriöksi pikemminkin kuin biologisesti perustelluksi hypoteesiksi.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Ei saatavilla todistepakettissa — lääke ei ole tällä hetkellä markkinoilla Taiwanissa eikä mitään lupia/käyttöaihe-tietuetta ole olemassa |
| Ennustettu uusi käyttöaihe | Paikallinen jäykän raajan oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99.06% (rank 9036) |
| Todisteen taso | L5 |
| Markkinoinnin asema (Taiwan) | Ei markkinoilla (Ei markkinoilla) |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Yksityiskohtaista DrugBankista peräisin olevaa toimintamekanismin tekstiä ei palautettu tässä todistepakettissa (merkitty korkeaa vakavuutta olevaksi tietoaukoksi DG002). Yleisesti tunnetun farmakologian perusteella pikemminkin kuin aineiston vahvistetun sisällön perusteella, empagliflozin kuuluu SGLT2 (natriumglukoosi-yhteiskuljetin-2) -esto-aineiden luokkaan, joka toimii munuaisen proksimaalikäytävässä vähentämällä glukoosin takaisinimeytymistä.

Paikallinen jäykän raajan oireyhtymä on paikallistunut muunnelma jäykän henkilön oireyhtymän spektrissä — autoimmuunisairaus, jonka aiheuttaa anti-GAD65-vasta-aineiden hyökkäys GABAergiikia neuroneita vastaan, mikä johtaa riittämättömään keskussäätöisen inhibitoriisen signaloinnin ja lihasrigiditeettiin. Ei ole olemassa vakiintunutta farmakologista polkua, joka yhdistäisi munuaisen SGLT2-inhibition keskussäätöisen GABAergisen neurotransmissioon tai autoimmuunivasta-aineiden modulointiin.

Todistepaketin oma muutostyön perusteluteksti on selkeä tästä kohdasta: se karakterisoi empagliflozin–jäykän-raajan-oireyhtymä ja empagliflozin–klassinen-SPS yhdistelmiä (sijoitukset 9036 ja 9037, lähes identtisillä pisteillä) todennäköisesti **tietokaavion häiriöksi metabolisten ja neurologisten solmujen välisenä esiintymisenä**, ei biologisesti uskottavaksi hypoteesiksi. Mikään mekanistinen silta, prekliininen tutkimus, kliininen tutkimus tai julkaistu tapauskertomus ei tue yhteyttä. Tämä tulisi lukea matalan luottamuksen, tutkivaksi mallin tulokseksi pikemminkin kuin vahvistetuksi muutostyön signaaliksi.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

## Taiwanin markkinatiedot

Lupien tietueita ei ole saatavilla — empagliflozin ei ole tällä hetkellä markkinoilla Taiwanissa (0 lupaa tiedostoissa).

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

*(Huomautus: TFDA-pakkausselosteen varoitukset/kontraindikaatiot ja DDI-tietokanta palautuivat molemmat ilman tietoja tähän lääkkeeseen — virallisen TFDA-pakkausselosteen hakeminen on merkitty estävänä tietoaukoksi DG001, ja se on ratkaistava, ennen kuin mikään turvallisuuden arviointi (S1) voi edetä.)*

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ei ole kliinisiä tutkimuksia tai kirjallisuuden todistusaineistoa, ei uskottavaa mekanistista yhteyttä SGLT2-inhibition ja jäykän henkilön oireyhtymän patofysiologian välillä, ja ennuste itse sijaitsee matalan mallin sijoituksella (9036) ja lähdeperusteluteksti kuvaa sitä eksplisiittisesti todennäköisesti tietokaavion häiriöksi. Yhdistettynä vahvistamattomiin alkuperäisen käyttöaiheeseen ja Taiwanin turvallisuustietoihin, ei ole perusteita edetä tämän ehdokkaan kanssa tällä hetkellä.

**Edetäkseen seuraavaa tarvitaan:**
- Virallinen TFDA-pakkausseloste (varoitukset, kontraindikaatiot) — tällä hetkellä estävä tietoaukko (DG001)
- Vahvistettu DrugBankista peräisin oleva toimintamekanismin tieto (DG002)
- Empagliflozinin alkuperäisen hyväksytyn käyttöaiheeseen ja Taiwanin lupauksen tilan vahvistaminen
- Riippumaton prekliininen tai mekanistinen todiste, joka yhdistää SGLT2-inhibition GABAergiseen/autoimmuunisiin polkuihin, ennen kuin sijoitetaan enemmän tähän käyttöaiheeseen
- ClinicalTrials.gov-, ICTRP- ja PubMed-uudelleenseulonta toistuvasti, koska kaikki kolme palautuivat nollahiteiksi 2026-04-20 kyselypäivämääränä

---

**Huomautus tarkistuksellesi:** lähdemallin Quick Overview -kenttä on merkitty "Suomen markkinoinnin asemaksi" (ja osion otsikko "Suomen markkinatiedot"), mutta tämän todistepaketin todelliset tiedot sijaitsevat `taiwan_regulatory`-kohdassa ja ne on haettu TFDA:sta (`query_log` lähde `tfda`/`tfda_package_insert`). Merkitsin nämä Taiwan-kohdaksi raportissa sen sijaan, että levitin sitä näyttävää copy-paste-virhettä Suomen-projektin mallista. Koska `.claude/p0_consistency_check.sh` on olemassa nimenomaan tämän luokan ristiinprojektin copy-paste-ongelmien jäljittämiseksi, haluat ehkä ajaa sen raportin generoinnin mallin/kehotteen lähteeseen vahvistamaan ja korjaamaan sen ylätasolla.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

