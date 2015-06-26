
function updatediv(div, pagina, time) {
//alert(div+pagina+time);
    ajaxsimple(pagina, div);
    window.setTimeout("updatediv('" + div + "','" + pagina + "','" + time + "');", time);
}

function requeridoup(div) {
    if (document.getElementById(div) != null)
        document.getElementById(div).style.display = 'block';
}

function requeridodown(div) {
    if (document.getElementById(div) != null)
        document.getElementById(div).style.display = 'none';
}

function limpiarspan(campo) {
    if (document.getElementById(campo) != null)
        document.getElementById(campo).innerHTML = '&nbsp;';
}
function leermas(tipo, campo) {

    if (tipo == 1) {
        document.getElementById(campo + '_datosadicionales').style.display = 'block';
        document.getElementById(campo + '_leermasx').style.display = 'none';
    } else {
        document.getElementById(campo + '_datosadicionales').style.display = 'none';
        document.getElementById(campo + '_leermasx').style.display = 'block';
    }

}
function copiarlabel()
{
    alert('xxxxx');
}
function cssmenu(i, campo, modelo, controler)
{
//alert(i+' , '+campo+' , '+modelo+' , '+controler);
    var array = document.getElementById(campo).value;
    var id = array.split(",");
    var matriz = new Array(id.length);
    var m;
    for (m = 0; m < id.length; m++)
    {
        matriz[m] = id[m];
        if (i == matriz[m]) {
            document.getElementById(matriz[m]).className = 'lis_selecmenuactivo';
        }
        else {
            document.getElementById(matriz[m]).className = 'lis_selecmenu';

        }
    }
    document.getElementById('dondemodelo').value = modelo;
    document.getElementById('dondecontroler').value = controler;
    document.getElementById('buscadorindex').value = '';

    //document.getElementById('titlebuscador').innerHTML='Escriba y se filtrara<br />por lo escrito en "'+modelo+'"';
    //document.getElementById('buscadorindex').readOnly = false;
    //document.getElementById('tdayuda').style.display='block';
    //document.getElementById('tdcerrarsession').style.display='block';

}



function imprimir(url, id_valor)
{
    id = document.getElementById(id_valor).value;

    //id=document.getElementById('id_imprimir').value;
    //id="Vmtab2QyTnNRbEpRVkRBOQ==";
    //ref="TARJETAPRODUCTIVA/pdf_produtor/"+id;
    ref = url + "/" + id;
    window.open(ref, 'IMPRIMIR', 'width=900,height=600');
    return;
}




function nada()
{
    return 1;
}

function copia_texto(id_original, id_desino)
{
    var cop = document.getElementById(id_original).value;
    document.getElementById(id_desino).value = cop;
}

function stopRKey(evt) {
    var evt = (evt) ? evt : ((event) ? event : null);
    var node = (evt.target) ? evt.target : ((evt.srcElement) ? evt.srcElement : null);
    //id => buscadorproducto
    if ((evt.keyCode == 13) && (node.type == "text") && (node.id=="buscadorproducto")) {
        return false;
    }
    return true;
}
function EnviaFormulariobuscador(event, url_cargar, id_cargar, cod, formulario, minimoBuscar) //evento,Div a actualizar, accion, id_formulario
{
    minimoBuscar = minimoBuscar || 0;
    var codigo = document.getElementById(cod).value;
    codigo = codigo.trim();
    if ((event.keyCode == 13) && (codigo.length >= minimoBuscar) && (codigo != '')) {
        urlc = url_cargar + '/' + codigo;
        new Ajax.Updater(id_cargar, urlc,
                {
                    method: 'post',
                    asynchronous: true,
                    evalScripts: true,
                    parameters: Object.extend($(formulario).serialize()),
                    onLoading: function(request) {
                        Element.show('div_loader');
                        Element.show('div_loader_img');
                    },
                    onComplete: function(request) {
                        Element.hide('div_loader')
                        Element.hide('div_loader_img')
                    },
                    requestHeaders: ['X-Update', id_cargar]
                });

    }
    //Event.seal(event);
    //return true;
}

