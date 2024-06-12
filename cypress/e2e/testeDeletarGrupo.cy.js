describe('Deletar um grupo', () => {
  it('Deletar Grupo 1', () => {
    cy.visit('/')

    cy.get('.login > input').type("professor")
    cy.get('.password > input').type('senha123')
    cy.get('button').click()

    cy.get('#addGroup').click()
    cy.get('#name').type("Grupo 1")
    cy.get('.create-group-container > #confirmButton').click()
    cy.get('#addGroup').click()
    cy.get('#name').type("Grupo 2")
    cy.get('.create-group-container > #confirmButton').click()

    cy.get('.group > div > a').contains('Grupo 1').closest('div').as('G1')
    cy.get('@G1').within(() => { 
        cy.get('.popover-container').click()
        cy.get('.popover-content > button').contains("Deletar").click()
    })
    cy.get('#delete-group-link').click()
  })

  it('Deletar Grupo 2', () => {
    cy.visit('/')

    cy.get('.login > input').type("professor")
    cy.get('.password > input').type('senha123')
    cy.get('button').click()

    cy.get('.group > div > a').contains('Grupo 2').closest('div').as('G2')
    cy.get('@G2').within(() => { 
        cy.get('.popover-container').click()
        cy.get('.popover-content > button').contains("Deletar").click()
    })
    cy.get('#delete-group-link').click()
  
})
 
})