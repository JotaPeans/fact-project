import 'cypress-file-upload'

describe('Importar Planilha', () => {
  it('Importando', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      cy.get('#addGroup').click()
      cy.get('#name').type("Grupo")
      cy.get('form > button').click()
      cy.get('.group > a').click()
  })
})