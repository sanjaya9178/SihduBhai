var flag=0
function load()
{
    setfooter();
    var idselect=document.getElementById("idselect")
    document.body.style.backgroundColor ="#f1f1f1"
    let url=window.location.href +'get_printers'
    let req=new XMLHttpRequest();
    req.onreadystatechange= function()
    {
        if(this.readyState == 4 && this.status==200)
        {
            let data=JSON.parse(req.responseText)
            for(var i=0;i<data.printer.length;i++)
            {
                var opt = document.createElement('option');
                opt.value = data.printer[i];
                opt.innerHTML = data.printer[i];
                idselect.appendChild(opt);
            }
        }
    }
    req.open("GET",url,true)
    req.send()
}
function setfooter()
{
    var url = window.location.href;
    var arr = url.split("/");
    document.getElementById("location").innerHTML=arr[3].toUpperCase();
    document.getElementById("instance").innerHTML=arr[4].toUpperCase();
}
function getlabeldata()
{
    var txtarea,txtcaps,txtdesc2,txtdesc1,txtitem,txtitemnumber
    var itemnumber,txtfrom,txtto,lblfrom,lblto,lblbinqty,txtbinqty
    var imgstr,urlbarcode,idfrom,idto,idbinqty,lblitemno,lbldesc,lblarea
    var imgbarcodeitemno,print_content,print_content1,lbldesc1,divcaps
    var Checklabel1,Checklabel2
    txtitemnumber=document.getElementById('txtitemnumber')
    txtitem=document.getElementById('txtitem')
    txtarea=document.getElementById('txtarea')
    txtcaps=document.getElementById('txtcaps')
    txtdesc1=document.getElementById('txtdesc1')
    txtdesc2=document.getElementById('txtdesc2')
    txtcaps=document.getElementById('txtcaps')
    txtfrom=document.getElementById('txtfrom')
    txtto=document.getElementById('txtto')
    txtbinqty=document.getElementById('txtbinqty')
    lblbinqty=document.getElementById('lblbinqty')
    lblfrom=document.getElementById('lblfrom')
    lblto=document.getElementById('lblto')
    idfrom=document.getElementById('imgbarcode0')
    idto=document.getElementById('imgbarcode1')
    idbinqty=document.getElementById('imgbarcode2')
    lblitemno=document.getElementById('lblitemno')
    lbldesc=document.getElementById('lbldesc')
    lblarea=document.getElementById('lblarea')
    imgbarcodeitemno=document.getElementById('imgbarcodeitemno')
    print_content=document.getElementById('print_content')
    print_content1=document.getElementById('print_content1')
    lbldesc1=document.getElementById('lbldesc1')
    divcaps=document.getElementById('divcaps')
    Checklabel1=document.getElementById('Checklabel1')
    Checklabel2=document.getElementById('Checklabel2')
    itemnumber=txtitemnumber.value
    txtitem.value=itemnumber
    txtarea.value=" "
    txtcaps.value=" "
    txtdesc1.value=" "
    txtdesc2.value=" "
    txtfrom.value=" "
    txtto.value=" "
    txtbinqty.value=" "
    lblto.innerHTML=" "
    lblfrom.innerHTML=" "
    lblbinqty.innerHTML=" "
    idfrom.src=" "
    idto.src=" "
    idbinqty.src=" "
    imgbarcodeitemno.src=" "
    lblitemno.innerHTML=" "
    lbldesc.innerHTML=" "
    lbldesc1.innerHTML=" "
    lblarea.innerHTML=" "
    divcaps.innerHTML=" "
    print_content.style.display="none"
    print_content1.style.display="none"
    let url=window.location.href +'bin_labels_details?item_number='+itemnumber
    let req=new XMLHttpRequest();
    flag=0
    Checklabel1.checked = false;
    Checklabel2.checked = false;
    req.onreadystatechange= function()
    {
        if(this.readyState == 4 && this.status==200)
        {
            let data=JSON.parse(req.responseText)
            txtarea.value=data.data[2].AREA
            txtcaps.value=data.data[3].CAPS_LOCATION
            divcaps.innerHTML=data.data[3].CAPS_LOCATION
            txtdesc1.value=data.data[1].item_description.substring(0,16)
            lblitemno.innerHTML=itemnumber
            lbldesc.innerHTML=data.data[1].item_description.substring(0,16)
            lblarea.innerHTML=data.data[2].AREA
            if(data.data[1].item_description.length >15)
            {
                txtdesc2.value=data.data[1].item_description.substring(16,data.data[1].item_description.length)
                lbldesc1.innerHTML=data.data[1].item_description.substring(16,data.data[1].item_description.length)
            }
             if(!data.data[4].FROM && !data.data[5].TO)
            {
                alert("No Data")
                flag=0
            }
            else
            {
                txtfrom.value=data.data[4].FROM
                lblfrom.innerHTML=data.data[4].FROM
                txtto.value=data.data[5].TO
                txtbinqty.value=data.data[6].BIN_QTY
                lblbinqty.innerHTML=data.data[6].BIN_QTY
                lblto.innerHTML=data.data[5].TO
                flag=1
                Checklabel1.checked = true;
                Checklabel2.checked = true;
                urlbarcode=window.location.href +'barcode_generator?input_string='+data.data[4].FROM
                req.onreadystatechange= function()
                {
                    if(this.readyState == 4 && this.status==200)
                    {
                        imgstr="data:image/png;base64,"+req.responseText
                        idfrom.src=imgstr
                        let urlbarcode2=window.location.href +'barcode_generator?input_string='+data.data[6].BIN_QTY
                        req.onreadystatechange= function()
                        {
                            if(this.readyState == 4 && this.status==200)
                            {
                                imgstr="data:image/png;base64,"+req.responseText
                                idbinqty.src=imgstr
                                let urlbarcode1=window.location.href +'barcode_generator?input_string='+data.data[5].TO
                                req.onreadystatechange= function()
                                {
                                    if(this.readyState == 4 && this.status==200)
                                    {
                                        imgstr="data:image/png;base64,"+req.responseText
                                        idto.src=imgstr
                                        let urlbarcodeitemno=window.location.href +'barcode_generator?input_string='+itemnumber
                                        req.onreadystatechange= function()
                                        {
                                            if(this.readyState == 4 && this.status==200)
                                            {
                                                imgstr="data:image/png;base64,"+req.responseText
                                                imgbarcodeitemno.src=imgstr
                                                print_content.style.display="block"
                                                print_content1.style.display="block"

                                            }
                                        }
                                        req.open("GET",urlbarcodeitemno,true)
                                        req.send()
                                    }
                                }
                                req.open("GET",urlbarcode1,true)
                                req.send()
                            }
                        }
                        req.open("GET",urlbarcode2,true)
                        req.send()
                    }
                }
                req.open("GET",urlbarcode,true)
                req.send()
            }
        }
    }
    req.open("GET",url,true)
    req.send()
}
function printDiv(divName) {
     var printContents = document.getElementById(divName).innerHTML;
     var originalContents = document.body.innerHTML;
     document.body.innerHTML = printContents;
     window.print();
     document.body.innerHTML = originalContents;
}
function showlabels()
{
    var checkBox1 = document.getElementById("Checklabel1");
    var checkBox2 = document.getElementById("Checklabel2");
     if (checkBox1.checked == true && flag==1)
     {
           print_content1.style.display = "block";
     }
     else
     {
        print_content1.style.display="none"
     }
     if (checkBox2.checked == true && flag==1)
     {
           print_content.style.display = "block";
     }
     else
     {
         print_content.style.display="none"

     }

}
function handle(e)
{
     if(e.keyCode === 13)
     {
         e.preventDefault(); // Ensure it is only this code that runs
         getlabeldata()
     }
}
