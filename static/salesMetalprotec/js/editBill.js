function modifyBill()
{
    idBillInfo = document.getElementById('billInfo').value
    typeItemsBill = document.getElementById('typeItemsBill').value
    originBill = document.getElementById('originBill').value
    legalAddressClient = document.getElementById('legalAddressClient').value
    deliveryAddress = document.getElementById('deliveryAddress').value
    dateBill = document.getElementById('dateBill').value
    relatedDocumentBill = document.getElementById('relatedDocumentBill').value
    currencyBill = document.getElementById('currencyBill').value
    erBuy = document.getElementById('erBuy').value
    erSel = document.getElementById('erSel').value
    commentBill = document.getElementById('commentBill').value
    paymentQuotation = document.getElementById('paymentQuotation').value
    nroQuotes = '0'

    updatedpvnIGV = []
    updatedDiscount = []
    updatedQuantity = []
    updatedFree = []
    dateQuoteBill = []

    if(paymentQuotation === 'CREDITO')
    {
        nroQuotes = document.getElementById('numberQuotes').value
        totalDatesQuotes = document.getElementsByClassName('dateQuoteInfo')
        for(let i = 0; i < totalDatesQuotes.length; i++)
        {
            dateQuoteInfo = totalDatesQuotes[i].value
            dateQuoteBill.push(dateQuoteInfo)
        }
    }

    if(typeItemsBill === 'PRODUCTOS')
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


    billInfo = {
        'idBillInfo':idBillInfo,
        'typeItemsBill':typeItemsBill,
        'originBill':originBill,
        'legalAddressClient':legalAddressClient,
        'deliveryAddress':deliveryAddress,
        'billData':{
            'dateBill':dateBill,
            'relatedDocumentBill':relatedDocumentBill,
            'currencyBill':currencyBill,
            'erBuy':erBuy,
            'erSel':erSel,
            'commentBill':commentBill,
            'paymentQuotation':paymentQuotation,
        },
        'updatedpvnIGV':updatedpvnIGV,
        'updatedDiscount':updatedDiscount,
        'updatedQuantity':updatedQuantity,
        'updatedFree':updatedFree,
        'nroQuotes':nroQuotes,
        'dateQuoteBill':dateQuoteBill
    }

    fetch('/salesMetalprotecupdateBill',{
        method:"POST",
        headers:
        {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(billInfo)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    window.location.href = '/salesMetalprotecbillsMetalprotec'
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