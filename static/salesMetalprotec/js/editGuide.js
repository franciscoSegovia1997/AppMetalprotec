document.addEventListener('DOMContentLoaded',()=>{
    selectDeparment = document.getElementById('selectDeparment')
    deparmentDeparture = document.getElementById('deparmentDeparture')
    selectDeparment.onchange = function()
    {
        selectedDeparment = selectDeparment.value
        if(selectedDeparment !== '')
        {
            deparmentDeparture.value = selectedDeparment
        }
        else
        {
            deparmentDeparture.value = ''
        }
    }
})

function modifyGuide()
{
    idGuideInfo=document.getElementById('idGuideInfo').value
    legalAddressClient=document.getElementById('legalAddressClient').value
    deliveryAddress=document.getElementById('deliveryAddress').value
    deparmentDeparture=document.getElementById('deparmentDeparture').value
    provinceDeparture=document.getElementById('provinceDeparture').value
    districtDeparture=document.getElementById('districtDeparture').value
    addressDeparture=document.getElementById('addressDeparture').value
    ubigeoDeparture=document.getElementById('ubigeoDeparture').value
    dateGuide=document.getElementById('dateGuide').value
    dateGivenGoods=document.getElementById('dateGivenGoods').value
    extraWeight=document.getElementById('extraWeight').value
    purposeTransportation=document.getElementById('purposeTransportation').value
    modeTransportation=document.getElementById('modeTransportation').value
    ubigeoClient=document.getElementById('ubigeoClient').value
    commentGuide=document.getElementById('commentGuide').value
    razonSocialTranporter=document.getElementById('razonSocialTranporter').value
    rucTransporter=document.getElementById('rucTransporter').value
    vehiclePlate=document.getElementById('vehiclePlate').value
    dniDriver=document.getElementById('dniDriver').value
    licenceDriver=document.getElementById('licenceDriver').value
    nameDriver=document.getElementById('nameDriver').value

    updatedWeights = []
    newWeightsInfo = document.getElementsByClassName('weightData')
    for(let i = 0; i < newWeightsInfo.length; i++)
    {
        newWeights = [newWeightsInfo[i].dataset.info.slice(2),newWeightsInfo[i].value]
        updatedWeights.push(newWeights)
    }


    guideInfo = {
        'idGuideInfo':idGuideInfo,
        'legalAddressClient':legalAddressClient,
        'deliveryAddress':deliveryAddress,
        'updatedWeights':updatedWeights,
        'driverData':{
            'nameDriver':nameDriver,
            'licenceDriver':licenceDriver,
            'dniDriver':dniDriver,
            'vehiclePlate':vehiclePlate,
        },
        'transporterData':{
            'rucTransporter':rucTransporter,
            'razonSocialTranporter':razonSocialTranporter,
        },
        'guideData':{
            'dateGuide':dateGuide,
            'dateGivenGoods':dateGivenGoods,
            'extraWeight':extraWeight,
            'purposeTransportation':purposeTransportation,
            'modeTransportation':modeTransportation,
            'ubigeoClient':ubigeoClient,
            'commentGuide':commentGuide,
        },
        'departureData':{
            'deparmentDeparture':deparmentDeparture,
            'provinceDeparture':provinceDeparture,
            'districtDeparture':districtDeparture,
            'addressDeparture':addressDeparture,
            'ubigeoDeparture':ubigeoDeparture,
        }
    }

    fetch('/salesMetalprotecupdateGuide',{
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(guideInfo)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    window.location.href = '/salesMetalprotecguidesMetalprotec'
}

function getCookie(name) 
{
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") 
    {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) 
        {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) 
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}