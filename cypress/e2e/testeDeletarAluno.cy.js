describe('Deletar ALuno', () => {
  it('Deletar Aluno X9', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      //cy.get('#addGroup').click()
      //cy.get('#name').type("Deletar A")
      //cy.get('form > button').click()
      
      cy.get('.group > a').contains('Deletar A').closest('.group').as('DA')
      cy.get('@DA').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('a').click()
    })

      //importar planilha

      cy.get('#toEdit').click()
      cy.get('#deletarAluno').click()
      cy.get('#displayDeAlunos').contains('X9').click({force: true})
      cy.get('#remover-confirmation').click()
      cy.get('#save').click()

      // Verifica se o seletor está selecionando o elemento correto
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            // Se o link for encontrado, clique nele
            cy.wrap($link).click();
        }
      })


      cy.get('.group > a').contains('Deletar A').closest('.group').as('DA')
      cy.get('@DA').within(() => {
          cy.get('.popover-button').click()
          cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
  })
})