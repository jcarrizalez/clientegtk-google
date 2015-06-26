function ordenar(evento,valor,tipo,campo,tabs) { 

valor1=valor.substring(0, 2);
valor2=valor.substring(2, 15);
//valor.length
if(valor2.length==7)valor2='0'+valor.substring(2, 15);
if(valor2.length==6)valor2='00'+valor.substring(2, 15);
document.getElementById(campo).value = valor1+valor2;
}

function value(campo,valor) { 
document.getElementById(campo).value =valor;
}

/*
function chek_defect(cek,id,mensaje){
  
    if(document.getElementById(cek).checked){
         document.getElementById(id).value = mensaje;
         document.getElementById(id).disabled = true;
    }
     else{
          document.getElementById(id).value = '';
          document.getElementById(id).disabled = false;
     }
  
}*/


//////////// ESTA FUNCION VALIDA TEXTO, NUMERICO, TELEFONO, CORREO, MONEDA, FECHA - SOLO EN LA ENTRADA DE CHARTS //////////////


function validate(evento,valor,tipo,campo,tabs) { 
//////////// PATRON DE TODOS LOS CARACTERES ///////////////////////////
//patron = /[!#$%&`()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
///////////////////////////////////////////////////////////////////////

if (tipo=='texto'){ //alert(tipo +' -' +valor);
valor = v_texto(evento,valor,tipo,campo,tabs);
}
else if (tipo=='direccion'){
valor = v_direccion(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='todo'){
valor = v_todo(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='numerico'){
valor = v_numerico(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='clave'){
valor = v_clave(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='celular'){
valor = v_celular(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='telefono'){
valor = v_telefono(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='correo'){
valor = v_correo(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='moneda'){
decimal=2;
valor = v_moneda(evento,valor,tipo,campo,tabs,decimal);
}
else  if (tipo=='rif'){
valor = v_rif(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='cedula'){
valor = v_cedula(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='select'){
valor = v_select(evento,valor,tipo,campo,tabs);
}
else  if (tipo=='fecha'){
valor = v_fecha(evento,valor,tipo,campo,tabs);
}
else if (tipo=='textarea'){
valor = v_todo(evento,valor,tipo,campo,tabs);
}
else if (tipo=='hora'){
valor = v_hora(evento,valor,tipo,campo,tabs);
}
else if (tipo=='numeromenos'){
valor = v_numeromenos(evento,valor,tipo,campo,tabs);
}
else if (tipo=='numerossinmenos'){
valor = v_numerossinmenos(evento,valor,tipo,campo,tabs);
}
else{
valor = v_error(evento,valor,tipo,campo,tabs);
}
return valor;

}
//////////////////////////////////// ESTA FUNCION ES PARA LLAMAR A strreplace() DANDO UN VALOR ////////////////////
function str(valor){

valor=strreplace(valor,'  ');
valor=strreplace(valor,' ');
valor=strreplace(valor,'.');
valor=strreplace(valor,'@');
valor=strreplace(valor,'-');
valor=strreplace(valor,'#');
return valor;
}

//////////////////////////////////// ESTA FUNCION RESPONDE A  str() DANDO UN VALOR ////////////////////
function strreplace(valor,lt){
var numero=0;
for(i=0;i<valor.length;i++)
{
if(valor.charAt(i)==lt) numero++;
}
if(numero==2){ml=lt+lt;}
else if(numero==3){ml=lt+lt+lt;}
else if(numero==4){ml=lt+lt+lt+lt;}
else if(numero==5){ml=lt+lt+lt+lt+lt;}
else if(numero==6){ml=lt+lt+lt+lt+lt+lt;}
else if(numero==7){ml=lt+lt+lt+lt+lt+lt+lt;}
else if(numero==8){ml=lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==9){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==10){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==11){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==12){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==13){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==14){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==15){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==16){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==17){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==18){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==19){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else if(numero==20){ml=lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt+lt;}
else{ml=lt;}
valor = valor.replace(ml , lt);
return valor;
}

//////////////////////////////////// ESTA FUNCION PERMITE VER SI EXISTEN DOS LETRAS EN LA CADENA Y QUITA LA ULTIMA ////////////////////

function BuscaLetra(valor,letra,campo){
var numero=0;
var sig=1;
for(i=0;i<valor.length;i++)
{
if(valor.charAt(i)==letra) numero++;
}
if(numero>1){
numero = valor.lastIndexOf(letra);
valor = valor.substring(0, numero);
//alert(valor);
document.getElementById(campo).value = valor;
}
return valor;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////// ESTA FUNCION CREA MASCARAS A LOS INPUT SEGUN PATRON DECLARADO ////////////////////

var patronfecha = new Array(2,2,4);
var patrontelefono = new Array(4,7);


function mascara(d,sep,pat,nums,campo,tabs){

if(d.valant != d.value){
	val = d.value
	largo = val.length
	val = val.split(sep)
	val2 = ''
	for(r=0;r<val.length;r++){
		val2 += val[r]	
	}
	if(nums){
		for(z=0;z<val2.length;z++){
			if(isNaN(val2.charAt(z))){
				letra = new RegExp(val2.charAt(z),'g')
				val2 = val2.replace(letra,'')
			}
		}
	}
	val = ''
	val3 = new Array()
	for(s=0; s<pat.length; s++){
		val3[s] = val2.substring(0,pat[s])
		val2 = val2.substr(pat[s])
	}
	for(q=0;q<val3.length; q++){
		if(q ==0){
			val = val3[q]
		}
		else{
			if(val3[q] != ''){
				val += sep + val3[q]
				}
		}
	}
	d.value = val
	d.valant = val
	}
liacamposfn(campo,tabs);


}


function liacamposfn(campo,tabs){
	if(tabs=='_h')
	limpiarspan(campo+'_h_em');
	else
	limpiarspan(campo+'_em');
}



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_texto(evento,valor,tipo,campo,tabs){
//alert('mmm');
patronx = /[!#$%&`()*+,-./0123456789:;<=>?@[\]^_{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
valor = valor.replace(patronx , '');
valor = str(valor);
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_direccion(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`*+,-./:;<=>?@[\]^{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’“”„†‡•…‰€™'"]/g;
valor = str(valor);
valor = valor.replace(patron , '');
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_todo(evento,valor,tipo,campo,tabs){

valor = str(valor);
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_numerico(evento,valor,tipo,campo,tabs){
patronc = /\D/g;
valor = str(valor);
valor = valor.replace(patronc , '');
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;

}
function v_numerico(evento,valor,tipo,campo,tabs){
patronc = /\D/g;
valor = str(valor);
valor = valor.replace(patronc , '');
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_numeromenos(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`()* +,./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
valor = str(valor);
valor = valor.replace(patron , '');
document.getElementById(campo).value = valor;
//liacamposfn(campo,tabs);
return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_numerossinmenos(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`()*+,-./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
valor = str(valor);
valor = valor.replace(patron , '');
document.getElementById(campo).value = valor;
//liacamposfn(campo,tabs);
return valor;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_clave(evento,valor,tipo,campo,tabs){

patron = '';
var sr=valor.length, css;
if(sr==1)css = 'clave1';
else if(sr==2)css = 'clave2';
else if(sr==3)css = 'clave3';
else if(sr==4)css = 'clave4';
else if(sr==5)css = 'clave5';
else if(sr==6)css = 'clave6';
else if(sr==7)css = 'clave7';
else if(sr==8)css = 'clave8';
else if(sr==9)css = 'clave9';
else if(sr==10)css = 'clave10';
else if(sr==11)css = 'clave11';
else if(sr==12)css = 'clave12';
else if(sr==13)css = 'clave13';
else if(sr==14)css = 'clave14';
else if(sr==15)css = 'clave15';
else css = 'claven';

document.getElementById(campo).className = css;


valor = str(valor);

liacamposfn(campo,tabs);

return valor;

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_celular(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`()*+,./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
length
if(valor.substring(0, 1)!=0)valor='';
pos2=valor.substring(1, 2);
if(pos2!=4)valor=valor.substring(0, 1);
pos3=valor.substring(2, 3);
if(pos3!=1 && pos3!=2)valor=valor.substring(0, 2);
pos4=valor.substring(3, 4);
if(pos4!=2 && pos4!=4 && pos4!=6)valor=valor.substring(0, 3);
if(pos3==2 && pos4==2)valor=valor.substring(0, 3);
valor1 = valor.substring(0, 4);valor1 = valor1.replace(patron , '');
valor2 = valor.substring(4, 15);valor2 = valor2.replace(patron , '');
if(valor.substring(4, 5)!='-' && valor.substring(4, 5)!=''){
if(valor.substring(3, 4)!='' && valor.substring(3, 4)!='-'){
valor = valor1+'-'+valor2;
}
else{
valor = valor1+valor2;
}
}
else{
valor = valor1+valor2;
}
if(valor=='-'){
valor = '';
}
valor=BuscaLetra(valor,'-',campo);
//mascara(valor,'-',patrontelefono,true); 


valor = str(valor);

document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);



return valor;

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_telefono(evento,valor,tipo,campo,tabs){


//valor = v_telefono(evento,valor,tipo,campo,tabs);

patron = /[!#$%&`()*+,./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

if(valor.substring(0, 1)!=0)valor='';  // posision 1
//pos2=valor.substring(1, 2);
//if(pos2!=4)valor=valor.substring(0, 1);

if(valor.substring(1, 2)!=2)valor=valor.substring(0, 1);  // posision 2

if(valor.substring(2, 3)==2 || valor.substring(2, 3)==0)valor=valor.substring(0, 2);  // posision 3
valor1 = valor.substring(0, 4);valor1 = valor1.replace(patron , '');
valor2 = valor.substring(4, 15);valor2 = valor2.replace(patron , '');
if(valor.substring(4, 5)!='-' && valor.substring(4, 5)!=''){
if(valor.substring(3, 4)!='' && valor.substring(3, 4)!='-'){
valor = valor1+'-'+valor2;
}
else{
valor = valor1+valor2;
}
}
else{
valor = valor1+valor2;
}
if(valor=='-'){
valor = '';
}
valor=BuscaLetra(valor,'-',campo);
//mascara(valor,'-',patrontelefono,true);




valor = str(valor);
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);

return valor;

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_correo(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`()*+,/:;<=>?[\]^{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
valor=BuscaLetra(valor,'@',campo);

valor = str(valor);
valor = valor.replace(patron , '');
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);

return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_moneda(evento,valor,tipo,campo,tabs,decimal){
//valor = v_telefono(evento,valor,tipo,campo,tabs);
patron = /[!#$%&`()*+/:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

valor = valor.replace('.' , ',');
valor = valor.replace(patron , '');

if(valor.substring(0, 1)==',')valor='0,';

valor=BuscaLetra(valor,',',campo);
valor=BuscaLetra(valor,'-',campo);


if(valor.substring(0, 1)!='-'){

valor = valor.split("-");
valor1 = valor[0];
largo = valor1.length;
if(largo>0){
valor1 = valor[0];
}
valor = valor1;

}

valor = str(valor);


valor = valor.split(",");
valor1 = valor[0];
if (typeof valor[1] != "undefined"){
valor2 = valor[1];
largo = valor2.length;
if(largo>decimal){
valor2 = valor2.substring(0, decimal);
}
valor = valor1+","+valor2;
}
document.getElementById(campo).value = valor;
//liacamposfn(campo,tabs);

return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF // RIF
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_rif(evento,valor,tipo,campo,tabs){

patron1 = /[!#$%&`()*+,-./0123456789:;<=>?@ABCDEFHIKLMNÑOPQRSTUWXYZ[\]^_abcdefhiklmnñopqrstuwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

patron2 = /[!#$%&`()*+,-./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

valor1 = valor.substring(0, 1);valor1 = valor1.replace(patron1 , '');
valor2 = valor.substring(1, 15);valor2 = valor2.replace(patron2 , '');



if(valor.substring(0, 1)!='J' && valor.substring(0, 1)!='j' && valor.substring(0, 1)!='G' && valor.substring(0, 1)!='g'
 && valor.substring(0, 1)!='V' && valor.substring(0, 1)!='v'
 //&& valor.substring(0, 1)!='E' && valor.substring(0, 1)!='e'
 ){
valor = '';
}



else if(valor.substring(2, 3)!='-' && valor.substring(2, 3)!='')valor = valor1+'-'+valor2;

if(valor.substring(0, 1)=='V' || valor.substring(0, 1)=='v'){
if(valor.substring(1, 2)!='-' && valor.substring(1, 2)!='0' && valor.substring(1, 2)!='1' && valor.substring(1, 2)!='2' && valor.substring(1, 2)!='3' && valor.substring(1, 2)!='4'/* && valor.substring(1, 2)!='5' && valor.substring(1, 2)!='6' && valor.substring(1, 2)!='7' && valor.substring(1, 2)!='8' && valor.substring(1, 2)!='9'*/)valor = valor.substring(0,1);
if(valor.substring(2,3)>='5')valor = valor.substring(0,2);
if(valor.substring(2,4)>='41')valor = valor.substring(0,3);
}
else if(valor.substring(0, 1)=='E' || valor.substring(0, 1)=='e'){

if(/*valor.substring(1, 2)!='0' && valor.substring(1, 2)!='1' && valor.substring(1, 2)!='2' && valor.substring(1, 2)!='3' &&  */valor.substring(1, 2)!='4' && valor.substring(1, 2)!='5' && valor.substring(1, 2)!='6' && valor.substring(1, 2)!='7' && valor.substring(1, 2)!='8' && valor.substring(1, 2)!='9' && valor.substring(1, 2)!='-')valor = valor.substring(0,1);
if(valor.substring(2,3)<='3')valor = valor.substring(0,2);
if(valor.substring(2,4)<='40')valor = valor.substring(0,3);
}



valor=BuscaLetra(valor,'-',campo);
valor = valor.replace(' ' , '');
valor=BuscaLetra(valor,' ',campo);
valor = str(valor);

document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);



return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CEDULA  // CEDULA  // CEDULA  // CEDULA  // CEDULA  // CEDULA  // CEDULA  // CEDULA  // CEDULA  
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_cedula(evento,valor,tipo,campo,tabs){

patron1 = /[!#$%&`()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUWXYZ[\]^_abcdefghijklmnñopqrstuwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;
patron2 = /[!#$%&`()*+,-./:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;


valor1 = valor.substring(0, 1);valor1 = valor1.replace(patron1 , '');
valor2 = valor.substring(1, 15);valor2 = valor2.replace(patron2 , '');


if(valor.substring(0, 1)!='V' && valor.substring(0, 1)!='v' 
        //&& valor.substring(0, 1)!='E' && valor.substring(0, 1)!='e'
        ){
valor = '';
}



else if(valor.substring(2, 3)!='-' && valor.substring(2, 3)!='')valor = valor1+'-'+valor2;

if(valor.substring(0, 1)=='V' || valor.substring(0, 1)=='v'){
if(valor.substring(1, 2)!='-' && valor.substring(1, 2)!='0' && valor.substring(1, 2)!='1' && valor.substring(1, 2)!='2' && valor.substring(1, 2)!='3' && valor.substring(1, 2)!='4'/* && valor.substring(1, 2)!='5' && valor.substring(1, 2)!='6' && valor.substring(1, 2)!='7' && valor.substring(1, 2)!='8' && valor.substring(1, 2)!='9'*/)valor = valor.substring(0,1);
if(valor.substring(2,3)>='5')valor = valor.substring(0,2);
if(valor.substring(2,4)>='41')valor = valor.substring(0,3);
}
else if(valor.substring(0, 1)=='E' || valor.substring(0, 1)=='e'){

if(/*valor.substring(1, 2)!='0' && valor.substring(1, 2)!='1' && valor.substring(1, 2)!='2' && valor.substring(1, 2)!='3' &&  */valor.substring(1, 2)!='4' && valor.substring(1, 2)!='5' && valor.substring(1, 2)!='6' && valor.substring(1, 2)!='7' && valor.substring(1, 2)!='8' && valor.substring(1, 2)!='9' && valor.substring(1, 2)!='-')valor = valor.substring(0,1);
if(valor.substring(2,3)<='3')valor = valor.substring(0,2);
if(valor.substring(2,4)<='40')valor = valor.substring(0,3);
}


valor=BuscaLetra(valor,' ',campo);
valor=BuscaLetra(valor,'-',campo);
valor = valor.replace(' ' , '');
valor = str(valor);

document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);

return valor;

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_select(evento,valor,tipo,campo,tabs){
patron = '';

valor = str(valor);
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);



return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_fecha(evento,valor,tipo,campo,tabs){
patron = /[!#$%&`()*+,:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

valor = valor.replace('.' , '-');
valor = valor.replace('/' , '-');
valor = str(valor);
valor = valor.replace(patron , '');

valor1 = valor.substring(0, 2);
valor2 = valor.substring(2, 6);
valor3 = valor.substring(0, 5);
valor4 = valor.substring(5, 15);


if(valor.substring(0,1)>='4')valor = "";
else if(valor.substring(0,1)=='-')valor = valor.substring(0,0);
else if(valor.substring(1,2)=='-')valor = valor.substring(0,1);
else if(valor.substring(0,2)=='00')valor = valor.substring(0,1);
else if(valor.substring(0,2)>31)valor = valor.substring(0,1);
else if(valor.substring(2,3)>1)valor = valor.substring(0,2);
else if(valor.substring(3,4)>1)valor = valor.substring(0,3);
else if(valor.substring(3,4)=='-')valor = valor.substring(0,3);
else if(valor.substring(4,5)=='-')valor = valor.substring(0,4);

else if(valor.substring(2, 3)!='-' && valor.substring(2, 3)!='')valor = valor1+'-'+valor2;
else if(valor.substring(3,5)=='00')valor = valor.substring(0,4);
else if(valor.substring(3,5)>12)valor = valor.substring(0,4);
else if(valor.substring(6,7)=='0')valor = valor.substring(0,6);
else if(valor.substring(6,7)>='3')valor = valor.substring(0,6);
else if(valor.substring(5,6)>='3')valor = valor.substring(0,5);
else if(valor.substring(5,6)=='0')valor = valor.substring(0,5);

else if(valor.substring(5, 6)!='-' && valor.substring(5, 6)!='')valor = valor3+'-'+valor4;

else if(valor.substring(6,7)=='-')valor = valor.substring(0,6);
else if(valor.substring(7,8)=='-')valor = valor.substring(0,7);
else if(valor.substring(6,8)<='18')valor = valor.substring(0,7);
else if(valor.substring(6,8)>='22')valor = valor.substring(0,7);
else if(valor.substring(8,9)=='-')valor = valor.substring(0,8);
else if(valor.substring(9,10)=='-')valor = valor.substring(0,9);

document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_hora(evento,valor,tipo,campo,tabs){
patron = /[!#$%&`()*+,-./ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz;<=>?@{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

valor = valor.replace('.' , ':');
valor = valor.replace('/' , ':');
valor = valor.replace('-' , ':');
valor = str(valor);
valor = valor.replace(patron , '');

valor1 = valor.substring(0, 2);
valor2 = valor.substring(2, 6);
valor3 = valor.substring(0, 5);
valor4 = valor.substring(5, 15);


if(valor.substring(0,1)>='3')valor = "";
else if(valor.substring(0,1)==':')valor = valor.substring(0,0);
else if(valor.substring(0,1)=='-')valor = valor.substring(0,0);
else if(valor.substring(1,2)==':')valor = valor.substring(0,1);
//else if(valor.substring(0,2)=='00')valor = valor.substring(0,1);
else if(valor.substring(0,2)>23)valor = valor.substring(0,1);
else if(valor.substring(2,3)>5)valor = valor.substring(0,2);
else if(valor.substring(3,4)>5)valor = valor.substring(0,3);
//else if(valor.substring(3,4)>1)valor = valor.substring(0,3);
else if(valor.substring(3,4)==':')valor = valor.substring(0,3);
else if(valor.substring(4,5)==':')valor = valor.substring(0,4);

else if(valor.substring(2, 3)!=':' && valor.substring(2, 3)!='')valor = valor1+':'+valor2;
else if(valor.substring(3,5)=='00')valor = valor.substring(0,4);
else if(valor.substring(3,5)>59)valor = valor.substring(0,4);
//else if(valor.substring(6,7)=='0')valor = valor.substring(0,6);
//else if(valor.substring(6,7)>='6')valor = valor.substring(0,6);

//else if(valor.substring(5,6)=='0')valor = valor.substring(0,5);

else if(valor.substring(5, 6)!=':' && valor.substring(5, 6)!='')valor = valor3+':'+valor4;
//else if(valor.substring(5,6)>='6')valor = valor.substring(0,5);
else if(valor.substring(6,7)>='6')valor = valor.substring(0,6);

else if(valor.substring(6,7)==':')valor = valor.substring(0,6);
else if(valor.substring(7,8)==':')valor = valor.substring(0,7);
//else if(valor.substring(6,8)<='60')valor = valor.substring(0,7);
else if(valor.substring(6,8)>='59')valor = valor.substring(0,7);
else if(valor.substring(8,9)==':')valor = valor.substring(0,8);
else if(valor.substring(9,10)==':')valor = valor.substring(0,9);

document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);
return valor;
}



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function v_error(evento,valor,tipo,campo,tabs){

patron = /[!#$%&`()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\]^_abcdefghijklmnñopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸƒ–—‘’‚“”„†‡•…‰€™'"]/g;

document.getElementById(campo).value = 'ERROR';

valor = str(valor);
valor = valor.replace(patron , '');
document.getElementById(campo).value = valor;
liacamposfn(campo,tabs);

return valor;
}
