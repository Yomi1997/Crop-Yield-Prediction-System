<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Crop Yield Prediction - Nigeria</title>

  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" crossorigin="anonymous">
  <script src="https://kit.fontawesome.com/728d1d3dec.js" crossorigin="anonymous"></script>
  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" crossorigin="anonymous"></script>
</head>
<body>

<div class="svgs">
  <img src="imgs/bg_svg.svg">
</div>

<div class="page" id="part1">
  <div class="info">
    <div class="heading">
      <div class="title text-primary">Crop Yield Prediction</div>
      <div class="title-support">Using Machine Learning for Nigerian Agriculture</div>
    </div>
    <div class="dev">
      <div class="text-primary"><i class="far fa-file-code"></i>&nbsp;Developed by:</div>
      <ul>
       <li>COMPUTER SCIENCE STUDENT CLASS 2025</li>
      </ul>
    </div>
    <div class="btn-grp">
      <a href="#part3" class="try">Try it!</a>
    </div>
  </div>
  <div class="imgContainer">
    <img src="imgs/flowers.svg" alt="">
  </div>
  <div class="scrollIndicator"></div>
</div>

<div class="page" id="part2">
  <div class="card myCard">
    <div class="myCard-img"><img src="imgs/input.svg" alt=""></div>
    <div class="myCard-title text-blue">Enter Farm Info</div>
    <div class="myCard-body">Provide details like the crop, farm area, soil type, and Nigerian state of cultivation.</div>
  </div>
  <div class="card myCard">
    <div class="myCard-img"><img src="imgs/weather.svg" alt=""></div>
    <div class="myCard-title text-green">Live Weather Fetch</div>
    <div class="myCard-body">Temperature, humidity, and rainfall are fetched in real-time from Nigerian cities.</div>
  </div>
  <div class="card myCard">
    <div class="myCard-img"><img src="imgs/model.svg" alt=""></div>
    <div class="myCard-title text-orange">Prediction Engine</div>
    <div class="myCard-body">A trained ML model built on Nigerian crop data predicts the best crop for your farm.</div>
  </div>
  <div class="scrollIndicator"></div>
</div>

<div class="container p-5 page" id="part3">
  <div class="imgContainer">
    <img src="imgs/plant.svg" alt="">
  </div>
  <div class="card shadow-lg col-6 p-0 mx-auto">
    <div class="card-header text-primary text-center">
      <h3><u>Crop Yield Predictor</u></h3>
    </div>
    <div class="card-body">
      <div class="form-group">
        <label for="state">State:</label>
        <select class="form-control" name="state" id="state" required>
          <option value="">--Select State--</option>
          <option value="Abia">Abia</option>
          <option value="Adamawa">Adamawa</option>
          <option value="Akwa Ibom">Akwa Ibom</option>
          <option value="Anambra">Anambra</option>
          <option value="Bauchi">Bauchi</option>
          <option value="Bayelsa">Bayelsa</option>
          <option value="Benue">Benue</option>
          <option value="Borno">Borno</option>
          <option value="Cross River">Cross River</option>
          <option value="Delta">Delta</option>
          <option value="Ebonyi">Ebonyi</option>
          <option value="Edo">Edo</option>
          <option value="Ekiti">Ekiti</option>
          <option value="Enugu">Enugu</option>
          <option value="FCT">FCT</option>
          <option value="Gombe">Gombe</option>
          <option value="Imo">Imo</option>
          <option value="Jigawa">Jigawa</option>
          <option value="Kaduna">Kaduna</option>
          <option value="Kano">Kano</option>
          <option value="Katsina">Katsina</option>
          <option value="Kebbi">Kebbi</option>
          <option value="Kogi">Kogi</option>
          <option value="Kwara">Kwara</option>
          <option value="Lagos">Lagos</option>
          <option value="Nasarawa">Nasarawa</option>
          <option value="Niger">Niger</option>
          <option value="Ogun">Ogun</option>
          <option value="Ondo">Ondo</option>
          <option value="Osun">Osun</option>
          <option value="Oyo">Oyo</option>
          <option value="Plateau">Plateau</option>
          <option value="Rivers">Rivers</option>
          <option value="Sokoto">Sokoto</option>
          <option value="Taraba">Taraba</option>
          <option value="Yobe">Yobe</option>
          <option value="Zamfara">Zamfara</option>
        </select>
      </div>

      <div class="form-group">
        <label for="lga">Local Government:</label>
        <select class="form-control" name="lga" id="lga" disabled>
          <option value="">--Select LGA--</option>
        </select>
      </div>

      <div class="form-group">
        <label for="crop">Crop:</label>
        <select class="form-control" name="crop" id="crop"></select>
      </div>

      <div class="form-group">
        <label for="area">Area (in acres):</label>
        <input type="number" min="1" max="10000000" class="form-control" id="area" placeholder="Enter area">
      </div>

      <div class="form-group">
        <label for="soil">Soil Type:</label>
        <select class="form-control" name="soil" id="soil"></select>
      </div>

      <div class="row">
        <button class="btn btn-primary mx-auto" id="submit" disabled>Predict</button>
      </div>
    </div>
    <div class="card-footer" id="prediction"></div>
  </div>
