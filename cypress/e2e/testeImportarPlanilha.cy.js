describe('Importar Planilha', () => {
  it('Importando', () => {
      cy.visit('/')

      cy.get('.login > input').type("professor")
      cy.get('.password > input').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo")
      cy.get('form > button').contains('Confirmar').click()
      
      cy.get('.group > a').contains('Grupo').closest('.group').as('G')
      cy.get('@G').within(() => { 
        cy.get('a').click()
      })

      const fileName = 'Copy_of_Fake_FACT_-_Grupo_0X_respostas_arrumado.xlsx' 

      cy.get('#uploadfileInput').attachFile(fileName)
      cy.get('button').click()

      cy.get('header > a').then(($link) => {
        if ($link.length) {
            // Se o link for encontrado, clique nele
            cy.wrap($link).click();
        }
      })

      cy.get('@G').within(() => {
          cy.get('.popover-button').click()
          cy.get('.popover-content > .delete-group').click()
      })
      cy.get('#delete-group-link').click()
  })
})