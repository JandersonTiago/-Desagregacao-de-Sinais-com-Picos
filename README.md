# Relatório Técnico: Desagregação de Sinal com Picos

## 1. Introdução:
A desagregação de sinal é uma técnica que visa decompor um sinal complexo em suas componentes individuais. Este relatório aborda a metodologia utilizada para desagregar sinais de amplitude ao identificar picos no espectro de frequência. A implementação em Python utiliza bibliotecas como NumPy, SciPy e Matplotlib para processamento de sinais e visualização.

## 2. Metodologia:
A metodologia empregada envolve os seguintes passos:
### 2.1 Carregamento de Dados:
Os dados são carregados a partir de arquivos CSV contendo informações sobre a amplitude e o tempo do sinal.
### 2.2 Aplicação da FFT:
A Transformada Rápida de Fourier (FFT) é aplicada ao sinal para obter seu espectro de frequência.
### 2.3 Identificação de Picos:
Utilizando a função `find_peaks` da SciPy, os picos no espectro de frequência são identificados com base em um threshold definido.
### 2.4 Projeto e Aplicação de Filtros:
São projetados filtros Butterworth de baixa e alta frequência. Os filtros são aplicados ao sinal original para obter componentes de baixa e alta frequência.
### 2.5 Visualização e Salvar Resultados:
Os resultados são visualizados usando a Matplotlib, exibindo o sinal original, a componente de baixa frequência, a componente de alta frequência e os picos identificados. Os dados filtrados são salvos em novos arquivos CSV.

## 3. Parâmetros Ajustáveis:
Os parâmetros ajustáveis incluem as frequências de corte para os filtros de baixa e alta, a taxa de amostragem (`fs`), e a ordem dos filtros (`order`).

## 4. Resultados Obtidos:
Os resultados são apresentados visualmente em gráficos que mostram o sinal original, a componente de baixa frequência, a componente de alta frequência e os picos identificados. Esses gráficos permitem uma análise qualitativa das contribuições de diferentes frequências no sinal original.

## 5. Conclusão:
A desagregação de sinal revela informações valiosas sobre as componentes de frequência presentes nos dados originais. A metodologia implementada permite a identificação de picos no espectro de frequência, oferecendo insights sobre as contribuições de baixa e alta frequência no sinal. Os parâmetros ajustáveis fornecem flexibilidade para adaptar a técnica a diferentes tipos de sinais.

## 6. Sugestões para Melhorias Futuras:
- Explorar técnicas avançadas de processamento de sinais.
- Considerar métodos automatizados para ajuste de parâmetros.
- Avaliar o desempenho da desagregação em diferentes conjuntos de dados.

## 7. Referências:
- Documentação das bibliotecas utilizadas: NumPy, SciPy, Matplotlib.
