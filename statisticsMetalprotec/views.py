from django.shortcuts import render
import time
from decimal import Decimal, DecimalException,getcontext
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from salesMetalprotec.models import invoiceSystem, billSystem, quotationSystem, guideSystem, creditNoteSystem
import datetime
from django.db.models import Q

getcontext().prec = 10

# Create your views here.
def mainDashboard(request):
    return render(request,'mainDashboard.html')

def clientsDashboard(request):
    return render(request,'clientsDashboard.html')

def productsDashboard(request):
    return render(request,'productsDashboard.html')

def sellDashboard(request):
    return render(request,'sellDashboard.html')

def productsStatistics(request):
    timeInfo = request.GET.get('timeInfo')
    qtInfo = request.GET.get('qtInfo')
    time.sleep(1.5)
    if timeInfo == '0':
        if qtInfo == '15':
            infoCodes = ['2391133601', '1A01999901', 'SIKATECHO3GRIS', '1509260101', '1510999903', '2392999903', '1624830101', '2223237501', '1509000201', '1509832901', '1509000101', '1625999901', '1766999901', '1769999902', 'Otros']
            infoValues = [Decimal('15237.00'), Decimal('14145.91'), Decimal('9788.10'), Decimal('8630.16'), Decimal('8616.62'), Decimal('7347.00'), Decimal('5344.80'), Decimal('5338.72'), Decimal('5100.00'), Decimal('5100.00'), Decimal('3831.42'), Decimal('3723.99'), Decimal('3118.59'), Decimal('3034.68'), 39848.46]
            infoProducts = ['FASTHANE 600 ROJO RAL 3000 1 GL', 'JET ECOPOXY 90 . 1 GL', 'SIKAFILL TECHO-3 FIBRA GRIS x 20 LT', 'DURAPOX ESMALTE 950 AZUL ELECTRICO 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'FASTHANE 600 CATALIZADOR . 1/4 GL', 'JET 62 ZP ANTICORROSIVO GRIS 1 GL', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'DURAPOX ESMALTE 950 BLANCO OPTICO 1711 1 GL', 'DURAPOX ESMALTE 950 GRIS NIEBLA 1680 1 GLS', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'JET 62 ZP ANTICORROSIVO CATALIZADOR . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'Otros']
        elif qtInfo == '10':
            infoCodes = ['2391133601', '1A01999901', 'SIKATECHO3GRIS', '1509260101', '1510999903', '2392999903', '1624830101', '2223237501', '1509000201', 'Otros']
            infoValues = [Decimal('15237.00'), Decimal('14145.91'), Decimal('9788.10'), Decimal('8630.16'), Decimal('8616.62'), Decimal('7347.00'), Decimal('5344.80'), Decimal('5338.72'), Decimal('5100.00'), 58657.14]
            infoProducts = ['FASTHANE 600 ROJO RAL 3000 1 GL', 'JET ECOPOXY 90 . 1 GL', 'SIKAFILL TECHO-3 FIBRA GRIS x 20 LT', 'DURAPOX ESMALTE 950 AZUL ELECTRICO 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'FASTHANE 600 CATALIZADOR . 1/4 GL', 'JET 62 ZP ANTICORROSIVO GRIS 1 GL', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'DURAPOX ESMALTE 950 BLANCO OPTICO 1711 1 GL', 'Otros']
        else:
            infoCodes = ['2391133601', '1A01999901', 'SIKATECHO3GRIS', '1509260101', 'Otros']
            infoValues = [Decimal('15237.00'), Decimal('14145.91'), Decimal('9788.10'), Decimal('8630.16'), 90404.28]
            infoProducts = ['FASTHANE 600 ROJO RAL 3000 1 GL', 'JET ECOPOXY 90 . 1 GL', 'SIKAFILL TECHO-3 FIBRA GRIS x 20 LT', 'DURAPOX ESMALTE 950 AZUL ELECTRICO 1 GL', 'Otros']
    elif timeInfo == '1':
        if qtInfo == '15':
            infoCodes = ['2223130101', '1A06999901', '1A01999901', '1766999901', '2391133601', '1765883101', '1510999903', '1765406201', 'SIKATECHO3GRIS', '2223237501', '1509260101', '1624830101', '2392999903', '1923999901', 'Otros']
            infoValues = [Decimal('48647.66'), Decimal('35448.14'), Decimal('25175.38'), Decimal('20616.60'), Decimal('15237.00'), Decimal('13097.58'), Decimal('12125.77'), Decimal('10629.92'), Decimal('9788.10'), Decimal('9727.62'), Decimal('9028.20'), Decimal('8202.66'), Decimal('7347.00'), Decimal('7110.31'), 123677.17]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOL . 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'FASTHANE 600 ROJO RAL 3000 1 GL', 'JET 70 MP GRIS RAL 7040 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET 70 MP VERDE RAL 6019 K5 1 GL', 'SIKAFILL TECHO-3 FIBRA GRIS x 20 LT', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'DURAPOX ESMALTE 950 AZUL ELECTRICO 1 GL', 'JET 62 ZP ANTICORROSIVO GRIS 1 GL', 'FASTHANE 600 CATALIZADOR . 1/4 GL', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'Otros']
        elif qtInfo == '10':
            infoCodes = ['2223130101', '1A06999901', '1A01999901', '1766999901', '2391133601', '1765883101', '1510999903', '1765406201', 'SIKATECHO3GRIS', 'Otros']
            infoValues = [Decimal('48647.66'), Decimal('35448.14'), Decimal('25175.38'), Decimal('20616.60'), Decimal('15237.00'), Decimal('13097.58'), Decimal('12125.77'), Decimal('10629.92'), Decimal('9788.10'), 165092.96]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOL . 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'FASTHANE 600 ROJO RAL 3000 1 GL', 'JET 70 MP GRIS RAL 7040 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET 70 MP VERDE RAL 6019 K5 1 GL', 'SIKAFILL TECHO-3 FIBRA GRIS x 20 LT', 'Otros']
        else:
            infoCodes = ['2223130101', '1A06999901', '1A01999901', '1766999901', 'Otros']
            infoValues = [Decimal('48647.66'), Decimal('35448.14'), Decimal('25175.38'), Decimal('20616.60'), 225971.33]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOL . 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'Otros']
    elif timeInfo == '3':
        if qtInfo == '15':
            infoCodes = ['2223130101', '1A01999901', '1A06999901', '1766999901', '1510999903', '1923999901', '2391133601', '2223237501', '1509000101', '1527999902', '1509832901', '1922890001', '1769999902', '1770999902', 'Otros']
            infoValues = [Decimal('86743.83'), Decimal('42985.06'), Decimal('38773.35'), Decimal('37933.37'), Decimal('31666.37'), Decimal('28261.16'), Decimal('22960.50'), Decimal('21752.26'), Decimal('21591.69'), Decimal('18769.36'), Decimal('18082.39'), Decimal('17636.90'), Decimal('17169.34'), Decimal('16834.79'), 345039.89]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET ECOPOL . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'FASTHANE 600 ROJO RAL 3000 1 GL', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'FASTIPOXI ESMALTE EPOXICO - PARTE B . 1/2 GL', 'DURAPOX ESMALTE 950 GRIS NIEBLA 1680 1 GLS', 'JET BITUFLEX 70 PF NEGRO 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'FASTIMAS MASILLA - PARTE B . 1/2 GL', 'Otros']
        elif qtInfo == '10':
            infoCodes = ['2223130101', '1A01999901', '1A06999901', '1766999901', '1510999903', '1923999901', '2391133601', '2223237501', '1509000101', 'Otros']
            infoValues = [Decimal('86743.83'), Decimal('42985.06'), Decimal('38773.35'), Decimal('37933.37'), Decimal('31666.37'), Decimal('28261.16'), Decimal('22960.50'), Decimal('21752.26'), Decimal('21591.69'), 433532.67]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET ECOPOL . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'FASTHANE 600 ROJO RAL 3000 1 GL', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'Otros']
        else:
            infoCodes = ['2223130101', '1A01999901', '1A06999901', '1766999901', 'Otros']
            infoValues = [Decimal('86743.83'), Decimal('42985.06'), Decimal('38773.35'), Decimal('37933.37'), 559764.65]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'JET ECOPOL . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'Otros']
    elif timeInfo == '6':
        if qtInfo == '15':
            infoCodes = ['2223130101', '1A01999901', '1510999903', '1509000101', '1766999901', '1923999901', '1769999902', '1527999902', '1770999902', '1509832901', '1A06999901', '1625999901', '2223237501', '1624830101', 'Otros']
            infoValues = [Decimal('153100.44'), Decimal('81589.43'), Decimal('73223.50'), Decimal('66325.35'), Decimal('61665.79'), Decimal('51681.47'), Decimal('48929.74'), Decimal('48864.57'), Decimal('48595.19'), Decimal('40854.14'), Decimal('40628.09'), Decimal('38542.71'), Decimal('37634.41'), Decimal('37561.78'), 701876.82]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'JET 70 MP - CATALIZADOR . 1 GL', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'FASTIPOXI ESMALTE EPOXICO - PARTE B . 1/2 GL', 'FASTIMAS MASILLA - PARTE B . 1/2 GL', 'DURAPOX ESMALTE 950 GRIS NIEBLA 1680 1 GLS', 'JET ECOPOL . 1 GL', 'JET 62 ZP ANTICORROSIVO CATALIZADOR . 1 GL', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'JET 62 ZP ANTICORROSIVO GRIS 1 GL', 'Otros']
        elif qtInfo == '10':
            infoCodes = ['2223130101', '1A01999901', '1510999903', '1509000101', '1766999901', '1923999901', '1769999902', '1527999902', '1770999902', 'Otros']
            infoValues = [Decimal('153100.44'), Decimal('81589.43'), Decimal('73223.50'), Decimal('66325.35'), Decimal('61665.79'), Decimal('51681.47'), Decimal('48929.74'), Decimal('48864.57'), Decimal('48595.19'), 897097.95]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'JET 70 MP - CATALIZADOR . 1 GL', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'FASTIPOXI ESMALTE EPOXICO - PARTE B . 1/2 GL', 'FASTIMAS MASILLA - PARTE B . 1/2 GL', 'Otros']
        else:
            infoCodes = ['2223130101', '1A01999901', '1510999903', '1509000101', 'Otros']
            infoValues = [Decimal('153100.44'), Decimal('81589.43'), Decimal('73223.50'), Decimal('66325.35'), 1156834.71]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'Otros']
    else:
        if qtInfo == '15':
            infoCodes = ['2223130101', '1510999903', '1A01999901', '1509000101', '1923999901', '1766999901', '1769999902', '1770999902', '1509832901', '2223237501', '1922890001', '2391133601', '1625999901', '1527999902', 'Otros']
            infoValues = [Decimal('203978.56'), Decimal('132148.63'), Decimal('120497.70'), Decimal('120335.70'), Decimal('96060.51'), Decimal('78768.23'), Decimal('76884.05'), Decimal('76338.84'), Decimal('67411.05'), Decimal('65123.06'), Decimal('56761.66'), Decimal('55535.05'), Decimal('55251.14'), Decimal('53241.31'), 1142256.95]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'FASTIMAS MASILLA - PARTE B . 1/2 GL', 'DURAPOX ESMALTE 950 GRIS NIEBLA 1680 1 GLS', 'OCEAN JET ANTIFOULING AZUL 2003 1 GL', 'JET BITUFLEX 70 PF NEGRO 1 GL', 'FASTHANE 600 ROJO RAL 3000 1 GL', 'JET 62 ZP ANTICORROSIVO CATALIZADOR . 1 GL', 'FASTIPOXI ESMALTE EPOXICO - PARTE B . 1/2 GL', 'Otros']
        elif qtInfo == '10':
            infoCodes = ['2223130101', '1510999903', '1A01999901', '1509000101', '1923999901', '1766999901', '1769999902', '1770999902', '1509832901', 'Otros']
            infoValues = [Decimal('203978.56'), Decimal('132148.63'), Decimal('120497.70'), Decimal('120335.70'), Decimal('96060.51'), Decimal('78768.23'), Decimal('76884.05'), Decimal('76338.84'), Decimal('67411.05'), 1428169.17]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'JET BITUFLEX 70 PF CATALIZADOR . 1 GL', 'JET 70 MP - CATALIZADOR . 1 GL', 'FASTIMAS MASILLA - PARTE A . 1/2 GL', 'FASTIMAS MASILLA - PARTE B . 1/2 GL', 'DURAPOX ESMALTE 950 GRIS NIEBLA 1680 1 GLS', 'Otros']
        else:
            infoCodes = ['2223130101', '1510999903', '1A01999901', '1509000101', 'Otros']
            infoValues = [Decimal('203978.56'), Decimal('132148.63'), Decimal('120497.70'), Decimal('120335.70'), 1823631.85]
            infoProducts = ['OCEAN JET ANTIFOULING ROJO 1033 1 GL', 'DURAPOX ESMALTE 950 - CATALIZADOR  1/4 GLS', 'JET ECOPOXY 90 . 1 GL', 'DURAPOX ESMALTE 950 BLANCO 1700 1 GLS', 'Otros']

    return JsonResponse({
        'infoCodes':infoCodes,
        'infoValues':infoValues,
        'infoProducts':infoProducts,
    })


