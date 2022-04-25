
from bot import Response

def getResponseList() -> list:

    responseList: Response = []

    # Creating responses objects for different questions
    res1 = Response('El número de contacto del ITLA es  (809) 738-4852',  
                    ['telefono', 'contacto', 'número', 'comunicarme', 'comunicar'], 
                    single_response= True)

    res2 = Response('Estamos ubicados en Boca Chica, La Caleta', 
                    ['ubicacion', 'direccion', 'donde', 'ubicados'], 
                    single_response=True)

    res3 = Response('''Actualmente la oferta académica del ITLA contiene las siguientes carreras: 
                \n Desarrollo de software \n Mecatronica \n Multimedia \n Seguridad informatica \n Inteligencia Artificial \n Ciencia de datos \n Manufactura \n Dispositivos medicos \n Diseño Industrial \n Energias renovables \n Sonido\n''', 
                ['carreras', 'tecnologos', 'tecnicas'],
                single_response=True)

    res4 = Response('El pago de inscripción cuesta RD$ 6,640 pesos', 
                ['inscripcion', 'precio', 'cuanto', 'costo'],
                required_words=['inscripcion'])

    res5 = Response('Cada crédito tiene un costo de 520 pesos', 
                ['creditos', 'cuanto', 'costo', 'precio'],
                required_words=['creditos'])

    res6 = Response('Los tecnólogos por lo regular duran 7 cuatrimestres (2 años y 4 meses)',
                    ['carrera', 'tecnologo', 'dura', 'cuanto', 'que'],
                    required_words=['tiempo'])

    res7 = Response('El sitio web del ITLA es https://itla.edu.do/ (Abrir en un navegador)',
                    ['web', 'pagina'],
                    single_response=True)

    res8 = Response('El ITLA fue fundado el 13 de agosto del año 2000. Más información acceder a: https://itla.edu.do/historia/',
                    ['fundado', 'fundada', 'fundacion', 'inauguracion', 'fundo'], 
                    required_words=['cuando'])

    res9 = Response('En el ITLA tenemos la beca excelencia, la cual cubre todos los créditos durante la carrera. También hay becas en otras instituciones, como en la MESCyT, El ministerio de la juventud, etc', 
    ['becas', 'cuales', 'cual'], required_words=['becas'] )

    res10 = Response('Actualmente el rector del ITLA es el Sr.Omar Méndez Lluberes', 
                    ['rector', 'cual', 'quien'],
                    required_words=['rector'])

    responseList.append(res1)
    responseList.append(res2)
    responseList.append(res3)
    responseList.append(res4)
    responseList.append(res5)
    responseList.append(res6)
    responseList.append(res7)
    responseList.append(res8)
    responseList.append(res9)
    responseList.append(res10)

    return responseList