<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Concepção de sistema de automação industrial
</center></font>

>*Observação 1: A estrutura inicial deste documento é só um exemplo. O seu grupo deverá alterar esta estrutura de acordo com o que está sendo solicitado nos artefatos.*

>*Observação 2: O índice abaixo não precisa ser editado se você utilizar o Visual Studio Code com a extensão **Markdown All in One**. Essa extensão atualiza o índice automaticamente quando o arquivo é salvo.*

**Sumário**

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
- [Referências](#referências)
- [Anexos](#anexos)


# Autores

* Amanda Fontes
* Gabriel Pascoli
* Gabriela Dias
* Gustavo Pereira
* João Carazzato
* Kil Matheus
* Luiz Borges


# Visão Geral do Projeto

## Parceiro de Negócios

O Instituto de Pesquisas Tecnológicas configura uma das maiores instituições de pesquisa do Brasil. Fundado em 1899, o IPT é vinculado à Secretaria de Desenvolvimento Econômico do Estado de São Paulo e colabora significativamente para o processo de desenvolvimento do país. É reconhecido nos meios técnicos nacionais e internacionais por, sobretudo, atender às demandas da sociedade e do setor produtivo.

A atuação multidisciplinar do instituto contempla diferentes segmentos: energia, transporte, petróleo e gás, meio ambiente, construção civil, cidades, saúde, segurança e outros. As soluções designadas pelo IPT, bem como os serviços prestados pela instituição, destinam-se a suprir as lacunas tecnológicas apresentadas pelos múltiplos setores com os quais a entidade trabalha.

## Definição do Problema

*Descrição_do_problema*

## Objetivos

### Objetivos gerais

O objetivo do parceiro é automatizar o processo de ensaio de separação de materiais magnéticos, bem como sua análise — procedimentos realizados pelo laboratório para seus respectivos clientes.  Dessa maneira, o IPT visa à realização de ensaios de maior eficiência a partir da padronização desse processo, cortando custos e otimizando os procedimentos envolvidos.

### Objetivos específicos



# Análise de Negócio


## Contexto da indústria


## Análise financeira

Considerando o processo de separação magnética realizado, atualmente, pelo Instituto de Pesquisas Tecnológicas, dispõem-se abaixo os valores referentes ao início da operação.

| **Componente**| **Valor** |
|--- |--- |
| Operador | R$ 150,00 | 
| Ímã de Neodímio | R$ 2000,00 | 
| Bandejas (x 3) | R$ 138,00 | 
| Saco Zip Lock (x 10) | R$ 24,00 | 
| Total | R$ 2312,00 ||

**<font size=2> Tabela 1 — Valores correspondentes aos componentes do procedimento de separação magnética atual </font>**

| **Componente**| **Valor** |
|--- |--- |
| DOBOT Magician Lite| R$ 15000,00 - R$ 25000,00 | 
| Raspberry Pi Pico W | R$ 80,00 - R$ 110,00 | 
| Eletroímã (x 4) | R$ 240,00 | 
| Total | R$ 15320,00 ||

**<font size=2> Tabela 2 — Valores correspondentes aos componentes da solução desenvolvida para o novo procedimento </font>**


## Análise SWOT

![](https://lh6.googleusercontent.com/zG8EnpZDgBawCTeDtsdIlDg2p6Ucljp306zIdN2e-vJLtzRxG_w4UnhNh5kEH32OZFgOrrOLHLhEsK2zV2kvmrZR1lcEbKyZ-tMikonjjLosjdmX5_fPNudNE6e7JZkfUH1QL_X20P0MP9xkGtSSoBw)
**<font size=2> Figura 1 — Análise SWOT (forças, oportunidades, fraquezas e ameaças) do Instituto de Pesquisas Tecnológicas </font>**

## Value Proposition Canvas

![](https://lh5.googleusercontent.com/xYxOS-4i-mqXFikfxJAc7g0b_FhPT96ku_k4FdCSHb3YkBMeSY1eqs4W_UaXE3cQJeg-VFHbNcAk1VyiD-jfpKKON3ua7EBH9ka5fBGwX1h3VGxSt3bfBo4WJKTvUS08PMLSops4Ap2DkbRSgd3jYMk)
**<font size=2> Figura 2 — Value Proposition Canvas do atual procedimento de separação magnética realizado pelo IPT </font>**


## Matriz de Riscos

![](https://lh6.googleusercontent.com/PsuqnxqBCrQZD-gd0dvqBnxThe2AOZWL6vFaLv27mIcgcPJA148UVNPkAnvzPRf696h6kdDlmeOSMsuxcbGsQ7I_WNAlkO6A7GrB65i5mTCvBZB_YU6-Kf9qKl5sqVSC8ANSYEWgnSgn2K9Eush8ml0)**<font size=2> Figura 3 — Matriz de Riscos da solução desenvolvida </font>**

# Arquitetura do Sistema

## Módulos do Sistema e Visão Geral (Big Picture) (1.0)


| **Componente**| **Descrição da função/características/requisitos** |
|--- |--- |
| DOBOT Magician Lite | Será utilizado o braço robótico Dobot Magician Lite, produto desenvolvido pela Minipa. O robô é inteligente, multifuncional e introduz uma série de métodos de interação entre software e hardware, com foco em um processo de aprendizagem baseado na liberdade de criação. | 
| Raspberry Pi Pico W | Constitui um poderoso microcontrolador com conexão wireless que conta com uma série de aplicações. No contexto do projeto, será programado em MicroPython. É considerada uma ferramenta compacta e de baixo custo. | 
| Eletroímã | Peça composta por um solenóide com um núcleo de material ferromagnético. Ao ser percorrido por um campo elétrico, gera ao seu redor um campo magnético. No projeto, será utilizado para o processo de separação magnética e ficará acoplado ao braço robótico. || 

**<font size=2> Tabela 3 — Componentes do sistema e descrição de suas respectivas funções, características e requisitos </font>**

### Croqui da Solução

**![](https://lh6.googleusercontent.com/ztk3zc9XaL34iNjuaPBuNVShRFIyjokR2Jst5DncvFbHIP54xMl98ww9CKMHN8QmR6n_dpUhHCBDjhhLnVa-wM5NKoTncqdeOXLbuwEs-bQmc2i5oCHimDtJOG6Kifzzl1vRTCi0IrapvS6h1T3StKI)**

**![](https://lh6.googleusercontent.com/h4amFfWdV1cBVHwKohGJG-WkZxRD2XilNjKyljW65xQtF6-O_A-T3Vr2XQTKXalTua54MzlmMWVOQPJDdET_461QWDJG2EaT0YILkZ0aF1DRAhSqUgUCoRmJkkrOlTCSnLFsZ_9a8OftsXZsOJtS0iA)**

## Módulos do Sistema e Visão Geral (Big Picture) (2.0)

**![](https://lh4.googleusercontent.com/Z5mUwJhEBQMw7qMIhjXzP2YzD2WnL8AAS5TnRI3obXeeZ5wV_fIfszd9qe3LvEW1ql9qz9bZnjREranW4u2LUhCnXDGfMPerODt9Z6T7X5SKTqfQKILhZ0A05YJ4FuuEE-oZA1XZSNeos0sty9EX2jE)**

| **Componente / Conexão**| **Descrição da função** | Tipo: entrada / saída / atuador |
|--- |--- | --- |
| Eletroímã, fios | Recebe uma corrente do Raspberry Pi Pico W, por meio da qual gera um campo eletromagnético. Espera-se que o ímã atraia os materiais interessantes para o ensaio. | Entrada: 12V |
| Raspberry Pi Pico W, fios (Micro USB) | Microcontrolador principal da solução, responsável por se comunicar via serial com o script python do braço robótico, receber e analisar dados dos sensores ao longo da operação e atuar perante eles. | Entrada: Sensores, dados ( Leituras analógicas). Saída: Volts, dados |
| Célula de carga + Amplificador Operacional | Sensor eletromecânico que possibilita a verificação da variação de força ou peso de uma determinada estrutura. (Bandeja com os materiais ferromagnéticos). | Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga) |
| Sensor de distância | Sensor infravermelho que nos permite converter suas leituras por meio de um cálculo polinomial de quinto grau a uma determinada distância em cm. (Braço e bandeja). | Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga) |
| Ponte H | Utilizado como regulador da corrente do eletroímã | Entrada: Energia elétrica. Saída: Energia elétrica |


**<font size=2> Tabela 3 — Componentes do sistema contendo suas respectivas formas de conexão, funções e especificações relacionadas a entrada e saída </font>**


## Sensores

### Testes preliminares de resposta dos sensores

Começamos os testes, primeiramente, buscando entender os sensores que precisávamos para o projeto, a fim de deixá-lo mais completo. A partir disso, entendemos a necessidade de um **sensor de distância**, para manter o teste o mais preciso possível a partir das necessidades do cliente (manter a mesma distância para maior precisão do processo) eliminando os pontos negativos que o robô tinha por atuar sozinho. Os testes desse sensor foram realizados em junção a um copo de café, atuando com o objeto que queríamos descobrir a distância, funcionando da seguinte forma: possuindo duas lentes, a primeira emite uma luz infravermelha enquanto a segunda captura os sinais da mesma, essa captura funciona através da reflexão da luz na superfície do objeto/local que queremos saber a distância, ao retornar a segunda lente, a partir da intensidade que a luz retorna, é possível descobrir a distância através de um fórmula, medindo distâncias entre 4 a 30 cm com um máximo de 2 cm de desvio da medida real. Em seguida, decidimos utilizar uma **célula de carga** (1kg) e um módulo conversor hx711 específico para realizar leituras analógicas melhores, para verificar a variação de peso na bandeja de deposição de material ferromagnético já minerado. Para o teste, utilizamos dois mini ímãs colocados um em seguida do outro, para assim analisar as variações nas leituras da célula. Concluímos que o funcionamento dela seria eficaz para nossa solução uma vez que sua sensibilidade permitirá que encerramos o processo de mineração com precisão, ou seja, quando já não ocorrer deposição de ferro magnético minerado neste ensaio.

### Demonstrações de Funcionamento dos Sensores

[**DEMONSTRAÇÃO DA CALIBRAÇÃO DO SENSOR DE DISTÂNCIA INFRAVERMELHO**
](https://drive.google.com/file/d/1Ca5yPUheEd5piRgm2pBVEWkggLV0Kput/view?usp=sharing)

[**DEMONSTRAÇÃO DA LEITURA DA CÉLULA DE CARGA**](https://drive.google.com/file/d/1_PykpKwE5UDx0YWhsY6CiHbBpMDh4OsE/view?usp=sharing)

## Atuadores

## Testes preliminares de resposta dos atuadores

Diante das necessidades do projeto, os atuadores principais seriam o **braço robótico**, o microcontrolador **Raspberry Pi Pico W**, uma **ponte H** e os **eletroímãs**. A princípio, o braço poderá ser manipulado por meio de um script em Python que irá conter os comandos ideais para realizar sua movimentação. Assim, será possível realizar adaptações para cada ensaio diante dos dados gerados pelos sensores e as ferramentas englobados na solução. O microcontrolador Raspberry ficará responsável pela centralização da solução, dispondo dos dados dos sensores e se comunicando com os scripts de outros atuadores via serial. Por exemplo, em contato com o script do braço robótico previamente citado, ele atualizará as informações necessárias para o procedimento ter a melhor acurácia e precisão possível, como o momento de finalizar o ensaio e a distância que ele precisa se movimentar para se posicionar corretamente sobre a bandeja.

Dando início aos testes, foi possível realizar a movimentação do braço de acordo com suas respectivas dimensões e a das ferramentas presentes no ensaio (bandeja), com o eletroímã já acoplado a ele e a um raspberry juntamente a uma ponte H. Com isso, foi possível realizar um protótipo crítico da solução, uma vez que seus principais componentes e funcionalidades estavam presentes. Foi possível observar o braço percorrendo o caminho já delimitado em seu script em conjunto com o acionamento e desligamento do eletroímã nos momentos apropriados.

# Análise de Experiência do Usuário


## User Stories

1.  Enquanto operador do ensaio de separação de minérios, quero automatizar o processo, a fim de que este se torne mais eficiente.
    
3.  Enquanto operador do ensaio, quero que um único ímã seja suficiente para realizar a separação de material magnético.
    
4.  Enquanto operador do ensaio, quero parametrizar as variáveis envolvidas no processo, a fim de obter resultados precisos sob múltiplas circunstâncias.
    
5.  Enquanto operador responsável pelas etapas envolvidas no ensaio, quero ser avisado pelo robô quando ele finaliza o ensaio.
    
6.  Enquanto operador responsável pelas múltiplas etapas envolvidas no ensaio, gostaria de gerar relatórios automaticamente, para analisar, com maior eficiência, os resultados do ensaio.


## Protótipo de interface com o usuário

Abaixo, encontram-se as imagens relativas à prototipação da interface gráfica por meio da qual será possível manipular e configurar o robô.

**![](https://lh4.googleusercontent.com/-leIWCVZ6h71iuO5nrKRNCiL6M3v2s-F6YT3wfqj0WZ_n9rTOn_-JtPe_AKyriKC6r2yKJwvpkDY7q4fpvTuPOmWiN0arAbJAvKxDDWQNKsdRn00KxmeLaTNXBvXr0R1pZT9EUWhXsyjWl4k0Xk_3G8)**
**![](https://lh3.googleusercontent.com/AAZiukdZP169G3rSsd7Mjdb5XNqiA1DmRrz5wreyyGKyAWW7B-RLvG1KOppVzq9wZypDRm8BksFqkm-j6af3J6eeuTFOCKVYBPaA_y-oCN19bxBpjudHgHvxYOhdAZmhhJhdXBlPmbbqtx3rzBkM8BE)**
**![](https://lh6.googleusercontent.com/OW5uM3qnbidyQepBadF9RvSuumPyCVdJYkqrgdwJfAM97-keoVPAuGMx9JuE7CCqDapeCSrc6VBYfo1D8VZ6nQgTq7gsUWm5gjuk2Dnt0-wdf94ZfrX8OfGU3L5kO9a8zZHVNnNBTfHVSeBkijjpOMg)**

# Referências


# Anexos

[Protótipo da Solução](https://www.figma.com/file/qpL2svgLY1MpCohLCb2k15/Magne?node-id=0%3A1&t=zmi4EzKLzb1IFHik-1)

[Arquitetura da Solução](https://drive.google.com/file/d/1GmHzUDCgvJjUn4TxMIrUaGz_GWzLzhXE/view?usp=sharing)

[Apresentação da Sprint I](https://drive.google.com/file/d/1Jz6XxM3A0B85eHnMizRiv6yyCspteYLu/view?usp=share_link)

Apresentação da Sprint II
