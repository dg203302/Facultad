function enviar_datos(datos,parrafo_informe){
    fetch("https://jsonplaceholder.typicode.com/posts",{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response=>response.json())
    .then(data=>{
        parrafo_informe.textContent="Datos enviados correctamente";
        console.log('Success:', data);
    })
    .catch(error=>{
        parrafo_informe.textContent="Error al enviar los datos";
        console.error('Error:', error);
    });
}
document.getElementById('Formulario').addEventListener('submit', function(event){
    event.preventDefault();
    const usuarios_existentes=["admin","administrador","root","Ana","Pepe","Pedro"];
    let usuario=document.getElementById("ingreso_usuario").value;
    let correo=document.getElementById("ingreso_correo").value;
    const regexCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    let contrasena=document.getElementById("ingreso_contra").value;
    let confirmar_contrasena=document.getElementById("ingreso_repetir_contra").value;
    const parrafo_informe=document.getElementById("mensaje_usuario");
    if (usuario.lenght<3){
        parrafo_informe.textContent = "El campo usuario debe tener al menos 3 caracteres";
        return;
    }
    else if (usuarios_existentes.includes(usuario)){
        parrafo_informe.textContent = "El usuario ya existe";
        return;
    }
    if (!regexCorreo.test(correo)){
        parrafo_informe.textContent = "El correo no es valido";
        return;
    }
    if (contrasena.lenght<8){
        parrafo_informe.textContent = "La contraseña debe tener al menos 8 caracteres";
        return;
    }
    if (contrasena!=confirmar_contrasena){
        parrafo_informe.textContent = "Las contraseñas no coinciden";
        return;
    }
    enviar_datos({usuario,correo,contrasena},parrafo_informe);
});