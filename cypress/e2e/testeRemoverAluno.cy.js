describe('Remover ALuno', () => {
  it('Remover Aluno X9', () => {
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
    cy.get('#select-cc').select('X9')
    cy.get('#select-cc').select('X1')
    cy.get('.confirm').click()
    cy.get('.back-url').click()
    
    cy.get('.myGroupButtons > a').click()
    cy.get('.alunos-selected-container > .alunos > #alunos-cc > p').contains("X9").closest('p').as('X9')
    cy.get('@X9').within(() => { 
      cy.get("button").click()
    })
    cy.get('.confirm').click()
    cy.get('.back-url').click()
  })

  it('Remover Aluno X17', () => {
    cy.visit('/')

    cy.get('.login > input').type("professor")
    cy.get('.password > input').type('senha123')
    cy.get('button').click()

    cy.get('.group > div > a').contains('Grupo 1').closest('div').as('G1')
    cy.get('@G1').within(() => {
      cy.get('a').click()
    })

    cy.get('.myGroupButtons > a').click()
    cy.get('#select-design').select('X17')
    cy.get('#select-design').select('X15')
    cy.get('.confirm').click()
    cy.get('.back-url').click()
    
    cy.get('.myGroupButtons > a').click()
    cy.get('.alunos-selected-container > .alunos > #alunos-design > p').contains("X17").closest('p').as('X17')
    cy.get('@X17').within(() => { 
      cy.get("button").click()
    })
    cy.get('.confirm').click()
    cy.get('.back-url').click()
    cy.get('header > a').then(($link) => {
      if ($link.length) {
          cy.wrap($link).click();
      }
    })

    cy.get('@G1').within(() => { //define um contexto restrito ao elemento pai capturado
      cy.get('.popover-container').click()
      cy.get('.popover-content > button').contains("Deletar").click()
    })
    cy.get('#delete-group-link').click()
  })

})