function ajaxbuscador(event, url, id_cargar, array)
{

    if (event.keyCode == 13) {
        var res;
        if (array)
        {
            var id = array.split(",");
            var matriz = new Array(id.length);
            var minx = new Array();
            var cadena, n, valor, i;
            for (i = 0; i < id.length; i++)
            {
                matriz[i] = vacio(document.getElementById(id[i]).value);
                minx.push('_&_' + matriz[i]);
            }
            cadena = minx.toString();
            n = cadena.replace(",_&_", "/");
            for (i = 0; i < id.length; i++)
            {
                n = n.replace(",_&_", "/");
            }
            n = n.replace("_&_", "/");
            Cargar(id_cargar, "/" + url + n);

        }
        else
        {
            Cargar(id_cargar, "/" + url);

        }

    }


}



function ajax(url, id_cargar, array)
{
    var res;
    if (array)
    {
        var id = array.split(",");
        var matriz = new Array(id.length);
        var minx = new Array();
        var cadena, n, valor, i;
        for (i = 0; i < id.length; i++)
        {
            matriz[i] = vacio(document.getElementById(id[i]).value);
            minx.push('_&_' + matriz[i]);
        }
        cadena = minx.toString();
        n = cadena.replace(",_&_", "/");
        for (i = 0; i < id.length; i++)
        {
            n = n.replace(",_&_", "/");
        }
        n = n.replace("_&_", "/");
        Cargar(id_cargar, "/" + url + n);

    }
    else
    {
        Cargar(id_cargar, "/" + url);

    }

}

function ajaxUnValor(url, id_cargar, valor)
{
    if (valor)
        url += "/" + valor;

     Cargar(id_cargar, url);

}

function ajax_pregunta(url, id_cargar, pre, array)
{
    var res;
    if (confirm(pre))
    {
        if (array)
        {
            var id = array.split(",");
            var matriz = new Array(id.length);
            var minx = new Array();
            var cadena, n, valor, i;
            for (i = 0; i < id.length; i++)
            {
                matriz[i] = vacio(document.getElementById(id[i]).value);
                minx.push('_&_' + matriz[i]);
            }
            cadena = minx.toString();

            n = cadena.replace(",_&_", "/");
            for (i = 0; i < id.length; i++)
            {
                n = n.replace(",_&_", "/");
            }
            n = n.replace("_&_", "/");
            Cargar(id_cargar, "/" + url + n);

        }
        else
        {
            Cargar(id_cargar, "/" + url);

        }
    }
    return;
}



function ajaxsimple(url, id_cargar, array)
{
    var res;
    if (array)
    {
        var id = array.split(",");
        var matriz = new Array(id.length);
        var minx = new Array();
        var cadena, n, valor, i;
        for (i = 0; i < id.length; i++)
        {
            matriz[i] = vacio(document.getElementById(id[i]).value);
            minx.push('_&_' + matriz[i]);
        }
        cadena = minx.toString();
        n = cadena.replace(",_&_", "/");
        for (i = 0; i < id.length; i++)
        {
            n = n.replace(",_&_", "/");
        }
        n = n.replace("_&_", "/");
        Cargarsimple(id_cargar, "/" + url + n);

    }
    else
    {
        Cargarsimple(id_cargar, "/" + url);

    }

}










function confirmarl(url_cargar, id_cargar, pre)
{
    var res;
    if (pre != 'No')
    {
        res = confirm(pre);
        if (res)
            Cargar(url_cargar, id_cargar);
    }
    else
        Cargar(url_cargar, id_cargar);
}

function EnviaFormularioPregunta(url_cargar, id_cargar, formulario, pre, tipo)
{
    res = confirm(pre);
    if (res)
        EnviaFormulario(id_cargar, url_cargar, formulario, formulario);
    return;
}

