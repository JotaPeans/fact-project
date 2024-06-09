<h1 align="center">✔️ Fact </h1>
<div align="center">
   <img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/t/JotaPeans/fact-project/main">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/JotaPeans/fact-project">
</div>
<p align="center"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Status">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Status">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="Status">
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt="Status">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="Status">
    <img src="https://img.shields.io/badge/Pandas-1572B6?style=for-the-badge&logo=Pandas&color=black" alt="Status"></p>


Nós, do grupo VERTEX, apresentamos o FaCT: Uma solução web inovadora para avaliação e feedback contínuos. 📊📈


A aplicação é:

- Essencial para Promover a Transparência e Objetividade nas Avaliações 🌟;
- Perfeita para Acompanhar o Desenvolvimento de Competências 🛠️;
- Excelente para Fomentar um Ambiente de Feedback Construtivo 💬;
- Uma Ferramenta Valiosa para Decisões Baseadas em Dados 🔍;
- Incentiva a Autogestão e o Autoaprimoramento 🚀;
- Fomenta a Cultura de Excelência e Melhoria Contínua 🌱;

## Integrantes
* Antonio Paulo Barros

* Clara Machado de Araújo

* Davi Gomes

* João Pedro Fontes

* Heloísa Tanaka

* Larissa Sobrinho Santos

* Leonardo Guedes

## Histórias e Validações 📜

1. Eu, como usuário professor, gostaria de criar um grupo;
2. Eu, como usuário professor, desejo importar uma planilha FACT;
3. Eu, como usuário professor, gostaria de visitar a página de cada grupo;
4. Eu, como usuário professor, gostaria de criar um aluno manualmente;
5. Eu, como usuário professor, desejo excluir um aluno de um grupo;
6. Eu, como usuario professor, gostaria de adicionar outros usuários professor para gerenciar o grupo;
7. Eu, como usuário professor, gostaria de excluir grupos existentes;
8. Eu, como usuário professor, gostaria de mudar qualquer informação relacionado aos alunos;
9. Eu, como usuario professor, gostaria de criar um form de avaliação para cada grupo automaticamente;
10. Eu, como usuário professor, gostaria de adicionar um aluno novo manualmente ao grupo.


    ## Validações
      
    - **História 1**: Criar um Grupo  <br/>
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu importo uma planilha com as informações dos alunos participantes do gurpo,
                                   Então o novo grupo deve ser adicionado à lista de grupos e uma mensagem de confirmação deve ser exibida.

    - **História 2**: Importar Planilha <br/> 
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu seleciono a opção de importar planilhas, faço o upload do arquivo correto e confirmo a importação,
                                   Então os dados da planilha devem ser importados e atualizados no sistema, e uma mensagem de confirmação deve ser exibida. 

    - **História 3**: Visualizar Informações de Grupo <br/>
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu clico no nome de um grupo na lista de grupos,
                                   Então eu devo ser redirecionado para a página desse grupo específico, onde posso ver detalhes e gerenciar o grupo.

    - **História 4**: Adicionar um Aluno <br/>
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu preencho os dados do aluno e clico no botão de criar aluno,
                                   Então o novo aluno deve ser adicionado à lista de alunos e uma mensagem de confirmação deve ser exibida. 

    - **História 5**: Excluir um Aluno <br/>
      - **Validação de história**: Dado que eu sou um usuário autenticado com permissões para gerenciar alunos em um grupo,
                                   Quando eu acesso a lista de alunos do grupo, seleciono o aluno que desejo excluir e clico na opção de excluir,
                                   Então o aluno deve ser removido da lista de alunos do grupo e uma mensagem de confirmação deve ser exibida.
        
    - **História 6**: Adicionar outros usuários professor para gerenciar o grupo <br/>
       - **Validação de história**: Dado que eu sou um usuário professor autenticado e tenho permissões de administrador do grupo,
                                    Quando eu seleciono a opção de adicionar professor, insiro os detalhes do novo professor e confirmo,
                                    Então o novo professor deve ser adicionado à lista de administradores do grupo e uma notificação de sucesso deve ser exibida.
         
    - **História 7**: Excluir grupos existentes <br/>
      - **Validação de história**: Dado que eu sou um usuário autenticado com permissões para excluir grupos,
                                   Quando eu seleciono um grupo existente e clico na opção de excluir,
                                   Então o grupo deve ser removido da lista de grupos.
        
    - **História 8**: Mudar qualquer informação relacionada aos alunos <br/>
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu seleciono um aluno, edito as informações desejadas e salvo as alterações,
                                   Então as novas informações do aluno devem ser atualizadas no sistema e uma mensagem de confirmação deve ser exibida.
        
    - **História 9**: Criar um formulário de avaliação para cada grupo automaticamente <br/>
      - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu seleciono a opção de criar um formulário de avaliação e confirmo a criação para cada grupo,
                                   Então um formulário de avaliação deve ser gerado automaticamente para cada grupo e uma mensagem de confirmação deve ser exibida.
        
    - **História 10**: Adicionar um aluno novo manualmente ao grupo <br/>
         - **Validação de história**: Dado que eu sou um usuário professor autenticado,
                                   Quando eu seleciono um grupo, insiro os detalhes do novo aluno e confirmo a adição,
                                   Então o aluno deve ser adicionado à lista de alunos do grupo selecionado e uma mensagem de confirmação deve ser exibida.
   

