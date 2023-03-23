<table>
<tr>
<td>
<a  href= "https://www.ipt.br/"><img  src="https://www.ipt.br/imagens/logo_ipt.gif"  alt="IPT"  border="0"  width="70%"></a>
</td>
<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="30%"></a>
</td>
</tr>
</table>

<font size='20'><center>
Concepção de sistema de automação industrial
</center></font>

# **Sumário**

- [**Sumário**](#sumário)
- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Parceiro de Negócios](#parceiro-de-negócios)
  - [Definição do Problema](#definição-do-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
- [Análise de Negócio](#análise-de-negócio)
  - [Contexto da indústria](#contexto-da-indústria)
  - [Análise financeira](#análise-financeira)
  - [Análise SWOT](#análise-swot)
  - [Value Proposition Canvas](#value-proposition-canvas)
  - [Matriz de Riscos](#matriz-de-riscos)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Módulos do Sistema e Visão Geral (Big Picture) (1.0)](#módulos-do-sistema-e-visão-geral-big-picture-10)
    - [Croqui da Solução](#croqui-da-solução)
  - [Módulos do Sistema e Visão Geral (Big Picture) (2.0)](#módulos-do-sistema-e-visão-geral-big-picture-20)
  - [Sensores](#sensores)
    - [Testes preliminares de resposta dos sensores](#testes-preliminares-de-resposta-dos-sensores)
    - [Demonstrações de Funcionamento dos Sensores](#demonstrações-de-funcionamento-dos-sensores)
  - [Atuadores](#atuadores)
    - [Testes preliminares de resposta dos atuadores](#testes-preliminares-de-resposta-dos-atuadores)
- [Análise de Experiência do Usuário](#análise-de-experiência-do-usuário)
  - [User Stories](#user-stories)
  - [Protótipo de interface com o usuário](#protótipo-de-interface-com-o-usuário)
  - [Dispositivos Eletrônicos](#dispositivos-eletrônicos)
    - [Dispositivo acoplado à garra do braço robótico (eletroímãs e sensor infravermelho)](#dispositivo-acoplado-à-garra-do-braço-robótico-eletroímãs-e-sensor-infravermelho)
    - [Balança invertida: sistema de pesagem utilizando célula de carga](#balança-invertida-sistema-de-pesagem-utilizando-célula-de-carga)
    - [Dispositivo principal: Raspberry Pi Pico W e Ponte H](#dispositivo-principal-raspberry-pi-pico-w-e-ponte-h)
  - [Dispositivos Mecânicos](#dispositivos-mecânicos)
    - [Bandeja Radial](#bandeja-radial)
  - [Validação de Dispositivos](#validação-de-dispositivos)
- [Referências](#referências)
- [Anexos](#anexos)


# Autores

[Amanda Ribeiro Fontes](https://www.linkedin.com/in/amanda-fontes/)
[Gabriel Pascoli](https://www.linkedin.com/in/gabriel-pascoli-73733b200/)
[Gabriela Barretto Dias](https://www.linkedin.com/in/gabriela-dias-38b484250/)
[Gustavo Francisco Neto Pereira](https://www.linkedin.com/in/gustavo-pereira1/)
[João Pedro Gonçalves Carazzato](https://www.linkedin.com/in/jo%C3%A3o-pedro-gon%C3%A7alves-carazzato-147120231/)
[Kil Matheus Gomes Teixeira](https://www.linkedin.com/in/kil-matheus-gomes-teixeira-78257020a/)
[Luiz Fernando da Silva Borges](https://www.linkedin.com/in/sbluizfernando/)

# Visão Geral do Projeto

## Parceiro de Negócios

O Instituto de Pesquisas Tecnológicas configura uma das maiores instituições de pesquisa do Brasil. Fundado em 1899, o IPT é vinculado à Secretaria de Desenvolvimento Econômico do Estado de São Paulo e colabora significativamente para o processo de desenvolvimento do país. É reconhecido nos meios técnicos nacionais e internacionais por, sobretudo, atender às demandas da sociedade e do setor produtivo.

A atuação multidisciplinar do instituto contempla diferentes segmentos: energia, transporte, petróleo e gás, meio ambiente, construção civil, cidades, saúde, segurança e outros. As soluções designadas pelo IPT, bem como os serviços prestados pela instituição, destinam-se a suprir as lacunas tecnológicas apresentadas pelos múltiplos setores com os quais a entidade trabalha.

## Definição do Problema

*Descrição_do_problema*

## Objetivos

### Objetivos gerais

O objetivo do parceiro é automatizar o processo de ensaio de separação de materiais magnéticos, bem como sua análise — procedimentos realizados pelo laboratório para seus respectivos clientes. Dessa maneira, o IPT visa à realização de ensaios de maior eficiência a partir da padronização desse processo, cortando custos e otimizando os procedimentos envolvidos.

### Objetivos específicos


# Análise de Negócio

## Contexto da indústria

*Contexto_da_indústria*

## Análise financeira

Considerando o processo de separação magnética realizado, atualmente, pelo Instituto de Pesquisas Tecnológicas, dispõem-se abaixo os valores referentes ao início da operação.

| **Componente**| **Valor** |
|--- |--- |
| Operador | R$ 150,00 |
| Ímã de Neodímio | R$ 2000,00 |
| Bandejas (x 3) | R$ 138,00 |
| Saco Zip Lock (x 10) | R$ 24,00 |
| Total | R$ 2312,00 ||

**<font  size=2> Tabela 1 — Valores correspondentes aos componentes do procedimento de separação magnética atual </font>**

| **Componente**| **Valor** |
|--- |--- |
| DOBOT Magician Lite| R$ 15000,00 - R$ 25000,00 |
| Raspberry Pi Pico W | R$ 80,00 - R$ 110,00 |
| Eletroímã (x 4) | R$ 240,00 |
| Total | R$ 15320,00 ||

**<font  size=2> Tabela 2 — Valores correspondentes aos componentes da solução desenvolvida para o novo procedimento </font>**

Em suma, a qualidade dos ensaios constitui o elemento que agrega valor à solução. Com a retirada da mão de obra, cuja ação no ensaio passa a ser automatizada, o tempo ganho pelo operador para outras tarefas é significativo a longo prazo, salvando um custo operacional para os stakeholders. Diante da análise dos custos da operação e retorno dos ensaios — supondo o valor de R$ 2000,00 por ensaio —, a solução se pagaria em, aproximadamente, nove ensaios.

## Análise SWOT
![](https://lh6.googleusercontent.com/zG8EnpZDgBawCTeDtsdIlDg2p6Ucljp306zIdN2e-vJLtzRxG_w4UnhNh5kEH32OZFgOrrOLHLhEsK2zV2kvmrZR1lcEbKyZ-tMikonjjLosjdmX5_fPNudNE6e7JZkfUH1QL_X20P0MP9xkGtSSoBw)

**<font size=2> Figura 1 — Análise SWOT (forças, oportunidades, fraquezas e ameaças) do Instituto de Pesquisas Tecnológicas </font>**

## Value Proposition Canvas
![](https://lh5.googleusercontent.com/xYxOS-4i-mqXFikfxJAc7g0b_FhPT96ku_k4FdCSHb3YkBMeSY1eqs4W_UaXE3cQJeg-VFHbNcAk1VyiD-jfpKKON3ua7EBH9ka5fBGwX1h3VGxSt3bfBo4WJKTvUS08PMLSops4Ap2DkbRSgd3jYMk)

**<font size=2> Figura 2 — Value Proposition Canvas do atual procedimento de separação magnética realizado pelo IPT </font>**

## Matriz de Riscos
![](https://lh6.googleusercontent.com/PsuqnxqBCrQZD-gd0dvqBnxThe2AOZWL6vFaLv27mIcgcPJA148UVNPkAnvzPRf696h6kdDlmeOSMsuxcbGsQ7I_WNAlkO6A7GrB65i5mTCvBZB_YU6-Kf9qKl5sqVSC8ANSYEWgnSgn2K9Eush8ml0)

**<font size=2> Figura 3 — Matriz de Riscos da solução desenvolvida </font>**

# Arquitetura do Sistema

## Módulos do Sistema e Visão Geral (Big Picture) (1.0)

| **Componente**| **Descrição da função/características/requisitos** |
|--- |--- |
| DOBOT Magician Lite | Será utilizado o braço robótico Dobot Magician Lite, produto desenvolvido pela Minipa. O robô é inteligente, multifuncional e introduz uma série de métodos de interação entre software e hardware, com foco em um processo de aprendizagem baseado na liberdade de criação. |
| Raspberry Pi Pico W | Constitui um poderoso microcontrolador com conexão wireless que conta com uma série de aplicações. No contexto do projeto, será programado em MicroPython. É considerada uma ferramenta compacta e de baixo custo. |
| Eletroímã | Peça composta por um solenóide com um núcleo de material ferromagnético. Ao ser percorrido por um campo elétrico, gera ao seu redor um campo magnético. No projeto, será utilizado para o processo de separação magnética e ficará acoplado ao braço robótico. ||

**<font  size=2> Tabela 3 — Componentes do sistema e descrição de suas respectivas funções, características e requisitos </font>**

  
### Croqui da Solução
![](https://lh6.googleusercontent.com/ztk3zc9XaL34iNjuaPBuNVShRFIyjokR2Jst5DncvFbHIP54xMl98ww9CKMHN8QmR6n_dpUhHCBDjhhLnVa-wM5NKoTncqdeOXLbuwEs-bQmc2i5oCHimDtJOG6Kifzzl1vRTCi0IrapvS6h1T3StKI)
  **<font  size=2> Figura 4 — Versão inicial do croqui da solução </font>**

![](https://lh6.googleusercontent.com/h4amFfWdV1cBVHwKohGJG-WkZxRD2XilNjKyljW65xQtF6-O_A-T3Vr2XQTKXalTua54MzlmMWVOQPJDdET_461QWDJG2EaT0YILkZ0aF1DRAhSqUgUCoRmJkkrOlTCSnLFsZ_9a8OftsXZsOJtS0iA)
  **<font  size=2> Figura 5 — Versão inicial do dispositivo mecânico de suporte para eletroímãs </font>**
  

## Módulos do Sistema e Visão Geral (Big Picture) (2.0)
![](https://lh4.googleusercontent.com/Z5mUwJhEBQMw7qMIhjXzP2YzD2WnL8AAS5TnRI3obXeeZ5wV_fIfszd9qe3LvEW1ql9qz9bZnjREranW4u2LUhCnXDGfMPerODt9Z6T7X5SKTqfQKILhZ0A05YJ4FuuEE-oZA1XZSNeos0sty9EX2jE)
    **<font  size=2> Figura 6 — Diagrama da solução </font>**


| **Componente / Conexão**| **Descrição da função** | Tipo: entrada / saída / atuador |
|--- |--- | --- |
| Eletroímã, fios | Recebe uma corrente do Raspberry Pi Pico W, por meio da qual gera um campo eletromagnético. Espera-se que o ímã atraia os materiais interessantes para o ensaio. | Entrada: 12V |
| Raspberry Pi Pico W, fios (Micro USB) | Microcontrolador principal da solução, responsável por se comunicar via serial com o script python do braço robótico, receber e analisar dados dos sensores ao longo da operação e atuar perante eles. | Entrada: Sensores, dados ( Leituras analógicas). Saída: Volts, dados |
| Célula de carga + Amplificador Operacional | Sensor eletromecânico que possibilita a verificação da variação de força ou peso de uma determinada estrutura. (Bandeja com os materiais ferromagnéticos). | Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga) |
| Sensor de distância | Sensor infravermelho que nos permite converter suas leituras por meio de um cálculo polinomial de quinto grau a uma determinada distância em cm. (Braço e bandeja). | Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga) |
| Ponte H | Utilizado como regulador da corrente do eletroímã | Entrada: Energia elétrica. Saída: Energia elétrica |

**<font  size=2> Tabela 3 — Componentes do sistema contendo suas respectivas formas de conexão, funções e especificações relacionadas a entrada e saída </font>**

## Sensores

### Testes preliminares de resposta dos sensores

**Sensor: 
Função:
Controle:
Entrada esperada:
Saída esperada:
Entrada obtida:
Saída obtida:**

**Sensor: 
Função:
Controle:
Entrada esperada:
Saída esperada:
Entrada obtida:
Saída obtida:**

Começamos os testes, primeiramente, buscando entender os sensores que precisávamos para o projeto, a fim de deixá-lo mais completo. A partir disso, entendemos a necessidade de um **sensor de distância**, para manter o teste o mais preciso possível a partir das necessidades do cliente (manter a mesma distância para maior precisão do processo) eliminando os pontos negativos que o robô tinha por atuar sozinho. Os testes desse sensor foram realizados em junção a um copo de café, atuando com o objeto que queríamos descobrir a distância, funcionando da seguinte forma: possuindo duas lentes, a primeira emite uma luz infravermelha enquanto a segunda captura os sinais da mesma, essa captura funciona através da reflexão da luz na superfície do objeto/local que queremos saber a distância, ao retornar a segunda lente, a partir da intensidade que a luz retorna, é possível descobrir a distância através de um fórmula, medindo distâncias entre 4 a 30 cm com um máximo de 2 cm de desvio da medida real. Em seguida, decidimos utilizar uma **célula de carga** (1kg) e um módulo conversor hx711 específico para realizar leituras analógicas melhores, para verificar a variação de peso na bandeja de deposição de material ferromagnético já minerado. Para o teste, utilizamos dois mini ímãs colocados um em seguida do outro, para assim analisar as variações nas leituras da célula. Concluímos que o funcionamento dela seria eficaz para nossa solução uma vez que sua sensibilidade permitirá que encerramos o processo de mineração com precisão, ou seja, quando já não ocorrer deposição de ferro magnético minerado neste ensaio.

### Demonstrações de Funcionamento dos Sensores

Abaixo, encontram-se os vídeos de demonstração de funcionamento dos sensores utilizados na solução.

[<img src="https://lh3.googleusercontent.com/fqUKYFc17_odvZCvnTXnoRLqCDH9Pn9qDU89iT06e85d7JCMgehLY_zv11d5XwpVpe9WBhRMjyfWFEQnsnYrQ1qyxWmC6A1tT2TWTOM-Va5HO0muF4CpKcszElloyR_C5pqJr0lwGDwhx7vwfNHzgyg" width="100%">](https://drive.google.com/file/d/1Ca5yPUheEd5piRgm2pBVEWkggLV0Kput/view?usp=sharing/)
**<font size="2"> Vídeo para demonstração da calibração do sensor de distância infravermelho </font>**

[<img src="https://lh6.googleusercontent.com/auAXAe9Xtx8LeL_hgrhevCSoSas-2hgLQiDJkmaKQMo5Aln3AQPqphcAsPrAwtK9bnkqbQE60VdnC7FYCSS_ISZA1q_zkiNb_pNwf5CONbB9MUBZJx5vqdt1c2HjwwsXzADE1AOcUq4_KOQLKPHPiGU" width="100%">](https://drive.google.com/file/d/1_PykpKwE5UDx0YWhsY6CiHbBpMDh4OsE/view?usp=sharing)
**<font size=2> Vídeo para demonstração da leitura da célula de carga </font>**

## Atuadores

### Testes preliminares de resposta dos atuadores

Atuador: 
Função:
Controle:
Entrada esperada:
Saída esperada:
Entrada obtida:
Saída obtida:

 Diante das necessidades do projeto, os atuadores principais seriam o **braço robótico**, o microcontrolador **Raspberry Pi Pico W**, uma **ponte H** e os **eletroímãs**. A princípio, o braço poderá ser manipulado por meio de um script em Python que irá conter os comandos ideais para realizar sua movimentação. Assim, será possível realizar adaptações para cada ensaio diante dos dados gerados pelos sensores e as ferramentas englobados na solução. O microcontrolador Raspberry ficará responsável pela centralização da solução, dispondo dos dados dos sensores e se comunicando com os scripts de outros atuadores via serial. Por exemplo, em contato com o script do braço robótico previamente citado, ele atualizará as informações necessárias para o procedimento ter a melhor acurácia e precisão possível, como o momento de finalizar o ensaio e a distância que ele precisa se movimentar para se posicionar corretamente sobre a bandeja.

Dando início aos testes, foi possível realizar a movimentação do braço de acordo com suas respectivas dimensões e a das ferramentas presentes no ensaio (bandeja), com o eletroímã já acoplado a ele e a um raspberry juntamente a uma ponte H. Com isso, foi possível realizar um protótipo crítico da solução, uma vez que seus principais componentes e funcionalidades estavam presentes. Foi possível observar o braço percorrendo o caminho já delimitado em seu script em conjunto com o acionamento e desligamento do eletroímã nos momentos apropriados.

# Análise de Experiência do Usuário

## User Stories

1. Enquanto operador do ensaio de separação de minérios, quero automatizar o processo, a fim de que este se torne mais eficiente.

2. Enquanto operador do ensaio, quero que um único ímã seja suficiente para realizar a separação de material magnético.

3. Enquanto operador do ensaio, quero parametrizar as variáveis envolvidas no processo, a fim de obter resultados precisos sob múltiplas circunstâncias.

4. Enquanto operador responsável pelas etapas envolvidas no ensaio, quero ser avisado pelo robô quando ele finaliza o ensaio.  

5. Enquanto operador responsável pelas múltiplas etapas envolvidas no ensaio, gostaria de gerar relatórios automaticamente, para analisar, com maior eficiência, os resultados do ensaio.

 
## Protótipo de interface com o usuário

Abaixo, encontram-se as imagens relativas à prototipação da interface gráfica por meio da qual será possível manipular e configurar o robô.

A primeira imagem mostra como seria a tela de início, tem como principal objetivo mostrar o Status de todas as integrações da solução. Qual é a situação atual do Robô, que tipo de comando ele está recebendo e retornando, e a situação dos componentes, se o imã está em funcionamento e com quanto de voltagem está trabalhando, qual é o peso da bandeja final e se o sistema de revolvimento está em funcionamento. Na lateral direita de página, podemos ver controles que podem movimentar o robô de maneira mais precisa e linear, podendo mover os 3 eixos de coordenadas, uma de cada vez. Tambem pode-se reparar no campo mais abaixo, o controle de atuadores na qual o mesmo pode acionar o compente acoplado utilizando voltagem ou pneumático.

![](https://lh4.googleusercontent.com/-leIWCVZ6h71iuO5nrKRNCiL6M3v2s-F6YT3wfqj0WZ_n9rTOn_-JtPe_AKyriKC6r2yKJwvpkDY7q4fpvTuPOmWiN0arAbJAvKxDDWQNKsdRn00KxmeLaTNXBvXr0R1pZT9EUWhXsyjWl4k0Xk_3G8)
![](https://lh3.googleusercontent.com/AAZiukdZP169G3rSsd7Mjdb5XNqiA1DmRrz5wreyyGKyAWW7B-RLvG1KOppVzq9wZypDRm8BksFqkm-j6af3J6eeuTFOCKVYBPaA_y-oCN19bxBpjudHgHvxYOhdAZmhhJhdXBlPmbbqtx3rzBkM8BE)![](https://lh6.googleusercontent.com/OW5uM3qnbidyQepBadF9RvSuumPyCVdJYkqrgdwJfAM97-keoVPAuGMx9JuE7CCqDapeCSrc6VBYfo1D8VZ6nQgTq7gsUWm5gjuk2Dnt0-wdf94ZfrX8OfGU3L5kO9a8zZHVNnNBTfHVSeBkijjpOMg)

## Dispositivos Eletrônicos

### Dispositivo acoplado à garra do braço robótico (eletroímãs e sensor infravermelho)

Materiais utilizados:

- Dois eletroímãs de 9V.

- Uma placa universal (3cmX4cm)

- Um Led RGB

- Jumpers, Solda e Parafusos (2)

- AutoDesk Inventor para modelagem

- Impressora 3D  

Diante da necessidade de acoplar os eletroímãs e o sensor infravermelho em uma extensão do braço robótico e proteje-los (principalmente da água utilizada nos ensaios), decidimos por colocar-los na parte interior de uma estrutura com o formato de um martelo, na cabeça se encontram os sensores acoplados à placa universal devidamente ligados e o cabo servirá para a conexão braço-suporte e para passar o devido cabeamento que acompanhará o braço robótico por cima. Optamos por deixar o espaço dos eletroímãs e do sensor infra-vermelho pré-estabelecidos e bem delimitados para que não se movimentem durante os ensaios, a fim de uma melhor precisão e acurácia destes. Segue abaixo o esquemático desta proposta com as devidas medidas para sua função:

![Suporte Eletroimã.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Suporte%20Eletroim%C3%A3.jpg?raw=true)

![Tampa Eletroimã.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Tampa%20Eletroim%C3%A3.jpg?raw=true)
  
![Eletroímãs e Sensor Infravermelho](https://lh3.googleusercontent.com/ao0c9nc6mhrP9Fmeg4wEZPEusdrDQIJ61dK5RoYkbhAcVE2yyj0SdazAUlfMO8u-v_EOarZFIAyTD3S7Z383lcbsPOpWUL6tHecSAR_HuqibPbG7mAPTlTrm3K7pNZkhVb2WumgjS6tATrm04RXj-wc)

![Eletroima2.jpeg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Eletroima2.jpeg?raw=true)

![Elertroima3.jpeg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Elertroima3.jpeg?raw=true)   

[Modelo 3D - Suporte Eletroímãs](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/desenho_suporte_eletroima/modelo%203D/arquivo%20de%20modelo%203d/Suporte%20Eletroim%C3%A3.ipt)

[Modelo 3D - Tampa Eletroímãs](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/desenho_suporte_eletroima/modelo%203D/arquivo%20de%20modelo%203d/Tampa%20Eletroim%C3%A3.ipt)

### Balança invertida: sistema de pesagem utilizando célula de carga

Materiais utilizados:

- Célula de Carga (1KG)

- Dois Parafusos e duas porcas

- Duas madeiras MDF (10cmX6cm)

- Imãs de Neodímio (Utilizamos dois de um HD)

- AutoDesk Inventor para modelagem

- Impressora 3D

A fim de analisar a todo o momento o resultado da mineração magnética, decidimos utilizar de uma balança invertida, contando com dois imãs de neodímio acoplados na parte superior do sistema (visando que a deformação da célula seja por indução magnética, por isso o nome) e a estrutura física necessária para manter a célula de carga estável (madeiras presas em cada uma de suas devidas extremidades com os parafusos e porcas). Com isso desenvolvemos esse esquemático responsável por interagir com os materiais magnéticos já minerados e constantemente indicar se houve uma nova deposição deste. Assim, caso seja o momento de encerrar o ensaio, saberemos com mais precisão diante das medidas fornecidas por esse sistema. Segue o esquemático:

![Sistema de Pesagem.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Sistema%20de%20Pesagem.jpg?raw=true)

![BI-Cima.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Cima.jpg?raw=true)
  
![BI-Cima2.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Cima2.jpg?raw=true)
  
![BI-Lado.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Lado.jpg?raw=true)
  
[Modelo 3D - Balança Invertida](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/desenho_suporte_eletroima/modelo%203D/arquivo%20de%20modelo%203d/Sistema%20de%20Pesagem.ipt)
 
Após o desenvolvimento de seu Critical Prototype (Protótipo Crítico), temos a seguir o resultados dos testes nas condições imaginadas para esta proposta, sendo o objetivo a possibilidade de análise da variação do material magnético depositado na última bandeja. Segue vídeo para validação:


[<img src="https://lh3.googleusercontent.com/LEucmNsJTVKrFEJilw-L9K_mW73_YonFrutF2LBpQdQBBJtlpJAzWrnxKNiPXgJjcz0PUfj1uXqKpZDLee4G5w87_VubbwwtLm1lI6OCIn4xfy2Su3Dk0Yfhb_0TrT6ElUhsCQsXMZdjToojH60N_I8" width="100%">](https://drive.google.com/file/d/1h4DZN_CTTuU6obXVIsl4oBb2Dh6Px9GG/view?usp=share_link)
<center><font size="2"> Vídeo para demonstração do funcionamento da balança invertida </font></center>


### Dispositivo principal: Raspberry Pi Pico W e Ponte H

*Descrição da placa principal*

Materiais utilizados:

- Raspberry pi pico w

- Ponte H

- Placa universal

- Jumpers e solda

A solução conta com o microcontrolador Rasperry Pi Pico W e com o auxílio de uma ponte H ligada a este, conseguimos desenvolver o controle de corrente dos eletroímãs, algo crítico para o projeto. A fim de manter seguro e organizados, acoplamos esses materiais em uma placa universal de maneira que fique fixo com seu circuito e portanto de mais fácil integração ao resto do sistema como um todo (esta parte da solução está vinculada com o suporte para os eletroímãs, uma vez que a ponte-H é responsável por alimentar estes e permitir sua polarização e despolarização de maneira imediata e precisa). Com isso, desenvolvemos a estrutura necessária para garantir a segurança e eficiência dessa parte da solução, soldando os dispositivos em uma placa universal de maneira adequada. Segue o esquemático para consolidar esse sistema:

![Diagrama Esquemático Placa Principal.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Diagrama%20Esquem%C3%A1tico%20Placa%20Principal.jpg?raw=true)

![Frente.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Frente.jpg?raw=true)
  
## Dispositivos Mecânicos

*Descrição dos dispositivos mecânicos fabricados*

### Bandeja Radial

 Materiais utilizados:

 - Autodesk Inventor para modelagem
- Impressora 3D

Diante da análise das dimensões de movimento do braço robótico (Rotação de 270° e 34 cm de raio), optamos por um conjunto de três bandejas radiais que permitirão o aproveitamento máximo dessas dimensões. Segue o esquemático:

![Conjunto de Bandeja Radial.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Conjunto%20de%20Bandeja%20Radial.jpg?raw=true)

[Arquivo Autodesk Inventor - Bandeja Radial](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/desenho_suporte_eletroima/modelo%203D/arquivo%20de%20modelo%203d/Bandeja%20Radial.ipt)


## Validação de Dispositivos

Para fins de validação dos protótipos iniciais da solução, segue a consolidação da integração dos componentes: [Eletroimã e Sensor-iv](#eletroímã-e-sensor-infravermelho), [Balança Invertida](#célula-de-carga---balança-invertida) e [Raspberry e Ponte-H](#raspberry-pi-pico-w-e-ponte-h) e vídeo de seu funcionamento:

![Critical-Prototype.jpg](https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Critical-Prototype.jpg?raw=true)  

 Vídeo demonstrativo dos dispositivos em funcionamento:
 
[<img src="https://lh4.googleusercontent.com/72hif2xu81BUXbT-QnjV6JxvITd-5OMrs_6IRucYrypywCMPoHQbRooMXUI68x3uT1HOcjXxZzqC4WylVjOw3ospo_CIIq_OPmc0d3pswFj2GK29BPvGuL-KFxiPYhK57hlKPKO8l5GG_PTrYPJQdXg" width="100%">](https://drive.google.com/file/d/1txtCYVejKdHhF4Ub3VqGtsHanooMbTtl/view?usp=sharing)

## Análise do Processamento de Informações e Regras de Negócio
A comunicação entre dispositivos é fundamental para o sucesso do projeto em questão. Nesse sentido, para garantir um desempenho eficiente e preciso, foi necessário o desenvolvimento de um backend que atenda às necessidades específicas do sistema. A presente seção tem como objetivo apresentar as principais características e funcionalidades desse backend, visando fornecer informações claras e objetivas para o uso e manutenção dos dispositivos envolvidos.

### Instruções de instalação gerais
- Instalar a última versão do Python (3.11.2) <br>
- Instalar IDE compatível com o Raspberry Pi Pico W (Para todo o desenvolvimento do projeto e suas testagens foi-se utilizado o Thonny) <br>
- A ordem das conexões da barra de pinos macho deve ser seguida conforme a imagem abaixo onde: <br>
A: Comunicação da balança <br>
B: Comunicação da balança <br>
C: 5V da balança <br>
D: Acionador do led <br>
E: Acionador do led <br>
F: GND da balança <br>
G: 2ª polaridade do eletroimã <br>
H: GND do Led <br>
I: 1ª polaridade do eletroimã <br>
"FOTO DAS CONEXÕES"

### Arquivos importantes

#### Célula de Carga
Nome do arquivo: backend_celula_de_carga.py <br>
<img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/diagramas_backend/C%C3%A9lula%20de%20carga.png?raw=true"  width="25%">

# Referências
  

# Anexos

[Protótipo da Solução](https://www.figma.com/file/qpL2svgLY1MpCohLCb2k15/Magne?node-id=0%3A1&t=zmi4EzKLzb1IFHik-1)

[Arquitetura da Solução](https://drive.google.com/file/d/1GmHzUDCgvJjUn4TxMIrUaGz_GWzLzhXE/view?usp=sharing)

[Apresentação Sprint I - Entendimento do Negócio e Entendimento do Design](https://drive.google.com/file/d/1Jz6XxM3A0B85eHnMizRiv6yyCspteYLu/view?usp=share_link)
