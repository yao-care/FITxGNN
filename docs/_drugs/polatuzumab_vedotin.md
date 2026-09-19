---
layout: default
title: Polatuzumab Vedotin
parent: Pelkkä mallin ennuste (L5)
nav_order: 302
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Polatuzumab vedotin: B-solujen lymfoomasta (DLBCL) HER2-positiiviseen rintasyöpään

## Yhden lauseen yhteenveto

Polatuzumab vedotin on anti-CD79b-vasta-aine-lääke-konjugaatti (ADC), jonka tunnettu lääkeryhmä kohdistuu B-solujen lymfoomiin, kuten DLBCL:hen; vahvistetut alkuperäisen indikaation ja sääntelytiedot tälle todistusaineistolle eivät ole vielä käytettävissä. TxGNN-malli ennustaa mahdollista tehokkuutta **HER2-positiiviseen rintasyöpään**, ennustepisteen ollessa **99.34%**, mutta **nolla kliinistä tutkimusta** ja **nolla julkaisua** tällä hetkellä tukee tätä suuntaa — tämä on pelkästään malli-pohjainen signaali.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei vahvistettu tässä todistusaineistossa (lisenssiteksti tai indikaatiotiedot eivät saatavilla); lääkeryhmän tausta viittaa B-solujen lymfoomiin (esim. DLBCL) |
| Ennustettu uusi indikaatio | HER2-positiivinen rintasyöpä |
| TxGNN-ennustepiste | 99.34% |
| Todistusaineiston taso | L5 |
| Markkinatilanne Suomessa | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Polatuzumab vedotinin yksityiskohtainen toimintamekanismia koskeva tieto ei ole saatavilla tässä todistusaineistossa. Tarjotun uudelleenkäyttöperustuksen perusteella lääke on CD79b:tä kohdistettu vasta-aine-lääke-konjugaatti (ADC) — CD79b on B-solujen reseptorikomplementin komponentti, jonka ilmaisu on fysiologisesti rajoittautunut B-lymfosyyttisarjaan (normaalit B-solut ja B-solujen lymfoomat, kuten DLBCL).

HER2-positiivinen rintasyöpä sen sijaan on epiteelistä lähtöisin oleva kasvain, jota ajaa HER2/ERBB2-geeniamplifikaatio ja seuraava PI3K/MAPK-signalointi — signaaliväylä, jolla ei ole tunnettua leikkauspistettä CD79b/B-solujen reseptori-signaloinnin kanssa. Kirjallisuudessa ei ole raportoitu CD79b:n ilmaisusta rintasyöpäsoluissa.

TxGNN-pistemäärä 0.9934 heijastaa graafisen neuroverkkolinkkiennusteen tulosta, joka saattaa siepata "syöpä"- ja "ADC-lääke"-solmuluokkien välistä samanesiintymiskuviota tietoverkossa mieluummin kuin aito molekyylitason mekanistinen todiste. Yhdistettynä alkuperäisten MOA-tietojen puuttumiseen, tällä ennusteella puuttuu tällä hetkellä varmennettava biologinen perusta.

---

## Kliinisen tutkimuksen todistusaineisto

Tällä hetkellä ei ole rekisteröityjä liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todistusaineisto

Tällä hetkellä liittyvää kirjallisuutta ei ole saatavilla.

---

## Markkinatilanne Suomessa

Polatuzumab vedotinilla ei tällä hetkellä ole markkinointilupia Suomessa (0 lupaa rekisterissä; markkinatilanne: Ei markkinoilla).

---

## Sytotoksisuus

| Kohde | Sisältö |
|------|--------|
| Sytotoksisuuden luokittelu | Kohdennettu lääkehoito — vasta-aine-lääke-konjugaatti (ADC), uudelleenkäyttöperustuksen mukaan (anti-CD79b ADC) |
| Luuydinsupression riski | Katso pakkausselosteen varoitukset ja varotoimet |
| Emetisuuden luokittelu | Katso pakkausselosteen varoitukset ja varotoimet |
| Valvontakohteet | Katso pakkausselosteen varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausselosteen varoitukset ja varotoimet |

---

## Turvallisuuteen liittyvät näkökohdat

Katso pakkausselosteen turvallisuustietoja.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelu:**
TxGNN-pistemäärä on korkea, mutta mitään tukevaa kliinistä tutkimusta tai julkaisua ei ole, eikä lääkkeen tunnetulla mekanismilla (CD79b/B-solujen reseptori-signalointi) ole vakiintunutta yhteyttä HER2-ohjattuun rintasyöpäbiologiaan. Tämä on L5-luokituksinen, pelkästään mallipohjaisesti ennustettu signaali, jolla on epäsuotuisa mekanistinen perustelu, eikä se täytä kriteerejä edistyä alkuperäisen seulonnan ohi.

**Jotta edistyminen olisi mahdollista, tarvitaan seuraavaa:**
- TFDA/Fimean pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estää (DG001)
- Vahvistettu alkuperäinen indikaatio ja muodollinen MOA-dokumentaatio DrugBank/sääntelylähteiden kautta (DG002)
- Lääkkeen vuorovaikutus (DDI)-tiedot — nykyinen kysely palautti not_found
- Mikä tahansa ilmaantuva prekliininen tai kliininen todiste, joka linkittää CD79b/ADC-mekanismin HER2-positiiviseen rintasyöpään, ennen kuin tätä indikaatiota uudelleen harkitaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