def clientStatistics(request):
    timeInfo = request.GET.get('timeInfo')
    qtInfo = request.GET.get('qtInfo')
    time.sleep(2)
    if timeInfo == '0':
        if qtInfo == '15':
            infoRucs = ['20603159234', '20569300194', '20609004054', '20487853446', '20100003351', '20609076179', '20479977390', '20604779261', '20487981363', '20603686498', '20608626469', '20602406653', '20606592249', '20601799309', 'Otros']
            infoValues = [Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), Decimal('18131.49'), Decimal('12812.07'), Decimal('10229.63'), Decimal('6548.40'), Decimal('4767.00'), Decimal('4679.34'), Decimal('4366.58'), Decimal('3900.79'), Decimal('3803.02'), Decimal('3429.46'), Decimal('2652.30'), 10502.72]
            infoClientes = ['PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'ARENRUSTIK S.A.C.', 'SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'INDECON J & L E.I.R.L.', 'AUROMAR SOCIEDAD ANONIMA CERRADA', 'ARV INGENIERIA Y CONSTRUCCION E.I.R.L.', 'PESQUERA JEHOVA PROVEERA S.A.C.', 'MEGUI INVESTMENT S.A.C.', 'PESQUERA R & Z E.I.R.L.', 'COMERCIALIZADORA FABIAN E.I.R.L.', 'BIOZA S.A.C.', 'INVERSIONES BJES E.I.R.L.', 'Otros']
        elif qtInfo == '10':
            infoRucs = ['20603159234', '20569300194', '20609004054', '20487853446', '20100003351', '20609076179', '20479977390', '20604779261', '20487981363', 'Otros']
            infoValues = [Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), Decimal('18131.49'), Decimal('12812.07'), Decimal('10229.63'), Decimal('6548.40'), Decimal('4767.00'), Decimal('4679.34'), 28654.87]
            infoClientes = ['PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'ARENRUSTIK S.A.C.', 'SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'INDECON J & L E.I.R.L.', 'AUROMAR SOCIEDAD ANONIMA CERRADA', 'ARV INGENIERIA Y CONSTRUCCION E.I.R.L.', 'PESQUERA JEHOVA PROVEERA S.A.C.', 'Otros']
        else:
            infoRucs = ['20603159234', '20569300194', '20609004054', '20487853446', 'Otros']
            infoValues = [Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), Decimal('18131.49'), 67691.31]
            infoClientes = ['PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'ARENRUSTIK S.A.C.', 'Otros']
    elif timeInfo == '1':
        if qtInfo == '15':
            infoRucs = ['20100003351', '20603159234', '20569300194', '20609004054', '20487853446', '20602406653', '20601794030', '20609076179', '20427635601', '20606015195', '20555751185', '20608273736', '20479977390', '20604779261', 'Otros']
            infoValues = [Decimal('164869.59'), Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), Decimal('22675.69'), Decimal('10875.04'), Decimal('10524.10'), Decimal('10229.63'), Decimal('8153.42'), Decimal('7893.06'), Decimal('7166.26'), Decimal('7166.26'), Decimal('6548.40'), Decimal('4767.00'), 51607.91]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'ARENRUSTIK S.A.C.', 'COMERCIALIZADORA FABIAN E.I.R.L.', 'GROUP CAMAR PERU S.A.C.', 'INDECON J & L E.I.R.L.', 'PESQUERA CALYPSO S.A.C.', 'CORPORACION LIBRIARY S.A.C.', 'MAERO S.A.C', 'KETITA S.A.C.', 'AUROMAR SOCIEDAD ANONIMA CERRADA', 'ARV INGENIERIA Y CONSTRUCCION E.I.R.L.', 'Otros']
        elif qtInfo == '10':
            infoRucs = ['20100003351', '20603159234', '20569300194', '20609004054', '20487853446', '20602406653', '20601794030', '20609076179', '20427635601', 'Otros']
            infoValues = [Decimal('164869.59'), Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), Decimal('22675.69'), Decimal('10875.04'), Decimal('10524.10'), Decimal('10229.63'), Decimal('8153.42'), 85148.89]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'ARENRUSTIK S.A.C.', 'COMERCIALIZADORA FABIAN E.I.R.L.', 'GROUP CAMAR PERU S.A.C.', 'INDECON J & L E.I.R.L.', 'PESQUERA CALYPSO S.A.C.', 'Otros']
        else:
            infoRucs = ['20100003351', '20603159234', '20569300194', '20609004054', 'Otros']
            infoValues = [Decimal('164869.59'), Decimal('40314.93'), Decimal('27014.32'), Decimal('24586.28'), 147606.77]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'PRO STEEL PERU S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'Otros']
    elif timeInfo == '3':
        if qtInfo == '15':
            infoRucs = ['20100003351', '20609664151', '20603159234', '20487853446', '20602717993', '10329334657', '20600516176', '20519142521', '20569300194', '20609004054', '20555751185', '20478156228', '20602389660', '20427635601', 'Otros']
            infoValues = [Decimal('204414.15'), Decimal('109650.59'), Decimal('56562.14'), Decimal('41405.33'), Decimal('39354.88'), Decimal('38952.74'), Decimal('38406.35'), Decimal('28811.32'), Decimal('27014.32'), Decimal('24586.28'), Decimal('23506.74'), Decimal('20341.37'), Decimal('19581.50'), Decimal('16306.84'), 215954.83]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'PRO STEEL PERU S.A.C.', 'ARENRUSTIK S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'KING STEEL PERU S.A.C.', 'EMPRESA PESQUERA JADA S.A.C', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'MAERO S.A.C', 'KANDY CORPORACION S.A.C. - KANDYCORP S.A.C.', 'EMPRESA GRUPO JIVO SOCIEDAD ANONIMA CERRADA', 'PESQUERA CALYPSO S.A.C.', 'Otros']
        elif qtInfo == '10':
            infoRucs = ['20100003351', '20609664151', '20603159234', '20487853446', '20602717993', '10329334657', '20600516176', '20519142521', '20569300194', 'Otros']
            infoValues = [Decimal('204414.15'), Decimal('109650.59'), Decimal('56562.14'), Decimal('41405.33'), Decimal('39354.88'), Decimal('38952.74'), Decimal('38406.35'), Decimal('28811.32'), Decimal('27014.32'), 320277.56]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'PRO STEEL PERU S.A.C.', 'ARENRUSTIK S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'KING STEEL PERU S.A.C.', 'EMPRESA PESQUERA JADA S.A.C', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'Otros']
        else:
            infoRucs = ['20100003351', '20609664151', '20603159234', '20487853446', 'Otros']
            infoValues = [Decimal('204414.15'), Decimal('109650.59'), Decimal('56562.14'), Decimal('41405.33'), 492817.17]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'PRO STEEL PERU S.A.C.', 'ARENRUSTIK S.A.C.', 'Otros']
    elif timeInfo == '6':
        if qtInfo == '15':
            infoRucs = ['20100003351', '20609664151', '10329334657', '20487853446', '20602717993', '20569300194', '20603159234', '20602389660', '20600516176', '10329884762', '20605983325', '20603686498', '20380336384', '20519142521', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('132232.95'), Decimal('127393.76'), Decimal('113508.68'), Decimal('98055.84'), Decimal('69955.40'), Decimal('56803.92'), Decimal('55971.33'), Decimal('54870.13'), Decimal('42776.32'), Decimal('33558.24'), Decimal('33198.31'), Decimal('32640.60'), Decimal('29540.50'), 519050.28]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'PRO STEEL PERU S.A.C.', 'EMPRESA GRUPO JIVO SOCIEDAD ANONIMA CERRADA', 'KING STEEL PERU S.A.C.', 'SANCHEZ CONDORI GRISELDA SOFIA', 'CORPORACION NAUTICA S.A.C.', 'MEGUI INVESTMENT S.A.C.', 'PESQUERA EXALMAR S.A.A.', 'EMPRESA PESQUERA JADA S.A.C', 'Otros']
        elif qtInfo == '10':
            infoRucs = ['20100003351', '20609664151', '10329334657', '20487853446', '20602717993', '20569300194', '20603159234', '20602389660', '20600516176', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('132232.95'), Decimal('127393.76'), Decimal('113508.68'), Decimal('98055.84'), Decimal('69955.40'), Decimal('56803.92'), Decimal('55971.33'), Decimal('54870.13'), 690764.25]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'PRO STEEL PERU S.A.C.', 'EMPRESA GRUPO JIVO SOCIEDAD ANONIMA CERRADA', 'KING STEEL PERU S.A.C.', 'Otros']
        else:
            infoRucs = ['20100003351', '20609664151', '10329334657', '20487853446', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('132232.95'), Decimal('127393.76'), Decimal('113508.68'), 1026420.87]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'ALLMAR S.A.C.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'Otros']
    else:
        if qtInfo == '15':
            infoRucs = ['20100003351', '10329334657', '20487853446', '20609664151', '20602717993', '20602389660', '20603159234', '10222633554', '20605983325', '20569300194', '20601825491', '20603686498', '20531925646', '20609004054', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('207986.41'), Decimal('203209.24'), Decimal('132232.95'), Decimal('111639.84'), Decimal('101482.33'), Decimal('93282.32'), Decimal('87126.49'), Decimal('85655.92'), Decimal('84508.12'), Decimal('82289.79'), Decimal('77990.81'), Decimal('75079.94'), Decimal('72539.78'), 1070681.2]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'ALLMAR S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'EMPRESA GRUPO JIVO SOCIEDAD ANONIMA CERRADA', 'PRO STEEL PERU S.A.C.', 'AYBAR ACEVEDO FRED LUIS', 'CORPORACION NAUTICA S.A.C.', 'EMPRESA JEHOVA PODEROSO GIGANTE E.I.R.L.', 'FERSERVICE NAVAL E INDUSTRIAL E.I.R.L.', 'MEGUI INVESTMENT S.A.C.', 'CORPORACION WALTER S.A.C.', 'INDUSTRIAS ESQUIVEL S.A.C.', 'Otros']
        elif qtInfo == '10':
            infoRucs = ['20100003351', '10329334657', '20487853446', '20609664151', '20602717993', '20602389660', '20603159234', '10222633554', '20605983325', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('207986.41'), Decimal('203209.24'), Decimal('132232.95'), Decimal('111639.84'), Decimal('101482.33'), Decimal('93282.32'), Decimal('87126.49'), Decimal('85655.92'), 1463089.64]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'ALLMAR S.A.C.', 'FERRETERIA INDUSTRIAL THAIS E.I.R.L.', 'EMPRESA GRUPO JIVO SOCIEDAD ANONIMA CERRADA', 'PRO STEEL PERU S.A.C.', 'AYBAR ACEVEDO FRED LUIS', 'CORPORACION NAUTICA S.A.C.', 'Otros']
        else:
            infoRucs = ['20100003351', '10329334657', '20487853446', '20609664151', 'Otros']
            infoValues = [Decimal('302581.12'), Decimal('207986.41'), Decimal('203209.24'), Decimal('132232.95'), 1942276.54]
            infoClientes = ['SERVICIOS INDUSTRIALES DE LA MARINA S.A.', 'VELASQUEZ NUÑEZ SILVIA DEL PILAR', 'ARENRUSTIK S.A.C.', 'ALLMAR S.A.C.', 'Otros']

    return JsonResponse({
        'infoRucs':infoRucs,
        'infoValues':infoValues,
        'infoClientes':infoClientes
    })