</div>

<script>
const lgas = {
  "Abia": ["Aba North", "Umuahia North", "Isiala Ngwa"],
  "Adamawa": ["Yola North", "Mubi South", "Jimeta"],
  "Akwa Ibom": ["Uyo", "Eket", "Ikot Ekpene"],
  "Anambra": ["Awka South", "Onitsha North", "Nnewi North"],
  "Bauchi": ["Bauchi", "Katagum", "Misau"],
  "Bayelsa": ["Yenagoa", "Brass", "Ogbia"],
  "Benue": ["Makurdi", "Gboko", "Otukpo"],
  "Borno": ["Maiduguri", "Biu", "Konduga"],
  "Cross River": ["Calabar South", "Ogoja", "Ikom"],
  "Delta": ["Warri South", "Asaba", "Ughelli North"],
  "Ebonyi": ["Abakaliki", "Afikpo North", "Onicha"],
  "Edo": ["Benin City", "Esan Central", "Oredo"],
  "Ekiti": ["Ado-Ekiti", "Ekiti South-West", "Ikere"],
  "Enugu": ["Enugu East", "Nsukka", "Udi"],
  "FCT": ["Abuja Municipal", "Bwari", "Gwagwalada"],
  "Gombe": ["Gombe", "Kaltungo", "Balanga"],
  "Imo": ["Owerri Municipal", "Okigwe", "Orlu"],
  "Jigawa": ["Dutse", "Hadejia", "Kazaure"],
  "Kaduna": ["Kaduna North", "Zaria", "Chikun"],
  "Kano": ["Nasarawa", "Tarauni", "Dala"],
  "Katsina": ["Katsina", "Daura", "Funtua"],
  "Kebbi": ["Birnin Kebbi", "Zuru", "Yauri"],
  "Kogi": ["Lokoja", "Okene", "Idah"],
  "Kwara": ["Ilorin West", "Offa", "Patigi"],
  "Lagos": ["Ikeja", "Ikorodu", "Epe"],
  "Nasarawa": ["Lafia", "Keffi", "Akwanga"],
  "Niger": ["Minna", "Bida", "Kontagora"],
  "Ogun": ["Abeokuta South", "Ijebu Ode", "Sagamu"],
  "Ondo": ["Akure South", "Owo", "Ondo West"],
  "Osun": ["Osogbo", "Ilesa East", "Ede South"],
  "Oyo": ["Ibadan North", "Ogbomoso North", "Iseyin"],
  "Plateau": ["Jos North", "Barkin Ladi", "Shendam"],
  "Rivers": ["Port Harcourt", "Obio-Akpor", "Bonny"],
  "Sokoto": ["Sokoto North", "Wamako", "Gwadabawa"],
  "Taraba": ["Jalingo", "Takum", "Wukari"],
  "Yobe": ["Damaturu", "Potiskum", "Nguru"],
  "Zamfara": ["Gusau", "Kaura Namoda", "Talata Mafara"]
};

$(document).ready(() => {
  $('#submit').prop('disabled', true);
  $('#prediction').hide();

  const crops = ["maize", "rice", "cassava", "yam", "cocoa", "groundnut"];
  const soils = ["loamy", "sandy", "clay"];

  let cropOpts = '<option value="" selected disabled>Select Crop</option>';
  crops.forEach(c => cropOpts += `<option value="${c}">${c}</option>`);
  $('#crop').html(cropOpts);

  let soilOpts = '<option value="" selected disabled>Select Soil</option>';
  soils.forEach(s => soilOpts += `<option value="${s}">${s}</option>`);
  $('#soil').html(soilOpts);

  $('#state').on('change', function () {
    const selected = $(this).val();
    let options = '<option value="" selected disabled>Select LGA</option>';
    if (lgas[selected]) {
      lgas[selected].forEach(lga => {
        options += `<option value="${lga}">${lga}</option>`;
      });
      $('#lga').html(options).prop('disabled', false);
    } else {
      $('#lga').html('<option value="">--No LGA--</option>').prop('disabled', true);
    }
  });

  $('select, input').on('change keyup', () => {
    const filled = $('#state').val() && $('#lga').val() && $('#crop').val() && $('#area').val() && $('#soil').val();
    $('#submit').prop('disabled', !filled);
  });

  $('#submit').click(() => {
    const paras = `state=${$('#state').val()}&lga=${$('#lga').val()}&crop=${$('#crop').val()}&area=${$('#area').val()}&soil=${$('#soil').val()}`;
    $.get('predict.php?' + paras, (data) => {
      $('#prediction').html(data).show();
    });
  });
});
</script>
</body>
</html>
