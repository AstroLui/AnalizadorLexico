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
