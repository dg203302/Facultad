function verificarGanador_empate(){
    if(tablero.every(elemento=>elemento!='')){
        alert('Empate');
        reiniciar();
    }
    else{
        for(let i=0;i<combinaciones_ganadoras.length;i++){
            let combinacion=combinaciones_ganadoras[i];
            let a=combinacion[0];
            let b=combinacion[1];
            let c=combinacion[2];
            if(tablero[a]==tablero[b] && tablero[b]==tablero[c] && tablero[a]!=''){
                alert('Ganador: '+tablero[a]);
                reiniciar();
            }
        }
    }
}
function jugar(posicion){
    if(tablero[posicion]==''){
        let boton=document.getElementById('boton_'+posicion);
        tablero[posicion]=turno_actual;
        console.log(tablero);
        boton.innerText=turno_actual;
        if(turno_actual=='X'){
            turno_actual='O';
            texto.innerText='Jugador actual: '+turno_actual;
        }
        else{
            turno_actual='X';
            texto.innerText='Jugador actual: '+turno_actual;
        }
        verificarGanador_empate();
    }
}
function reiniciar(){
    tablero=['', '', '', '', '', '', '', '', ''];
    turno_actual='X';
    texto.innerText='Jugador actual: '+turno_actual;
    for(let i=0;i<9;i++){
        let boton=document.getElementById('boton_'+i);
        boton.innerText='';
    }
}
const combinaciones_ganadoras=[  //indices de las posiciones que forman una combinacion ganadora
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];
var tablero = ['','','','','','','','',''];
var turno_actual='X';
var texto=document.getElementById('jugador_actual');
texto.innerText='Jugador actual: '+turno_actual;