function para_p()
{
    var person = {fname: "John", lname: "Doe", age: 25, };
    for (x in person)
    {
        alert(x + ' , ' + person[x]);
    }
}
function evalua_indice(indice, valores) { //eventos
    var res = '';
    //var valores=eventos.toArray;
    //var valores='{onCreate:"confirm(Objeto es Inicializado. Esto es despues de que los parametros y la URL  han sido procesados, pero antes que se abra la conexion al objeto ajax (XHR object).)",onUninitialized:"confirm( (No requerido): Llamado justo despues de que el Objeto Ajax (XHR object) es creado.)",onLoading:"confirm((No Requerido): Disparado cuando el Objeto Ajax (XHR) ha sido configurado y la conexion ha sido abierta.)",onLoaded:"confirm( (No Requerido): Disparado una vez que el Objeto Ajax (XHR) ha sido configurado y la conexion ha sido abierta, y el metod send ha sido llamado (Envio de solicitud real).)",onInteractive:"confirm((No Requerido): Disparado cada vez que el solicitante recibe una parte de la respuesta (pero no la parte final), en caso de ser enviado en varios paquetes.)",onSuccess:"confirm( (Ejecuto Sastifactoriamente)=> Se invoca cuando una solicitud se completa y su código de estado no está definido y ocurre antes onComplete.)",onFailure:"confirm( (Ocurrio un error de ruta) => Se invoca cuando una solicitud se completa y existe el código de estado y ocurre antes onComplete....)",onException:"confirm( (Ocurrio un error de codigo) => Se activa cada vez que surja un error del Objeto Ajax (XHR). Tiene una firma personalizada: el primer argumento es el solicitante (es decir, una instancia Ajax.Request), y el segundo es el objeto de excepción.)",onComplete:"confirm((Finaliza la peticion)=> dispara al final del ciclo de vida de una petición, una vez completada la solicitud, las devoluciones de llamada de estado específico son llamados, y los posibles comportamientos automáticos son procesados​​. Garantizado para funcionar independientemente de lo que ocurrió durante la petición.)",}'
    for (i in valores)
    {

        if (indice == i) {
            //alert("evento =>"+ i +" , indice => "+indice+", Accion => "+valores[i]);
            res = valores[i];
            break;
        }
    }
    return res;
}

function AjaxDinamico(div, url, eventos, eval, asincrono, codificacion)
{
    //alert(eventos);
    var base = eventos.split('&_:_&');
    var listener = new Array(base.length);
    var i;
    for (i = 0; i < base.length; )
    {
        listener[base[i]] = base[i + 1];
        i += 2;
    }
    //onCreate&_:_&"confirm(Objeto es Inicializado. Esto es despues de que los parametros y la URL  han sido procesados, pero antes que se abra la conexion al objeto ajax (XHR object).)"&_:_&onUninitialized&_:_&"confirm( (No requerido): Llamado justo despues de que el Objeto Ajax (XHR object) es creado.)"&_:_&onLoading&_:_&"confirm((No Requerido): Disparado cuando el Objeto Ajax (XHR) ha sido configurado y la conexion ha sido abierta.)"&_:_&onLoaded&_:_&"confirm( (No Requerido): Disparado una vez que el Objeto Ajax (XHR) ha sido configurado y la conexion ha sido abierta, y el metod send ha sido llamado (Envio de solicitud real).)"&_:_&onInteractive&_:_&"confirm((No Requerido): Disparado cada vez que el solicitante recibe una parte de la respuesta (pero no la parte final), en caso de ser enviado en varios paquetes.)"&_:_&onSuccess&_:_&"confirm( (Ejecuto Sastifactoriamente)=> Se invoca cuando una solicitud se completa y su código de estado no está definido y ocurre antes onComplete.)"&_:_&onFailure&_:_&"confirm( (Ocurrio un error de ruta) => Se invoca cuando una solicitud se completa y existe el código de estado y ocurre antes onComplete....)"&_:_&onException&_:_&"confirm( (Ocurrio un error de codigo) => Se activa cada vez que surja un error del Objeto Ajax (XHR). Tiene una firma personalizada: el primer argumento es el solicitante (es decir, una instancia Ajax.Request), y el segundo es el objeto de excepción.)"&_:_&onComplete&_:_&"confirm((Finaliza la peticion)=> dispara al final del ciclo de vida de una petición, una vez completada la solicitud, las devoluciones de llamada de estado específico son llamados, y los posibles comportamientos automáticos son procesados​​. Garantizado para funcionar independientemente de lo que ocurrió durante la petición.)"&_:_&   /*
    new Ajax.Updater(div, url,
            {
                encoding: codificacion,
                asynchronous: asincrono,
                evalScripts: eval,
                onCreate: function(request) {
                    evalua_indice('onCreate', listener);
                },
                onUninitialized: function(request) {
                    evalua_indice('onUninitialized', listener);
                },
                onLoading: function(request) {
                    evalua_indice('onLoading', listener);
                },
                onLoaded: function(request) {
                    evalua_indice('onLoading', listener);
                },
                onInteractive: function(request) {
                    evalua_indice('onLoading', listener);
                },
                onSuccess: function(request) {//evalua_indice('onLoading',listener);
                    alert('prueba');
                },
                onException: function(request) {
                    evalua_indice('onLoading', listener);
                },
                onComplete: function(request) {
                    evalua_indice('onLoading', listener);
                },
                requestHeaders: ['X-Update', div]
            });
}

