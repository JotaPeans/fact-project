describe('Deletar um grupo', () => {
  it('Criar', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo")
      cy.get('form > button').click()
  })

  it('Deletar', () => {
    cy.visit('/')

    cy.get('[placeholder="Usuário"]').type("professor")
    cy.get('[placeholder="Senha"]').type('senha123')
    cy.get('button').click()

    cy.get('.group > .popover-container > .popover-button').click()
    cy.get('.popover-content > .delete-group').click()
    cy.get('#delete-group-link').click()
  
})
 
})