document.addEventListener('DOMContentLoaded',()=>{

    deleteAllQuotationSections()
    setTimeForQuotationEmission()
    deleteClientSection()
    deleteSellerSection()

    //Quotation items variables section
    selectClient = document.getElementById('selectClient')
    clientAddress = document.getElementById('clientAddress')
    typeItems = document.getElementById('typeItems')
    selectProduct = document.getElementById('selectProduct')
    selectService = document.getElementById('selectService')
    selectSeller = document.getElementById('selectSeller')

    selectSeller.onchange = function()
    {
        chargeSellerInfo()
    }

    selectClient.onchange = function()
    {
        chargeClientInfo()
    }

    clientAddress.onchange = function()
    {
        chargeAddressInfo()
    }

    typeItems.onchange = function()
    {
        if(typeItems.value == 'PRODUCTOS')
        {
            deleteAllQuotationSections()
            showProductQuotationSection()
        }
        else if(typeItems.value == 'SERVICIOS')
        {
            deleteAllQuotationSections()
            showServiceQuotationSection()
        }
        else
        {
            deleteAllQuotationSections()
        }
    }

    selectProduct.onchange = function()
    {
        chargeFieldsProduct()
    }

    selectService.onchange = function()
    {
        chargeFieldsService()
    }

    $('#servicesTable').on('click', 'input[type="button"]', function(e){
        $(this).closest('tr').remove()
    })

    $('#productsTable').on('click', 'input[type="button"]', function(e){
        $(this).closest('tr').remove()
    })
})

function setTimeForQuotationEmission()
{
    Date.prototype.toDateInputValue = (function() {
        var local = new Date(this);
        local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
        return local.toJSON().slice(0,10);
    });
    $('#dateQuotation').val(new Date().toDateInputValue());
}

function deleteAllQuotationSections()
{
    btnAddProduct=document.getElementById('btnAddProduct')
    btnAddService=document.getElementById('btnAddService')
    productsSection=document.getElementById('productsSection')
    productsItems=document.getElementById('productsItems')
    servicesSection=document.getElementById('servicesSection')
    servicesItems=document.getElementById('servicesItems')

    btnAddProduct.style.display = 'none'
    btnAddService.style.display = 'none'
    productsSection.style.display = 'none'
    servicesSection.style.display = 'none'
    productsItems.innerHTML = ''
    servicesItems.innerHTML = ''
}

function showProductQuotationSection()
{
    btnAddProduct=document.getElementById('btnAddProduct')
    productsSection=document.getElementById('productsSection')
    btnAddProduct.style.display = ''
    productsSection.style.display = ''
}

function showServiceQuotationSection()
{
    btnAddService=document.getElementById('btnAddService')
    servicesSection=document.getElementById('servicesSection')
    btnAddService.style.display = ''
    servicesSection.style.display = ''
}

function deleteAddProductInfo()
{
    selectProduct=document.getElementById('selectProduct')
    nameProduct=document.getElementById('nameProduct')
    measureUnitProduct=document.getElementById('measureUnitProduct')
    codeProduct=document.getElementById('codeProduct')
    pvnIGVProduct=document.getElementById('pvnIGVProduct')
    discountProduct=document.getElementById('discountProduct')
    currencyProduct=document.getElementById('currencyProduct')
    quantityProduct=document.getElementById('quantityProduct')
    storeProduct=document.getElementById('storeProduct')

    nameProduct.value=''
    measureUnitProduct.value=''
    codeProduct.value=''
    pvnIGVProduct.value=''
    discountProduct.value=''
    quantityProduct.value=''

    selectProduct.selectedIndex = '0'
    $('#selectProduct').selectpicker('refresh')
    currencyProduct.selectedIndex = '0'
    $('#currencyProduct').selectpicker('refresh')

    while(storeProduct.length > 0)
    {
        storeProduct.remove(0)
    }

    firstOption = document.createElement('option')
    firstOption.value = ''
    firstOption.innerHTML = ''
    storeProduct.appendChild(firstOption)
    storeProduct.selectedIndex = '0'
    $('#storeProduct').selectpicker('refresh')
}

