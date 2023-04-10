<table>
<tr>
<td>
<a  href= "https://www.ipt.br/"><img  src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/outros/logo_ipt.png?raw=true"  alt="IPT"  border="0"  width="30%"></a>
</td>
<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="30%"></a>
</td>
</tr>
</table>
<br>

<h2 align="center">Concepção de sistema de automação industrial</font></h2>


# **Sumário**

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
    - [Diagrama da Solução](#diagrama-da-solução)
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
  - [Análise do Processamento de Informações e Regras de Negócio](#análise-do-processamento-de-informações-e-regras-de-negócio)
    - [Instruções de instalação gerais](#instruções-de-instalação-gerais)
    - [Arquivos importantes](#arquivos-importantes)
      - [Célula de Carga](#célula-de-carga)
- [Referências](#referências)
- [Anexos](#anexos)


# Autores

[Amanda Ribeiro Fontes](https://www.linkedin.com/in/amanda-fontes/) <br>
[Gabriel Pascoli](https://www.linkedin.com/in/gabriel-pascoli-73733b200/)<br>
[Gabriela Barretto Dias](https://www.linkedin.com/in/gabriela-dias-38b484250/)<br>
[Gustavo Francisco Neto Pereira](https://www.linkedin.com/in/gustavo-pereira1/)<br>
[João Pedro Gonçalves Carazzato](https://www.linkedin.com/in/jo%C3%A3o-pedro-gon%C3%A7alves-carazzato-147120231/)<br>
[Kil Matheus Gomes Teixeira](https://www.linkedin.com/in/kil-matheus-gomes-teixeira-78257020a/)<br>
[Luiz Fernando da Silva Borges](https://www.linkedin.com/in/sbluizfernando/)<br>

# Visão Geral do Projeto

## Parceiro de Negócios

O Instituto de Pesquisas Tecnológicas configura uma das maiores instituições de pesquisa do Brasil. Fundado em 1899, o IPT é vinculado à Secretaria de Desenvolvimento Econômico do Estado de São Paulo e colabora significativamente para o processo de desenvolvimento do país. É reconhecido nos meios técnicos nacionais e internacionais por, sobretudo, atender às demandas da sociedade e do setor produtivo.

A atuação multidisciplinar do instituto contempla diferentes segmentos: energia, transporte, petróleo e gás, meio ambiente, construção civil, cidades, saúde, segurança e outros. As soluções designadas pelo IPT, bem como os serviços prestados pela instituição, destinam-se a suprir as lacunas tecnológicas apresentadas pelos múltiplos setores com os quais a entidade trabalha.

## Definição do Problema

Um dos serviços prestados pelo Instituto de Pesquisas Tecnológicas consiste em um ensaio de separação de conteúdo ferromagnético a partir de amostras obtidas por mineradoras. O ensaio, contudo, é feito de forma manual: é necessária a presença de um operador responsável pela condução dos procedimentos utilizados. No ensaio, a amostra, que se encontra despejada sobre uma bandeja, é submetida a uma varredura feita pelo operador utilizando um ímã envolvido por um material plástico. Posteriormente, o material capturado pelo ímã é lavado em uma segunda bandeja contendo água, a fim de que as impurezas eventualmente misturadas ao material coletado sejam removidas. Por fim, o material ferromagnético contido no ímã, já livre das impurezas, é depositado em uma terceira bandeja com água. O processo realizado atualmente demonstra ser uma atividade cansativa para o operador que a executa, além de não apresentar a precisão desejada quanto à separação de todo o material que se deseja obter. Nesse contexto, propor uma solução automatizada seria de significativa utilizade para o cliente, visto que o serviço se tornaria mais eficiente.

## Objetivos

### Objetivos gerais

O objetivo do parceiro é automatizar o processo de ensaio de separação de materiais magnéticos, bem como sua análise — procedimentos realizados pelo laboratório para seus respectivos clientes. Dessa maneira, o IPT visa à realização de ensaios de maior eficiência a partir da padronização desse processo, cortando custos e otimizando os procedimentos envolvidos.

### Objetivos específicos

- Construção um sistema de hardware capaz de realizar, de maneira autônoma, o ensaio de separação de material ferromagnético realizado pelo IPT.

- Implementação de interface integrada ao robô, por meio da qual será possível manipular as variáveis envolvidas no ensaio.

- Centralização dos dados envolvidos no ensaio, por meio da geração de relatório automatizado, para que haja um controle eficiente de informações.

# Análise de Negócio

## Contexto da indústria

A indústria de mineração constitui um setor da economia global que envolve a extração de recursos da natureza, a exemplo dos minérios metálicos. Nesse contexto, o uso da separação magnética representa uma ferramenta de fundamental importância no processamento mineral. Além de econômica, a técnica se demonstra eficaz no que concerne ao tratamento de materiais que serão posteriormente utilizados na produção de bens e serviços em diversos setores: construção civil, indústria automotiva, eletrônica, entre outros.

O uso de soluções de automação tem sido adotado, recorrentemente, em processos industriais de separação de misturas. Portanto, uma vantagem da separação magnética é que ela pode ser automatizada com significativa facilidade. Em empresas que utilizam o processo, é possível afirmar que a adoção da automatização na separação magnética possibilitaria a otimização do uso de recursos, a redução de possíveis erros causados pela ação humana, a padronização dos procedimentos utilizados, entre outras vantagens. No caso do Instituto de Pesquisas Tecnológicas, compreende-se que sua posição perante à indústria de mineração seria de maior competitividade em vista da qualidade do serviço oferecido.

## Análise financeira

Considerando o processo de separação magnética realizado, atualmente, pelo Instituto de Pesquisas Tecnológicas, dispõem-se abaixo os valores referentes ao início da operação.

<br>
<table align="center">
  <tr>
    <th>Componente</th>
    <th>Valor</th>
  </tr>
  <tr>
    <td>Operador </td>
    <td>R$ 150,00</td>
<tr>
	<td>Ímã de Neodímio</td>
	<td>R$ 2000,00</td>
</tr>
<tr>
	<td>Bandejas (x 3)</td>
	<td>R$ 138,00</td>
</tr>
<tr>
	<td>Saco Zip Lock (x 10)</td>
	<td>R$ 24,00</td>
</tr>
<tr>
	<td>Total</td>
	<td>R$ 2312,00</td>
</tr>
</table>
<br>
<p align="center"><font size=2><b> Tabela 1 — Valores correspondentes aos componentes do procedimento de separação magnética atual </b></font></p>

<br>
<table align="center">
  <tr>
    <th>Componente</th>
    <th>Valor</th>
  </tr>
  <tr>
    <td>DOBOT Magician Lite</td>
    <td>R$ 15000,00 - R$ 25000,00</td>
<tr>
	<td>Raspberry Pi Pico W</td>
	<td>R$ 80,00 - R$ 110,00</td>
</tr>
<tr>
	<td>Eletroímã (x 4)</td>
	<td>R$ 240,00</td>
</tr>
<tr>
	<td>Total</td>
	<td>R$ 24,00</td>
</tr>
<tr>
	<td>Total</td>
	<td>R$ 15320,00</td>
</tr>
</table>
<br>
<p align="center"><font size=2><b>Tabela 2 — Valores correspondentes aos componentes da solução desenvolvida para o novo procedimento</b></font></p>

Em suma, a qualidade dos ensaios constitui o elemento que agrega valor à solução. Com a retirada da mão de obra, cuja ação no ensaio passa a ser automatizada, o tempo ganho pelo operador para outras tarefas é significativo a longo prazo, salvando um custo operacional para os stakeholders. Diante da análise dos custos da operação e retorno dos ensaios — supondo o valor de R$ 2000,00 por ensaio —, a solução se pagaria em, aproximadamente, nove ensaios.

## Persona

<br>
<div align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/negocios/persona.png?raw=true" width="600" height=auto></img></div>
<p align="center"><font size=2><b>Figura 1 — Persona da solução</b></font></p>
<br>

## Análise SWOT

<br>
<div align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/negocios/analise_swot.png?raw=true" width="600" height=auto></img></div>
<p align="center"><font size=2><b>Figura 2 — Análise SWOT (forças, oportunidades, fraquezas e ameaças) do Instituto de Pesquisas Tecnológicas</b></font></p>
<br>

## Value Proposition Canvas

<br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/negocios/value_proposition_canvas.png?raw=true" width="80%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 3 — Value Proposition Canvas do atual procedimento de separação magnética realizado pelo IPT</b></font></p>
<br>

## Matriz de Riscos


<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/negocios/risk_matrix.png?raw=true" width="80%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 4 — Matriz de Riscos da solução desenvolvida</b></font></p>
<br>

# Arquitetura do Sistema

## Módulos do Sistema e Visão Geral (1.0)

<br>
<table align="center">
  <tr>
    <th>Componente</th>
    <th>Descrição da função/características/requisitos</th>
  </tr>
  <tr>
    <td>DOBOT Magician Lite</td>
    <td>Será utilizado o braço robótico Dobot Magician Lite, produto desenvolvido pela Minipa. O robô é inteligente, multifuncional e introduz uma série de métodos de interação entre software e hardware, com foco em um processo de aprendizagem baseado na liberdade de criação.</td>
<tr>
	<td>Raspberry Pi Pico W</td>
	<td>Constitui um poderoso microcontrolador com conexão wireless que conta com uma série de aplicações. No contexto do projeto, será programado em MicroPython. É considerada uma ferramenta compacta e de baixo custo.</td>
</tr>
<tr>
	<td>Eletroímã</td>
	<td>Peça composta por um solenóide com um núcleo de material ferromagnético. Ao ser percorrido por um campo elétrico, gera ao seu redor um campo magnético. No projeto, será utilizado para o processo de separação magnética e ficará acoplado ao braço robótico.</td>
</tr>
</table>
<br>
<p align="center"><font size=2><b>Tabela 3 — Componentes do sistema e descrição de suas respectivas funções, características e requisitos</b></font></p>

  
### Croqui da Solução

O croqui da solução se encontra na figura disposta abaixo e exibe a visão vertical da solução. As três formas retangulares correspondem às bandejas utilizadas no ensaio, enquanto o círculo representa a área do robô. A área destacada em azul configura o alcance do braço robótico. No croqui, encontram-se também as dimensões da bandeja, a amplitude de varredura do robô e o limite do ângulo de rotação.

<br>
<p align="center"><img src="https://lh6.googleusercontent.com/ztk3zc9XaL34iNjuaPBuNVShRFIyjokR2Jst5DncvFbHIP54xMl98ww9CKMHN8QmR6n_dpUhHCBDjhhLnVa-wM5NKoTncqdeOXLbuwEs-bQmc2i5oCHimDtJOG6Kifzzl1vRTCi0IrapvS6h1T3StKI" width="600" height=auto></img></p>
<p align="center"><font size=2><b>Figura 5 — Versão inicial do croqui da solução</b></font></p>
<br>

<br>
<p align="center"><img src="https://lh6.googleusercontent.com/h4amFfWdV1cBVHwKohGJG-WkZxRD2XilNjKyljW65xQtF6-O_A-T3Vr2XQTKXalTua54MzlmMWVOQPJDdET_461QWDJG2EaT0YILkZ0aF1DRAhSqUgUCoRmJkkrOlTCSnLFsZ_9a8OftsXZsOJtS0iA" width="600" height=auto></img></p>
<p align="center"><font size=2><b>Figura 6 — Versão inicial do dispositivo mecânico de suporte para eletroímãs</b></font></p>
<br>

## Módulos do Sistema e Visão Geral (2.0)

### Diagrama da Solução

O diagrama da solução se encontra disposto na figura abaixo e exemplifica as conexões entre cada módulo componente da solução. Além dos dispositivos de hardware, são exibidos também os artefatos de software integrados ao servidor de aplicação responsável pela manutenção do funcionamento do produto.

<br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/diagrama_solucao/Diagrama%20da%20Solu%C3%A7%C3%A3o.png?raw=true" width="600" height=auto></img></p>
<p align="center"><font size=2><b>Figura 7 — Diagrama da solução</b></font></p>

<br>
<table align="center">
  <tr>
    <th>Componente / Conexão</th>
    <th>Descrição da função</th>
    <th>Tipo: entrada / saída / atuador</th>
  </tr>
  <tr>
    <td>Eletroímã, fios</td>
    <td>Recebe uma corrente do Raspberry Pi Pico W, por meio da qual gera um campo eletromagnético. Espera-se que o ímã atraia os materiais interessantes para o ensaio.</td>
    <td>Entrada: 12V</td>
<tr>
	<td>Raspberry Pi Pico W, fios (Micro USB)</td>
	<td>Microcontrolador principal da solução, responsável por se comunicar via serial com o script python do braço robótico, receber e analisar dados dos sensores ao longo da operação e atuar perante eles.</td>
	<td>Entrada: Sensores, dados (Leituras analógicas). Saída: Volts, dados</td>
</tr>
<tr>
	<td>Célula de carga + Amplificador Operacional</td>
	<td>Sensor eletromecânico que possibilita a verificação da variação de força ou peso de uma determinada estrutura. (Bandeja com os materiais ferromagnéticos).</td>
	<td>Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga)</td>
</tr>
<tr>
	<td>Sensor de distância</td>
	<td>Sensor infravermelho que nos permite converter suas leituras por meio de um cálculo polinomial de quinto grau a uma determinada distância em cm. (Braço e bandeja).</td>
	<td>Entrada: Energia elétrica. Saída: dados (Leituras analógicas da célula de carga)</td>
</tr>
<tr>
	<td>Ponte H</td>
	<td>Utilizado como regulador da corrente do eletroímã</td>
	<td>Entrada: Energia elétrica. Saída: Energia elétrica</td>
</tr>
</table>
<br>
<p align="center"><font size=2><b>Tabela 4 — Componentes do sistema contendo suas respectivas formas de conexão, funções e especificações relacionadas a entrada e saída</b></font></p>
<br>

Diante das necessidades do projeto, os atuadores principais seriam o braço robótico, o microcontrolador Raspberry Pi Pico W, uma ponte H e eletroímãs. A princípio, o braço poderá ser manipulado por meio de um script Python que irá conter os comandos correspondentes à sua movimentação. Desse modo, será possível realizar adaptações para cada ensaio diante dos dados gerados pelos sensores e as ferramentas englobados na solução. O microcontrolador ficará responsável por embarcar o firmware dos módulos da solução, dispondo dos dados dos sensores e se comunicando com os scripts dos atuadores via serial. Ao entrar em execução paralelamente ao script do braço robótico mencionado, ele atualizará as informações necessárias para que o procedimento apresente uma melhor precisão.

#### Dobot Magician Lite

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/dobot.jpg?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 8 — Braço robótico Dobot Magician Lite</b></font></p>

**Tipo de componente:** dispositivo robótico<br>
**Função:** realizar, de forma autônoma, a rotina do ensaio de separação magnética<br>
**Controle:** via interface de usuário<br>

#### Raspberry Pi Pico W

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/raspberry.png?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 9 — Microcontrolador Raspberry Pi Pico W</b></font></p>

**Tipo de componente:** microcontrolador<br>
**Função:** armazenar o firmware responsável pelo controle dos sensores e atuadores da solução<br>
**Controle:** atrelado ao robô; em execução uma vez que o firmware é embarcado no microcontrolador<br>

## Sensores

#### Sensor Infravermelho de Distância

**Observação:** o sensor infravermelho limita-se à primeira versão da arquiterura da solução e sua utilização ficou restrita a testes. Seu descarte será justificado, posteriormente, na seção referente aos testes realizados.

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/sensor_infravermelho.png?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 10 — Sensor infravermelho de distância</b></font></p>

**Sensor:** sensor infravermelho de distância<br>
**Tipo de sensor:** sensor eletromecânico de medição<br>
**Função:** detectar a distância entre a garra do braço robótico e as bordas de cada bandeja<br>
**Controle:** automático e realizado no início de cada ensaio<br>
**Entrada esperada:** sinal analógico referente à distância entre lente e material<br>
**Saída esperada:** distância, em centímetros, entre sensor e objeto<br>
**Entrada obtida:**  sinal analógico referente à distância entre lente e material<br>
**Saída obtida:** distância, em centímetros, entre sensor e objeto<br>

**Funcionamento do sensor**

O sensor infravermelho possui duas lentes: a primeira emite radiação infravermelha, enquanto a segunda captura os sinais obtidos por meio da radiação. A captura funciona através da reflexão da luz na superfície do objeto cuja distância deseja-se obter. Ao retornar à segunda lente, a intensidade da luz permite a obtenção da distância por meio de um cálculo que leva em consideração distâncias entre 4 e 30 centímetros. É importante destacar que pode haver um desvio máximo de dois centímetros da medida real.

**Realização de testes**

Para a prototipação do projeto, foi necessária uma fase de entendimento e reflexão acerca de quais sensores se fariam necessários na solução. A princípio, ponderou-se a ideia de acrescentar ao protótipo um sensor infravermelho de distância, a fim de que as varreduras realizadas pelo braço robótico fossem padronizadas quanto à área percorrida. Foram realizados testes simples nos quais a capacidade de medição do sensor foi colocada à prova. Embora o uso do sensor em questão pudesse ser utilizado para evitar possíveis problemas relacionados à autonomia de atuação do robô, soluções alternativas ao uso do sensor foram encontradas, o que ocasionou o descarte da ideia. 

#### Célula de Carga & HX711

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/celula_carga_hx711.png?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 11 — Célula de carga junto ao módulo HX711</b></font></p>

**Sensor:** célula de carga & módulo amplificador HX711<br>
**Tipo de sensor:** sensor eletromecânico de medição<br>
**Função:** detectar a quantidade de material ferromagnético obtido em uma varredura<br>
**Controle:** automático e cíclico enquanto o ensaio se encontra em execução<br>
**Entrada esperada:** sinal analógico referente à variação de força exercida sobre a célula<br>
**Saída esperada:** valor numérico indicativo da quantidade do material coletado<br>
**Entrada obtida:** sinal analógico referente à variação de força exercida sobre a célula<br>
**Saída obtida:** valor numérico indicativo da quantidade do material coletado<br>

**Funcionamento do sensor**

A célula de carga, através do módulo amplificador HX711, deve receber um sinal analógico quando sofre deformação. Isto é, para situações em que materiais exercem um campo magnético sobre a célula, e esta sofre a ação de uma força, ocorre a medição analógica do nível de deformação provocado pelo campo magnético em questão. Cálculos podem ser realizados a fim de que o valor de saída seja convertido para unidades de massa. Desse modo, o sensor atua como uma balança invertida em que a força peso atua de modo a puxar a célula para cima, diferentemente das formas convencionais de pesagem utilizadas em outros tipos de balança.

### Testes preliminares de resposta dos sensores

Utilizando a célula de carga (1kg) e um módulo conversor HX711 para a realização de melhores leituras analógicas, foram realizados testes a fim de verificar a variação de peso na última bandeja do ensaio, referente à deposição do material ferromagnético minerado. Para isso, foram utilizados dois ímãs de neodímio colocados lado a lado sobre a célula e, posteriormente, foram aproximados materiais magnéticos capaz de provocar variações na leitura realizada pelo sensor. A conclusão foi de que seu funcionamento seria eficaz para a solução desenvolvida, uma vez que a sensibilidade apresentada demonstrou ser suficiente para a precisão que se desejava obter no processo de medição do material depositado. Desse modo, quando a variação de leitura da célula for mínima, o cliente terá o indicativo de que já não há material ferromagnético para ser depositado, de modo que o ensaio possa ser encerrado.

#### Demonstração de funcionamento dos sensores

Abaixo, encontram-se os vídeos de demonstração de funcionamento dos sensores utilizados na solução.

<p align="center"><a href="https://drive.google.com/file/d/1Ca5yPUheEd5piRgm2pBVEWkggLV0Kput/view?usp=sharing/"><img src="https://lh3.googleusercontent.com/fqUKYFc17_odvZCvnTXnoRLqCDH9Pn9qDU89iT06e85d7JCMgehLY_zv11d5XwpVpe9WBhRMjyfWFEQnsnYrQ1qyxWmC6A1tT2TWTOM-Va5HO0muF4CpKcszElloyR_C5pqJr0lwGDwhx7vwfNHzgyg" width="50%"></img></a></p>
<p align="center"><font size=2><b>Vídeo para demonstração da calibração do sensor de distância infravermelho</b></font></p>

<p align="center"><a href="https://drive.google.com/file/d/1_PykpKwE5UDx0YWhsY6CiHbBpMDh4OsE/view?usp=sharing"><img src="https://lh6.googleusercontent.com/auAXAe9Xtx8LeL_hgrhevCSoSas-2hgLQiDJkmaKQMo5Aln3AQPqphcAsPrAwtK9bnkqbQE60VdnC7FYCSS_ISZA1q_zkiNb_pNwf5CONbB9MUBZJx5vqdt1c2HjwwsXzADE1AOcUq4_KOQLKPHPiGU" width="50%"></img></a></p>
<p align="center"><font size=2><b>Vídeo para demonstração da leitura da célula de carga</b></font></p>

## Atuadores

#### Eletroímã

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/eletroima.png?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 12 — Eletroímã solenóide</b></font></p>

**Atuador:** eletroímã solenóide<br>
**Tipo de atuador:** dispositivo eletromagnético<br>
**Função:** capturar o material ferromagnético da amostra<br>
**Controle:** automático e constante durante a varredura<br>
**Entrada esperada:** sinal elétrico capaz de induzir campo magnético<br>
**Saída esperada:** geração de campo magnético capaz de atrair material magnético<br>
**Entrada obtida:** sinal elétrico capaz de induzir campo magnético<br>
**Saída obtida:** geração de campo magnético capaz de atrair material magnético<br>

#### Ponte H

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/media/componentes/ponte_h.png?raw=true" width="40%"></img></p>
<p align="center"><font size=2><b>Figura 13 — Ponte H</b></font></p>

**Atuador:** ponte H<br>
**Tipo de atuador:** circuito eletrônico<br>
**Função:** inversão da polaridade da corrente que flui para os eletroímãs<br>
**Controle:** atrelado ao firmware embarcado no microcontrolador<br>

### Testes preliminares de resposta dos atuadores

No primeiro teste realizado, foi possível coordenar a movimentação do braço com o eletroímã já acoplado a ele e a um microcontrolador juntamente à ponte H. Dessa forma, foi possível concretizar um protótipo crítico da solução, uma vez que os componentes de maior relevância já estavam em funcionamento. Foi possível observar o braço percorrendo o caminho já delimitado em seu script em conjunto com o acionamento e desligamento do eletroímã nos momentos apropriados.

### Testes finais de resposta dos atuadores

Abaixo, encontram-se vídeos de demonstração referentes aos últimos testes realizados durante a última semana de desenvolvimento do projeto.

_Vídeos_

# Análise de Experiência do Usuário

## User Stories

1. Enquanto operador do ensaio de separação de minérios, quero automatizar o processo, a fim de que este se torne mais eficiente.

2. Enquanto operador do ensaio, quero que um único ímã seja suficiente para realizar a separação de material magnético.

3. Enquanto operador do ensaio, quero parametrizar as variáveis envolvidas no processo, a fim de obter resultados precisos sob múltiplas circunstâncias.

4. Enquanto operador responsável pelas etapas envolvidas no ensaio, quero ser avisado pelo robô quando ele finaliza o ensaio.  

5. Enquanto operador responsável pelas múltiplas etapas envolvidas no ensaio, gostaria de gerar relatórios automaticamente, para analisar, com maior eficiência, os resultados do ensaio.

 
## Protótipo de interface com o usuário

### Versão 1.0

Abaixo, encontram-se as imagens relativas à primeira versão da prototipação da interface gráfica por meio da qual será possível manipular e configurar o robô.

A primeira imagem mostra como seria a tela de início, tem como principal objetivo mostrar o Status de todas as integrações da solução. Qual é a situação atual do Robô, que tipo de comando ele está recebendo e retornando, e a situação dos componentes, se o imã está em funcionamento e com quanto de voltagem está trabalhando, qual é o peso da bandeja final e se o sistema de revolvimento está em funcionamento. Na lateral direita de página, podemos ver controles que podem movimentar o robô de maneira mais precisa e linear, podendo mover os 3 eixos de coordenadas, uma de cada vez. Tambem pode-se reparar no campo mais abaixo, o controle de atuadores na qual o mesmo pode acionar o compente acoplado utilizando voltagem ou pneumático.

<p align="center"><img src="https://lh4.googleusercontent.com/-leIWCVZ6h71iuO5nrKRNCiL6M3v2s-F6YT3wfqj0WZ_n9rTOn_-JtPe_AKyriKC6r2yKJwvpkDY7q4fpvTuPOmWiN0arAbJAvKxDDWQNKsdRn00KxmeLaTNXBvXr0R1pZT9EUWhXsyjWl4k0Xk_3G8" width="50%"></img></p>
<p align="center"><font size=2><b>Figura 14 — Tela de interface de usuário (versão 1.0)</b></font></p>

<p align="center"><img src="https://lh3.googleusercontent.com/AAZiukdZP169G3rSsd7Mjdb5XNqiA1DmRrz5wreyyGKyAWW7B-RLvG1KOppVzq9wZypDRm8BksFqkm-j6af3J6eeuTFOCKVYBPaA_y-oCN19bxBpjudHgHvxYOhdAZmhhJhdXBlPmbbqtx3rzBkM8BE" width="50%"></img></p>
<p align="center"><font size=2><b>Figura 15 — Tela de interface de usuário (versão 1.0)</b></font></p>

<p align="center"><img src="https://lh6.googleusercontent.com/OW5uM3qnbidyQepBadF9RvSuumPyCVdJYkqrgdwJfAM97-keoVPAuGMx9JuE7CCqDapeCSrc6VBYfo1D8VZ6nQgTq7gsUWm5gjuk2Dnt0-wdf94ZfrX8OfGU3L5kO9a8zZHVNnNBTfHVSeBkijjpOMg" width="50%"></img></p>
<p align="center"><font size=2><b>Figura 16 — Tela de interface de usuário (versão 1.0)</b></font></p>

### Versão 2.0

<p align="center"><img src="https://lh5.googleusercontent.com/ZViqolIPfW3kLjJQgTnW5MkBmjN898MZy8-lvXjTz1IPSv6aeOTJjbJfEen0k8ZadyW3YlR_wdLpcW8RFHtutDw6B3ZHngoqcyKLlxWqEyJ_dlXfVOr6mtQHwKvB6lwjV2hH2VYEH7kc" width="50%"></img></p>
<p align="center"><font size=2><b>Figura 17 — Tela de interface de usuário (versão 2.0)</b></font></p>

<p align="center"><img src="https://lh4.googleusercontent.com/ld8LCiTVFjiahYIs0YtQFlDBaFXtl8HLrXyyQUMQy_rWG0e78vrk6Ei8O3qzDISUQIvr4MFWdajMHAXTiFLQYKdSkbLwFHgduBCtkoqFWObtJc1gjKhwLUN93QpN8LjO9_dACr0T2jN1" width="50%"></img></p>
<p align="center"><font size=2><b>Figura 18 — Tela de interface de usuário (versão 2.1)</b></font></p>

## Dispositivos Eletrônicos

### Dispositivo acoplado à garra do braço robótico (eletroímãs & sensor infravermelho)

**Materiais utilizados:**

- Eletroímã de 9V (2 un.)

- Placa universal (3x4 cm) (1 un.)

- Um LED (1 un.)

- Jumpers, solda e parafusos (2 un.)

**Tecnologias utilizadas**

- Autodesk Inventor 

- Impressora 3D  

Diante da necessidade de acoplar os eletroímãs e o sensor infravermelho em uma extensão do braço robótico e proteje-los (principalmente da água utilizada nos ensaios), decidimos por colocar-los na parte interior de uma estrutura com o formato de um martelo, na cabeça se encontram os sensores acoplados à placa universal devidamente ligados e o cabo servirá para a conexão braço-suporte e para passar o devido cabeamento que acompanhará o braço robótico por cima. Optamos por deixar o espaço dos eletroímãs e do sensor infra-vermelho pré-estabelecidos e bem delimitados para que não se movimentem durante os ensaios, a fim de uma melhor precisão e acurácia destes. Segue abaixo o esquemático desta proposta com as devidas medidas para sua função:

<h3>Desenho técnico do dispositivo eletrônico dos eletroímãs</h3>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Suporte%20Eletroim%C3%A3.jpg?raw=true" width="50%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 17 — Desenho técnico referente ao dispositivo eletrônico em que ficam acoplados os eletroímãs</b></font></p>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Tampa%20Eletroim%C3%A3.jpg?raw=true" width="50%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 19 — Desenho técnico referente à tampa do dispositivo eletrônico em que ficam acoplados os eletroímãs</b></font></p>


**Observação:** os arquivos referentes à modelagem 3D do dispositivo podem ser encontrados no mesmo diretório em que se encontra o presente documento.

<h3>Imagens do dispositivo eletrônico dos eletroímãs</h3>

<p align="center"><img src="https://lh3.googleusercontent.com/ao0c9nc6mhrP9Fmeg4wEZPEusdrDQIJ61dK5RoYkbhAcVE2yyj0SdazAUlfMO8u-v_EOarZFIAyTD3S7Z383lcbsPOpWUL6tHecSAR_HuqibPbG7mAPTlTrm3K7pNZkhVb2WumgjS6tATrm04RXj-wc" width="40%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 20 — Visão oblíqua da primeira versão da fabricação do dispositivo eletrônico dos eletroímãs</b></font></p>
  
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Eletroima2.jpeg?raw=true" width="40%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 21 — Visão oblíqua da primeira versão da fabricação do dispositivo eletrônico dos eletroímãs</b></font></p>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Elertroima3.jpeg?raw=true" width="40%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 22 — Visão lateral da primeira versão da fabricação do dispositivo eletrônico dos eletroímãs</b></font></p>

### Balança invertida: sistema de pesagem utilizando célula de carga

Materiais utilizados:

- Célula de Carga (1KG)

- Dois Parafusos e duas porcas

- Duas madeiras MDF (10cmX6cm)

- Imãs de Neodímio (Utilizamos dois de um HD)

- AutoDesk Inventor para modelagem

- Impressora 3D

A fim de analisar a todo o momento o resultado da mineração magnética, decidimos utilizar de uma balança invertida, contando com dois imãs de neodímio acoplados na parte superior do sistema (visando que a deformação da célula seja por indução magnética, por isso o nome) e a estrutura física necessária para manter a célula de carga estável (madeiras presas em cada uma de suas devidas extremidades com os parafusos e porcas). Com isso desenvolvemos esse esquemático responsável por interagir com os materiais magnéticos já minerados e constantemente indicar se houve uma nova deposição deste. Assim, caso seja o momento de encerrar o ensaio, saberemos com mais precisão diante das medidas fornecidas por esse sistema. Segue o esquemático:

<h3>Desenho técnico do dispositivo da balança invertida</h3>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Sistema%20de%20Pesagem.jpg?raw=true" width="50%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 23 — Desenho técnico referente ao dispositivo da balança invertida</b></font></p>

**Observação:** os arquivos referentes à modelagem 3D do dispositivo podem ser encontrados no mesmo diretório em que se encontra o presente documento.

<h3>Imagens do dispositivo da balança invertida</h3>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Cima.jpg?raw=true" width="70%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 24 — Visão vertical do dispositivo da balança invertida</b></font></p>


<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Cima2.jpg?raw=true" width="70%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 25 — Visão vertical ampliada do dispositivo da balança invertida</b></font></p>


<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/BI-Lado.jpg?raw=true" width="70%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 26 — Visão frontal do dispositivo da balança invertida</b></font></p>

Após o desenvolvimento de seu Critical Prototype (Protótipo Crítico), temos a seguir o resultados dos testes nas condições imaginadas para esta proposta, sendo o objetivo a possibilidade de análise da variação do material magnético depositado na última bandeja. Segue vídeo para validação:

<p align="center"><a href="https://drive.google.com/file/d/1h4DZN_CTTuU6obXVIsl4oBb2Dh6Px9GG/view?usp=share_link"><img src="https://lh3.googleusercontent.com/LEucmNsJTVKrFEJilw-L9K_mW73_YonFrutF2LBpQdQBBJtlpJAzWrnxKNiPXgJjcz0PUfj1uXqKpZDLee4G5w87_VubbwwtLm1lI6OCIn4xfy2Su3Dk0Yfhb_0TrT6ElUhsCQsXMZdjToojH60N_I8" width="50%"></img></a></p>
<p align="center"><font size=2><b>Vídeo para demonstração do funcionamento da balança invertida</b></font></p>

### Dispositivo principal: Raspberry Pi Pico W & Ponte H

Materiais utilizados:

- Raspberry Pi Pico W (1 un.)

- Ponte H (1 un.)

- Placa universal (1 un.)

- Jumpers e solda

A solução conta com o microcontrolador Rasperry Pi Pico W e com o auxílio de uma ponte H ligada a este, conseguimos desenvolver o controle de corrente dos eletroímãs, algo crítico para o projeto. A fim de manter seguro e organizados, acoplamos esses materiais em uma placa universal de maneira que fique fixo com seu circuito e portanto de mais fácil integração ao resto do sistema como um todo (esta parte da solução está vinculada com o suporte para os eletroímãs, uma vez que a ponte-H é responsável por alimentar estes e permitir sua polarização e despolarização de maneira imediata e precisa). Com isso, desenvolvemos a estrutura necessária para garantir a segurança e eficiência dessa parte da solução, soldando os dispositivos em uma placa universal de maneira adequada. Segue o esquemático para consolidar esse sistema:

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Diagrama%20Esquem%C3%A1tico%20Placa%20Principal.jpg?raw=true" width="50%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 27 — Esquemático da placa do microcontrolador integrado à ponte H</b></font></p>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Frente.jpg?raw=true" width="40%" height=auto></img></p>
<p align="center"><font size=2><b>Figura 28 — Placa principal: microcontrolador, ponte H e buzzer</b></font></p>

  
## Dispositivos Mecânicos

### Materiais e métodos da fabricação dos dispositivos mecânicos

As imagens incluídas na documentação mostram o processo de impressão 3D das peças. <br>
As figuras DB1 e DC1 representam a posição da peça a ser impressa, já as figuras DB2 e DC2 representam o processo de fatiamento - que define o caminho percorrido pelo bico da impressora para imprimir todos os detalhes do objeto. As linhas verdes presentes nas primeiras figuras representam a base da impressão, que é responsável por sustentar toda a peça durante o processo de impressão. Além disso, os filamentos de suporte visíveis na imagem auxiliam na impressão de partes que requerem suporte adequado. <br>
A fim de tornar os dispositivos adequado às necessidades do projeto, o material escolhido foi o filamento PLA.
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/desenhos_tecnicos/arquivos_impressao/1.jpeg?raw=true" width=35%></img></p><br>
<p align="center"><font size=1>Figura DB1 — Posição da parte inferior do dispositivo que comporta os eletroímãs</font></p><br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/desenhos_tecnicos/arquivos_impressao/3.jpeg?raw=true" width=25%></img></p><br>
<p align="center"><font size=1>Figura DC1 — Posição da parte superior do dispositivo que comporta os eletroímãs</font></p><br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/desenhos_tecnicos/arquivos_impressao/2.jpeg?raw=true" width=35%></img></p><br>
<p align="center"><font size=1>Figura DB2 — Fatiamento da parte inferior do dispositivo que comporta os eletroímãs</font></p><br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/desenhos_tecnicos/arquivos_impressao/4.jpeg?raw=true" width=25%></img></p>
<p align="center"><font size=1>Figura DC2 — Fatiamento da parte superior do dispositivo que comporta os eletroímãs</font></p><br>

### Bandeja radial

**Observação:** a prototipação da bandeja radial limita-se às versões iniciais da arquitetura da solução. Dadas as limitações encontradas, foi necessário o descarte da ideia e a posterior utilização de bandejas padronizadas de formato retangular.

 Tecnologias utilizadas:

 - Autodesk Inventor
- Impressora 3D

Diante da análise das dimensões de movimento do braço robótico (Rotação de 270° e 34 cm de raio), optamos por um conjunto de três bandejas radiais que permitirão o aproveitamento máximo dessas dimensões. Segue o esquemático:

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Conjunto%20de%20Bandeja%20Radial.jpg?raw=true" width="70%" height=auto></img></p>

## Validação de Dispositivos

Para fins de validação dos protótipos iniciais da solução, segue a consolidação da integração dos componentes: [Eletroimã e Sensor-iv](#eletroímã-e-sensor-infravermelho), [Balança Invertida](#célula-de-carga---balança-invertida) e [Raspberry e Ponte-H](#raspberry-pi-pico-w-e-ponte-h) e vídeo de seu funcionamento:

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Diagrama%20Esquem%C3%A1tico%20Placa%20Principal.jpg?raw=true" width="70%" height=auto></img></p>

<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/edicao-documentacao/media/Critical-Prototype.jpg?raw=true" width="70%" height=auto></img></p>


 Vídeo demonstrativo dos dispositivos em funcionamento:
 
[<p align="center"><img src="https://lh4.googleusercontent.com/72hif2xu81BUXbT-QnjV6JxvITd-5OMrs_6IRucYrypywCMPoHQbRooMXUI68x3uT1HOcjXxZzqC4WylVjOw3ospo_CIIq_OPmc0d3pswFj2GK29BPvGuL-KFxiPYhK57hlKPKO8l5GG_PTrYPJQdXg" width="80%"></p>](https://drive.google.com/file/d/1txtCYVejKdHhF4Ub3VqGtsHanooMbTtl/view?usp=sharing)

## Análise do Processamento de Informações e Regras de Negócio

A comunicação entre dispositivos é fundamental para o sucesso do projeto em questão. Nesse sentido, para garantir um desempenho eficiente e preciso, foi necessário o desenvolvimento de um backend que atenda às necessidades específicas do sistema. A presente seção tem como objetivo apresentar as principais características e funcionalidades desse backend, visando fornecer informações claras e objetivas para o uso e manutenção dos dispositivos envolvidos.

### Instruções de instalação gerais
1. Instale a última versão do Python (3.11.2) <br>
- Documentação de instalação do Python: https://docs.python.org/3/download.html <br>
2. Instale uma IDE compatível com o Raspberry Pi Pico W (Para todo o desenvolvimento do projeto e suas testagens foi-se utilizado o Thonny) <br>
- Documentação de instalação do Thonny: <br>
Para Windows: https://github.com/thonny/thonny/wiki/Windows <br>
Para Mac: https://github.com/thonny/thonny/wiki/MacOSX <br>
Para Linux: https://github.com/thonny/thonny/wiki/Linux <br>
3. A ordem das conexões da barra de pinos macho da placa principal deve ser seguida conforme a imagem abaixo, onde: <br>
<b>A:</b> Comunicação da balança <br>
<b>B:</b> Comunicação da balança <br>
<b>C:</b> 5V da balança <br>
<b>D:</b> Acionador do led <br>
<b>E:</b> Acionador do led <br>
<b>F:</b> GND da balança <br>
<b>G:</b> 2ª polaridade do eletroimã <br>
<b>H:</b> GND do Led <br>
<b>I:</b> 1ª polaridade do eletroimã <br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/esquematicos_eletronicos/Foto%20real%20do%20esquema%20de%20conex%C3%A3o%20da%20Placa%20Principal.jpg?raw=true"  width="40%"></p>
<p align="center"><font size="1"> Figura xx: Conexão da placa principal e etiquetagem dos jumpers </font></p>

### Representação dos arquivos de backend do projeto:

### Célula de Carga
<b>Nome do arquivo:</b> backend_celula_de_carga.py <br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/diagramas_backend/C%C3%A9lula%20de%20carga.png?raw=true"  width="25%"></p>
<p align="center"><font size="1"> Figura xx: Diagrama de funcionamento simplicado do código da célula de carga </font></p><br>

### Eletroímã
<b>Nome do arquivo:</b> backend_iv_e_eletroima.py <br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/raw/main/docs/diagramas_backend/Eletro%C3%ADm%C3%A3.png"  width="25%"></p>
<p align="center"><font size="1"> Figura xx: Diagrama de funcionamento simplicado do código do eletroímã </font></p><br>

### Dobot
<b>Nome do arquivo:</b> controle_dobot_lite.py <br>
<p align="center"><img src="https://github.com/2023M5T2-Inteli/2023M5T2-Inteli-grupo-5-Magneminers/blob/main/docs/diagramas_backend/Controle%20do%20Dobot.png?raw=true"  width="25%"></p>
<p align="center"><font size="1"> Figura xx: Diagrama de funcionamento simplicado do código de controle do dobot </font></p><br>

# Referências
  

# Anexos

[Protótipo da Solução](https://www.figma.com/file/qpL2svgLY1MpCohLCb2k15/Magne?node-id=0%3A1&t=zmi4EzKLzb1IFHik-1)

[Arquitetura da Solução](https://drive.google.com/file/d/1GmHzUDCgvJjUn4TxMIrUaGz_GWzLzhXE/view?usp=sharing)

[Apresentação Sprint I - Entendimento do Negócio e Entendimento do Design](https://drive.google.com/file/d/1Jz6XxM3A0B85eHnMizRiv6yyCspteYLu/view?usp=share_link)
