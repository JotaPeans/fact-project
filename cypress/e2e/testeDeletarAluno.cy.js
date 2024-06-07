describe('Deletar ALuno', () => {
  it('Deletar Aluno X9', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Deletar A")
      cy.get('form > button').contains('Enviar').click()
      
      cy.get('.group > a').contains('Deletar A').closest('.group').as('DA')
      cy.get('@DA').within(() => { 
        cy.get('a').click()
    })

     
      const fileName = 'Copy_of_Fake_FACT_-_Grupo_0X_respostas_arrumado.xlsx' 

      cy.get('#uploadfileInput').attachFile(fileName)
      cy.get('button').click()

      cy.get('#toEdit').click()
      cy.get('#deletarAluno').click()
      cy.get('#displayDeAlunos').contains('X9').click({force: true})
      cy.get('#remover-confirmation').click()
      cy.get('#save').click()

      // Wait for the header link to be available and clickable
    cy.get('header > a').should('be.visible').then(($link) => {
      if ($link.length) {
        // If the link is found, click it
        cy.wrap($link).click();
      }
    })

      cy.get('@DA').within(() => {
          cy.get('.popover-button').click()
          cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
  })
})