function deleteAddServiceInfo()
{
    selectService=document.getElementById('selectService')
    nameService=document.getElementById('nameService')
    measureUnitService=document.getElementById('measureUnitService')
    pvnIGVService=document.getElementById('pvnIGVService')
    currencyService=document.getElementById('currencyService')
    discountService=document.getElementById('discountService')

    nameService.value=''
    measureUnitService.value=''
    pvnIGVService.value=''
    discountService.value=''

    selectService.selectedIndex='0'
    $('#selectService').selectpicker('refresh')
    currencyService.selectedIndex='0'
    $('#currencyService').selectpicker('refresh')
}

function chargeFieldsService()
{
    idService = document.getElementById('selectService').value
    if(idService !== '')
    {
        fetch(`/servicesMetalprotecgetServiceData?idService=${idService}`)
        .then(response => response.json())
        .then(data => {

            nameService=document.getElementById('nameService')
            measureUnitService=document.getElementById('measureUnitService')
            pvnIGVService=document.getElementById('pvnIGVService')
            currencyService = document.getElementById('currencyService')

            nameService.value=data.editNameService
            measureUnitService.value=data.editMeasureUnit
            pvnIGVService.value=data.editPvnIGV

            for(let i = 0; i < currencyService.options.length; i++ )
            {
                if(currencyService.options[i].value === data.editCurrencyService)
                {
                    currencyService.selectedIndex = String(i)
                    $('#currencyService').selectpicker('refresh')
                    break;
                }
            }
        })
    }
    else
    {
        deleteAddServiceInfo()
    }
}

function chargeFieldsProduct()
{
    idProduct = document.getElementById('selectProduct').value
    storeProduct = document.getElementById('storeProduct')
    if(idProduct !== '')
    {
        fetch(`/productsMetalprotecgetProductData?idProduct=${idProduct}`)
        .then(response => response.json())
        .then(data => {
            nameProduct=document.getElementById('nameProduct')
            measureUnitProduct=document.getElementById('measureUnitProduct')
            codeProduct=document.getElementById('codeProduct')
            pvnIGVProduct=document.getElementById('pvnIGVProduct')
            currencyProduct=document.getElementById('currencyProduct')

            nameProduct.value=data.editNameProduct
            measureUnitProduct.value=data.editMeasureUnit
            codeProduct.value=data.editCodeProduct
            pvnIGVProduct.value=data.editPvnIGV

            for(let i = 0; i < currencyProduct.options.length; i++ )
            {
                if(currencyProduct.options[i].value === data.editCurrencyProduct)
                {
                    currencyProduct.selectedIndex = String(i)
                    $('#currencyProduct').selectpicker('refresh')
                    break;
                }
            }
        })

        fetch(`/productsMetalprotecgetProductStock?idProduct=${idProduct}`)
        .then(response => response.json())
        .then(data => {
            for(let i = 0;i < data.stockStoreProduct.length; i++)
            {
                newOption = document.createElement('option')
                newOption.value = data.stockStoreProduct[i][0]
                newOption.innerHTML = data.stockStoreProduct[i][0]
                storeProduct.appendChild(newOption)
            }
            storeProduct.selectedIndex = '0'
            $('#storeProduct').selectpicker('refresh')
        })
    }
    else
    {
        deleteAddProductInfo()
    }
}

