# pythonanalisedados
##### Data Science Academy
##### Fundamentos de Linguagem Python Para Análise de Dados e Data Science
##### Aula 1
- Exibindo mensagens com função print e somando valores
##### Aula 2
- Calculadora 4 operações básicas
##### Aula 3
- Algorítmo booble sort
##### Capítulo 4
- Cap04-01-numeros
- Cap04-02-variavel
- Cap04-03-strings
- Cap04-04-listas
- Cap04-05-dicionarios
- Cap04-06-tuplas
- Exercicios_cap04
##### Capítulo 5
- Cap05-01-condicionais
- Cap05-01-placeholder
- Cap05-02-loop_for
- Cap05-03-loop-while
- Cap05-04-range
- Cap05-05-metodos
- Cap05-06-funcoes
- Cap05-07-lambda
- Cap05-08-List-comprehesion

##### Capítulo 6
- Cap06-01-arquivos
    - Read, Write arquivos usando Python
- Cap06-02-txt-csv-json
    - Manipulação de arquivo de TXT usando Python
    - Manipulação de arquivo CSV usando Python
    - Manipulação de arquivo JSON usando Python
    - Web Scraping usando Python
- Cap06-03-módulos-e-pacotes
    - Evidênciando diferenças entre módulos e pacotes
- Cap06-04-Map
    - Usando a função map
- Cap06-05-Reduce
    - Usando a função reduce
- Cap06-06-Filter
    - Usando a função filter
- Cap06-07-Zip
    - Usando a função zip
- Cap06-08-Enumerate
    - Usando a função enumerate
- Cap06-09-Tratamento de Erros e Exceções
    - Erros e Exceções
- Cap06-10-Regex Python
    - Regex com função "re" e regex normal
##### Capítulo 7
- Cap07-01-Prática de exercícios
    - Jogo da forca
    - Jogo da forca versão 2
    - Pseudocodigo jogo da forca
- Cap08-01-POO-classes
    - Classes
        - métodos
        - atributos
        - objetos

- Cap08-02-Objetos</br>
`Uma classe tem métodos e atributos, tudo em Python são objetos, então um objeto tem métodos e atributos. Objetos são uma instância de uma classe.`
- Cap08-03-Métodos</br>
`O primeiro método que todas as classes devem fornecer é o construtor. O construtor define a maneira como os objetos de dados são criados. Para criar um objeto Fraction, precisaremos fornecer dois dados, o numerador e denominador. Em Python, o método construtor é sempre chamado `<strong>__init__</strong>` (com dois underscores antes e depois de init).`

```
    class Somar:

    def __init__(self, param1, param2):

        self.parametro1 = param1
        self.parametro2 = param2
```
`
- Cap08-04-Herança
    - Sintaxe:<br/>
A sintaxe básica para herança em Python é a seguinte:
`
```
class ClassePai:
    def __init__(self, atributo1):
        self.atributo1 = atributo1

    def metodo_pai(self):
        print("Método da classe pai")

class ClasseFilha(ClassePai):
    def __init__(self, atributo1, atributo2):
        super().__init__(atributo1)  # Chama o construtor da classe pai
        self.atributo2 = atributo2

    def metodo_filha(self):
        print("Método da classe filha")

```
- Cap08-05-Polimorfismo
    - Sobrescrita de Métodos (Overriding)
    - Métodos com o Mesmo Nome (Duck Typing)
    - Jogo da forca (POO)


- Cap09-Funções Numpy