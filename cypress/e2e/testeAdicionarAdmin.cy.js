describe('Adicionar admin a um grupo', () => {
  it('Admin Grupo 1', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 1")
      cy.get('form > button').contains('Enviar').click()

      cy.get('.group > a').contains('Grupo 1').closest('.group').as('G1') //captura elemento pai
      cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
          cy.get('.popover-button').click()
          cy.get('.popover-content > .gerenciar-group').click()
      })
      cy.get('#usuariosProfessores').cy.select()
  })
 
})