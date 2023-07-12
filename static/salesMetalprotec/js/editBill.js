function modifyInvoice()
{
    idBillInfo = document.getElementById('billInfo').value
    legalAddressClient = document.getElementById('legalAddressClient').value
    deliveryAddress = document.getElementById('deliveryAddress').value
    dateBill = document.getElementById('dateBill').value
    relatedDocumentBill = document.getElementById('relatedDocumentBill').value
    currencyBill = document.getElementById('currencyBill').value
    erBuy = document.getElementById('erBuy').value
    erSel = document.getElementById('erSel').value
    commentBill = document.getElementById('commentBill').value
    paymentQuotation = document.getElementById('paymentQuotation').value

    updatedpvnIGV = []
    updatedDiscount = []
    updatedQuantity = []
    updatedFree = []

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

    billInfo = {
        'idBillInfo':idBillInfo,
        'billData':{
            'legalAddressClient':legalAddressClient,
            'deliveryAddress':deliveryAddress,
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
    }

    fetch('/salesMetalprotecupdateInvoice',{
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