function addServiceInfo()
{
    selectService = document.getElementById('selectService')
    nameService = document.getElementById('nameService')
    measureUnitService = document.getElementById('measureUnitService')
    pvnIGVService = document.getElementById('pvnIGVService')
    currencyService = document.getElementById('currencyService')
    discountService = document.getElementById('discountService')

    servicesItems = document.getElementById('servicesItems')

    servicesItems.innerHTML += `
        <tr class="text-center align-items-center">
            <td data-info=${selectService.value}>${nameService.value}</td>
            <td>${measureUnitService.value}</td>
            <td>${currencyService.value}</td>
            <td style="width:80px;"><input type="text" class="form-control" value="${pvnIGVService.value}"></td>
            <td style="width:80px;"><input type="text" class="form-control" value="${discountService.value}"></td>
            <td><input type="button" class="btn btn-secondary" value="Eliminar"></td>
        </tr>
    `
    deleteAddServiceInfo()

}

function addProductInfo()
{
    selectProduct=document.getElementById('selectProduct')
    nameProduct=document.getElementById('nameProduct')
    measureUnitProduct=document.getElementById('measureUnitProduct')
    codeProduct=document.getElementById('codeProduct')
    pvnIGVProduct=document.getElementById('pvnIGVProduct')
    discountProduct=document.getElementById('discountProduct')
    currencyProduct=document.getElementById('currencyProduct')
    quantityProduct=document.getElementById('quantityProduct')
    storeProduct=document.getElementById('storeProduct')

    productsItems = document.getElementById('productsItems')

    productsItems.innerHTML += `
        <tr class="text-center">
            <td data-info=${selectProduct.value}>${nameProduct.value}</td>
            <td>${codeProduct.value}</td>
            <td>${measureUnitProduct.value}</td>
            <td>${storeProduct.value}</td>
            <td>${currencyProduct.value}</td>
            <td style="width:80px;"><input type="text" class="form-control" value="${pvnIGVProduct.value}"></td>
            <td style="width:80px;"><input type="text" class="form-control" value="${discountProduct.value}"></td>
            <td style="width:80px;"><input type="text" class="form-control" value="${quantityProduct.value}"></td>
            <td style="width:60px;"><input class="form-check-input" type="checkbox"></td>
            <td><input type="button" class="btn btn-secondary" value="Eliminar"></td>
        </tr>
    `

    deleteAddProductInfo()
}

function deleteClientSection()
{
    selectClient = document.getElementById('selectClient')
    clientAddress=document.getElementById('clientAddress')
    identificationClient=document.getElementById('identificationClient')
    documentClient=document.getElementById('documentClient')
    typeClient=document.getElementById('typeClient')
    emailClient=document.getElementById('emailClient')
    contactClient=document.getElementById('contactClient')
    phoneClient=document.getElementById('phoneClient')
    legalAddressClient=document.getElementById('legalAddressClient')
    deliveryAddress=document.getElementById('deliveryAddress')
    selectClient.selectedIndex='0'
    $('#selectClient').selectpicker('refresh')

    while(clientAddress.length > 0)
    {
        clientAddress.remove(0)
    }

    firstOption = document.createElement('option')
    firstOption.value = ''
    firstOption.innerHTML = ''
    clientAddress.appendChild(firstOption)
    clientAddress.selectedIndex = '0'
    $('#clientAddress').selectpicker('refresh')

    identificationClient.value=''
    documentClient.value=''
    typeClient.value=''
    emailClient.value=''
    contactClient.value=''
    phoneClient.value=''
    legalAddressClient.value=''
    deliveryAddress.value=''
}

