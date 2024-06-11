describe('Importar Planilha', () => {
  it('Importando', () => {
      cy.visit('/')

      cy.get('.login > input').type("professor")
      cy.get('.password > input').type('senha123')
      cy.get('button').click()

      cy.get('#addStudent').click()
      
      const fileName = 'PlanilhaFact.xlsx' 
     

      cy.get('#alunos-upload').attachFile(fileName)
      cy.wait(100)
      cy.get('#upload-excel > .add-student-container > #confirmButton').click()
  })
})