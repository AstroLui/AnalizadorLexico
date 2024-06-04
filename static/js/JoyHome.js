function openMenu()
{ 
    var menu = document.getElementById('menuInit');
    var menuBool = menu.classList.contains('hidden'); 

    (menuBool)
    ?
        menu.classList.remove('hidden')
    :
        menu.classList.add('hidden')
}
var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    // muestro las líneas de código
    lineNumbers: true,
    // elijo el tema
    theme: 'icecoder',
    mode: 'python',
    // esto deshabilita la opción de reescribir
  });