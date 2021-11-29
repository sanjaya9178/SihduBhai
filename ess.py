<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ITEM DISPLAY</title>
    {% load static %}

</head>
<body>

<div id="div1">
    {% csrf_token %}
    <input name="Itemnumber" id="item">Item Number</input>
<!--    <button id="btn">Print</button>-->

</div>

    <p> Select one from the given printer options:
        <select id="select1">
            <option value="wmic">One note for windwos 10</option>
            <option value="printer">Microsoft XPS Document Writer</option>
            <option value="list">Microsoft Print to PDF</option>
            <option value="brief">Fax</option>
        </select>
    </p>

    <p> The value of the option selected is:
        <span class="output"></span>
    </p>


    <button onclick="get_printers()"> Check option </button>

    <script type="text/javascript">
    function get_printers() {
        selectElement = document.querySelector('#select1');
        output = selectElement.value;
        document.querySelector('.output').textContent = output;
    }
    </script>


<button id="btn">Print</button>
<!--    <input type="button" id="btn" value="Print">-->
</body>
<!--<input type="checkbox" id="Checklabel" class="chk" onclick="showlabel()">-->
<!--<label class="labels" > Bin label </label>-->
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script src="{% static '/js/index.js' %}"></script>
</body>
</html>





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
  })
});
}



def get_printers(request):
    data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\n')
    print(data)
    data = data[1:]
    printers = []
    for lines in data:
        for printer in lines.split("  "):
            if (printer != ""):
                printers.append(printer)
                break
    print_page = []
    for each in range(1, 100):
        each = each+1
        print_page.append(each)
        if each > 100:
            break

    return render(request,'itemdisplay.html',{"printer_option":printers, "printer_page":print_page},)

    # return HttpResponse(json.dumps({"printer": printers ,"page_print":print_page}), content_type='application_type')