## Link de produção
### <a target="_blank">https://fact-project.azurewebsites.net</a>

<br/>

<details>
  <summary><h1>Primeira Entrega 📦</h1></summary>

  ## Diagrama

  ![image](https://github.com/JotaPeans/fact-project/assets/142417937/f5e9b824-4de7-4464-bb53-b6fd6a54aa93)


  ## Relatos do método Pair Programming

  *Relato Programação em Par:*
  - **Larissa e Heloísa**:
      Realizamos pair programming para implementar recursos de HTML e CSS.
    
      *Resultado:* A implementação ocorreu perfeitamente bem e como esperado. Html do site e polimento do CSS saiu como planejado e ficamos contentes com o resultado, além de, encontrar e relatar bugs.
    
      *Conclusão:* Pair programming fortaleceu nossa colaboração e confiança como equipe.

  - **Leonardo e João Pedro**:
      Adotamos o pair programming para otimizar o uso do Pandas e aprimorar aspectos de desenvolvimento frontend.
    
      *Resultado:* A colaboração resultou em um uso eficiente do Pandas, permitindo manipulações de dados complexas e otimizadas. Além disso, conseguimos implementar e refinar a interface do usuário com técnicas avançadas de frontend, melhorando a usabilidade e estética do projeto. Durante o processo, também identificamos e corrigimos diversos bugs.
    
      *Conclusão:* O pair programming não só melhorou a qualidade do nosso trabalho, mas também reforçou nossa capacidade de trabalhar juntos de forma eficaz, aumentando a confiança mútua e a habilidade de resolver problemas em equipe.

  - **Davi e Clara**:
      Realizamos pair programming para ajustar o HTML da página de login.
    
      *Resultado:* Após algumas discordâncias entre duas opções de layout, chegamos a um consenso. Essa escolha resultou numa versão final que não só atendeu aos requisitos técnicos, mas também às necessidades dos usuários. Esse processo colaborativo nos permitiu identificar e solucionar questões chave para a melhoria da página.
    
      *Conclusão:* O pair programming reforçou nossa colaboração e confiança como equipe, mostrando que a comunicação eficaz é essencial para superar divergências e alcançar um objetivo comum.

  - **Leonardo e Antonio**:
      Empregamos o pair programming para a criação e edição de áreas de frontend em nosso projeto.
    
      *Resultado:* A sessão de programação conjunta possibilitou uma criação eficiente de interfaces de usuário atraentes e responsivas. Ajustamos e otimizamos o código HTML e CSS para garantir compatibilidade e performance em diversos dispositivos. Além disso, conseguimos identificar e corrigir erros de design e funcionalidade durante o desenvolvimento.
    
      *Conclusão:* O pair programming provou ser uma estratégia valiosa, não apenas para a qualidade técnica do trabalho, mas também para fortalecer nossa colaboração e comunicação como equipe. A experiência reforçou nossa confiança mútua e habilidade de trabalhar juntos sob diferentes desafios técnicos.


  ## ScreenCast Protótipo Lo-Fi

  ### <a target="_blank">https://drive.google.com/file/d/16dqrQXCb4nZW6ziJDBjjgWukM2sCImw5/view?usp=sharing</a>

  ## ScreenCast do Uso do Sistema

  ### <a target="_blank">https://drive.google.com/file/d/1BaxPXs_i-CIUNxLiuHPePcDXowg_S8I7/view?usp=sharing</a>

  <br/><br/>
   ## Issue/Bug Tracker

  ![image](https://github.com/JotaPeans/fact-project/assets/95260401/f81995f8-1bf9-4d1f-a234-8088fe5b0d4e)

   <br/><br/>
  ![LOGO FACT](https://github.com/JotaPeans/fact-project/assets/130470569/873cab2c-2c03-45fb-8791-952a7ddc7a7b)
</details>

<br/>

# Contribuidores 👨‍👩‍👧‍👦
<a href="https://github.com/JotaPeans/fact-project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jotapeans/fact-project" />
</a>
<p><a href="https://github.com/apabsp">Antonio Paulo Barros</a> - apabsp@cesar.school 📩</p>
<p><a href="https://github.com/helotanaka">Heloisa Tanaka</a> - htf@cesar.school 📩</p>
<p><a href="https://github.com/leooghub">Leonardo Guedes</a> - lccg@cesar.school 📩</p> 
<p><a href="https://github.com/jotapeans">João Pedro Fontes</a> - jpff2@cesar.school 📩</p>
<p><a href="https://github.com/lariisantos">Larissa Santos</a> - lss2@cesar.school 📩</p>
<p><a href="https://github.com/claramachadoaj">Clara Machado</a> - cma3@cesar.school 📩</p>
<p><a href="https://github.com/daviruy61">Davi Gomes</a> - dgfra@cesar.school 📩</p>
