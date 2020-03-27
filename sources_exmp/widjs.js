console.log("Ssup !")
getdata()
    .then(response => {
        console.log("done")    
    })
    .catch(error =>{
        console.error(error);
    });

async function getdata()
{
    const response = await fetch('https://api-covid19-in.herokuapp.com/getdata')
    const js = await response.json()
    console.log(js)
    var rec = js.results[0]["recoveries"]
    var act = js.results[0]["active"]
    var dea = js.results[0]["deaths"]
    var mig = js.results[0]["migrated"]
    var psa = js.results[0]["passengers_screened_airport"]
    var tot = js.results[0]["total"]
    document.getElementsById('covid19-rec').innerHTML = rec
    document.getElementsById('covid19-act').innerHTML = act
    document.getElementsById('covid19-mig').innerHTML = mig
    document.getElementsById('covid19-dea').innerHTML = dea
    document.getElementsById('covid19-psa').innerHTML = psa
    document.getElementsById('covid19-tot').innerHTML = tot

}