def resumeSalesxYear(request):
    yearInfo = request.GET.get('yearInfo')
    if yearInfo == '2022':
        monthList = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        salesSoles = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('35923.7940'), Decimal('131441.8230'), Decimal('65129.74'), Decimal('65324.44'), Decimal('44164.63')]
        salesDollars = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('16833.24'), Decimal('34117.826'), Decimal('32061.43'), Decimal('42216.38'), Decimal('13216.01')]
        tcInfo = 3.653

    if yearInfo == '2023':
        monthList = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        salesSoles = [
            Decimal('117884.37'),
            Decimal('106753.65'),
            Decimal('208551.55'),
            Decimal('86361.46'),
            Decimal('136334.64'),
            Decimal('244306.92'),
            getTotalSales('2023-07-01','2023-07-31','SOLES'),
            getTotalSales('2023-08-01','2023-08-31','SOLES'),
            getTotalSales('2023-09-01','2023-09-30','SOLES'),
            getTotalSales('2023-10-01','2023-10-31','SOLES'),
            getTotalSales('2023-11-01','2023-11-30','SOLES'),
            getTotalSales('2023-12-01','2023-12-31','SOLES')
            ]
        salesDollars = [
            Decimal('31976.09'),
            Decimal('22971.42'),
            Decimal('32488.74'),
            Decimal('31802.68'),
            Decimal('26918.91'),
            Decimal('6292.70'),
            getTotalSales('2023-07-01','2023-07-31','DOLARES'),
            getTotalSales('2023-08-01','2023-08-31','DOLARES'),
            getTotalSales('2023-09-01','2023-09-30','DOLARES'),
            getTotalSales('2023-10-01','2023-10-31','DOLARES'),
            getTotalSales('2023-11-01','2023-11-30','DOLARES'),
            getTotalSales('2023-12-01','2023-12-31','DOLARES')
            ]
        tcInfo = 3.653

    if yearInfo == '2024':
        monthList = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        salesSoles = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]
        salesDollars = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]
        tcInfo = 3.653

    if yearInfo == '2025':
        monthList = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        salesSoles = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]
        salesDollars = [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]
        tcInfo = 3.653

    return JsonResponse({
        'salesSoles':salesSoles,
        'salesDollars':salesDollars,
        'tcInfo':tcInfo,
    })

