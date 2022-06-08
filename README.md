# Projeto Mini_lake

## Instruções

Este repositório é um template de um projeto Python `beerlog`: Bruno Rocha e Jefferson.  

## Acompanhamento de aprendizados

```python
# formata todos os codigos das pasta "x"
black -l 79 minilake

# acessar o banco de dados via linha de commando
sqlite3 mini_lake.db
# pra sair utilizar
.quit

# hack remove warnings
import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar
warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

# visualização de dados como excel
from rich.table import Table
from rich.console import Console

# select
minilake list
# insert
minilake add "Letra" "Sour" --flavor=6 --image=8 --cost=5
minilake add "Lagunitas" "IPA" --flavor=7 --image=6 --cost=8

# add uvicorn
poetry add uvicorn

# command
uvicorn minilake.api:api --reload

# documentação integrada
localhost:8000/docs
localhost:8000/redoc

# QUALIDADE DE CODIGO
# verificar error de padronização nos arquivos.py
flake8 minilake/

# reordenação de imports padronização PEP8
isort --profile=black -m 3 minilake/

# test unitário ( qualidade de software )
pytest -v

# test funcional
pytest -s -v tests/test_core.py

# alterando a configuração de banco de dados para test
export MINILAKE_DATABASE__url="sqlite:///testing.db"

# remove a alteração de variavel de ambiente
unset MINILAKE_DATABASE__url

# teste FUNCIONAL com typer

# CI: continuos integration
mkdir -p .github/workflows

```

### Qualidade onde podem ser aplicadas

* Qualidade de Produto
* Qualidade de Projeto
* Qualidade de Infra
* Qualidade de Código
* Qualidade de Software

### CI: continuos integration