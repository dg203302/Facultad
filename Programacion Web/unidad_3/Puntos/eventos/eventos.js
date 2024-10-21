setTimeout(() => {
    document.getElementsByTagName('header')[0].style.backgroundColor='red';
    document.getElementsByTagName('footer')[0].style.backgroundColor='blue';
}, 5000);
function saludar(){
    const contenedor=document.getElementById('saludo');
    const saludo=document.createElement('p');
    saludo.textContent='Holaaa!!';
    contenedor.appendChild(saludo);
}
document.getElementById('getDataBtn').addEventListener('click', function(){
    fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response=>response.json())
    .then(data=>{
        const elementos=data.slice(0,10);
        let contenedor=document.getElementById('contenedor');
        if(!contenedor){
            contenedor=document.createElement('div');
            contenedor.id='contenedor';
            document.body.appendChild(contenedor);
        }
        let lista=document.createElement('ul');
        contenedor.appendChild(lista);
        elementos.forEach(elemento=>{
            let item_lista=document.createElement('li');
            item_lista.textContent=elemento.title;
            lista.appendChild(item_lista);
        });
    })
    .catch(Error=>{
        console.error('Error al obtener los datos')
    });
});