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
    var iLine = 1;
    var content = '';
    var tooltip = '';
    for(var i = 0; i < Object.entries(data).length; i++){
        if(data[i]['0'] != "NEWLINE"){
            content += data[i]['1'] + ''
            if(i == Object.entries(data).length-1){
                tooltip += data[i]['0']
            }else{
                tooltip += data[i]['0'] + ' - '
            }
        }else if(data[i]['0'] == "NEWLINE"){
            newLine(codeSpaceMirror, tooltip, iLine, content);
            iLine++;
            newLineEmpty(codeSpaceMirror, iLine);
            iLine++;
        }
    }
    newLine(codeSpaceMirror, tooltip, iLine, content);
    iLine++;
}

function newLine(nodeFather, tooltip, iLine, content){
    var code = document.createElement('div');
        code.innerHTML = 
        `
            <div class="tooltip tooltip-bottom" data-tip="${tooltip}">
                <pre class="cursor-pointer" data-prefix=${iLine}>${content}</pre>
            </div>
        `
    nodeFather.appendChild(code); 
}
function newLineEmpty(nodeFather, iLine){
    var code = document.createElement('div');
        code.innerHTML = 
        `
            <div>
                <pre class="cursor-pointer" data-prefix=${iLine}></pre>
            </div>
        `
    nodeFather.appendChild(code); 
}