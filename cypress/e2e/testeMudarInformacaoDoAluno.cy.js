describe('Mudar Informação do Aluno', () => {
  it('Mudar Informação do Aluno X5', () => {
    cy.visit('/')

    cy.get('[placeholder="Usuário"]').type("professor")
    cy.get('[placeholder="Senha"]').type('senha123')
    cy.get('button').click()

    cy.get('#addGroup').click()
    cy.get('#name').type("Mudar A")
    cy.get('form > button').contains('Enviar').click()
    
    cy.get('.group > a').contains('Mudar A').closest('.group').as('MA')
    cy.get('@MA').within(() => { 
      cy.get('a').click()
    })

    const fileName = 'Copy_of_Fake_FACT_-_Grupo_0X_respostas_arrumado.xlsx'

    cy.get('#uploadfileInput').attachFile(fileName)
    cy.get('button').click()

    cy.get('main > .alunos-container').contains('X5').click()
    cy.get('[open=""] > .detalhesLowerButtons > .editarAluno').click()
    cy.get('#nomeDoAluno').clear().type('XNovo')
    cy.get('#emailDoAluno').clear().type('XNovo@cesar.school')
    cy.get('#confirmar-editar-aluno').click()

    cy.get('header > a').should('be.visible').then(($link) => {
      if ($link.length) {
        cy.wrap($link).click();
      }
    })

      cy.get('@MA').within(() => {
          cy.get('.popover-button').click()
          cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
  })
})
