---
layout: default
title: Prasterone
parent: Pelkkä mallin ennuste (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: hyväksytystä indikaatiosta puuttumisesta hepariinin kofaktori 2 -puutokseen

## Yhden lauseen yhteenveto

Prasterone (DHEA, DrugBank DB01708) ei ole tällä hetkellä markkinoitu tässä lainkäyttöalueella eikä sillä ole rekisterissä olevaa hyväksyttyä indikaatiota, joten sen alkuperäistä kliinistä käyttöä ei voida määrittää saatavilla olevista tiedoista. TxGNN-mallin korkein sijoitettu ennustus osoittaa **hepariinin kofaktori 2:n puutokseen**, mutta tätä signaalia tukee **0 kliinistä tutkimusta** ja **0 julkaisua**, ja ehdotettu mekanismi kulkee uskottavasti *väärään suuntaan* — androgeeniset steroidit yhdistetään yleensä prokoagulantti-profiiliin, ei antikoagulantti-profiiliin. Tämän kandidaatin tulisi käsitellä spekulatiivisena, kunnes riippumaton mekanistinen tai kliininen näyttö ilmaantuu.

---

## Pika-yhteenveto

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei rekisterissä — lääke ei ole markkinoitu tällä markkinalla, hyväksyttyä indikaatiotekstiä ei ole saatavilla |
| Ennustettu uusi indikaatio | Hepariinin kofaktori 2:n puutos |
| TxGNN-ennustepisteet | 99.99% |
| Näyttötaso | L5 (vain malliennuste, ei tukevia tutkimuksia tai kirjallisuutta) |
| Markkinatila Suomessa | ✗ Ei markkinoitu |
| Hyväksyntojen lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla prasteronelle. Tunnettujen tietojen perusteella prasterone on luonnollisesti esiintyvä adrenaalisen steroidiesiaine, joka metaboloituu androgeeneiksi ja estrogeeneiksi; sitä ei ole hyväksytty hoitona tällä markkinalla, joten sen kliininen tehokkuusprofiili on dokumentoimaton.

Hepariinin kofaktori 2:n (HCII) puutos on harvinainen perinnöllinen sairaus, jossa antikoagulanttisesti vaikuttavan plasmavalkuaisaineen aktiivisuuden väheneminen lisää laskimotromboosin riskiä. Terapeuttisesti hyödyllinen aine tälle sairaudelle tarvitsisi tukea antikoagulanttiaktiviteettiä tai muuten vähentää verenhyytymisen taipumusta. Näyttöpaketin oma mekanistinen arviointi korostaa suuntaongelmaa: androgeeni-/DHEA-siihen liittyvät yhdisteet raportoidaan yleisemmin kirjallisuudessa *prokoagulantti*-assosiaatioon kuin suojaaviin vaikutuksiin (esim. kohonneet verenhyytymisen riskit korkean androgeenin tiloissa kuten PCOS, mainittu liittyvässä ennustetussa indikaatiossa samassa paketissa).

Kokonaisuutena TxGNN-pisteet heijastuvat todennäköisesti läheisyyttä DHEA-siihen liittyvien solmujen ja verenhyytymisväylän solmujen välillä tietokaaviosssa, pikemminkin kuin validoitua terapeuttista suhdetta. Ilman kliinisten tutkimusten tai kirjallisuuden vahvistusta ja mekanistisen ristiriidan ollessa uskottava, tämä ennuste tulisi käsitellä ainoastaan hypoteesinmuodostava signaalina, ei uudelleenkäyttökandidaatiksi, joka olisi valmis arviointiin.

---

## Kliinisten tutkimusten näyttö

Tällä hetkellä asiaa käsittelevät rekisteröidyt kliiniset tutkimukset puuttuvat.

---

## Kirjallisuusnäyttö

Tällä hetkellä asiaan liittyvää kirjallisuutta ei ole saatavilla.

---

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta.

*(Huomio: taustalla oleva data-paketti merkitsee TFDA:n/sääntelyviranomaisen pakkausselosteen Blocking-tietokuiluksi — tämä on ratkaistava ennen turvallisuuteen perustuvaa jatko/ei-jatko -päätöstä.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelu:**
Parhaiten sijoitettu ennustus (hepariinin kofaktori 2:n puutos) ei ole tuettu kliinisillä tutkimuksilla tai kirjallisuudella (L5, puhtaasti mallista johtuva), ja ehdotettu mekanismi voi olla ristiriidassa terapeuttisen tarpeen kanssa — androgeeninen aktiivisuus yhdistetään useammin kohonneeseen verenhyytymisen riskiin kuin antikoagulantti-puutoksen korjaamiseen. Yhdessä MOA-tiedon ja TFDA/Fimean merkintätiedon puuttumisen kanssa on riittämätön perusta tämän kandidaatin edistämiselle.

**Jatkon edellyttävät seuraavat:**
- Prasteronen vaikutusmekanismin (MOA) vahvistaminen DrugBankista tai pääasiallisista farmakologian lähteistä
- Sääntelyviranomaisen pakkausseloste (varoitukset, vasta-aiheet, lääkkeelliset vuorovaikutukset) Blocking-tietokuilun sulkemiseksi (DG001)
- Prekliininen tai farmakodynaaminen tieto DHEA:n vaikutuksesta HCII-aktiivisuuteen/verenhyytymisen riskiin, suuntamekanistisen ongelman ratkaisemiseksi
- Jos tämä ohjelma jatkuu, harkitse uudelleensuuntausta **sklerodermaahaan** (sijoitus 7, sama näyttöpaketti), joka saavutti päätösvaiheen S1 L4-näytöllä — kuusi kohortti/tapaus-vertailututkimusta osoittavat johdonmukaisesti alentunutta seerumin DHEA-S -tasoa järjestelmällisen skleroosipotilailta, jotka korreloivat sairauden vakavuuden kanssa, tarjoten yhtenäisemmän (puutoksentäyttöisen) mekanistisen perustelun kuin parhaiten sijoitettu kandidaatti täällä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

