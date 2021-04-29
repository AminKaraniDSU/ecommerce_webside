var updateBtns = document.getElementsByClassName('update-cart')
for(var i=0; i< updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click', function(){
        var producrId = this.dataset.product
        var action = this.dataset.action

        console.log("producrId: ",producrId, " action: ",action)
        console.log("User: ", user)
        if(user === 'AnonymousUser'){
            console.log("User is not log inn")
        }
        else{
            updateUserOrder(producrId, action)
        }
    })
}

function updateUserOrder(producrId, action){
    console.log("User is log inn, Sending Data")
    console.log("csrftoken: ", csrftoken)
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'producrId': producrId, 'action': action
        })
    })

        .then(response => {
            return response.json()
        })
        .then((data) => {
            console.log("Data: ",data)
            location.reload()
        })
}