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

<details>
  <summary><h1>Segunda Entrega 📦</h1></summary>
  
  <details>
     <summary><h3>Relatos Pair Programing</h3></summary>
   <details>

      
   <summary>Antonio e Clara</summary>
   
   Empregamos o pair programming para desenvolver a funcionalidade de adicionar outros usuários professores ao sistema, permitindo o gerenciamento de grupos.

   **Resultado**: A sessão de programação conjunta resultou na implementação eficaz de uma interface intuitiva e segura, onde professores podem adicionar e gerenciar outros colegas de profissão. Durante o desenvolvimento, focamos em assegurar que a funcionalidade fosse simples e direta, otimizando o fluxo de trabalho do usuário e garantindo a segurança dos dados.

   **Conclusão**: O pair programming provou ser uma abordagem valiosa para o desenvolvimento desta funcionalidade, melhorando não apenas a qualidade técnica do produto, mas também a colaboração e comunicação entre os membros da equipe. A experiência trouxe benefícios significativos em termos de eficiência de desenvolvimento e confiança mútua, reforçando nossa habilidade de enfrentar desafios técnicos de forma coesa.
   </details>

   
   <details>
   <summary>Leonardo e Davi</summary>
   
   Empregaram o pair programming para desenvolver a funcionalidade que permite aos professores modificar informações de alunos no sistema educacional.


   **Resultado**: A sessão de programação conjunta resultou na implementação de um sistema flexível e seguro, onde professores podem alterar informações dos alunos de forma eficaz. Durante o desenvolvimento, focamos em criar uma interface amigável e intuitiva, garantindo que as alterações sejam feitas com precisão e que os dados dos alunos sejam protegidos adequadamente.

   **Conclusão**: O uso do pair programming foi crucial não apenas para a qualidade técnica do desenvolvimento, mas também para fortalecer a colaboração e comunicação entre Leonardo e Davi. Essa abordagem melhorou significativamente a eficiência do processo de desenvolvimento e reforçou a confiança e a habilidade de trabalhar em conjunto diante de desafios técnicos.
   </details>
   <details>
      <summary>João Pedro e Antonio</summary>
    
   Utilizaram o pair programming para desenvolver a funcionalidade que permite aos professores criar automaticamente um formulário de avaliação para cada grupo de alunos.

   **Resultado**: A colaboração direta resultou na implementação de uma funcionalidade que automatiza a criação de formulários de avaliação, melhorando significativamente a eficiência do processo educacional. Durante o desenvolvimento, eles se concentraram em garantir que a interface fosse intuitiva e que os formulários gerados atendessem às necessidades específicas de cada grupo, com opções de personalização flexíveis.

   **Conclusão**: A estratégia de pair programming mostrou-se extremamente valiosa, não só para a qualidade técnica do projeto, mas também para fomentar uma forte colaboração entre João Pedro e Antonio. Essa metodologia não apenas facilitou a resolução de problemas complexos durante o desenvolvimento, mas também fortaleceu a comunicação e a confiança mútua, ampliando a capacidade de ambos para lidar com futuros desafios técnicos.
   </details>
   <details>
   <summary>Tanaka e Larissa</summary>

   Utilizaram o pair programming para implementar a funcionalidade de exclusão de grupos existentes no sistema educacional, com o auxílio de Cypress para testes automatizados.

   **Resultado**: A sessão de codificação conjunta permitiu a criação de uma solução robusta que possibilita aos professores excluir grupos de maneira eficiente e segura. Durante o processo, aprimoramos a interface para garantir uma experiência de usuário clara e sem erros, permitindo que decisões sobre a exclusão de grupos sejam feitas de forma informada e precisa. A utilização do Cypress como ferramenta de testes automatizados assegurou que todos os cenários críticos fossem rigorosamente testados, garantindo a estabilidade e a confiabilidade da funcionalidade.

   **Conclusão**: A estratégia de pair programming, enriquecida pela integração de testes automatizados com Cypress, mostrou-se essencial para a qualidade técnica e a segurança da nova funcionalidade. Além disso, a colaboração intensa entre Tanaka e Larissa durante o desenvolvimento fortaleceu a comunicação e o trabalho em equipe, ampliando a capacidade de lidar com desafios técnicos complexos e reforçando a confiança mútua entre os desenvolvedores.
   </details>
   <details>
      <summary>João Pedro e Leonardo</summary>
   
   
   Utilizaram o pair programming para desenvolver a funcionalidade que permite aos professores adicionar manualmente novos alunos aos grupos no sistema educacional.

   **Resultado**: A sessão de programação conjunta facilitou a implementação de uma interface amigável e eficiente para adicionar alunos. Durante o desenvolvimento, eles se concentraram em criar uma experiência de usuário intuitiva, com validações claras para garantir que os dados do aluno sejam inseridos corretamente. Essa funcionalidade simplifica o processo de gestão de grupos, permitindo aos professores personalizar suas turmas conforme necessário.

   **Conclusão**: A estratégia de pair programming se mostrou extremamente valiosa, melhorando não apenas a qualidade técnica do desenvolvimento, mas também a colaboração entre João Pedro e Leonardo. A metodologia promoveu uma comunicação efetiva e permitiu que ambos os desenvolvedores compartilhassem conhecimentos, resultando em uma solução mais robusta e confiável.
   </details>
  </details>
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
