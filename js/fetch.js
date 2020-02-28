
// Fetch a file and download it.
fetch(new_str)
    .then(resp => resp.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'trx.csv';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        alert('your file has downloaded!');
    })
    .catch((e) => alert(e));


fetch(new_str)
            .then((response) => {
                console.log(response.status);
                //download(new_str, "trx.csv");
            }).catch((error) => {
                items++;
                if (items>5){
                    $('#download_csv').modal('show');
                }
                console.log({error});
                console.log({items})

function download(dataurl, filename) {
    var a = document.createElement("a");
    a.href = dataurl;
    a.setAttribute("download", filename);
    a.click();
};