def salesxMonths(request):
    monthInfo = request.GET.get('monthInfo')
    if monthInfo == '10':
        monthList = [
            'Noviembre',
            'Diciembre',
            'Enero',
            'Febrero',
            'Marzo',
            'Abril',
            'Mayo',
            'Junio',
            'Julio',
            'Agosto'
        ]
        salesSoles = [
            Decimal('65324.44'),
            Decimal('44164.63'),
            Decimal('117884.37'),
            Decimal('106753.65'),
            Decimal('208551.55'),
            Decimal('86361.46'),
            Decimal('136334.64'),
            Decimal('244306.92'),
            getTotalSales('2023-07-01','2023-07-31','SOLES'),
            getTotalSales('2023-08-01','2023-08-31','SOLES')
        ]
        salesDollars = [
            Decimal('42216.38'),
            Decimal('13216.01'),
            Decimal('31976.09'),
            Decimal('22971.42'),
            Decimal('32488.74'),
            Decimal('31802.68'),
            Decimal('26918.91'),
            Decimal('6292.70'),
            getTotalSales('2023-07-01','2023-07-31','DOLARES'),
            getTotalSales('2023-08-01','2023-08-31','DOLARES')
        ]

    if monthInfo == '5':
        monthList = [
            'Abril',
            'Mayo',
            'Junio',
            'Julio',
            'Agosto'
        ]
        salesSoles = [
            Decimal('86361.46'),
            Decimal('136334.64'),
            Decimal('244306.92'),
            getTotalSales('2023-07-01','2023-07-31','SOLES'),
            getTotalSales('2023-08-01','2023-08-31','SOLES')
        ]
        salesDollars = [
            Decimal('31802.68'),
            Decimal('26918.91'),
            Decimal('6292.70'),
            getTotalSales('2023-07-01','2023-07-31','DOLARES'),
            getTotalSales('2023-08-01','2023-08-31','DOLARES')
        ]

    if monthInfo == '3':
        monthList = [
            'Junio',
            'Julio',
            'Agosto'
        ]
        salesSoles = [
            Decimal('244306.92'),
            getTotalSales('2023-07-01','2023-07-31','SOLES'),
            getTotalSales('2023-08-01','2023-08-31','SOLES')
        ]
        salesDollars = [
            Decimal('6292.70'),
            getTotalSales('2023-07-01','2023-07-31','DOLARES'),
            getTotalSales('2023-08-01','2023-08-31','DOLARES')
        ]

    return JsonResponse({
        'monthList':monthList,
        'salesSoles':salesSoles,
        'salesDollars':salesDollars
    })

