describe('Visitar grupos', () => {
  it('Visitar G1, G2, G3', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 1")
      cy.get('form > button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 2")
      cy.get('form > button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo 3")
      cy.get('form > button').click()
  })
})