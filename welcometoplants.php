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
        array_push($choices, $plant->name);
    }
}

$choices_string = implode(',', $choices);


answer()
$input = ask('Welcome to Talk to Plant. We have the health status of' . $plants->numPlants . 'plants. ' .  
             'Please say the name of the plant you wish to talk to. Your plants are: ' . $choices_string, array( 
                 "choices" => $choices_string, 
                 "attempts" => 5,
                 "voice" => "Serena",
                 ));


say('You requested ')

hangup()
?>