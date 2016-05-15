<?php
answer();


$name = 'Michel';
$numPlants = 4;
$name = 'HahahahaHahahahaHahahahaHahahahaahahaha';
$temp = '3';
$humidity = '4';
$light = '500000000000 cat dog owl hello world';
$response = {"Plant1": {"name":"carrie"}, "Plant2": {"name":"george"}};


/*say('''
Hi, ?{} welcome to Talk to Plant.
We currently have records for ?{} plants.
Which plant would you you like to talk to?
''' .format(name, numPlants), {"voice":"Serena"}
);*/


function get_plant_choices(){
    $plant_choices = '';
    for keys in response.keys():
        $plant_choices = response[keys]["name"] + ',' + plant_choices; //Concatenate keys
    return str(plant_choices).rstrip(','); //Remove trailing comma
}
$plant_names = get_plant_choices();

$selected_plant = ask("Please say the name of the following options: " + plant_names, {
         "choices": plant_names,
         "attempts":5,
         "timeout":10.0,
         "onBadChoice": lambda event : say('''
                                         I'm sorry, I didn't understand that.
                                         Please repeat the name of the plant you wish to talk to.
                                         ''' )});

say('''
You requested information for: {}.
We have gathered the following information about your plant's environment:
Temperature: {}.
Humidity: {}.
Light: {}.
'''.format(selected_plant.value, temp, humidity, light), {"voice":"Serena"}
);

say('''
According to our advanced machine learning algorithms,
your plant's overall health is: 87%.
Warning: Temperature is 10% below the suggested threshold.
'''
);

hangup();

?>