describe('Adicionar admin a um grupo', () => {
  it('Admin Grupo 1', () => {
      cy.visit('/')

      cy.get('.login > input').type("professor")
      cy.get('.password > input').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 1")
      cy.get('form > button').contains('Confirmar').click()

      cy.visit('/')

      cy.get('.group > a').contains('Grupo 1').closest('.group').as('G1') //captura elemento pai
      cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
          cy.get('.popover-button').click()
          cy.get('.popover-content > .gerenciar-group').click()
      })
      cy.get('#usuariosProfessores').select('coordenador')
      cy.get('#botaoDoConfia').click()

      cy.visit('/')

      cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
          cy.get('.popover-button').click()
          cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
  })
 
})