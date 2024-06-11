// cypress/support/file-upload-utils.js
Cypress.Commands.add('uploadFile', (fileName, fileType = ' ', selector) => {
    cy.fixture(fileName, 'base64').then((content) => {
      const el = document.querySelector(selector);
      const blob = b64toBlob(content, fileType);
      const file = new File([blob], fileName, { type: fileType });
      const dataTransfer = new DataTransfer();
      dataTransfer.items.add(file);
      el.files = dataTransfer.files;
      cy.wrap(el).trigger('change', { force: true });
    });
  });
  
  function b64toBlob(b64Data, contentType = '', sliceSize = 512) {
    const byteCharacters = atob(b64Data);
    const byteArrays = [];
  
    for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      const slice = byteCharacters.slice(offset, offset + sliceSize);
  
      const byteNumbers = new Array(slice.length);
      for (let i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }
  
      const byteArray = new Uint8Array(byteNumbers);
  
      byteArrays.push(byteArray);
    }
  
    const blob = new Blob(byteArrays, { type: contentType });
    return blob;
  }
  