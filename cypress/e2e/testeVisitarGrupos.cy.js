describe('Visitar grupos', () => {
  it('Visitar G1, G2, G3', () => {
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

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 3")
      cy.get('.create-group-container > #confirmButton').click()


      cy.get('.group > div > a').contains('Grupo 1').closest('div').as('G1')
      cy.get('.group > div > a').contains('Grupo 2').closest('div').as('G2')
      cy.get('.group > div > a').contains('Grupo 3').closest('div').as('G3') //captura elemento pai
      cy.get('@G3').within(() => { //define um contexto restrito ao elemento pai capturado
          cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('@G2').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('a').click()
      })
      cy.get('header > a').then(($link) => {
        if ($link.length) {
            cy.wrap($link).click();
        }
      })

      cy.get('@G3').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('.popover-container').click()
        cy.get('.popover-content > button').contains("Deletar").click()
       })
      cy.get('#delete-group-link').click()
      cy.get('@G2').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('.popover-container').click()
        cy.get('.popover-content > button').contains("Deletar").click()
       })
      cy.get('#delete-group-link').click()
      cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
        cy.get('.popover-container').click()
        cy.get('.popover-content > button').contains("Deletar").click()
       })
      cy.get('#delete-group-link').click()

  })
})