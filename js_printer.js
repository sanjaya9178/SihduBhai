iteam_no = document.getElementById("#item")

function printer(){
    $(document).ready(function(){
  $("#btn").click(function() {
      $.ajax({
          url: "/iteam/no/",
          type: "POST",
          data: {
              data1: $("#item").val(),
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
          },
          success: function (result) {
              console.log(result)
              $("#details").append('<h2>' + result.name + '</h2>')
              $("#details").append('<h2>' + result.number + '</h2>')
              $("#details").append('<h2>' + result.quentity + '</h2>')


          }

      });
        // window.print()
  })
});
}



// function printDiv() {
//      var printContents = document.getElementById('btn').innerHTML;
//      var originalContents = document.body.innerHTML;
//      console.log(printContents)
//
//      document.body.innerHTML = printContents;
//
//      window.print()
//
//
//      document.body.innerHTML = originalContents;
// }




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ITEM DISPLAY</title>
    {% load static %}

</head>
<body>
    <button>log</button>

<div id="div1">
    {% csrf_token %}
    <input name="Itemnumber" id="item">employ_id</input>
{#    <input type="button" value="Print">#}
{#    <input type="button" value="Print" onclick="window.print()">#}

    <button id="btn" onclick="printDiv">print</button>
</div>
{#    <form>#}
{#        <input type="button" value="Print"#}
{#               onclick="window.print()" />#}
{#    </form>#}

<div id="details">



</div>
<input type="checkbox" id="Checklabell" class="chk" onclick="showlabel()">
<label class="labels" > Bin label </label>
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script src="{% static '/js/index.js' %}"></script>
</body>
</html>