function EnviaFormulario(id_cargar, url_cargar, formulario, tipo) //Div a actualizar, accion, id_formulario
{
    if (tipo == 'guardando')
    {

        new Ajax.Updater(id_cargar, url_cargar,
                {
                    asynchronous: true,
                    evalScripts: true,
                    parameters: Object.extend($(formulario).serialize()),
                    onLoading: function(request) {
                        Element.show('div_loader');
                        Element.show('div_loader_img');
                    },
                    onComplete: function(request) {
                        Element.hide('div_loader')
                        Element.hide('div_loader_img')
                    },
                    requestHeaders: ['X-Update', id_cargar]}
        );
    }
    else if (tipo == 'cargando')
    {
        new Ajax.Updater(id_cargar, url_cargar,
                {
                    asynchronous: true,
                    evalScripts: true,
                    parameters: Object.extend($(formulario).serialize()),
                    onLoading: function(request) {
                        Element.show('div_loader');
                        Element.show('div_loader_img');
                    },
                    onComplete: function(request) {
                        Element.hide('div_loader')
                        Element.hide('div_loader_img')
                    },
                    requestHeaders: ['X-Update', id_cargar]}
        );
    }
    else
    {
        new Ajax.Updater(id_cargar, url_cargar,
                {
                    asynchronous: true,
                    evalScripts: true,
                    parameters: Object.extend($(formulario).serialize()),
                    onLoading: function(request) {
                        Element.show('div_loader');
                        Element.show('div_loader_img');
                    },
                    onComplete: function(request) {
                        Element.hide('div_loader')
                        Element.hide('div_loader_img')
                    },
                    requestHeaders: ['X-Update', id_cargar]}
        );
    }
}

function JqCargar(id_cargar, url_cargar, metodo, tipoInforamcion, variables)
{
    metodo = (metodo != '') ? metodo : 'POST';
    tipoInforamcion = (tipoInforamcion != '') ? tipoInforamcion : 'html';
    variables = (variables != '') ? variables : '';
    
    return $j.ajax({
        url: url_cargar,
        type: metodo,
        dataType: tipoInforamcion,
        data: variables,
        success: function(data) {
            $j(id_cargar).html(data);
        }
    });
}

