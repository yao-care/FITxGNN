---
layout: default
title: Anagrelide
parent: Pelkkä mallin ennuste (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Anagrelide
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

# Anagrelidi: Oleellisesta trombosytemiasta reaktiiviseen trombosytoosiin

## Yhden lauseen yhteenveto

Anagrelidi (DrugBank DB00261) on verihiutaleiden määrää alentava aine, jonka vakiintunut kliininen käyttö — tähän näyttöpakettiin sisältyvän kirjallisuuden mukaan — on oleellinen trombosytemia (ET), klonaalinen myeloproliferatiivinen häiriö. TxGNN-malli ennustaa, että se saattaa olla tehokas myös **reaktiiviseen trombosytoosiin**, mutta tätä suuntaa tukee tällä hetkellä vain **0 kliinistä tutkimusta** ja **10 tausta-/katsausartikkelia**, joista mikään ei suoraan testaa anagrelidiä reaktiivisessa trombosytoosissa. Huomionarvoista on, että useat näistä samaisista artikkeleista toteavat, että reaktiivinen trombosytoosi tyypillisesti **ei** vaadi verihiutaleiden määrää alentavaa lääkehoitoa, mikä heikentää pikemmin kuin vahvistaa uudelleenkäyttötapausta.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei dokumentoitu Suomen sääntelyaineistossa (lääkettä ei markkinoida siellä). Tähän näyttöpakettiin sisältyvän kirjallisuuden perusteella anagrelidiä käytetään oleellisen trombosytemia / klonaalisen trombosytoosin hoitoon (esim. PMID 16019501, 38455691) |
| Ennustettu uusi indikaatio | Reaktiivinen trombosytoosi |
| TxGNN ennustepisteet | 99.83% (ranking 2305) |
| Näyttötaso | L4 (vain tausta-/mekanistinen ja tapaus-tason kirjallisuus; yksikään kliininen tutkimus tai tutkimus ei suoraan testaa anagrelidiä tätä indikaatiota varten) |
| Suomen markkinatilanne | ✗ Ei markkinoida |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidä varalla |

---

## Miksi tämä ennuste on perusteltu?

Anagrelidiä koskevia yksityiskohtaisia toimintamekanismin tietoja on tällä hetkellä merkitty tietoaukoksi (DG002, korkea vakavuus) — DrugBank ei palauttanut tässä kyselyssä strukturoitua MOA-sisältöä. Haetun kirjallisuuden perusteella anagrelidiä kuvataan aineeksi, jota käytetään megakaryosyyttien proliferaation tukahduttamiseen ja verihiutaleiden tuotannon vähentämiseen, ja se on sijoitettu busulfaanin, hydroksikarbamiidin ja interferoni-alfan rinnalle klonaalisen trombosytoosin sytoreduktiivisena vaihtoehtona (PMID 7783354, 15270658).

Ennustetulla uudella indikaatiolla, reaktiivisella trombosytoosilla, on pinnallisesti samanlainen fenotyyppi alkuperäisen indikaation kanssa — molemmat ilmenevät kohonneina verihiutaleiden lukumäärinä. Tämä on todennäköisesti syy siihen, miksi TxGNN-tietokaavio linkitti ne: oleellinen trombosytemia ja reaktiivinen trombosytoosi käsitellään usein yhdessä differentiaalidiagnoosin kirjallisuudessa (PMID 10494240, 17171694, 1994734), mikä luo vahvan solmujen läheisyyden tietokaavissa, vaikka näillä kahdella tilalla on eri taustalla oleva biologia.

Tärkeää on, että tämä sama kirjallisuus toimii oikeastaan vastaan yksinkertaisen uudelleenkäyttölogiikan: reaktiivinen trombosytoosi on toisen taustalla olevan prosessin (infektio, tulehdus, pernan poisto, raudan puute jne.) sekundaarinen vastaus, ja useat tässä paketissa olevat lähteet toteavat eksplisiittisesti, että se "ei vaadi lääkehoitoa" useimmissa tapauksissa (PMID 15270658), toisin kuin klonaalinen trombosytoosi, jossa hoito ohjataan verihiutaleiden lukumäärän kynnysarvoilla ja trombotiikan riskillä (PMID 10494240). Mikä tahansa anagrelidihoito reaktiivisessa trombosytoosissa rajoittuisi todennäköisesti harvinaisiin, vaikeisiin/oireileviin tapauksiin (esim. äärimmäinen hypertromboosytoosi, jossa on pään ja sisäelinten riski, kuten kuvataan trombosyyttaaferesis-katsauksessa, PMID 28380402) — ei yleiseen reaktiiviseen trombosytoosiin, jota ennustettu indikaatio tarkoittaa. Tämä ero tulisi käsitellä varoituslipuksi pikemmin kuin ennusteen vahvistukseksi.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyviä kliinisiä tutkimuksia rekisteröity.

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeisiä tuloksia |
|------|-----|------|------|---------|
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Katsaus | Leukemia & Lymphoma | Anagrelidihoitoa koskevan kriittinen katsaus oleellisessa trombosytemiassa; erottaa klonaalisen trombosytoosin (vaatii sytoreduktiota) reaktiivisesta trombosytoosista (tavallisesti ei vaadi) |
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Katsaus | Expert Review of Anticancer Therapy | Anagrelidiä koskeva lääkeprofiilit (Agrylin) MOA ja terapeuttinen potentiaali klonaalisen trombosytoosin hoidossa; huomauttaa eksplisiittisesti, että reaktiivinen trombosytoosi ei vaadi hoitoa |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Katsaus | The Medical Journal of Australia | ET-diagnoosi vaatii reaktiivisen trombosytoosin poissulkemista; hoitokynnyksellä on verihiutaleiden lukumäärä >1000×10⁹/L |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Katsaus | The American Journal of the Medical Sciences | Trombosytoosin/trombosytemia taustalla olevan patofysiologia ja verihiutaleiden tuotannon sytokinisäätely; ei lääkekohtainen |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Katsaus | Rinsho Ketsueki (japani) | ET:n diagnoosi/hoitokatsaus; luettelee anagrelidiä aineeksi, joka tukahduttaa megakaryosyyttien proliferaatiota |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Tapausperustainen katsaus | Leukemia Research | Trombosyyttaaferesisin katsaus äärimmäisessä hypertromboosytoosissa myeloproliferatiivisissa neoplasmoissa; käsittelee lääkinnällisen sytoreduksion rajoja, kun nopea vähentäminen on tarpeen |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospektiivinen/Havainnoiva | Pediatric Blood & Cancer | Retrospektiivinen analyysi 12 pediatrisesta tapauksesta, jossa verrataan oleellista vs. reaktiivista trombosytemiaa; korostaa diagnostista päällekkäisyyttä |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Tapauskertomus | Srpski Arhiv za Celokupno Lekarstvo | ET, jossa ankyloiva spondyliitti (tila, joka liittyy reaktiiviseen trombosytoosiin), jota hoidetaan anagrelidiä sekä DMARD-lääkkeitä/etanersepta |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Tapauskertomus | European Journal of Case Reports in Internal Medicine | Akuutti sydäninfarkti ET-potilaalla, joka käyttää anagrelidihoitoa — turvallisuussignaali, joka liittyy trombotiikan/kardiaalisen riskin |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Tapauskertomus | Medicine | Perioperatiivisen hoidon ohjaus trombosytoosin osalta digitaalisessa replantaatiossa; ei anagrelidi-spesifinen |

---

## Suomen markkinatieto

Anagrelidiä ei ole tällä hetkellä markkinoitu Suomessa (0 markkinoille saattolupaa), joten tuote-/indikaatiotietoja ei ole saatavilla.

---

## Turvallisuuteen liittyvät näkökohdat

TFDA-pakkauksessa olevista varoituksista ja vasta-aiheista anagrelidiille ei voitu hankkia tietoa tässä kyselyssä (tietoaukko DG001, **Estävä vakavuus** — tämä tietoaukko yksinään estää ehdokkaan alkuvaiheen turvallisuusseulonnan täyttämisen). Lääkkeiden väliset vuorovaikutukset kyselty, mutta sitä ei löytynyt. Kunnes tämä tietoaukko ratkaistaan, katso suoraan anagrelidiä koskevan pakkauselosteen turvallisuustiedoista.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä varalla**

**Perustelut:**
- Näyttötaso on parhaimmillaan L4 — ei ole olemassa kliinisiä tutkimuksia, joissa suoraan testattaisiin anagrelidiä reaktiivisessa trombosytoosissa, eikä kirjallisuus ole oikeastaan tueksi; haettu kirjallisuus on tausta-/mekanistinen ja väittää päinvastoin, että useimpia reaktiivisia trombosytoosia ei vaadita verihiutaleiden määrää alentava lääkehoito.
- Estävän vakavuuden turvallisuustietoaukko (TFDA varoitukset/vasta-aiheet, DG001) tarkoittaa, että tämä ehdokas ei voi edetä turvallisuuden arviointiin riippumatta tehokkuuden näytöistä.

**Jotta edetään eteenpäin, seuraavaa tarvitaan:**
- Ratkaise DG001: hanki TFDA/virallisen pakkauselosteen varoitukset ja vasta-aiheet anagrelidiille
- Ratkaise DG002: hanki vahvistetut toimintamekanismin tiedot DrugBankista
- Tunnista kliinisesti uskottava reaktiivisen trombosytoosin alaryhmä (esim. vakava/oireilevainen hypertromboosytoosi, jossa on trombotiikan riski), eikä yleinen reaktiivisen trombosytoosin populaatio, ja etsi kaikki tapaussarjat tai tutkimukset, jotka koskevat sitä alaryhmää
- Selventää, miksi TxGNN sijoitti tämän assosiaation korkealle, kun kirjallisuuden näyttöperusta varoittaa oikeastaan reaktiivisen trombosytoosin rutiinilääkkeistä

*Huomio: Toinen ehdokas-indikaatio, "käänteinen Klippel-Trenaunay-oireyhtymä" (TxGNN-pisteet 99.59%, ranking 4816), arvioitiin myös tälle lääkkeelle. Sille ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta ja mekanistinen yhteys on epätodennäköinen (Klippel-Trenaunay-spektrin häiriöt liittyvät trombosytopenian/kulutuskoagulopatian, ei trombosytoosin). Sitä arvioidaan näyttötasolla L5 suosituksinaan **Pidä varalla** ja se on hyvin todennäköisesti tietokaavion solmujen läheisyyden artefakti pikemmin kuin aito uudelleenkäyttösignaali; tätä indikaatiota ei suositella jatkotutkimukseen.*

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

