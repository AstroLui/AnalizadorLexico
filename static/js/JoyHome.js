var editor = ace.edit("editor");
function Compilar()
{
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

