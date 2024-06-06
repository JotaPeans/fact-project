describe('Adicionar ALuno', () => {
  it('Adicionar Aluno X13', () => {
    cy.visit('/')

    cy.get('[placeholder="Usuário"]').type("professor")
    cy.get('[placeholder="Senha"]').type('senha123')
    cy.get('button').click()

    cy.get('#addGroup').click()
    cy.get('#name').type("Adicionar A")
    cy.get('form > button').click()
    
    cy.get('.group > a').contains('Adicionar A').closest('.group').as('AA')
    cy.get('@AA').within(() => { 
      cy.get('a').click()
    })

    const fileName = 'Copy_of_Fake_FACT_-_Grupo_0X_respostas_arrumado.xlsx'

    cy.get('#uploadfileInput').attachFile(fileName)
    cy.get('button').click()

    cy.get('#toEdit').click()
    cy.get('#adicionarAluno').click()
    cy.get('form > .aluno-unit').type("X13")
    cy.get('#adicionar-confirmation').click()
    cy.get('#save').click()

    // Wait for the header link to be available and clickable
    cy.get('header > a').should('be.visible').then(($link) => {
      if ($link.length) {
        // If the link is found, click it
        cy.wrap($link).click();
      }
    })

    cy.get('@AA').within(() => {
      cy.get('.popover-button').click()
      cy.get('.popover-content > .delete-group').click()
    })
    cy.get('#delete-group-link').click()
  })
})
