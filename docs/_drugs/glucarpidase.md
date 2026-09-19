---
layout: default
title: Glucarpidase
parent: Pelkkä mallin ennuste (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glukarpidaasi: Metotreksaatin myrkyllisyyden pelastamisesta diabeettiseen kataraktaan

## Yhden lauseen yhteenveto

Glukarpidaasi (DrugBank DB08898) on rekombinanttu bakteerinen karboksypeptidaasi G2, jota käytetään kliinisesti metotreksaatin nopeaan inaktivointiin potilailla, joilla on heikentynyt munuaisten eritys ja myrkylliset metotreksaatin plasmapitoisuudet. TxGNN-malli ennustaa mahdollista tehokkuutta **diabeettisessa kataraktassa**, mutta tällä ehdokkaalla on tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** sen tukemiseksi, ja näyttöpaketin oma mekanistinen katsaus merkitsee ennusteen biologisesti epäuskottavaksi.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Myrkylliset metotreksaatin pitoisuudet (folaatin antagonistin pelastushoito) — ei sijaita jäsennellyssä `original_indications`-kentässä; johdettu näyttöpaketin mekanistisesta kuvauksesta |
| Ennustettu uusi indikaatio | Diabeettinen katarakta |
| TxGNN-ennusteen pistemäärä | 99.85% (sijoitus 2057) |
| Näyttöaste | L5 |
| Markkinatilanne Suomessa | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla jäsennellyssä tietueessa (`original_moa` on tietoaukko). Näyttöpaketin perustelut kuitenkin toteavat, että glukarpidaasi on rekombinanttu karboksypeptidaasi G2, jonka ainoa vakiintunut farmakologinen rooli on metotreksaatin hydrolyysi inaktiivisiksi aineenvaihduntuotteiksi, jota käytetään potilaiden pelastamiseen metotreksaatin myrkyllisestä altistuksesta munuaisten vajaatoiminnan yhteydessä.

Diabeettisen kataraktan patofysiologia johtuu linssin kristalliinien ei-entsymaattisesta glykosylaatiosta, polyoli/sorbitoli-raidan aktivaatiosta ja oksidatiivisesta stressistä — mikään näistä ei ylitä folaattianalogin aineenvaihduntaa. Näyttöpaketin mekanistinen analyysi selvästi toteaa, että glukarpidaasin entsyymiaktiivisuuden ja linssin patologian välillä ei ole tunnettu biologinen yhteys, ja glukarpidaasilla ei ole vakiintunutta farmakokineettistä perustelua silmäkudoksen altistumiselle.

Merkittävää on, että kaikki 10 tämän lääkkeen TxGNN:n korkeimmin sijoittuneita ennusteita ovat kataraktan alityyppejä tai diabeettista retinopattiaa, lähes samoin pistemääryin (99.82–99.85%) tiiviisti ryhmittyneenä. Tämä kuvio on yhtenevämpi tilastollisen artefaktin kanssa upotusavaruuden läheisyydessä kuin aito farmakologinen signaali, ja se tulisi painottaa vastaavasti kun tulkitaan pistemäärää.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröity asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä kirjallisuuden näyttöä ei ole saatavilla.

## Markkinatilanne Suomessa

Glukarpidaasi ei ole markkinoilla Suomessa; markkinoinnin lupia ei ole rekisteröity (0 lupaa).

## Turvallisuusnäkökulmat

Katso pakkausseloste turvallisuustiedoista.

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Glukarpidaasin diabeettiselle kataraktalle (tai muille 9 ennustetulle kataraktan/retinopatian indikaatiolle) ei ole nolla kliinisen tutkimuksen eikä kirjallisuuden näyttöä, näyttöaste on L5 (vain mallin ennuste), ja näyttöpaketin oma mekanistinen katsaus ei löydä uskottavaa biologista yhteyttä metotreksaatin inaktivoinnin ja silmän linssin/verkon patologian välille. Lääkettä ei myöskään markkinoida Suomessa.

**Jatkaaksemme tarvitaan seuraavaa:**
- TFDA/Fimea pakkausseloste-tiedot turvallisuuden tietoa estävän aukon ratkaisemiseksi (DG001)
- Vahvistetut jäsennellyt alkuperäisen indikaation ja vaikutusmekanismin tiedot DrugBankista tai sääntelyhyväksynnän merkinnöistä (DG002)
- Riippumaton kirjallisuus-/prekliininen haku erityisesti tutkien mahdollisia silmän linssin tai verkon altistumis-/farmakokineettisiä tietoja glukarpidaasille
- TxGNN-signaalin uudelleenarviointi, kun otetaan huomioon epäilyttävä lähes samoin pistemääryin (99.82–99.85%) 10 katarakta-/retinopatia-termissä klusteroitu ryhmittymä, mikä viittaa mahdolliseen upotusavaruuden artefaktiin todellisen uuden käyttöindikaation signaalin sijasta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

