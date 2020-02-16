var int: soldiers;
var int: trucks;
constraint 2*soldiers + trucks <=100;
constraint soldiers + trucks <=80;
constraint soldiers <=40;
constraint soldiers >=0;
constraint trucks >=0;
solve maximize 3*soldiers + 2*trucks;
output[ "No.ofsoldiers = ", show(soldiers),"\n",
"No trucks = ",show(trucks), "\n",
"profit: ",show(3*soldiers + 2*trucks)];