document.getElementById("preferences").addEventListener("click", block_click);
function block_click() {
    
    document.write("button does things");

    
        var data = "";

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
        });

        xhr.open("DELETE", "https://api.twitter.com/2/users/2712395911/blocking/1460991245296312321");
        xhr.setRequestHeader("Authorization", "OAuth oauth_consumer_key=\"LKi9NfPzoRzF7Ha54SAd9bezO\",oauth_token=\"2712395911-ehqFfEGiM5COVQg149vqT5miIcvM8SorJmchg0N\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1667216000\",oauth_nonce=\"F24vqCHmB3K\",oauth_version=\"1.0\",oauth_signature=\"yYIMRL0qimWo3P61l%2FJqEDcSITM%3D\"");
        // WARNING: Cookies will be stripped away by the browser before sending the request.
        xhr.setRequestHeader("Cookie", "guest_id=v1%3A166721325154447851");

        xhr.send(data);
        alert(xhr.responseText);
        //document.getElementById("div").innerHTML = xmlhttp.statusText + ":" + xmlhttp.status + "<BR><textarea rows='100' cols='100'>" + xmlhttp.responseText + "</textarea>";
    

    console.write(xmlhttp.responseText);
        alert(xmlhttp.responseText);
        document.write(xmlhttp.responseText);
    

    } 