def sellerSalesTime(request):
    yearInfo = request.GET.get('yearInfo')
    currencyInfo = request.GET.get('currencyInfo')
    if yearInfo == '2022':
        if currencyInfo == 'SOLES':
            codeSeller = ['USR-16', 'USR-24', 'USR-19', 'otros']
            salesSeller = [[Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('35923.7940'), Decimal('127516.7930'), Decimal('52876.86'), Decimal('53516.53'), Decimal('27508.25')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('3925.03'), Decimal('12252.88'), Decimal('11797.56'), Decimal('16656.38')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('10.35'), Decimal('0')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]]
        else:
            codeSeller = ['USR-16', 'USR-24', 'USR-19', 'otros']
            salesSeller = [[Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('16833.24'), Decimal('34117.826'), Decimal('32061.43'), Decimal('42216.38'), Decimal('13216.01')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')], [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0')]]
    elif yearInfo == '2023':
        if currencyInfo == 'SOLES':
            codeSeller = [
                'USR-16',
                'USR-24',
                'USR-25',
                'otros'
            ]
            salesSeller = [
                [
                    Decimal('94391.37'),
                    Decimal('92530.85'),
                    Decimal('210142.79'),
                    Decimal('86361.46'),
                    Decimal('136334.64'),
                    Decimal('244273.02'),
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-16'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-16'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','SOLES','USR-16'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','SOLES','USR-16'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','SOLES','USR-16'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','SOLES','USR-16')
                ], 
                [
                    Decimal('23493.00'),
                    Decimal('14222.80'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-24'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-24'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','SOLES','USR-24'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','SOLES','USR-24'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','SOLES','USR-24'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','SOLES','USR-24')
                ], 
                [
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('33.90'),
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-25'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-25'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','SOLES','USR-25'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','SOLES','USR-25'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','SOLES','USR-25'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','SOLES','USR-25')
                ], 
                [
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0'),
                    Decimal('0')
                ]
            ]
        else:
            codeSeller = [
                'USR-16',
                'USR-24',
                'USR-25',
                'otros'
            ]
            salesSeller = [
                [
                    Decimal('31976.09'),
                    Decimal('22971.42'),
                    Decimal('32488.74'),
                    Decimal('31802.68'),
                    Decimal('26918.91'),
                    Decimal('6292.70'),
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-16'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-16'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','DOLARES','USR-16'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','DOLARES','USR-16'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','DOLARES','USR-16'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','DOLARES','USR-16')
                ],
                [
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-24'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-24'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','DOLARES','USR-24'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','DOLARES','USR-24'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','DOLARES','USR-24'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','DOLARES','USR-24')
                ],
                [
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-25'),
                    getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-25'),
                    getTotalSalesSellerCode('2023-09-01','2023-09-30','DOLARES','USR-25'),
                    getTotalSalesSellerCode('2023-10-01','2023-10-31','DOLARES','USR-25'),
                    getTotalSalesSellerCode('2023-11-01','2023-11-30','DOLARES','USR-25'),
                    getTotalSalesSellerCode('2023-12-01','2023-12-31','DOLARES','USR-25')
                ],
                [
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0'), 
                    Decimal('0')
                ]
            ]
    else:
        if currencyInfo == 'SOLES':
            codeSeller = []
            salesSeller = []
        else:
            codeSeller = []
            salesSeller = []
    return JsonResponse({
        'codeSeller':codeSeller,
        'salesSeller':salesSeller,
    })

