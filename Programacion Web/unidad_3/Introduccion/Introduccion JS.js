function punto_1(){
    var nombre="juan";
    console.log(nombre);
    nombre="pedro";
    console.log(nombre);

    let edad=30;
    console.log(edad);
    edad=31;
    console.log(edad);

    const pais="Argentina";
    console.log(pais);
    //pais="Brasil"; //error, ya que no se puede reasignar una constante

    //diferencias en scope
    if (true){
        var x=5;
        let y=10;
        const z=15;
    }
    console.log(x);
    //console.log(y); //error, ya que let tiene un scope de bloque
    //console.log(z); //error, ya que const tiene un scope de bloque
}
function punto_2(){
    /**hoisting con VAR */
    console.log(texto_1);
    var texto_1="hola mundo";
    console.log(texto_1);
    /**hoisting con LET */
    //console.log(numero_1); //error, ya que no se puede acceder a una variable let antes de ser declarada
    let numero_1=10;
    console.log(numero_1);
}
function suma(a,b){
    return a+b;
}
function punto_3(){
    let a=2, b=3;
    console.log(suma(a,b));
    const resta=function(a,b){
        return a-b;
    }
    console.log(resta);
    const multiplicacion=(a,b)=>a*b;
    console.log(multiplicacion);
}
function punto_4(){
    
    let Array=[1,2,3,4,5,6,11,23,1,989,0,1,111,645,50,45];
    
    let menor=Math.min(...Array);
    console.log('menor elemento del array',menor);
    
    suma_total=Array.reduce((acumulador,valor_actual)=>acumulador+valor_actual,0);
    console.log('suma total del array',suma_total);
    
    let Dobles=Array.map(elemento=>elemento*2);
    console.log('Array con elementos duplicados',Dobles);

    let mayores_a_10=Array.filter(elemento=>elemento>=10);
    console.log('Elementos mayores o iguales a 10',mayores_a_10);
    let menores_a_10=Array.filter(elemento=>elemento<=10);
    console.log('Elementos menores a 10',menores_a_10);
    
    let indice_primer_menor=Array.findIndex(elemento=>elemento>10);
    console.log('Indice del primer elemento mayor a 10',indice_primer_menor);
}
class Auto{
    constructor(ruedas,puertas,color,velocidad){
        this.ruedas=ruedas;
        this.puertas=puertas;
        this.color=color;
        this.velocidad=velocidad;
    }
    aumentar_velocidad(aumento){
        this.velocidad+=aumento;
    }
}
function punto_5(){
    let auto=new Auto(4,4,'verde',100);
    auto.aumentar_velocidad(50);
    console.log(auto.velocidad);
}
punto_1()
punto_2()
punto_3()
Punto_5()
punto_4()