function chargeClientInfo()
{
    idClient = document.getElementById('selectClient').value
    clientAddress = document.getElementById('clientAddress')
    if(idClient !== '')
    {
        fetch(`/clientsMetalprotecgetClientData?idClient=${idClient}`)
        .then(response => response.json())
        .then(data => {
            identificationClient=document.getElementById('identificationClient')
            documentClient=document.getElementById('documentClient')
            typeClient=document.getElementById('typeClient')
            emailClient=document.getElementById('emailClient')
            contactClient=document.getElementById('contactClient')
            phoneClient=document.getElementById('phoneClient')
            legalAddressClient=document.getElementById('legalAddressClient')

            documentClient.value=data.editDocumentClient
            identificationClient.value=data.editIdentificationClient
            emailClient.value=data.editEmailClient
            contactClient.value=data.editContactClient
            phoneClient.value=data.editPhoneClient
            legalAddressClient.value=data.editLegalAddressClient
            typeClient.value=data.editTypeClient
        })

        fetch(`/clientsMetalprotecgetClientAddress?idClient=${idClient}`)
        .then(response => response.json())
        .then(data => {
            while(clientAddress.length > 0)
            {
                clientAddress.remove(0)
            }
            firstOption = document.createElement('option')
            firstOption.value = ''
            firstOption.innerHTML = ''
            clientAddress.appendChild(firstOption)
            for(let i = 0;i < data.addressesClient.length; i++)
            {
                newOption = document.createElement('option')
                newOption.value = data.addressesClient[i]
                newOption.innerHTML = data.addressesClient[i]
                clientAddress.appendChild(newOption)
            }
            clientAddress.selectedIndex='0'
            $('#clientAddress').selectpicker('refresh')
        })

    }
    else
    {
        deleteClientSection()
    }
}

function chargeAddressInfo()
{
    clientAddress=document.getElementById('clientAddress')
    deliveryAddress=document.getElementById('deliveryAddress')
    if(clientAddress.value !== '')
    {
        deliveryAddress.value = clientAddress.value
    }
    else
    {
        deliveryAddress.value = ''
    }
}

function deleteSellerSection()
{
    selectSeller=document.getElementById('selectSeller')
    nameSeller=document.getElementById('nameSeller')
    codeSeller=document.getElementById('codeSeller')
    phoneSeller=document.getElementById('phoneSeller')

    selectSeller.selectedIndex='0'
    $('#selectSeller').selectpicker('refresh')

    nameSeller.value=''
    codeSeller.value=''
    phoneSeller.value=''
}

function chargeSellerInfo()
{
    idSeller = document.getElementById('selectSeller').value
    if(idSeller !== '')
    {
        fetch(`/getUserData?idUser=${idSeller}`)
        .then(response => response.json())
        .then(data => {

            nameSeller=document.getElementById('nameSeller')
            codeSeller=document.getElementById('codeSeller')
            phoneSeller=document.getElementById('phoneSeller')

            nameSeller.value = `${data.editName} ${data.editLastName}`
            codeSeller.value=data.editCode
            phoneSeller.value=data.editPhone
        })
    }
    else
    {
        deleteSellerSection()
    }
}