def sellerStatistics(request):
    qtInfo = request.GET.get('qtInfo')
    timeInfo = request.GET.get('timeInfo')
    if timeInfo == '0':
        if qtInfo == '10':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-25')
            ]
        elif qtInfo == '5':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-25')
            ]
        else:
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-08-01','2023-08-31','DOLARES','USR-25')
            ]
    elif timeInfo == '1':
        if qtInfo == '10':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-25')
            ]
        elif qtInfo == '5':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-25')
            ]
        else:
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-07-01','2023-07-31','DOLARES','USR-25')
            ]
    elif timeInfo == '3':
        if qtInfo == '10':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-25')
            ]
        elif qtInfo == '5':
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-25')
            ]
        else:
            sellerCode = ['USR-16', 'USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-06-01','2023-08-31','DOLARES','USR-25')
            ]
    elif timeInfo == '6':
        if qtInfo == '10':
            sellerCode = ['USR-16','USR-24','USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-25')
            ]
        elif qtInfo == '5':
            sellerCode = ['USR-16','USR-24','USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-25')
            ]
        else:
            sellerCode = ['USR-16','USR-24','USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','SOLES','USR-25')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-03-01','2023-08-31','DOLARES','USR-25')
            ]
    else:
        if qtInfo == '10':
            sellerCode = ['USR-16','USR-24','USR-25','USR-19']
            sellerSoles = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-25'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-19')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-25'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-19')
            ]
        elif qtInfo == '5':
            sellerCode = ['USR-16','USR-24','USR-25','USR-19']
            sellerSoles = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-25'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-19')
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-25'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-19')
            ]
        else:
            sellerCode = ['USR-16','USR-24','USR-25']
            sellerSoles = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','SOLES','USR-25'),
            ]
            sellerDollars = [
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-16'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-24'),
                getTotalSalesSellerCode('2023-01-01','2023-08-31','DOLARES','USR-25'),
            ]
    return JsonResponse({
        'sellerCode':sellerCode,
        'sellerSoles':sellerSoles,
        'sellerDollars':sellerDollars,
    })

