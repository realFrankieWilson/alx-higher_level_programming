// Check for document parsing.
if (document.readyState == 'loading') {
  // Wait for the DOMContentLoaded event to ensure the script
  // is imported in the <head> tag
  document.addEventListener('DOMContentLoaded', function () {
    changeColor('#FF0000');
  });
} else {
  // Check if the document has already finished parsing
  // If so, the color is changed immediately

  changeColor('#FF0000');
}

function changeColor (color) {
  const element = document.querySelector('header');
  try {
    if (element) {
      element.style.color = color;
    } else {
      throw new Error('<header> element not found');
    }
  } catch (error) {
    console.error(error.message);
  }
}
