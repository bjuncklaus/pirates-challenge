# Data Pirates Challenge
![alt-text](https://github.com/bjuncklaus/pirates-challenge/blob/master/pirate-icon.png "pirate icon")
## Pirate English Version
(_scroll down for English Version_)

This me solution fer Neoway's [data pirates challenge](https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md).

### Requirements:

I **strongly suggest** ye use some sort o' virtual environment, like [virtualenv](https://virtualenv.pypa.io/en/latest/). In order t' run th' project ye will needs:
* [Python](https://www.python.org/) 3+
* [Scrapy](https://scrapy.org/) 1.7.2

If ye wants t' run th' unit tests ye will also needs:
* [Requests](https://pypi.org/project/requests/) 2.22.0

Ye can loot 'n install th' above libs usin' [pip](https://pypi.org/project/pip/). Aft ye loot th' source code, go t' th' **root folder** 'n run `pip install -r requirements.txt`.

#### Note
I'm working on dockerizing everything on this [branch](https://github.com/bjuncklaus/pirates-challenge/tree/feature/dockerization).

### Execution:
Shall we capture some data now? T' execute th' code go t' thee root folder 'n run `scrapy crawl correios -o data/data.jl`, this will scrapy thee data from thee [correios](http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm) website 'n save it in th' _data folder_ fer some data analysis later!

Th' data should look similar t' this:

```json
{"uf": "DF", "record": {"localidade": ["Brasu00edlia"], "faixa_de_cep": ["70000-001 a 72799-999"]}}
{"uf": "AP", "record": {"localidade": ["Amapu00e1", "Calu00e7oene"], "faixa_de_cep": ["68950-000 a 68959-999", "68960-000 a 68972-999"]}}
```
(or take a look at this [sample file](https://github.com/bjuncklaus/pirates-challenge/blob/master/data/sample.jl))


Where `uf` be th' states acronym 'n th' `log` object contains th' data from cities o' th' specific state where `localidade` be th' name o' thee city 'n `faixa_de_cep` be th' zip code range o' that city.

#### Note
A `record` can contain several cities, therefore `localidade` 'n `faixa_de_cep` are both arrays where its indexes 'ave a one-t'-one mappin' (e.g. `localidade[2]` be directly related t' `faixa_de_cep[2]`).


---


## English version
This my solution for Neoway's [data pirates challenge](https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md).

### Requirements:

I **strongly suggest** you use some sort of virtual environment, like [virtualenv](https://virtualenv.pypa.io/en/latest/). In order to run the project you will need:
* [Python](https://www.python.org/) 3+
* [Scrapy](https://scrapy.org/) 1.7.2

If you want to run the unit tests you will also need:
* [Requests](https://pypi.org/project/requests/) 2.22.0

You can download and install the above libs using [pip](https://pypi.org/project/pip/). After you download the source code, go to the **root folder** and run `pip install -r requirements.txt`.

#### Note
I'm working on dockerizing everything on this [branch](https://github.com/bjuncklaus/pirates-challenge/tree/feature/dockerization).

### Execution:
Shall we get some data now? To execute the code go to the root folder and run `scrapy crawl correios -o data/data.jl`, this will scrapy thee data from thee [correios](http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm) website and save it in the _data folder_ for some data analysis later!

The data should look similar to this:

```json
{"uf": "DF", "record": {"localidade": ["Brasu00edlia"], "faixa_de_cep": ["70000-001 a 72799-999"]}}
{"uf": "AP", "record": {"localidade": ["Amapu00e1", "Calu00e7oene"], "faixa_de_cep": ["68950-000 a 68959-999", "68960-000 a 68972-999"]}}
```
(or take a look at this [sample file](https://github.com/bjuncklaus/pirates-challenge/blob/master/data/sample.jl))


Where `uf` is the states acronym and the `record` object contains the data from cities of the specific state where `localidade` is the name of thee city and `faixa_de_cep` is the zip code range of that city.

#### Note
A `record` can contain several cities, therefore `localidade` and `faixa_de_cep` are both arrays where its indexes have a one-to-one mapping (e.g. `localidade[2]` is directly related to `faixa_de_cep[2]`).