function Cargar(id_cargar, url_cargar)
{

    new Ajax.Updater(id_cargar, url_cargar,{
            asynchronous: true,
            evalScripts: true,
            onLoading: function(request) {
                Element.show('div_loader');
                Element.show('div_loader_img');
            },
            onComplete: function(request) {
                Element.hide('div_loader')
                Element.hide('div_loader_img')
            },
            requestHeaders: ['X-Update', id_cargar]}
    );
}
function Cargarsimple(id_cargar, url_cargar)
{

    new Ajax.Updater(id_cargar, url_cargar,{
        asynchronous: true,
        evalScripts: true,
        onLoading: function(request) {
        },
        onComplete: function(request) {
        },
        requestHeaders: ['X-Update', id_cargar]}
    );
}


function vacio(k)
{
    if (k == null || k.length == 0 || /^\s+$/.test(k))
        return 0;
    else
        return k;

}

function input_remoto_uno(url, id_cargar, uno)
{
    var u = vacio(document.getElementById(uno).value);
    var acc = "/" + url + "/" + u;
    Cargar(id_cargar, acc);
}

function input_remoto_dos(url, id_cargar, uno, dos)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var acc = "/" + url + "/" + u + "/" + d;
    Cargar(id_cargar, acc);
}

function input_remoto_tres(url, id_cargar, uno, dos, tres)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t;
    Cargar(id_cargar, acc);
}

function input_remoto_cuatro(url, id_cargar, uno, dos, tres, cuatro)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c;
    Cargar(id_cargar, acc);
}

function input_remoto_cinco(url, id_cargar, uno, dos, tres, cuatro, cinco)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci;
    Cargar(id_cargar, acc);
}

function input_remoto_seis(url, id_cargar, uno, dos, tres, cuatro, cinco, seis)
{

    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s;

    Cargar(id_cargar, acc);
}

function input_remoto_siete(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si;
    Cargar(id_cargar, acc);
}

function input_remoto_ocho(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o;
    Cargar(id_cargar, acc);
}

function input_remoto_nueve(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n;
    Cargar(id_cargar, acc);
}

function input_remoto_diez(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var di = vacio(document.getElementById(diez).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di;
    Cargar(id_cargar, acc);
}

function input_remoto_once(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var di = vacio(document.getElementById(diez).value);
    var on = vacio(document.getElementById(once).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di + "/" + on;
    Cargar(id_cargar, acc);
}

function input_dos_remoto_uno(url, id_cargar, uno, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var acc = "/" + url + "/" + u;
    var acc2 = "/" + url2 + "/" + u;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_dos(url, id_cargar, uno, dos, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var acc = "/" + url + "/" + u + "/" + d;
    var acc2 = "/" + url2 + "/" + u + "/" + d;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_tres(url, id_cargar, uno, dos, tres, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_cuatro(url, id_cargar, uno, dos, tres, cuatro, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_cinco(url, id_cargar, uno, dos, tres, cuatro, cinco, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_seis(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_siete(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_ocho(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_nueve(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_diez(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var di = vacio(document.getElementById(diez).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

function input_dos_remoto_once(url, id_cargar, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once, url2, id_cargar2)
{
    var u = vacio(document.getElementById(uno).value);
    var d = vacio(document.getElementById(dos).value);
    var t = vacio(document.getElementById(tres).value);
    var c = vacio(document.getElementById(cuatro).value);
    var ci = vacio(document.getElementById(cinco).value);
    var s = vacio(document.getElementById(seis).value);
    var si = vacio(document.getElementById(siete).value);
    var o = vacio(document.getElementById(ocho).value);
    var n = vacio(document.getElementById(nueve).value);
    var di = vacio(document.getElementById(diez).value);
    var on = vacio(document.getElementById(once).value);
    var acc = "/" + url + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di + "/" + on;
    var acc2 = "/" + url2 + "/" + u + "/" + d + "/" + t + "/" + c + "/" + ci + "/" + s + "/" + si + "/" + o + "/" + n + "/" + di + "/" + on;
    Cargar(id_cargar, acc);
    Cargar(id_cargar2, acc2);
}

