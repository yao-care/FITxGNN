# FITxGNN - Suomi: Laakkeiden uudelleenkaytto -ennusteet

[![Website](https://img.shields.io/badge/Website-fitxgnn.yao.care-blue)](https://fitxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Laakkeiden uudelleenkaytto (drug repurposing) -ennusteet Suomelle TxGNN-mallin avulla.

## Vastuuvapauslauseke

- Taman projektin tulokset on tarkoitettu ainoastaan tutkimuskayttoon eivatka ne muodosta laaketieteellista neuvontaa.
- Laakkeiden uudelleenkayttoehdokkaat vaativat kliinisen validoinnin ennen soveltamista.

## Projektin yleiskatsaus

| Kohde | Maara |
|-------|-------|
| **Laakeraportit** | 466 |
| **Ennusteet yhteensa** | 2,539,217 |

## Ennustemenetelmat

### Tietograafimenetelma (Knowledge Graph)
Suora laake-sairaussuhteiden kysely TxGNN-tietograafista, tunnistaen mahdollisia uudelleenkayttoehdokkaita biolaaketieteellisen verkoston olemassa olevien yhteyksien perusteella.

### Syvaoppimismenetelma (Deep Learning)
Kayttaa TxGNN:n esikoulutettua neuroverkon mallia ennustepisteiden laskemiseen, arvioiden uusien terapeuttisten kayttoindikaatioiden todennakoisyytta hyvaaksytyille laakkeille.

## Linkit

- Verkkosivusto: https://fitxgnn.yao.care
- TxGNN-julkaisu: https://doi.org/10.1038/s41591-023-02233-x
