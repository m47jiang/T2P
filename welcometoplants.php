<?php
$input = ask("Welcome to talk to plant, what would you like to inquire about today?",
array("choices"=>"Alice, Bob, Hello", "timeout"=>30.0, "mode"=>"speech"));
$plantnum;
say($input->value);
switch($input->value){
    case "Alice":
        $plantnum = "Plant1";
        break;
    case "Bob":
        $plantnum = "Plant2";
        break;
    case "Hello":
        $plantnum = "Plant3";
        break;
    default:
        $plantnum = "";
}
say($plantnum);
$curl_handle=curl_init();

curl_setopt($curl_handle,CURLOPT_URL,'https://blinding-inferno-9101.firebaseio.com/'.$plantnum.'.json');
curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);

$result = curl_exec($curl_handle);
say($result);
curl_close($curl_handle);

?>