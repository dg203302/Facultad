class Auto{
    constructor(ruedas,puertas,color,velocidad){
        this.ruedas=Ruedas;
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
punto_4()
Punto_5()