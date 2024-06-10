describe('Visitar grupos', () => {
  it('Visitar G1, G2, G3', () => {
      cy.visit('/')

      cy.get('.login > input').type("professor")
      cy.get('.password > input').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 1")
      cy.get('form > button').contains('Confirmar').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 2")
      cy.get('form > button').contains('Confirmar').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 3")
      cy.get('form > button').contains('Confirmar').click()


      cy.get('.group > a').contains('Grupo 3').closest('.group').as('G3')
      cy.get('@G3').within(() => { 
        cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('.group > a').contains('Grupo 1').closest('.group').as('G1')
      cy.get('@G1').within(() => { 
        cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('.group > a').contains('Grupo 2').closest('.group').as('G2')
      cy.get('@G2').within(() => { 
        cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('@G1').within(() => {
        cy.get('.popover-button').click()
        cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
      cy.get('@G2').within(() => {
        cy.get('.popover-button').click()
        cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
      cy.get('@G3').within(() => {
        cy.get('.popover-button').click()
        cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()

  })
})