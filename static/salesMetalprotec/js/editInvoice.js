function modifyInvoice()
{
    idInvoiceInfo = document.getElementById('invoiceInfo').value
    typeItemsInvoice = document.getElementById('typeItemsInvoice').value
    originInvoice = document.getElementById('originInvoice').value
    legalAddressClient = document.getElementById('legalAddressClient').value
    deliveryAddress = document.getElementById('deliveryAddress').value
    dateInvoice = document.getElementById('dateInvoice').value
    relatedDocumentInvoice = document.getElementById('relatedDocumentInvoice').value
    currencyInvoice = document.getElementById('currencyInvoice').value
    erBuy = document.getElementById('erBuy').value
    erSel = document.getElementById('erSel').value
    commentInvoice = document.getElementById('commentInvoice').value
    paymentQuotation = document.getElementById('paymentQuotation').value
    nroQuotes = '0'

    updatedpvnIGV = []
    updatedDiscount = []
    updatedQuantity = []
    updatedFree = []
    dateQuoteInvoice = []

    if(paymentQuotation === 'CREDITO')
    {
        nroQuotes = document.getElementById('numberQuotes').value
        totalDatesQuotes = document.getElementsByClassName('dateQuoteInfo')
        for(let i = 0; i < totalDatesQuotes.length; i++)
        {
            dateQuoteInfo = totalDatesQuotes[i].value
            dateQuoteInvoice.push(dateQuoteInfo)
        }
    }

    if(typeItemsInvoice === 'PRODUCTOS')
    {
        newpvnIGV = document.getElementsByClassName('pvnIGV')
        newDiscounts = document.getElementsByClassName('discountProduct')
        newQuantities = document.getElementsByClassName('quantityProduct')
        newFreeProducts = document.getElementsByClassName('freeProduct')

        for(let i = 0; i < newpvnIGV.length; i++)
        {
            newpvnIGVInfo = [newpvnIGV[i].dataset.info.slice(2),newpvnIGV[i].value]
            updatedpvnIGV.push(newpvnIGVInfo)
        }

        for(let i = 0; i < newDiscounts.length; i++)
        {
            newDiscountsInfo = [newDiscounts[i].dataset.info.slice(2),newDiscounts[i].value]
            updatedDiscount.push(newDiscountsInfo)
        }

        for(let i = 0; i < newQuantities.length; i++)
        {
            newQuantitiesInfo = [newQuantities[i].dataset.info.slice(2),newQuantities[i].value]
            updatedQuantity.push(newQuantitiesInfo)
        }

        for(let i = 0; i < newFreeProducts.length; i++)
        {
            freeProductInfo = '0'
            if(newFreeProducts[i].checked)
            {
                freeProductInfo = '1'
            }
            else
            {
                freeProductInfo = '0'
            }
            newFreeProductsInfo = [newFreeProducts[i].dataset.info.slice(2),freeProductInfo]
            updatedFree.push(newFreeProductsInfo)
        }
    }
    else
    {
        newpvnIGV = document.getElementsByClassName('pvnIGV')
        newDiscounts = document.getElementsByClassName('discountService')
        for(let i = 0; i < newpvnIGV.length; i++)
        {
            newpvnIGVInfo = [newpvnIGV[i].dataset.info.slice(2),newpvnIGV[i].value]
            updatedpvnIGV.push(newpvnIGVInfo)
        }

        for(let i = 0; i < newDiscounts.length; i++)
        {
            newDiscountsInfo = [newDiscounts[i].dataset.info.slice(2),newDiscounts[i].value]
            updatedDiscount.push(newDiscountsInfo)
        }
    }


    invoiceInfo = {
        'idInvoiceInfo':idInvoiceInfo,
        'typeItemsInvoice':typeItemsInvoice,
        'originInvoice':originInvoice,
        'legalAddressClient':legalAddressClient,
        'deliveryAddress':deliveryAddress,
        'invoiceData':{
            'dateInvoice':dateInvoice,
            'relatedDocumentInvoice':relatedDocumentInvoice,
            'currencyInvoice':currencyInvoice,
            'erBuy':erBuy,
            'erSel':erSel,
            'commentInvoice':commentInvoice,
            'paymentQuotation':paymentQuotation,
        },
        'updatedpvnIGV':updatedpvnIGV,
        'updatedDiscount':updatedDiscount,
        'updatedQuantity':updatedQuantity,
        'updatedFree':updatedFree,
        'nroQuotes':nroQuotes,
        'dateQuoteInvoice':dateQuoteInvoice
    }

    fetch('/salesMetalprotecupdateInvoice',{
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(invoiceInfo)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    window.location.href = '/salesMetalprotecinvoicesMetalprotec'
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