function createQuotation()
{
    idClient = document.getElementById('selectClient').value
    identificationClient=document.getElementById('identificationClient').value
    documentClient=document.getElementById('documentClient').value
    typeClient=document.getElementById('typeClient').value
    emailClient=document.getElementById('emailClient').value
    contactClient=document.getElementById('contactClient').value
    phoneClient=document.getElementById('phoneClient').value
    legalAddressClient=document.getElementById('legalAddressClient').value
    deliveryAddress=document.getElementById('deliveryAddress').value

    idSeller = document.getElementById('selectSeller').value
    nameSeller=document.getElementById('nameSeller').value
    codeSeller=document.getElementById('codeSeller').value
    phoneSeller=document.getElementById('phoneSeller').value

    dateQuotation=document.getElementById('dateQuotation').value
    expirationQuotation=document.getElementById('expirationQuotation').value
    relatedDocumentQuotation=document.getElementById('relatedDocumentQuotation').value
    currencyQuotation=document.getElementById('currencyQuotation').value
    erSel=document.getElementById('erSel').value
    erBuy=document.getElementById('erBuy').value
    paymentQuotation=document.getElementById('paymentQuotation').value
    quotesQuotation=document.getElementById('quotesQuotation').value
    expirationCredit=document.getElementById('expirationCredit').value
    commentQuotation=document.getElementById('commentQuotation').value

    if(document.getElementById('showDiscount').checked)
    {
        showDiscount = 'ON'
    }
    else
    {
        showDiscount = 'OFF'
    }

    if(document.getElementById('showSellPrice').checked)
    {
        showSellPrice = 'ON'
    }
    else
    {
        showSellPrice = 'OFF'
    }

    if(document.getElementById('showUnitPrice').checked)
    {
        showUnitPrice = 'ON'
    }
    else
    {
        showUnitPrice = 'OFF'
    }

    typeItems = document.getElementById('typeItems').value

    productsData = []
    servicesData = []
    productsItems = document.getElementById('productsItems')
    servicesItems = document.getElementById('servicesItems')

    for(let i = 0; i < productsItems.rows.length; i++)
    {
        cellsInfo = productsItems.rows.item(i)

        freeProduct = '0'
        if(cellsInfo.cells.item(8).firstChild.checked)
        {
            freeProduct = '1'
        }

        idProduct = cellsInfo.cells.item(0).dataset.info
        nameProduct = cellsInfo.cells.item(0).innerHTML
        codeProduct = cellsInfo.cells.item(1).innerHTML
        measureUnitProduct = cellsInfo.cells.item(2).innerHTML
        storeProduct = cellsInfo.cells.item(3).innerHTML
        currencyProduct = cellsInfo.cells.item(4).innerHTML
        pvnIGVProduct = cellsInfo.cells.item(5).firstChild.value
        discountProduct = cellsInfo.cells.item(6).firstChild.value
        quantityProduct = cellsInfo.cells.item(7).firstChild.value

        productInfo=[idProduct,nameProduct,codeProduct,measureUnitProduct,storeProduct,currencyProduct,pvnIGVProduct,discountProduct,quantityProduct,freeProduct]
        productsData.push(productInfo)
    }

    for(let i = 0; i < servicesItems.rows.length; i++)
    {
        cellsInfo = servicesItems.rows.item(i)

        idService = cellsInfo.cells.item(0).dataset.info
        nameService = cellsInfo.cells.item(0).innerHTML
        measureUnitService = cellsInfo.cells.item(1).innerHTML
        currencyService = cellsInfo.cells.item(2).innerHTML
        pvnIGVService = cellsInfo.cells.item(3).firstChild.value
        discountProduct = cellsInfo.cells.item(4).firstChild.value


        serviceInfo=[idService,nameService,measureUnitService,currencyService,pvnIGVService,discountProduct]
        servicesData.push(serviceInfo)
    }

    quotationInfo = {
        'productsData':productsData,
        'servicesData':servicesData,
        'clientData':{
            'idClient':idClient,
            'identificationClient':identificationClient,
            'documentClient':documentClient,
            'typeClient':typeClient,
            'emailClient':emailClient,
            'contactClient':contactClient,
            'phoneClient':phoneClient,
            'legalAddressClient':legalAddressClient,
            'deliveryAddress':deliveryAddress,
        },
        'sellerData':{
            'idSeller':idSeller,
            'nameSeller':nameSeller,
            'codeSeller':codeSeller,
            'phoneSeller':phoneSeller,
        },
        'quotationData':{
            'dateQuotation':dateQuotation,
            'expirationQuotation':expirationQuotation,
            'relatedDocumentQuotation':relatedDocumentQuotation,
            'currencyQuotation':currencyQuotation,
            'erSel':erSel,
            'erBuy':erBuy,
            'paymentQuotation':paymentQuotation,
            'quotesQuotation':quotesQuotation,
            'expirationCredit':expirationCredit,
            'commentQuotation':commentQuotation,
            'typeItems':typeItems,
        },
        'documentOptions':
        {
            'showDiscount':showDiscount,
            'showSellPrice':showSellPrice,
            'showUnitPrice':showUnitPrice,
        },
    }

    fetch('/salesMetalprotecnewQuotation',{
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(quotationInfo)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        window.location.assign('/salesMetalprotecquotationsMetalprotec')
    })
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