def getTotalSalesSellerCode(startDate, endDate, currencyInfo, codeSeller):
    finalSales = Decimal(0.0000)
    billsData = []
    invoicesData = []
    if startDate != '' and endDate != '':
        fechaInicio = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()
        fechaFin = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()
        
        billsFilter = billSystem.objects.filter(
            Q(dateBill__gte=fechaInicio) &
            Q(dateBill__lte=fechaFin)
        ).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado').filter(currencyBill=currencyInfo).order_by('-dateBill')
        
        for billItem in billsFilter:
            if len(creditNoteSystem.objects.filter(originCreditNote='BILL').filter(asociatedInvoice=None).exclude(asociatedBill=None).filter(asociatedBill__codeBill=billItem.codeBill)) == 0:
                if float(getValueBillSellerInfo(billItem,codeSeller)) != 0:
                    billsData.append([
                        getValueBillSellerInfo(billItem,codeSeller),
                        billItem.codeBill
                    ])
        for itemInfo in billsData:
            finalSales = Decimal(finalSales) + Decimal(itemInfo[0])


        invoicesFilter = invoiceSystem.objects.filter(
            Q(dateInvoice__gte=fechaInicio) &
            Q(dateInvoice__lte=fechaFin)
        ).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado').exclude(stateTeFacturo='Por Anular').filter(currencyInvoice=currencyInfo).order_by('-dateInvoice')
        for invoiceItem in invoicesFilter:
            if len(creditNoteSystem.objects.filter(originCreditNote='INVOICE').filter(asociatedBill=None).exclude(asociatedInvoice=None).filter(asociatedInvoice__codeInvoice=invoiceItem.codeInvoice)) == 0:
                if float(getValueInvoiceSellerInfo(invoiceItem,codeSeller)) != 0:
                    invoicesData.append([
                        getValueInvoiceSellerInfo(invoiceItem, codeSeller),
                        invoiceItem.codeInvoice
                    ])
        for itemInfo in invoicesData:
            finalSales = Decimal(finalSales) + Decimal(itemInfo[0])
    else:
        finalSales = Decimal(0.0000)
    return finalSales


def getTotalSales(startDate, endDate, currencyInfo):
    finalSales = Decimal(0.0000)
    billsData = []
    invoicesData = []
    if startDate != '' and endDate != '':
        fechaInicio = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()
        fechaFin = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()
        
        billsFilter = billSystem.objects.filter(
            Q(dateBill__gte=fechaInicio) &
            Q(dateBill__lte=fechaFin)
        ).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado').filter(currencyBill=currencyInfo).order_by('-dateBill')
        
        for billItem in billsFilter:
            if len(creditNoteSystem.objects.filter(originCreditNote='BILL').filter(asociatedInvoice=None).exclude(asociatedBill=None).filter(asociatedBill__codeBill=billItem.codeBill)) == 0:
                billsData.append([
                    getValueBill(billItem),
                    billItem.codeBill
                ])
        for itemInfo in billsData:
            finalSales = Decimal(finalSales) + Decimal(itemInfo[0])


        invoicesFilter = invoiceSystem.objects.filter(
            Q(dateInvoice__gte=fechaInicio) &
            Q(dateInvoice__lte=fechaFin)
        ).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado').exclude(stateTeFacturo='Por Anular').filter(currencyInvoice=currencyInfo).order_by('-dateInvoice')
        for invoiceItem in invoicesFilter:
            if len(creditNoteSystem.objects.filter(originCreditNote='INVOICE').filter(asociatedBill=None).exclude(asociatedInvoice=None).filter(asociatedInvoice__codeInvoice=invoiceItem.codeInvoice)) == 0:
                invoicesData.append([
                    getValueInvoice(invoiceItem),
                    invoiceItem.codeInvoice
                ])
        for itemInfo in invoicesData:
            finalSales = Decimal(finalSales) + Decimal(itemInfo[0])
    else:
        finalSales = Decimal(0.0000)
    return finalSales

