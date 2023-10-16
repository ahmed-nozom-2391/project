

function add_to_cart(element)
{
    let data = {};
    data['service']  = element.id;
    
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/my-account/my-cart", true);
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 201)
      {
        response = JSON.parse(this.responseText)
        document.getElementById("my_cart1").innerHTML = response.cart_services;
        document.getElementById("my_cart2").innerHTML = response.cart_services;
        element.innerHTML = "Added"
        element.onclick = ""
      }
    }
    xhttp.send(JSON.stringify(data));
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
