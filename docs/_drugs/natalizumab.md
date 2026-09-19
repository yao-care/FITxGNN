---
layout: default
title: Natalizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 256
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: Multippelskeloosista keuhkoputkentulehdukseen

## Yhden lauseen yhteenveto

Natalizumab on humanisoidtu monoklonaalinen vasta-aine, jota käytetään relapsoiva-remittentti multippelskleroosiin (RRMS) hoitoon estämällä α4-integriinivälitteistä valkosolun siirtymistä. TxGNN-malli ennustaa sen saattavan olla tehokas **keuhkoputkentulehduksessa**, mutta tämä ennuste ei tällä hetkellä ole tuettu kliinisillä tutkimuksilla eikä kirjallisuudella — se on vain mallin signaali, joka on ristiriidassa lääkkeen tunnetun immunosuppressiivisen riskiprofiilin kanssa.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen käyttöaihe | Multippelskleroosi (relapsoiva-remittentti) — päätelmä kirjallisuuskontekstista; ei ole läsnä Suomen markkinatiedoissa |
| Ennustettu uusi käyttöaihe | Keuhkoputkentulehdus |
| TxGNN-ennusteen pistemäärä | 99.46% |
| Näyttöastee | L5 |
| Suomen markkinatieto | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismia koskevaa tietoa ei ole saatavilla (DrugBank-haku palautti Data Gap -ilmoituksen). Todistusjoukon kirjallisuuskontekstista saatavilla olevien tietojen perusteella natalizumab on monoklonaalinen vasta-aine, joka kohdistuu α4-integriiniin ja jota käytetään relapsoiva-remittentti multippelskleroosiin; sen tehokkuus MS:ssä on hyvin vakiintunut siteeratussa kirjallisuudessa, joka toistuvasti viittaa sen käyttöön RRMS-potilaiden kohorteissa.

Keuhkoputkentulehdusta koskevan ennusteen osalta pisteytyksen yhteydessä annettu mekanistinen perustelu on selvästi skeptinen: α4-integriinisalpaaja voisi teoriassa vähentää valkosolun tunkeutumista ilmateiden limakalvoille, mutta keuhkoputkentulehdus on pääosin infektioperäinen tai ärsytyksestä johtuva. Natalizumabin määrittävä turvallisuushuoli on *lisääntynyt* infektioriskiä (erityisesti progressiivinen multifokaalinen leukoenkefalopatiia, PML, JC virus reaktivaation seurauksena) — suunta, joka on vastakkainen siihen, mitä tarvittaisiin infektioperäisen hengitystieinfektiota turvallisesti hoidettaessa. Mikään tässä todistusjoukon kliininen tutkimus tai julkaisu ei yhdistä natalizumabaa keuhkoputkentulehdukseen kumpaankaan suuntaan.

Lisäyhteydessä: tämän lääkkeen muista ennustetuista käyttöaiheista korkein todistusteho omaava kandidaatti (psoriasis, L4, 19 julkaisua) osoittaa *vastakkaisen* suhteen — useat tapausraportit ja kohorttitutkimus dokumentoivat natalizumabia **indusoivan tai pahentavan** psoriasia (paradoksaalinen reaktio), ei sen hoitamisen. Tämä kuvio vahvistaa, että korkea TxGNN-pistemäärä yksinään ei tulisi tulkita hoitosignaaliksi ilman suuntaa-antavaa kirjallisuustuella.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

## Kirjallisuusnäyttö

Tällä hetkellä asiaan liittyvää kirjallisuutta ei ole saatavilla

## Suomen markkinatieto

Natalizumabaa ei tällä hetkellä markkinoida Suomessa (markkinatila: Ei markkinoilla, 0 lupaa kirjatuissa tiedoissa). Tälle ehdokkaalle ei ole saatavilla tuotteen lupa-aineistoja.

## Turvallisuushuomiot

Turvallisuustietoja varten, ks. pakkausseloste. (TFDA/pakkausselosteen varoitukset, vasta-aiheet ja lääkkeiden väliset yhteisvaikutustiedot ovat kaikki odottamassa — ks. Data Gap DG001, Blocking severity.)

## Johtopäätös ja seuraavat askeleet

**Päätös: Odota**

**Perustelu:**
Keuhkoputkentulehdusta koskevalla ennusteella ei ole kliinistä tutkimusnäyttöä eikä kirjallisuustuella (L5, vain mallin ennuste), ja ehdotettu mekanismi on ristiriidassa natalizumabin tunnetun immunosuppressiivisen/infektioriskin profiilin kanssa (mukaan lukien PML), mikä tekee siitä biologisesti epätodennäköisen nykyisen näytön perusteella.

**Jatkaakseen tarvitaan seuraavaa:**
- TFDA/Suomen pakkausseloste-tiedot (turvallisuusvaroitukset, vasta-aiheet) — DG001, tällä hetkellä estää S1 turvallisuustarkistusta
- Varmistettu vaikutusmekanismi DrugBankista — DG002
- Esikliininen tai in vitro -näyttö, joka yhdistää α4-integriinisalpauksen keuhkoputkentulehduksen patofysiologiaan, koska sitä ei tällä hetkellä ole
- Jos tämän saman lääkkeen muita ehdokkaita jatketaan, aseta psoriasis (L4, 19 julkaisua) tarkistuksen etusijalle — huomaa kuitenkin, että nykyinen kirjallisuus viittaa siellä pikemminkin negatiiviseen (sairauden aiheuttavaan) suhteeseen kuin terapeuttiseen suhteeseen, joten se vaatisi myös huolellista uudelleenmuotoilua ennen eteenpäinmenemistä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

