# Verificador de password

## Descrição
- Verificador de regras para um password feito em Python, utilizando o Framework com Django-ninja.
- As regras possiveis são:
  - `minSize`: tem pelo menos x caracteres.
  - `minUppercase`: tem pelo menos x caracteres maiúsculos
  - `minLowercase`: tem pelo menos x caracteres minúsculos
  - `minDigit`: tem pelo menos x dígitos (0-9)
  - `minSpecialChars`: tem pelo menos x caracteres especiais ( Os caracteres especiais são os caracteres da seguinte string: "!@#$%^&*()-+\/{}[]" )
  - `noRepeted`: não tenha nenhum caractere repetido em sequência ( ou seja, "aab" viola esta
condição, mas "aba" não)


## Instalação
- O projeto foi criado utilizando Python 3.10.6, portanto é recomendado que seja utilizado a mesma versão.
- É recomendado usar um ambiente virtual para instalar as dependências.
- Para instalar as dependências, execute o comando `pip install -r requirements.txt`

## Execução
- Acesse a pasta `password_api_app` do terminal e execute o comando `python manage.py runserver`
- O projeto é uma API REST com apenas um endpoint e método permitido, que é o POST.
- Acesse o endpoint `http://localhost:8000/verify/` e envie um JSOn com o seguinte formato:
```json
{
    "password": "string",
    "rules": [
        {
            "rule": "string",
            "value": "string"
        }
    ]
}
```

## Exemplo de JSON
```json
{
"password": "TesteSenhaForte!123&",
	"rules": [
	{"rule": "minSize","value": 20},
	{"rule": "minSpecialChars","value": 2},
	{"rule": "noRepeted","value": 0},
	{"rule": "minDigit","value": 3},
	{"rule": "minUppercase","value": 3},
	{"rule": "minSpecialChars","value": 20}
	]
}
```
A saída esperada é: 
```json
{
	"verify": false,
	"noMatch": [
		"minSpecialChars"
	]
}
```