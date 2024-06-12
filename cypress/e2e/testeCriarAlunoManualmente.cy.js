describe('Criar Aluno Manualmente', () => {
    it('Criar aluno X18', () => {
        cy.visit('/')
        
        cy.get('.login > input').type("professor")
        cy.get('.password > input').type('senha123')
        cy.get('button').click()

        cy.get('#addStudent').click()
        cy.get('.tabs').contains("Manualmente").click()
        cy.get('#nome').type("X18")
        cy.get('#emailSchool').type("X8@cesar.school")
        cy.get('#matricula').type("2024100018")
        cy.get('#turma').type("DESG20241_A")
        cy.get('#add-manually > .add-student-container > #confirmButton').click()  
    })
   
  })