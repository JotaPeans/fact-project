describe('Mudar Informação do Aluno', () => {
  it('Mudar Informação do Aluno X5', () => {
    cy.visit('/')

    cy.get('.login > input').type("professor")
    cy.get('.password > input').type('senha123')
    cy.get('button').click()

    cy.get('#addGroup').click()
    cy.get('#name').type("Grupo 1")
    cy.get('.create-group-container > #confirmButton').click()

    cy.get('.group > div > a').contains('Grupo 1').closest('div').as('G1')
    cy.get('@G1').within(() => {
      cy.get('a').click()
    })

    cy.get('.myGroupButtons > a').click()
    cy.get('#select-cc').select('X7')
    cy.get('#select-cc').select('X5')
    cy.get('.confirm').click()
    cy.get('.back-url').click()

    cy.get('.alunos-container > details').contains("X5").click()
    cy.get('.alunos-container > details > .detalhesLowerButtons > .editarAluno').contains("Editar Aluno").click()
    cy.get('#nome-aluno').type("1")
    cy.get('.save-edit').click()

    cy.get('header > a').then(($link) => {
      if ($link.length) {
          cy.wrap($link).click();
      }
    })

    cy.get('@G1').within(() => { 
      cy.get('.popover-container').click()
      cy.get('.popover-content > button').contains("Deletar").click()
    })
    cy.get('#delete-group-link').click()
  })

  it('Mudar Informação do Aluno X51', () => {
    cy.visit('/')

    cy.get('.login > input').type("professor")
    cy.get('.password > input').type('senha123')
    cy.get('button').click()

    cy.get('#addGroup').click()
    cy.get('#name').type("Grupo 1")
    cy.get('.create-group-container > #confirmButton').click()

    cy.get('.group > div > a').contains('Grupo 1').closest('div').as('G1')
    cy.get('@G1').within(() => {
      cy.get('a').click()
    })

    cy.get('.myGroupButtons > a').click()
    cy.get('#select-cc').select('X7')
    cy.get('#select-cc').select('X51')
    cy.get('.confirm').click()
    cy.get('.back-url').click()

    cy.get('.alunos-container > details').contains("X5").click()
    cy.get('.alunos-container > details > .detalhesLowerButtons > .editarAluno').contains("Editar Aluno").click()
    cy.get('#nome-aluno').clear().type("X5")
    cy.get('.save-edit').click()

    cy.get('header > a').then(($link) => {
      if ($link.length) {
          cy.wrap($link).click();
      }
    })

    cy.get('@G1').within(() => { 
      cy.get('.popover-container').click()
      cy.get('.popover-content > button').contains("Deletar").click()
    })
    cy.get('#delete-group-link').click()
  })
})
