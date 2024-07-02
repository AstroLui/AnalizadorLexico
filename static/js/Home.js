const codeSpace = document.getElementById("codeSpace");

function Compilar()
{
    var datos = document.getElementById("codeSpace").value;
    var request = new Request('resultado', 
    {
        method: 'POST',
        body: JSON.stringify({ data : datos }),
        headers: new Headers()
    });
    fetch(request)
    .then(response => response.json())
    .then(data =>
        {
            tokens = data['data'];
            console.log(tokens)
            AddCodeSpace(tokens);
            
        })
    .catch(error =>{
        console.log(error);
    })

}

function AddCodeSpace(data){
    var codeSpaceMirror = document.getElementById("codeSpaceMirror");
    codeSpaceMirror.innerHTML = ``
    Object.entries(data).forEach(([key, value]) =>{
        var code = document.createElement('div');
        code.innerHTML = 
        `
            <pre data-prefix=${key}><code>${value['1']}</code></pre>
        `
        codeSpaceMirror.appendChild(code);
    })
}
