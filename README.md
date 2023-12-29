<h1> CardioCheck </h1>

Uma aplicação para a triagem de pacientes em contexto cardíaco, fazendo uso de modelos treinados em um [dataset](https://www.kaggle.com/datasets/hossamahmedaly/patient-priority-classification) do Kaggle.

Assim que um novo paciente chega ao local, o usuário pode, então, coletar informações básicas sobre o seu estado atual e passá-las por um modelo de
Machine Learning especializado, que realiza a triagem automaticamente. Existem, no momento 04 etiquetas de triagem possíveis, com maiores detalhes em uma página específica
da aplicação.

Devido a natureza do processo de triagem, eu achei pertinente disponibilizar dois modelos distintos: um para situações mais urgentes, aonde não há tempo de realizar
exames ou busca por resultados e outro para análise mais minuciosa. O primeiro modelo foi treinado em 09 colunas do dataset (com 92% de acurácia) e o último
em 14 colunas, com (99% de acurácia).

A aplicação está disponível em: https://cardiocheck.streamlit.app/.

<p align="center">
  <img src="https://github.com/KalimaraPeleteiro/CardioCheck/assets/94702837/d953f53c-5ec3-4803-b619-676edec4745b" width="400" />
  <img src="https://github.com/KalimaraPeleteiro/CardioCheck/assets/94702837/ff10264e-82b6-4fa4-9985-b8a536ec13d7" width="400" />
</p>
