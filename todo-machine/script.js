const mdlModal = document.getElementById('mdlModal');
const btnAddTodo = document.getElementById('btnAddTodo');
let isModal = false;

btnAddTodo.addEventListener('click', ()=>{
    isModal = !isModal;

    isModal? 
        mdlModal.style.display='none': mdlModal.style.display='block';
});