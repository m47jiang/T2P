<?php
$input = ask("Welcome to talk to plant, what would you like to inquire about today?",
array("CHOICES"=>"Lassie, Peaches, Prunes"));
$plantnum;
switch($input){
    case "Lassie":
        $plantnum = "Plant1";
        break;
    case "Peaches":
        $plantnum = "Plant2";
        break;
    case "Plums":
        $plantnum = "Plant3";
}
$curl_handle=curl_init();

curl_setopt($curl_handle,CURLOPT_URL,'https://blinding-inferno-9101.firebaseio.com/'.$plantnum->value.'.json');
curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);

$result = curl_exec($curl_handle);
say($result);
curl_close($curl_handle);

?>