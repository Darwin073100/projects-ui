const btnMenuToggle = document.getElementById('btnShowNav');
const menu = document.getElementById('movileMenu');
let isMenu = false;

btnMenuToggle.addEventListener('click',()=>{
    isMenu = !isMenu;
    isMenu? menu.style.display='block' : menu.style.display='none';
});



