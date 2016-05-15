<?php

$curl_handle=curl_init();

curl_setopt($curl_handle,CURLOPT_URL,'https://blinding-inferno-9101.firebaseio.com/.json');
curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);
curl_setopt($curl_handle, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl_handle, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl_handle, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($curl_handle, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json',
            'Accept: application/json'));



$plants = json_decode(curl_exec($curl_handle));
curl_close($curl_handle);
$choices = array();
foreach ($plants as $key => $plant) {
    if($key != 'numPlants') {
        $choices[$plant->name] = $plant;
    }
}

$choices_string = implode(',', array_keys($choices));

say('Welcome to Talk to Plant. We have the health status of ' . $plants->numPlants . ' plants.', array(
    "voice" => "Serena"));
    
function invalidInput() {
    say("I'm sorry, I did not understand you.", array("voice" => "Serena"));
}
    
$plant_name = ask('Please say the name of the plant you wish to talk to. Your plants are: ' . $choices_string, array( 
                 "choices" => $choices_string, 
                 "attempts" => 5,
                 "voice" => "Serena",
                 "onBadChoice" => invalidInput,
                 ));


say('You requested the health status for ' . $plant_name->value . '. Please wait while we connect you to your plant.',
   array( "voice" => "Serena") );
   

if ($plant_name->value == 'Napoleon') {
    $voice = "Victor";
}
else {
    $voice = "Allison";
}

say('Hi! This is ' . $plant_name->value . '. Here are my living conditions: ' .
    'Humidity: ' . $choices[$plant_name->value]->humidity . 'percent. '. 
    'Temperature: ' . $choices[$plant_name->value]->temperature . 'degrees Celsius. ' . 
    'Light: ' . $choices[$plant_name->value]->light . ' lux. ' .
    ' Overall, with these conditions, I am very happy. ' .
    ' Please note that the current temperature is 5% below my threshold temperature value, which is ' . $choices[$plant_name->value]->temperature * 1.05 .
    ' degrees Celsius. ', array( "voice" => $voice) );
?>