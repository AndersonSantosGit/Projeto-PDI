[![Python version](https://img.shields.io/badge/python-v2.7-orange.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.en.html)

# Projeto PDI

Projeto da disciplina Processamento Digital de Imagens (PDI) durante o semestre 2015.2.

Abaixo uma breve descrição dos módulos do projeto:

## Módulo 1 (codificação de cena)
  Entrada: Uma imagem digital
  
  Saída: Posição e descrição das características SIFT da imagem

  O exemplo abaixo ilustra os descritores plotados em uma determinada imagem:
 ![cow_orb](https://cloud.githubusercontent.com/assets/6972758/18066667/ac464440-6e0f-11e6-83ac-bbf5fac73151.png)

## Módulo 3 (segmentação)

  Entrada: Imagem digital
  
  Saída: Imagem segmentada

  O exemplo abaixo ilustra os descritores plotados em uma determinada imagem:
  - Imagem de entrada
  ![house](https://cloud.githubusercontent.com/assets/6972758/18067553/a5788f70-6e13-11e6-9bbd-1c529a5f1966.png)
  - Imagem com _superpixels_ ([SLIC](http://ivrl.epfl.ch/research/superpixels))
  ![house_slic](https://cloud.githubusercontent.com/assets/6972758/18067554/a57d5a78-6e13-11e6-9eb6-19e76b2710d4.png)
  - Imagem segmentada
  ![house_segmentation](https://cloud.githubusercontent.com/assets/6972758/18067778/b76fe254-6e14-11e6-92f8-b637c612127f.png)
  - Síntese
  ![house_three](https://cloud.githubusercontent.com/assets/6972758/18067555/a57f9e3c-6e13-11e6-8872-2ad2470245fb.png)


##Módulo 4 (similaridade entre formas)

  Entrada: Duas imagens digitais segmentadas

  Saída: Índice de similaridade (0 a 100) entre as formas dos objetos

  O exemplo abaixo ilustra uma síntese dos passos para obtenção da similaridade entre duas imagens:

  - Imagem segmentadas
  ![similaridade_gato_aviao](https://cloud.githubusercontent.com/assets/6972758/18068307/12b1994e-6e17-11e6-835d-73faedc84c01.png)
  
 - Match dos descritores entre as imagens
  ![similaridade_gato_aviao_sift](https://cloud.githubusercontent.com/assets/6972758/18068305/12aec50c-6e17-11e6-9f36-e0f34187f00f.png)

<p align="center">
  <strong>SIMILARIDADE: 2.16%</strong> 
</p> 
  
  - Imagem segmentadas
  ![similaridade_aviao_aviao](https://cloud.githubusercontent.com/assets/6972758/18068304/12aba944-6e17-11e6-826a-b086d4a01f5f.png)

  - Match dos descritores entre as imagens
  ![similaridade_aviao_aviao_sift](https://cloud.githubusercontent.com/assets/6972758/18068306/12b16f78-6e17-11e6-9a3d-6c055bb16bb0.png)

<p align="center">
  <strong>SIMILARIDADE: 84.3%</strong> 
</p>