def getValueInvoice(invoiceItem):
    valueInvoice = '0.00'
    try:
        quotationItem = None
        if invoiceItem.originInvoice == 'GUIDE':
            quotationItem = invoiceItem.guidesystem_set.all()[0].asociatedQuotation
        else:
            quotationItem = invoiceItem.asociatedQuotation
        valueInvoice = getValueQuotation(quotationItem)
    except:
        valueInvoice = '0.00'
    return valueInvoice

def getValueBill(billItem):
    valueBill = Decimal(0.0000)
    try:
        quotationItem = None
        if billItem.originBill == 'GUIDE':
            for guideItem in billItem.guidesystem_set.all():
                quotationItem = guideItem.asociatedQuotation
                tempValueQuotation = getValueQuotation(quotationItem)
                valueBill = Decimal(valueBill) + Decimal(tempValueQuotation)
        else:
            quotationItem = billItem.asociatedQuotation
            valueBill = getValueQuotation(quotationItem)
    except:
        valueBill = '0.00'
    valueBill = str(valueBill)
    return valueBill

def getValueBillSellerInfo(billItem, sellerCode):
    valueBill = Decimal(0.0000)
    try:
        quotationItem = None
        if billItem.originBill == 'GUIDE':
            for guideItem in billItem.guidesystem_set.all():
                quotationItem = guideItem.asociatedQuotation
                if quotationItem.quotationsellerdata.dataUserQuotation[2] == sellerCode:
                    tempValueQuotation = getValueQuotation(quotationItem)
                    valueBill = Decimal(valueBill) + Decimal(tempValueQuotation)
                else:
                    tempValueQuotation = Decimal(0.0000)
                    valueBill = Decimal(valueBill) + Decimal(tempValueQuotation)
        else:
            quotationItem = billItem.asociatedQuotation
            if quotationItem.quotationsellerdata.dataUserQuotation[2] == sellerCode:
                valueBill = getValueQuotation(quotationItem)
            else:
                valueBill = Decimal(0.0000)
    except:
        valueBill = '0.00'
    valueBill = str(valueBill)
    return valueBill

def getValueInvoiceSellerInfo(invoiceItem,sellerCode):
    valueInvoice = Decimal(0.0000)
    try:
        quotationItem = None
        if invoiceItem.originInvoice == 'GUIDE':
            for guideItem in invoiceItem.guidesystem_set.all():
                quotationItem = guideItem.asociatedQuotation
                if quotationItem.quotationsellerdata.dataUserQuotation[2] == sellerCode:
                    tempValueQuotation = getValueQuotation(quotationItem)
                    valueInvoice = Decimal(valueInvoice) + Decimal(tempValueQuotation)
                else:
                    tempValueQuotation = Decimal(0.0000)
                    valueInvoice = Decimal(valueInvoice) + Decimal(tempValueQuotation)
        else:
            quotationItem = invoiceItem.asociatedQuotation
            if quotationItem.quotationsellerdata.dataUserQuotation[2] == sellerCode:
                valueInvoice = getValueQuotation(quotationItem)
            else:
                valueInvoice = Decimal(0.0000)
    except:
        valueInvoice = '0.00'
    valueInvoice = str(valueInvoice)
    return valueInvoice

def getValueQuotation(quotationItem):
    valueQuotation = Decimal(0.000)
    try:
        if quotationItem.typeQuotation == 'PRODUCTOS':
            totalProductsQuotation = quotationItem.quotationproductdata_set.all()
            for productInfo in totalProductsQuotation:
                if quotationItem.currencyQuotation == 'SOLES':
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationItem.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                if quotationItem.currencyQuotation == 'DOLARES':
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = (Decimal(productInfo.dataProductQuotation[6])/Decimal(quotationItem.erSel))*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                if productInfo.dataProductQuotation[9] == '1':
                    v_producto = Decimal(0.00)
                valueQuotation = Decimal(valueQuotation) + Decimal(v_producto)
        else:
            totalServicesQuotation = quotationItem.quotationservicedata_set.all()
            for serviceInfo in totalServicesQuotation:
                if quotationItem.currencyQuotation == 'SOLES':
                    if serviceInfo.dataServiceQuotation[3] == 'DOLARES':
                        v_servicio = Decimal(serviceInfo.dataServiceQuotation[4])*Decimal(quotationItem.erSel)*Decimal(Decimal(1.00) - Decimal(serviceInfo.dataServiceQuotation[5])/100)
                    if serviceInfo.dataServiceQuotation[3] == 'SOLES':
                        v_servicio = Decimal(serviceInfo.dataServiceQuotation[4])*Decimal(Decimal(1.00) - (Decimal(serviceInfo.dataServiceQuotation[5])/100))
                if quotationItem.currencyQuotation == 'DOLARES':
                    if serviceInfo.dataServiceQuotation[3] == 'SOLES':
                        v_servicio = (Decimal(serviceInfo.dataServiceQuotation[4])/Decimal(quotationItem.erSel))*Decimal(Decimal(1.00) - (Decimal(serviceInfo.dataServiceQuotation[5])/100))
                    if serviceInfo.dataServiceQuotation[3] == 'DOLARES':
                        v_servicio = Decimal(serviceInfo.dataServiceQuotation[4])*Decimal(Decimal(1.00) - Decimal(serviceInfo.dataServiceQuotation[5])/100)
                valueQuotation = Decimal(valueQuotation) + Decimal(v_servicio)
    except:
        valueQuotation = Decimal(0.00)
    valueQuotation = Decimal('%.2f' % valueQuotation)
    valueQuotation = str(valueQuotation)
    return valueQuotation


