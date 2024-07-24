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
            tokens = data;
            console.log(tokens)
            AddCodeSpace(tokens['data']);
            traductor(tokens['trad']);
        })
    .catch(error =>{
        console.log(error);
    })

}
function AddCodeSpace(data){
    var codeSpaceMirror = document.getElementById("codeSpaceMirror");
    codeSpaceMirror.innerHTML = ``
    var iLine = 1;
    var arrayContent = []
    for(var i = 0; i < Object.entries(data).length; i++){
        if(data[i]['0'] != "SALTO"){
            arrayContent.push(new Token(data[i]['1'], data[i]['0']));
        }else if(data[i]['0'] == "SALTO"){
            try {
                if(data[i+1]['0'] == "SALTO"){
                    newLine(codeSpaceMirror, iLine, arrayContent);
                    arrayContent = []
                    iLine++;
                    newLineEmpty(codeSpaceMirror, iLine);
                    iLine++;
                }
                else{
                    newLine(codeSpaceMirror, iLine, arrayContent);
                    arrayContent = []
                    iLine++;
   
                }
            } catch (error) {
                newLine(codeSpaceMirror, iLine, arrayContent);
                arrayContent = []
                iLine++;
                newLineEmpty(codeSpaceMirror, iLine);
                iLine++;
            }
        }
    }
    if(data[Object.entries(data).length-1]['0'] != "SALTO"){
        newLine(codeSpaceMirror, iLine, arrayContent);
        iLine++;
    }

}

function newLine(nodeFather, iLine, arrayContent){
    var code = document.createElement('pre');
    code.className = "flex p-2 gap-2 items-center"
    code.setAttribute("data-prefix", iLine);
    arrayContent.forEach(element => {
        newItem(code, element.getType(), element.getValue());
    });
    nodeFather.appendChild(code); 
}

function newItem(nodeFather, tooltip, content){
    var tooltipContainer = document.createElement('div');
    tooltipContainer.setAttribute("data-tip", tooltip);
    tooltipContainer.classList.add("tooltip");
    tooltipContainer.innerHTML = `<span class="btn">${content}</span>`;
    nodeFather.appendChild(tooltipContainer);
}

function newLineEmpty(nodeFather, iLine){
    var code = document.createElement('div');
        code.innerHTML = 
        `
            <div>
                <pre class="" data-prefix=${iLine}></pre>
            </div>
        `
    nodeFather.appendChild(code); 
}

function traductor(data){
    const traductor = document.getElementById('codeTraductor');
    traductor.innerHTML = ``
    traductor.innerHTML = data    
}
class Token{
    constructor(value, type){
        this.value = value;
        this.type = type
    }
    getValue(){
        return this.value;
    }
    getType(){
        return this.type;
    }
}