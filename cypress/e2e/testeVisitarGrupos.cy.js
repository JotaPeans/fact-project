describe('Visitar grupos', () => {
  it('Criar', () => {
      cy.visit('/')

      cy.get('[placeholder="Usuário"]').type("professor")
      cy.get('[placeholder="Senha"]').type('senha123')
      cy.get('button').click()

      
  })
})