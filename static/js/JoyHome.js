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
    mode: 'javascript',
    // esto deshabilita la opción de reescribir
});


function Compilar()
{
    var datos = editor.getValue()
    var request = new Request('resultado', 
    {
        method: 'POST',
        body: JSON.stringify({ data : datos}),
        headers: new Headers()
    });
    fetch(request)
    .then(response => response.json())
    .then(data =>
        {
            document.getElementById('result').value = data['data'];
        })
    .catch(error =>{
        console.log(error);
    })

}

