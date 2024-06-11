describe('Importar Planilha', () => {
  it('Importando', () => {
      cy.visit('/')

      cy.get('.login > input').type("professor")
      cy.get('.password > input').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 1")
      cy.get('.create-group-container > #confirmButton').click()

      cy.get('#addStudent').click()
      
      const fileName = 'PlanilhaFact.xlsx' 
     

      cy.get('form').contains("arquivo").attachFile(fileName)
  })
})