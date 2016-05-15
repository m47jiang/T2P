<?php

$curl_handle=curl_init(); 

curl_setopt($curl_handle,CURLOPT_URL,'https://blinding-inferno-9101.firebaseio.com/Plant1.json');
curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2); 
curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);

$result = curl_exec($curl_handle); 
say($result);
curl_close($curl_handle);

?>
